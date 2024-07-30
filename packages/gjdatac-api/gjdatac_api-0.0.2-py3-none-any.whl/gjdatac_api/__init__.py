from .data_api_class import GJDataC
from .initializer import init  # 导入你的初始化函数

__all__ = ['GJDataC']


def __init__(ip_address, port, user_id, password):
    init(ip_address, port, user_id, password)  # 执行初始化验证
    return GJDataC()  # 验证成功后返回你的类实例
