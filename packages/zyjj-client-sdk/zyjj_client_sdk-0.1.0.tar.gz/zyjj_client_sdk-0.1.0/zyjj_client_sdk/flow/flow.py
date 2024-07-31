import json
import logging
import time
import traceback

from graphviz import Digraph
import threading

from zyjj_client_sdk.flow.base import FlowBase, FlowNode, FlowRelation, node_define, NodeInfo
import zyjj_client_sdk.flow.node as Node

node_type_map = {
    0: '开始节点',
    1: '结束节点',
    2: '代码节点',
    3: '获取配置',
    4: '检查积分',
    5: '扣除积分',
    6: '上传文件',
    7: '下载文件',
    8: '文件解析',
    9: '文件导出',
    10: '腾讯认证',
    11: '本地路径',
    12: '下载链接',
    13: '批量下载链接',
    14: 'ffmpeg积分',
}


class FlowService:
    def __init__(self, base: FlowBase, flow_data: dict):
        # 不同类型的节点处理函数
        self.__node_type_handle: dict[int, node_define] = {
            0: Node.node_input,
            1: Node.node_output,
            2: Node.node_code,
            3: Node.node_get_config,
            4: Node.node_check_point,
            5: Node.node_cost_point,
            6: Node.node_upload_file,
            7: Node.node_download_file,
            8: Node.node_file_parse,
            9: Node.node_file_export,
            10: Node.node_get_tencent_token,
            11: Node.node_generate_local_path,
            12: Node.node_download_url,
            13: Node.node_batch_download_url,
            14: Node.node_ffmpeg_point,
        }
        # 基本服务
        self.__base = base
        # 所有节点对应的信息
        self.__node_id_info: dict[str, FlowNode] = {}
        # 开始节点
        self.__start_node_id = ""
        self.__end_node_id = ""
        # 当前节点对应的后继节点
        self.__node_next: dict[str, list[FlowRelation]] = {}
        # 当前节点对应的前驱节点
        self.__node_prev: dict[str, list[FlowRelation]] = {}
        # 每个节点的输出数据
        self.__node_output: dict[str, dict[str, str]] = {}
        # 已经完成的节点
        self.__node_finish = set()
        # 所有关系节点
        self.__flow_relations = []
        #  每个节点的相关日志
        self.__node_log: dict[str, NodeInfo] = {}
        # 先解析所有node对应的type
        for node in flow_data["nodes"]:
            node_data = node["data"] if "data" in node else "{}"
            flow_node = FlowNode(node["node_id"], node["node_type"], node_data)
            self.__node_id_info[flow_node.node_id] = flow_node
            if flow_node.node_type == 0:
                self.__start_node_id = flow_node.node_id
            elif flow_node.node_type == 1:
                self.__end_node_id = flow_node.node_id
            self.__node_log[flow_node.node_id] = NodeInfo(
                node_id=flow_node.node_id,
                node_type=flow_node.node_type,
                data=flow_node.data
            )
            # 节点类型全部初始化
            self.__node_output[flow_node.node_id] = {}
            self.__node_prev[flow_node.node_id] = []
            self.__node_next[flow_node.node_id] = []

        # 解析出所有节点的依赖关系
        for relation in flow_data["relations"]:
            flow_relation = FlowRelation(
                relation["from"],
                relation["from_output"],
                relation["to"],
                relation["to_input"]
            )
            self.__flow_relations.append(flow_relation)
            self.__node_prev[flow_relation.to_id].append(flow_relation)
            self.__node_next[flow_relation.from_id].append(flow_relation)

    @staticmethod
    def __filter_dict_bytes(data: dict) -> dict:
        new_dict = {}
        for key, value in data.items():
            if isinstance(value, bytes):
                new_dict[key] = f'bytes({len(value)})'
            else:
                new_dict[key] = value
        return new_dict

    # 是否需要访问节点
    def __no_need_visited(self, node_id: str) -> bool:
        return node_id in self.__node_finish

    def __execute_node(self, node_id: str):
        # 当前节点如果执行过就直接返回
        if self.__no_need_visited(node_id):
            return
        # 获取当前节点的信息
        info = self.__node_id_info[node_id]
        # 获取当前节点的处理函数
        handle = self.__node_type_handle[info.node_type]
        handle_intput = {}
        # 先判断一下当前节点前驱节点都处理完了，并获取到输出
        for before in self.__node_prev.get(node_id, []):
            self.__execute_node(before.from_id)
            handle_intput[before.to_input] = self.__node_output[before.from_id][before.from_output]
        # 执行前再检查一下是否需要执行
        if self.__no_need_visited(node_id):
            return
        node_start = time.time()
        handle_extra = {}
        # data不为空不设置exta信息
        if info.data is not None and info.data != '':
            handle_extra = json.loads(info.data)
        # 设置当前节点的依赖信息，并传递给base，方便子模块调用
        self.__base.set_flow_relation(
            self.__node_id_info[node_id],
            self.__node_prev.get(node_id, []),
            self.__node_next.get(node_id, []),
        )
        try:
            # 执行当前节点
            self.__node_output[node_id] = handle(self.__base, handle_intput, handle_extra)
            # 标记当前节点已完成
            self.__node_finish.add(node_id)
            logging.info(f"execute node {node_id} cost {(time.time() - node_start) * 1000}ms")
            self.__node_log[node_id].status = 1
        except Exception as e:
            logging.error(f"execute node {node_start} err {e}")
            self.__node_log[node_id].status = 2
            self.__node_log[node_id].msg = traceback.format_exc()
            raise e
        finally:
            self.__node_log[node_id].cost = int((time.time() - node_start) * 1000)
        # 执行当前节点的后继节点
        for after in self.__node_next.get(node_id, []):
            self.__execute_node(after.to_id)

    # 触发流程
    def tiger_flow(self) -> dict:
        flow_start = time.time()
        status = 0
        msg = ""
        try:
            self.__execute_node(self.__start_node_id)
            status = 1
            # 直接返回结束节点的结果
            return self.__node_output[self.__end_node_id]
        except Exception as e:
            status = 2
            msg = traceback.format_exc()
            logging.error(msg)
            raise e
        finally:
            # 后台上报日志
            threading.Thread(target=self.save_flow_log, args=(
                int((time.time() - flow_start) * 1000),
                status,
                msg
            )).start()

    # 保存流程的日志
    def save_flow_log(self, cost: int, flow_status: int, flow_msg: str):
        logging.info(f"save flow status log {flow_status} {flow_msg}")
        log = {}
        # 获取流程描述
        node_desc = self.__base.get_desc()
        # 先绘制一下流程图
        dot = Digraph(comment='执行流程', graph_attr={'rankdir': 'LR'})
        for node_id, info in self.__node_id_info.items():
            color = "#f2f3f5"
            status = self.__node_log[node_id].status
            if status == 1:
                color = "#ecfeec"
            elif status == 2:
                color = "#fcede9"
            desc = ""
            if node_id in node_desc:
                desc = f'[{node_desc[node_id]}]'
            dot.node(
                name=node_id,
                label=f"{node_type_map[info.node_type]}{desc}({node_id})", style="filled",
                fillcolor=color
            )
        # 绘制依赖关系
        for relation in self.__flow_relations:
            dot.edge(relation.from_id, relation.to_id, label=f"{relation.from_output}->{relation.to_input}")
        # 保存节点数据时不去存储字节类型的数据
        node_datas = {}
        for key, value in self.__node_output.items():
            node_data = {}
            for key2, value2 in value.items():
                # 我们只转换基本类型，其他的都不转换
                if isinstance(value2, (str, int, float, bool, dict, list)):
                    node_data[key2] = value2
                else:
                    node_data[key2] = str(type(value2))
            node_datas[key] = node_data
        logging.info("node data {}".format(json.dumps(node_datas)))
        log["graph"] = dot.source
        log["node_data"] = node_datas
        # 节点的信息
        log["node_info"] = {k: v.__dict__ for k, v in self.__node_log.items()}
        log["node_relation"] = [relation.__dict__ for relation in self.__flow_relations]
        self.__base.api.upload_flow_log({
            "task_id": self.__base.task_id,
            "flow_log": json.dumps(log, ensure_ascii=False),
            "status": flow_status,
            "cost": cost,
            "msg": flow_msg,
            "create_time": int(time.time() * 1000),
        })
