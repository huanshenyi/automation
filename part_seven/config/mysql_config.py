def set_mysql_config(env):
    if env == "dev":
        db_config = {
            'host': "0.0.0.0",
            'user': "root",
            'passwd': '',
            'db': 'python_ui',
            'port': 3306,
            'charset': 'utf8'
        }
        return db_config

    if env == "pro":
        db_config = {
            'host': "0.0.0.0",
            'user': "root",
            'passwd': '',
            'db': 'python_ui',
            'port': 3306,
            'charset': 'utf8'
        }
        return db_config

