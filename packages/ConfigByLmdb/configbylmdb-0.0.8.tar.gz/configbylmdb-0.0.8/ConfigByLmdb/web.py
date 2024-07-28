import logging
import logging.config
from logging.handlers import TimedRotatingFileHandler
from typing import List, Union
import uvicorn
import os
from fastapi import FastAPI
from pydantic import BaseModel,Field
from .DB import ConfigDB,Structure 
from typing import List, Set, Tuple, Any, Optional
from fastapi.middleware.cors import CORSMiddleware

# 自定义日志配置
def setup_custom_logging(level:str):
    log_dir =  os.path.join(os.getcwd(),"logs")
    os.makedirs(log_dir, exist_ok=True)

    # 定义日志配置
    log_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": "[%(asctime)s] [%(levelname)s] [%(name)s:%(lineno)s] %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S %z",
            },
        },
        "handlers": {
            "file": {
                "()": TimedRotatingFileHandler,
                "filename": os.path.join(os.getcwd(),"logs","app.log"),
                "when": "midnight",
                "interval": 1,
                "backupCount": 7,
                "encoding": "utf-8",
                "formatter": "standard",
            },
        },
        "loggers": {
            "web":{"handlers": ["file"], "level": level, "propagate": False},
            "uvicorn": {"handlers": ["file"], "level": level, "propagate": False},
            "uvicorn.access": {"handlers": ["file"], "level": level, "propagate": False},
        },
    }
    logging.config.dictConfig(log_config)
    return log_config

custom_log_config = setup_custom_logging("INFO")
logger = logging.getLogger("web")

app = FastAPI()
db = ConfigDB()  # 全局共享的ConfigDB实例

# 允许所有来源
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

class InitDBParams(BaseModel):
    size: Optional[int]  = Field(default=256, ge=0, description="内存数据库大小")
    max_dbs: Optional[int]  = Field(default=512, ge=0, description="命名数据库最大数量")
    max_readers: Optional[int]  = Field(default=512, ge=0, description="事务开启最大数量")

class DataStructure(BaseModel):
    key:str
    data:Union[List[List[Any]] , str]

class CreateNameDBParams(BaseModel):
    description: str
    data_structure: DataStructure

class WriteParams(BaseModel):
    key:str
    value: Union[Any]

class GetLimitParams(BaseModel):
    start:int = Field(default=0, ge=0, description="起始位置")
    limit:int = Field(default=100, ge=0, description="获取的数量")

class SetParams(BaseModel):
    keys:List[str]
    value: Union[Any]

class GetParams(BaseModel):
    keys:List[str]

class BatchWriteModel(BaseModel):
    kv_list: List[dict]

class WriteModel(BaseModel):
    db_name: str
    name_db: str
    value: Union[str,int,float,None,list,dict] 

class MatchingParams(BaseModel):
    key:Union[str,int,None,float]
    start:int = Field(default=0, ge=0, description="起始位置")
    limit:int = Field(default=100, ge=0, description="获取的数量")

class DeleteByExcludeParams(BaseModel):
    include: Union[List[str],None] = Field(default=None, description="删除包含在内的key")
    exclude: Union[List[str],None]  = Field(default=None, description="删除不包含在内的key")

class ReadParams(BaseModel):
    key:str

def string_to_type(type_str: str):
    """
    根据字符串表示的类型名称，返回相应的Python类型对象。
    
    :param type_str: 表示类型的字符串，如 'string', 'str', 'int', 'float' 等。
    :return: 对应的Python类型，如果类型名称不识别，则返回 None。
    """
    type_mapping = {
        "string": str,
        "str": str,
        "int": int,
        "integer": int,
        "float": float,
        "bool": bool,
        "boolean": bool,
        "list": list,
        "tuple": tuple,
        "dict": dict,
    }

    return type_mapping.get(type_str.lower(),str)
   

# 然后，使用FastAPI的装饰器将ConfigDB类的方法暴露为API接口
@app.post("/init_db/{db_name}")
def init_db(db_name: str, initDBParams: InitDBParams):
    """
    创建或初始化LMDB数据库。
    
    **路径参数:**
    - `db_name` (str): 数据库名称。

    **请求体:**
    - `size` (int): 内存数据库大小(以M为单位)，默认为256。
    - `max_dbs` (int): 最多命名数据库数量，默认为512。
    - `max_readers` (int): 最多读写事务数量，默认为512。

    **响应:**
    - {"result": 结果}
    """
    if int(initDBParams.size) <= 0:
        initDBParams.size = 256
    if int(initDBParams.max_dbs) <= 0:
        initDBParams.max_dbs = 512
    if int(initDBParams.max_readers) <= 0:
        initDBParams.max_readers = 512
    return {"result": db.init_db(db_name, initDBParams.size, initDBParams.max_dbs, initDBParams.max_readers)}

@app.post("/create_name_db/{db_name}/{name_db}")
def create_name_db(db_name: str, name_db: str, createNameDBParams:CreateNameDBParams):
    """
    创建命名数据库。
    
    **路径参数:**
    - `db_name` (str): 数据库名称。
    - `name_db` (str): 命名数据库名称。

    **请求体:**
    - `description` (str): 命名数据库描述。
    - `data_structure` (dict): 数据结构定义。

    **响应:**
    - {"result": 结果}
    """
    try:
        data = []
        if type(createNameDBParams.data_structure.data) == list \
                and len(createNameDBParams.data_structure.data) > 0 \
                and type(createNameDBParams.data_structure.data[0]) == list:
            for key,_type in createNameDBParams.data_structure.data:
                data.append([key,string_to_type(_type)])
            createNameDBParams.data_structure.data = data
        else:
            createNameDBParams.data_structure.data = string_to_type(createNameDBParams.data_structure.data)
        structure = Structure(key = createNameDBParams.data_structure.key,data=createNameDBParams.data_structure.data)
        return {"result": db.create_name_db(db_name, name_db, createNameDBParams.description, structure)}
    except Exception as e:
        return {"result":False}

@app.post("/write/{db_name}/{name_db}")
def write(db_name: str, name_db: str, writeParams:WriteParams):
    """
    向指定的命名数据库写入键值对。
    
    **路径参数:**
    - `db_name` (str): 数据库名称。
    - `name_db` (str): 命名数据库名称。

    **请求体:**
    - `key` (str): 要写入的键。
    - `value` (any): 要写入的值，可以是字符串、整数、浮点数、字典或列表等。

    **响应:**
    - {"result": 结果}
    """
    return {"result": db.write(db_name, name_db, writeParams.key, writeParams.value)}

@app.post("/read/{db_name}/{name_db}")
def read(db_name: str, name_db: str, readParams: ReadParams):
    """
    从指定的命名数据库读取键值对。
    
    **路径参数:**
    - `db_name` (str): 数据库名称。
    - `name_db` (str): 命名数据库名称。
    
    **请求体:**
    - `key` (str): 要读取的键。

    **响应:**
    - {"result": 结果}
    """
    return {"result": db.read(db_name, name_db, readParams.key)}

@app.post("/delete/{db_name}/{name_db}/{key}")
def delete(db_name: str, name_db: str, key: str):
    """
    从指定的命名数据库删除键值对。
    
    **路径参数:**
    - `db_name` (str): 数据库名称。
    - `name_db` (str): 命名数据库名称。
    - `key` (str): 要删除的键。

    **响应:**
    - {"result": 结果}
    """
    return {"result": db.delete(db_name, name_db, key)}

@app.post("/batch_delete/{db_name}/{name_db}")
def batch_delete(db_name: str, name_db: str, deleteByExcludeParams: DeleteByExcludeParams):
    """
    从指定的命名数据库删除键值对。
    
    **路径参数:**
    - `db_name` (str): 数据库名称。
    - `name_db` (str): 命名数据库名称。
    

    **请求体:**
    - `include` (List[str]): 要删除的键列表。
    - `exclude` (List[str]): 要保留的键列表。

    **响应:**
    - {"result": 结果}
    """
    return {"result": db.batch_delete(db_name, name_db, deleteByExcludeParams.include,deleteByExcludeParams.exclude)}

@app.post("/updata/{db_name}/{name_db}")
def updata(db_name: str, name_db: str, writeParams:WriteParams):
    """
    更新指定的命名数据库中的键值对。
    
    **路径参数:**
    - `db_name` (str): 数据库名称。
    - `name_db` (str): 命名数据库名称。
    
    **请求体:**
    - `key` (str): 要更新的键。
    - `value` (any): 新的值，可以是字符串、整数、浮点数、字典或列表等。

    **响应:**
    - {"result": 结果}
    """
    return {"result": db.updata(db_name, name_db, writeParams.key, writeParams.value)}

@app.post("/batch_write/{db_name}/{name_db}")
def batch_write(db_name: str, name_db: str, batch_data: BatchWriteModel):
    """
    批量向指定的命名数据库写入键值对。
    
    **路径参数:**
    - `db_name` (str): 数据库名称。
    - `name_db` (str): 命名数据库名称。

    **请求体:**
    - `kv_list` (List[KeyValueModel]): 键值对列表，每个元素包含键和值。

    **响应:**
    - {"result": 结果}
    """
    return {"result": db.batch_write(db_name, name_db, batch_data.kv_list)}

@app.post("/set/{db_name}/{name_db}")
def set(db_name: str, name_db: str, setParams: SetParams):
    """
    设置数据库中嵌套字典的键值。
    
    **路径参数:**
    - `db_name` (str): 数据库名称。
    - `name_db` (str): 命名数据库名称。

    **请求体:**
    - `keys` (List[str]): 键的列表，表示要设置的嵌套路径。
    - `value` (any): 要设置的值，可以是字符串、整数、浮点数、字典或列表等。

    **响应:**
    - {"result": 结果}
    """
    return {"result": db.set(db_name, name_db, setParams.keys, setParams.value)}

@app.post("/get/{db_name}/{name_db}")
def get(db_name: str, name_db: str, getParams:GetParams):
    """
    获取数据库中嵌套字典的键值。
    
    **路径参数:**
    - `db_name` (str): 数据库名称。
    - `name_db` (str): 命名数据库名称。

    **请求体:**
    - `keys` (List[str]): 键的列表，表示要获取的嵌套路径。

    **响应:**
    - {"result": 结果}
    """
    return {"result": db.get(db_name, name_db, getParams.keys)}
    
@app.post("/remove/{db_name}/{name_db}")
def remove(db_name: str, name_db: str, removeParams:GetParams):
    """
    从数据库中移除嵌套字典的键。
    
    **路径参数:**
    - `db_name` (str): 数据库名称。
    - `name_db` (str): 命名数据库名称。

    **请求体:**
    - `keys` (List[str]): 键的列表，表示要移除的嵌套路径。

    **响应:**
    - {"result": 结果}
    """
    return {"result": db.remove(db_name, name_db, removeParams.keys)}
    
@app.post("/get_limit/{db_name}/{name_db}")
def get_limit(db_name: str, name_db: str, getLimitParams:GetLimitParams):
    """
    获取指定位置和数量的键值对。
    
    **路径参数:**
    - `db_name` (str): 数据库名称。
    - `name_db` (str): 命名数据库名称。

    **请求体:**
    - `start` (int): 开始位置，默认为0。
    - `limit` (int): 获取的数量，默认为100。

    **响应:**
    - {"result": 结果}
    """
    return {"result": db.get_limit(db_name, name_db, getLimitParams.start, getLimitParams.limit)}

@app.post("/matching/{db_name}/{name_db}/{mode}")
def matching(db_name: str, name_db: str, mode:int, matchingParams:MatchingParams):
    """
    执行字符匹配查询，支持键或值的深度匹配。
    
    **路径参数:**
    - `db_name` (str): 数据库名称。
    - `name_db` (str): 命名数据库名称。
    - `mode` (int): 匹配模式。

    **请求体:**
    - `key` (str|int|float|None): 需要匹配的值。
    - `start` (int): 开始位置，默认为0。
    - `limit` (int): 匹配的数量，默认为100。

    **响应:**
    - {"result": 结果}
    """
    result = db.matching(db_name, name_db, matchingParams.key, matchingParams.start, matchingParams.limit, matching_level = mode)
    return {"result": result}    

@app.post("/precise_matching/{db_name}/{name_db}/{mode}")
def precise_matching(db_name: str, name_db: str, mode:int, matchingParams:MatchingParams):
    """
    执行精确匹配。
    
    **路径参数:**
    - `db_name` (str): 数据库名称。
    - `name_db` (str): 命名数据库名称。
    - `mode` (int): 匹配模式。

    **请求体:**
    - `key` (str|int|float|None): 需要匹配的值。
    - `start` (int): 开始位置，默认为0。
    - `limit` (int): 匹配的数量，默认为100。

    **响应:**
    - {"result": 结果}
    """
    result = db.precise_matching(db_name, name_db, matchingParams.key, matchingParams.start, matchingParams.limit, matching_level = mode)
    return {"result": result}    

@app.post("/get_sum/{db_name}/{name_db}")
def get_sum(db_name: str, name_db: str):
    """
    获取指定命名数据库中存储的键值对总数。
    
    **路径参数:**
    - `db_name` (str): 数据库名称。
    - `name_db` (str): 命名数据库名称。

    **响应:**
    - {"result": 结果}
    """
    total = db.get_sum(db_name, name_db)
    return {"result": total}

@app.post("/get_db_info/{db_name}")
def get_db_info(db_name: str):
    """
    获取指定数据库的配置信息。
    
    **路径参数:**
    - `db_name` (str): 数据库名称。

    **响应:**
    - {"result": 结果}
    """
    return {"result": db.get_db_info(db_name)}

@app.post("/get_db_status/{db_name}")
def get_db_status(db_name: str):
    """
    获取指定数据库的打开状态。
    
    **路径参数:**
    - `db_name` (str): 数据库名称。

    **响应:**
    - {"result": 结果}
    """
    return {"result": db.get_db_status(db_name)}


@app.post("/get_db_name_list")
def get_db_name_list():
    """
    获取所有数据库的名称列表。
    
    **响应:**
    - {"result": 结果}
    """
    return {"result": db.get_db_name_list()}

@app.post("/get_name_database_list/{db_name}")
def get_name_database_list(db_name: str):
    """
    获取指定数据库下的所有命名数据库名称。
    
    **路径参数:**
    - `db_name` (str): 数据库名称。

    **响应:**
    - {"result": 结果}
    """
    return {"result": db.get_name_database_list(db_name)}

@app.post("/get_name_database_info/{db_name}")
def get_name_database_info(db_name: str,name_db:Optional[str] = None):
    """
    获取指定数据库的配置信息。
    
    **路径参数:**
    - `db_name` (str): 数据库名称。
    - `name_db` (str): 命名数据库名称。

    **响应:**
    - {"result": 结果}
    """
    return {"result": db.get_name_database_info(db_name,name_db)}

@app.post("/drop_name_db/{db_name}/{name_db}")
def drop_name_db(db_name: str, name_db: str):
    """
    删除指定数据库下的命名数据库。
    
    **路径参数:**
    - `db_name` (str): 数据库名称。
    - `name_db` (str): 命名数据库名称。

    **响应:**
    - {"result": 结果}
    """
    return {"result": db.drop_name_db(db_name, name_db)}

@app.post("/env_close/{db_name}")
def env_close(db_name: str):
    """
    关闭指定的数据库环境。
    
    **路径参数:**
    - `db_name` (str): 数据库名称。

    **响应:**
    - {"result": 结果}
    """
    return {"result": db.env_close(db_name)}

@app.post("/cleanup/{db_name}")
def cleanup(db_name: str):
    """
    删除指定的数据库及其配置文件。
    
    **路径参数:**
    - `db_name` (str): 数据库名称。

    **响应:**
    - {"result": 结果}
    """
    return {"result": db.cleanup(db_name)}

def run(port:int = 8080):
    uvicorn.run(app, host="0.0.0.0", port=port, log_config=custom_log_config)

if __name__ == "__main__":
    
    uvicorn.run(app, host="0.0.0.0", port=8080, log_config=custom_log_config)