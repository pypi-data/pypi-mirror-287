from fastapi.testclient import TestClient
from ..web import app

"""/init_db - 创建或初始化LMDB数据库。

测试用例：正常初始化、初始化失败（如传递无效参数）。
"""
def test_init_db_success():
    client = TestClient(app)
    response = client.post(
        "/init_db/db1",
        json={"size": 256, "max_dbs": 512, "max_readers": 512},
    )
    assert response.status_code == 200
    assert response.json() == {"result": True}

def test_init_db_failure():
    client = TestClient(app)
    response = client.post(
        "/init_db/db1",
        json={"size": -1, "max_dbs": 1024, "max_readers": 1024},
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 500  # 假设传入负数size会导致失败


"""/create_name_db - 创建命名数据库。

测试用例：正常创建、创建失败（如数据库已存在或参数错误）。
"""
def test_create_name_db_success():
    client = TestClient(app)
    description = "This is a test named database"
    data_structure = {
        "key": "test_key",
        "data": [
            ["a","str"],
            ['b',"int"]
        ]
    }
    response = client.post(
        "/create_name_db/db1/test_name_db",
        json={"description": description, "data_structure": data_structure},
    )
    assert response.status_code == 200
    assert response.json() == {"result": True}

def test_create_name_db_failure():
    client = TestClient(app)
    description = ""
    data_structure = {}  # 错误的数据结构
    response = client.post(
        "/create_name_db/db1/test_name_db2",
        json={"description": description, "data_structure": data_structure},
    )
    assert response.status_code == 400  # 假设数据结构错误会导致失败


"""/write - 写入键值对。

测试用例：正常写入、写入失败（如JSON格式错误）。
"""
def test_write_success():
    client = TestClient(app)
    key = "test_key"
    value = {"a": "hello", "b": 123}
    response = client.post(
        "/write/db1/test_name_db",
        json={"key": key, "value": value},
    )
    assert response.status_code == 200
    assert response.json() == {"result": True}

def test_write_failure():
    client = TestClient(app)
    key = "test_key"
    value = "invalid_json"  # 模拟JSON格式错误
    response = client.post(
        "/write/db1/test_name_db",
        json={"key": key, "value": value},
    )
    assert response.status_code == 200  # 假设JSON格式错误会导致失败
    assert response.json() == {"result": False}


"""/read - 读取键值对。

测试用例：正常读取、读取失败（如键不存在）。
"""
def test_read_success():
    client = TestClient(app)
    key = "test_key"
    response = client.post(
        "/read/db1/test_name_db/" + key
    )
    print(response.json())

def test_read_failure():
    client = TestClient(app)
    key = "non_existent_key"
    response = client.post(
        "/read/db1/test_name_db/" + key
    )
    print(response.json())


"""/delete - 删除键值对。

测试用例：正常删除、删除失败（如键不存在）。
"""
def test_delete_success():
    client = TestClient(app)
    key = "test_key"
    response = client.post(
        "/delete/db1/test_name_db/" + key
    )
    print(response.json())

def test_delete_failure():
    client = TestClient(app)
    key = "non_existent_key"
    response = client.post(
        "/delete/db1/test_name_db/" + key
    )
    print(response.json())  # 假设尝试删除不存在的键会导致失败


"""/updata - 更新键值对。

测试用例：正常更新、更新失败（如JSON格式错误）。
"""
def test_updata_success():
    client = TestClient(app)
    key = "test_key"
    value = {"a": "updated", "b": 456}
    response = client.post(
        "/updata/db1/test_name_db/" + key,
        json={"key":key,"value": value},
    )
    print(response.json())

def test_updata_failure():
    client = TestClient(app)
    key = "test_key"
    value = "invalid_json"  # 模拟JSON格式错误
    response = client.post(
        "/updata/db1/test_name_db/" + key,
        json={"key":key,"value": value}
    )
    print(response.json())


"""/batch_write - 批量写入键值对。

测试用例：正常批量写入、批量写入失败（如JSON格式错误）。
"""
def test_batch_write_success():
    client = TestClient(app)
    batch_data = [
        {"key3" : {"a": "hello", "b": 123}},
        {"key4" :{"a": "world", "b": 456}}
    ]
    response = client.post(
        "/batch_write/db1/test_name_db",
        json={"kv_list": batch_data},
    )
    print(response.json())

def test_batch_write_failure():
    client = TestClient(app)
    batch_data = [
        {"key5" : "invalid_json"},
        {"key6":{"a": "world", "g": 456}} # 模拟JSON格式错误
    ]
    response = client.post(
        "/batch_write/db1/test_name_db",
        json={"kv_list": batch_data},
    )
    print(response.json())  # 假设JSON格式错误会导致失败


"""/set - 设置嵌套字典的键值。

测试用例：正常设置、设置失败（如JSON格式错误）。
"""
def test_set_success():
    client = TestClient(app)
    keys = ["key3", "a"]
    value = "nested"
    response = client.post(
        "/set/db1/test_name_db",
        json={"keys": keys, "value": value},
    )
    print(response.json())

def test_set_failure():
    client = TestClient(app)
    keys = ["key3", "b"]
    value = "invalid_json"  # 模拟JSON格式错误
    response = client.post(
        "/set/db1/test_name_db",
        json={"keys": keys, "value": value},
    )
    print(response.json())  # 假设JSON格式错误会导致失败


"""/get - 获取嵌套字典的键值。

测试用例：正常获取、获取失败（如路径不存在）。
"""
def test_get_success():
    client = TestClient(app)
    keys = ["key3", "b"]
    response = client.post(
        "/get/db1/test_name_db",
        json={"keys": keys},
    )
    print(response.json())

def test_get_failure():
    client = TestClient(app)
    keys = ["non_existent_path"]
    response = client.post(
        "/get/db1/test_name_db",
        json={"keys": keys},
    )
    print(response.json())  # 假设路径不存在会导致失败


"""/remove - 移除嵌套字典的键。

测试用例：正常移除、移除失败（如路径不存在）。
"""
def test_remove_success():
    client = TestClient(app)
    keys = ["key3", "b"]
    response = client.post(
        "/remove/db1/test_name_db",
        json={"keys": keys},
    )
    print(response.json())

def test_remove_failure():
    client = TestClient(app)
    keys = ["non_existent_path"]
    response = client.post(
        "/remove/db1/test_name_db",
        json={"keys": keys},
    )
    print(response.json())  # 假设尝试删除不存在的路径会导致失败


"""/get_limit - 获取指定位置和数量的键值对。

测试用例：正常获取、获取失败（如数据库不存在）。

"""
def test_get_limit_success():
    client = TestClient(app)
    response = client.post(
        "/get_limit/db1/test_name_db",
        json={"start": 0, "limit": 10},
    )
    print(response.json())

def test_get_limit_failure():
    client = TestClient(app)
    response = client.post(
        "/get_limit/db1/non_existent_db",
        json={"start": 0, "limit": 10},
    )
    print(response.json())  # 假设数据库不存在会导致失败


"""/matching - 执行字符匹配查询。

测试用例：正常匹配、匹配失败（如无匹配项）。
"""
def test_matching_success():
    client = TestClient(app)
    key = "key"
    response = client.post(
        "/matching/db1/test_name_db",
        json={"key": key, "start": 0, "limit": 10},
    )
    print(response.json())

def test_matching_failure():
    client = TestClient(app)
    key = "non_existent_key"
    response = client.post(
        "/matching/db1/test_name_db",
        json={"key": key, "start": 0, "limit": 10},
    )
    print(response.json())  # 假设匹配不到任何键值对会导致失败


"""/get_sum - 获取键值对总数。

测试用例：正常获取总数、获取失败（如数据库不存在）。
"""
def test_get_sum_success():
    client = TestClient(app)
    response = client.post(
        "/get_sum/db1/test_name_db"
    )
    print(response.json()) 

def test_get_sum_failure():
    client = TestClient(app)
    response = client.post(
        "/get_sum/db1/non_existent_db"
    )
    print(response.json())   # 假设数据库不存在会导致失败


"""/get_db_info - 获取数据库配置信息。

测试用例：正常获取、获取失败（如数据库不存在）。
"""
def test_get_db_info_success():
    client = TestClient(app)
    response = client.post(
        "/get_db_info/db1"
    )
    print(response.json())

def test_get_db_info_failure():
    client = TestClient(app)
    response = client.post(
        "/get_db_info/non_existent_db"
    )
    print(response.json())  # 假设数据库不存在会导致失败


"""/get_db_name_list - 获取所有数据库名称列表。

测试用例：正常获取列表、获取失败（如无数据库）。
"""
def test_get_db_name_list_success():
    client = TestClient(app)
    response = client.post(
        "/get_db_name_list"
    )
    print(response.json())


"""get_name_database_list - 获取指定数据库下的所有命名数据库名称。

测试用例：正常获取列表、获取失败（如数据库不存在或无命名数据库）
"""
def test_get_name_database_list_success():
    client = TestClient(app)
    response = client.post(
        "/get_name_database_list/db1"
    )
    print(response.json())

def test_get_name_database_list_failure():
    client = TestClient(app)
    response = client.post(
        "/get_name_database_list/non_existent_db"
    )
    print(response.json())  # 假设数据库不存在会导致失败


"""/drop_name_db - 删除指定数据库下的命名数据库。

测试用例：正常删除、删除失败（如命名数据库不存在）。
"""
def test_drop_name_db_success():
    client = TestClient(app)
    response = client.post(
        "/drop_name_db/db1/test_name_db"
    )
    print(response.json()) 

def test_drop_name_db_failure():
    client = TestClient(app)
    response = client.post(
        "/drop_name_db/db1/non_existent_name_db"
    )
    print(response.json())   # 假设尝试删除不存在的命名数据库会导致失败


"""/drop_name_db - 删除指定数据库下的命名数据库。

测试用例：正常删除、删除失败（如命名数据库不存在）。
"""
def test_env_close_success():
    client = TestClient(app)
    response = client.post(
        "/env_close/db1"
    )
    print(response.json())

def test_env_close_failure():
    client = TestClient(app)
    response = client.post(
        "/env_close/non_existent_db"
    )
    print(response.json())  # 假设尝试关闭不存在的数据库环境会导致失败


"""/cleanup - 删除指定的数据库及其配置文件。

测试用例：正常清理、清理失败（如数据库不存在）。
"""
def test_cleanup_success():
    client = TestClient(app)
    response = client.post(
        "/cleanup/db1"
    )
    print(response.json())

def test_cleanup_failure():
    client = TestClient(app)
    response = client.post(
        "/cleanup/non_existent_db"
    )
    print(response.json())  # 假设尝试清理不存在的数据库会导致失败

if __name__ == "__main__":
    test_init_db_success()
    # test_init_db_failure()

    # test_create_name_db_success()
    # test_create_name_db_failure()

    # test_write_success()
    # test_write_failure()

    # test_read_success()
    # test_read_failure()

    # test_updata_success()
    # test_updata_failure()

    # test_delete_success()
    # test_delete_failure()

    # test_batch_write_success()
    # test_batch_write_failure()

    # test_set_success()
    # test_set_failure()

    # test_remove_success()
    # test_remove_failure()

    # test_get_success()
    # test_get_failure()

    # test_get_limit_success()
    # test_get_limit_failure()

    # test_matching_success()
    # test_matching_failure()

    # test_get_sum_success()
    # test_get_sum_failure()

    # test_get_db_info_success()
    # test_get_db_info_failure()

    # test_get_db_name_list_success()
   
    # test_get_name_database_list_success()
    # test_get_name_database_list_failure()

    # test_drop_name_db_success()
    # test_drop_name_db_failure()

    # test_env_close_success()
    # test_env_close_failure()

    # test_cleanup_success()
    # test_cleanup_failure()
