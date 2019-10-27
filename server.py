# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 10:01 AM
# @Author  : python疯子
# @File    : server.py
# @Software: PyCharm


from sanic import Sanic
from sanic import response
from sanic.exceptions import RequestTimeout

app = Sanic(__name__)

async def index(request):

    return response.json({"zxc": 123})


@app.route("/voice_server/v1", methods=["POST"])
async def func(request):
    '''
    流程：下载音频，读取音频信息并返回

    :param request: 包含音频名称的URL， 此处只为音频名称
    :return:  音频信息
    '''

    # 打印配置项
    print(app.config.DB_IP)

    # 获取入参信息
    voice = request.json
    template = voice.get("text")

    print("待翻译的内容为：", template)

    return response.json({"zxc": 123})

@app.route('/', methods=['GET'])
async def get_handler(request):

    return response.text('hello - sanic')

@app.route('/get1', methods=['GET'])
async def get_handler(request):

    load_sour()

    return response.text('GET request - sanic')



def load_sour():
    print("执行：load_sour")

    # imp 从 Python 3.4 之后弃用了，建议使用 importlib 代替
    # import imp
    # a = imp.load_source('mymod', 'my_config.py')

    import importlib
    a = importlib.machinery.SourceFileLoader('mymod', 'my_config.py').load_module()

    a.mymod()


# 防止等待超时 服务器崩溃
@app.exception(RequestTimeout)
def timeout(request, exception):
    return response.text('RequestTimeout from error_handler.', 408)


def run_as_server():
    # work 接口监听者   和内核合数相同
    app.run(host="0.0.0.0", port=8000, workers=2, debug=True)
    return


if __name__ == '__main__':

    run_as_server()
