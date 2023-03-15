import requests
import jsonpath
import time
import datetime
from datetime import datetime as dd


def view_dinner(token):
    url = "http://xwjgsw.ixinwu.com/web/api/weixinPos/dining/goodslist_tese?roomType=1"
    headers = {'Host': 'xwjgsw.ixinwu.com',
               'Accept-Encoding': 'gzip, deflate',
               'Authorization1': 'undefined',
               'Connection': 'keep-alive',
               'Accept': 'application/json,application/excel,text/plain,*/*',
               'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.29(0x18001d37) NetType/WIFI Language/zh_CN',
               'Authorization': token,
               'Referer': 'http://xwjgsw.ixinwu.com/wx/',
               'Accept-Language': 'zh-CN,zh-Hans;q=0.9'
               }

    res = requests.request("get", url, headers=headers)
    body_json = res.json()
    try:
        value = jsonpath.jsonpath(body_json, '$..gcode')[0]
    except:
        value = None

    return value


def add_dinner(gcode, token):
    url = "http://xwjgsw.ixinwu.com/web/api/weixinPos/dining/orderAdd_tese?goods_id="+gcode
    headers = {'Host': 'xwjgsw.ixinwu.com',
               'Accept-Encoding': 'gzip, deflate',
               'Authorization1': 'undefined',
               'Connection': 'keep-alive',
               'Accept': 'application/json,application/excel,text/plain,*/*',
               'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.29(0x18001d37) NetType/WIFI Language/zh_CN',
               'Authorization': token,
               'Referer': 'http://xwjgsw.ixinwu.com/wx/',
               'Accept-Language': 'zh-CN,zh-Hans;q=0.9'
               }

    res = requests.request("get", url, headers=headers)
    body_json = res.json()
    value = jsonpath.jsonpath(body_json, '$..msg')[0]

    return value


def bug_dinner(token):
    while True:
        good_code = view_dinner(token)
        if good_code is not None:
            print("gcode获取成功为---------"+good_code)
            while True:
                value = add_dinner(good_code, token)
                if value == "您已经预约过特色餐了":
                    print("抢购成功")
                    break
                else:
                    print("抢购失败继续抢购,code为 "+good_code+" msg为 "+value)
                    time.sleep(0.5)
                    continue
            break
        else:
            print("还没到时间，继续刷接口")
            time.sleep(1)
            continue

    return value

def funcname():
    r1 = requests.get(url='http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp',
                      headers={
                          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'})
    x = eval(r1.text)
    timeNum = int(x['data']['t'])
    timeStamp = float(timeNum / 1000)
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime


if __name__ == '__main__':
    token = input("请输入token")
    now_time = funcname()
    # null_date = (dd.strptime(now_time, '%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
    now_day = funcname().split(" ", 1)[0]
    buy_time = "12:00:16"
    real_bug_time = now_day + " " + buy_time
    t3 = time.mktime(time.strptime(real_bug_time, "%Y-%m-%d %H:%M:%S")) - time.mktime(
        (time.strptime(funcname(), "%Y-%m-%d %H:%M:%S")))
    print(t3)
    if t3 < 0:
        print("已经过12点啦")
    else:
        print("开始执行，距离12点还有" + str(t3) + "秒")
        time.sleep(t3)
        print(bug_dinner(token))
