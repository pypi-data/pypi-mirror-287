import logging
from typing import Optional

from zyjj_client_sdk.flow.base import FlowBase


# 输入节点
def node_input(base: FlowBase, data: dict, extra: Optional[dict]) -> dict:
    input_data = {}
    user_input = base.input_get()
    for unique in extra["uniques"]:
        if unique in user_input:
            input_data[unique] = user_input[unique]
        else:
            input_data[unique] = None

    return input_data


# 输出节点
def node_output(base: FlowBase, data: dict, extra: Optional[dict]) -> dict:
    return data


# 代码节点
def node_code(base: FlowBase, data: dict, extra: Optional[dict]) -> dict:
    return base.tiger_code(extra["id"], data)
