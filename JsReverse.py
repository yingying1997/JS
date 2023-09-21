# 安装方法：pip install PyExecJs -i https://pypi.tuna.tsinghua.edu.cn/simple
import execjs # 用于执行 JavaScript 代码的库

# 定义函数
def get_js(js_path, fuc_name, func_args):
    '''
    :param js_path:  js代码的文件路径
    :param fuc_name: 调用的js函数名称
    :param func_args: 传入的参数
    :return:
    '''
    # 1. 读取 js 代码
    with open(js_path, 'r', encoding='utf-8') as f:
        js_code = f.read()

    # 2. 编译 js 代码
    cjs = execjs.compile(js_code)

    # 3. 执行 js 代码，函数后面跟上一个参数
    # print(fuc_name, func_args)
    return cjs.call(fuc_name, func_args)

# 调用函数
# get_js('jsDemo.js', 'd1', 'hello', 'world')