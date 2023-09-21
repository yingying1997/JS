# 导入 requests 库，用于发送 HTTP 请求和处理 HTTP 响应
import requests
# 导入自定义模块，用于获取 JavaScript 代码生成的字典
from JsReverse import get_js # JsReverse 为文件名，get_js 为函数名

# 输入需要翻译的内容
trs = input('请输入需要翻译的内容')
# 调用 get_js 函数，传入 JavaScript 文件名'baidu.js'、函数名'b'和翻译内容 trs，获取生成的字典
dic = get_js('baidu.js', 'b', trs)
# 判断输入的是中文还是英文
length = len(trs[0].encode('utf-8')) # 第一个字符长度，一个字母长度是为1，汉字是为3
# 英文
if length == 1:
    dic['from'] = 'en'
    dic['to'] = 'zh'
# 中文
elif length == 3:
    dic['from'] = 'zh'
    dic['to'] = 'en'
# 打印字典
# print(dic)
# 设置翻译请求的 url
url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
# 请求头
headers = {
    'Acs-Token': '1687238994011_1687238994248_sKfCKQnOqNJPstsgIsKUPaqAYGqQnIFYiRYGiFYQlIQ+uev26ckgDP84N0sc9iBWm9m8CkW2nyiEwf2Nkr+8bGpHXAxRIArLKohyWWLDQsf6T3mPhsnt8wAI2EGbiEU21zkMCz4WHc49JrKS39GQphWRFrR6Rxu32HgHkqnebW3T7XKVJoRr3x55dGur43olklcdMSq7TOpNx9FDNL4i4dYpDyyjBJohySeR1BWbSHqJWo+IdOOFpNNz2ICr2jA3ngsBPByzUlk0Nr2zDVRfGfGeiZaMPd6BQbMLHVrU0cs8PX452MbNggwOVkN8cYPHGaXQOokzUAy13RMZtRRSqREFq+6oAk0evXXiHPAiGRRADoUYiwpYfKmw5k2nTISu5EpqTXOw/RlicgaHqgP+ubTc8EJ4QzCnBLMWDop+04+P0Ntzy0ngGRfdibhJ3ChIHbQQx+Ner2JCsrTlglUYfIT2Cw4VMvdc2ItaV3MAC2dt0cn7NK2ZLK933nMOwspa',
    'Cookie': 'BIDUPSID=B7CB7F26DDDA7D98FF29C3EEC2AFEE2E; PSTM=1682489485; BAIDUID=B7CB7F26DDDA7D988547B56FBC007491:FG=1; BAIDUID_BFESS=B7CB7F26DDDA7D988547B56FBC007491:FG=1; ZFY=YlAwfOaBfcP52N:AR2NYPavFtVsbTy8X5ubtZIMWNoqM:C; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1686816274,1686912230,1687238103; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1687238991; ab_sr=1.0.1_ZjFiNjI5YWYyMzkzMjkyNzA1YjkzY2Q0NDdjYjc5MGU3Mzg1NTExNzczODA1YzliOWJlMjhhMzE0NjM0MTY0YjVmNGMxOWM3MTRkYmRjMDBiZGFmZTgwNTNhZGI5OTdlNzFiN2M2ZWIxOTEyZWY2NWEwM2ZiZGE5NzA3YzVmOTYzYjZjNTc4ZWNhZGJmMTA0NDFlNjc5MTJiMzkxMTg0OQ==',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
# 发送 post 请求，传递数据字典 dic
res = requests.post(url, data=dic, headers=headers)
# 输出结果
print(res.json()['trans_result']['data'][0]['dst'])