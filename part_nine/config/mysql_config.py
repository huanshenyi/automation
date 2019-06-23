def set_mysql_config(env):
    if env == "dev":
        db_config = {
            "host": '127.0.0.1',
            'user': 'root',
            'passwd': 'root',
            'db': 'python_ui',
            'port': 3306,
            'charset': 'utf-8'
        }
    if env == "pro":
        db_config = {
            "host": '127.0.0.1',
            'user': 'root',
            'passwd': 'root',
            'db': 'python_ui',
            'port': 3306,
            'charset': 'utf-8'
        }

    return db_config