import json
import logging
import math
import uuid
from typing import Optional

import requests
from tencentcloud.common import credential
from zyjj_client_sdk.flow.base import FlowBase


# 获取默认参数
def get_val_or_default(key: str, data: dict, extra: Optional[dict], default=None):
    if key in data:
        return data[key]
    if extra is not None and key in extra:
        return extra[key]
    return default


# 获取云端配置
def node_get_config(base: FlowBase, data: dict, extra: Optional[dict]) -> dict:
    val = base.api.get_config(extra["name"])
    if "is_json" in extra and extra["is_json"]:
        val = json.loads(val)
    return {"val": val}


# 检查积分
def node_check_point(base: FlowBase, data: dict, extra: Optional[dict]) -> dict:
    point = get_val_or_default('point', data, extra)
    current_point = base.api.get_user_point(base.uid)
    if current_point < point:
        raise Exception(f"积分不足! 需要积分:{point} 当前积分:{current_point}")
    return {"point": point, "pass": data["pass"]}


# 扣除积分
def node_cost_point(base: FlowBase, data: dict, extra: Optional[dict]) -> dict:
    name = get_val_or_default("name", data, extra)
    desc = get_val_or_default("desc", data, extra)
    if not base.api.use_user_point(base.uid, name, data["point"], desc):
        raise Exception(f"积分不足！所需积分{data['point']}")

    return {"pass": data["pass"]}


# 上传文件
def node_upload_file(base: FlowBase, data: dict, extra: Optional[dict]) -> dict:
    oss = base.new_oss()
    # 先获取到云端路径
    cloud_path = ""
    if "cloud_path" in data:
        cloud_path = data["cloud_path"]
    elif "local_path" in data:
        cloud_path = oss.tencent_upload_by_local_path(base.uid, data["local_path"])
    elif "bytes_data" in data:
        cloud_path = oss.tencent_upload_by_bytes(
            base.uid,
            data["bytes_data"],
            get_val_or_default("bytes_ext", data, extra, "txt"),
        )
    logging.info(f"[upload-file] cloud path is {cloud_path}")
    # 判断需要输出哪些字段
    need_output = base.node_output_need()
    if "url" in need_output:
        return {"url": oss.tencent_get_url_by_key(cloud_path)}
    else:
        return {"cloud_path": cloud_path}


# 下载文件
def node_download_file(base: FlowBase, data: dict, extra: Optional[dict]) -> dict:
    oss = base.new_oss()
    cloud_path, source = data["cloud_path"], data["cloud_source"]
    # 直接下载到本地
    local_path = oss.tencent_download_file_by_key(cloud_path)
    # 判断需要输出哪些字段
    need_output = base.node_output_need()
    if "local_path" in need_output:
        return {"local_path": local_path}
    elif "bytes_data" in need_output:
        with open(local_path, "rb") as f:
            return {"bytes_data": f.read()}
    return {}


def _parse_file(file: dict) -> dict:
    return {
        "path": file["path"],
        "source": file["source"] if "source" in file else 0,
        "duration": file["duration"] if "duration" in file else 0,
        "size": file["size"] if "size" in file else 0,
        "name": file["name"] if "name" in file else file["path"].split("/")[-1],
        "ext": file["ext"] if "ext" in file else file["path"].split(".")[-1],
        "uid": file["uid"] if "uid" in file else uuid.uuid4().hex
    }


# 文件解析
def node_file_parse(base: FlowBase, data: dict, extra: Optional[dict]) -> dict:
    return _parse_file(data["file"])


# 文件组织
def node_file_export(base: FlowBase, data: dict, extra: Optional[dict]) -> dict:
    return {"file": _parse_file(data)}


# 腾讯云token
def node_get_tencent_token(base: FlowBase, data: dict, extra: Optional[dict]) -> dict:
    token = base.api.could_get_tencent_token()
    return {"token": credential.Credential(token["TmpSecretId"], token["TmpSecretKey"])}


# 生成本地路径
def node_generate_local_path(base: FlowBase, data: dict, extra: Optional[dict]) -> dict:
    ext = get_val_or_default('ext', data, extra)
    return {"path": base.tool_generate_local_path(ext)}


# 下载链接
def node_download_url(base: FlowBase, data: dict, extra: Optional[dict]) -> dict:
    bytes_data = requests.get(data["url"]).content
    need_output = base.node_output_need()
    if "bytes_data" in need_output:
        return {"bytes_data": bytes_data}
    else:
        path = base.tool_generate_local_path(get_val_or_default("ext", data, extra))
        with open(path, "wb") as f:
            f.write(bytes_data)
        return {"local_path": path}


# 批量文件下载
def node_batch_download_url(base: FlowBase, data: dict, extra: Optional[dict]) -> dict:
    referer = get_val_or_default('referer', data, extra, default='')
    ext = get_val_or_default('ext', data, extra, default='')
    oss = base.new_oss()
    url_list = []
    for url in data["url_list"]:
        b = requests.get(url, headers={"referer": referer}).content
        key = oss.tencent_upload_by_bytes(base.uid, b, ext)
        url_list.append(oss.tencent_get_url_by_key(key, expired=600))
    return {"url_list": url_list}


# ffmpeg 积分计算
def node_ffmpeg_point(base: FlowBase, data: dict, extra: Optional[dict]) -> dict:
    path = get_val_or_default("path", data, extra, default='')
    point = get_val_or_default("point", data, extra, default=0)
    duration = base.tool_ffmpeg_get_duration(path)
    final_point = math.ceil(float(point) * (duration/60))
    logging.info(f"[ffmpeg-point] path {path} point {point} duration: {duration} final point: {final_point}")

    return {"point": final_point}
