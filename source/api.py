#coding:utf8
import flask
import logging
from flask import request, jsonify

import sys
sys.path.append("..")
from source.utils import SETTINGS
from source.utils import _check
from source.lib.locations import locations
# from source.utils.move_fun import send_mark, move_to_point


app = flask.Flask(__name__)
app.config["DEBUG"] = SETTINGS.get("APP_DEBUG", False)
app.config["port"] = SETTINGS["PORT"]
app.config["host"] = SETTINGS["HOST"]

logger = logging.getLogger(name=SETTINGS.get("App_NAME", "main"))

#Done:连接测试
@app.route("/", methods=["GET", "POST"])
def home():
    """测试服务器是否可以连接
    """
    result = jsonify({
        "description": "连接 API 服务器成功"
    })
    logger.debug("连接到测试服务器")
    return result


# Done: 带参数请求
@app.route("/args", methods=["GET", "POST"])
def extract():
    """测试带参数请求是否成功
    """
    result = _check.check_parameters("id", "book")
    return jsonify(result)
    
# TODO: 平衡车移动 API 接口
@app.route("/move", methods=["GET", "POST"])
def move():
    """调用移动平衡车接口
    """
    location = _check.check_parameters("location")["location"]
    x, y = locations[location]
    import os
    from os import path
    # 直接调用运送到点
    os.system("python %s -x %s -y %s" % (
        path.join(path.dirname(__file__), "utils/move_fun.py", x, y
    )))

    

if __name__ == "__main__":
    # global goal_pub
    app.run(port=SETTINGS["PORT"], host=SETTINGS["HOST"])