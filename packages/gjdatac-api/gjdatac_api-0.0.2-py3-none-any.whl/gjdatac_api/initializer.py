import dolphindb as ddb


def init(ip_address, port, user_id, password):
    # 在这里实现 IP 地址和端口号的验证逻辑
    try:
        db_session = ddb.session()
        db_session.connect(ip_address, port, user_id, password)
    except Exception as e:
        raise Exception("please check your ip_address, port, user_id, password")
