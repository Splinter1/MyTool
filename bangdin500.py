import mysql.connector
import requests


def sql_query(N):
    # 连接数据库
    cnn = mysql.connector.connect(
        host="10.88.33.208",  # 数据库主机地址
        user="root",  # 数据库用户名
        passwd="#20as3SElksds0ew98!",  # 数据库密码
        port="3306",
        database="service_da_cim")
    # 根据设备编码查询物模型id
    query_model_id = "SELECT id FROM `service_da_cim`.`tb_da_thing_model_item` WHERE `cim` = 'testitem"+str(N)+"'"
    # print(query_model_id)
    cursor = cnn.cursor()
    cursor.execute(query_model_id)
    res = cursor.fetchall()
    # print(res)

    # byte->string: read_str = res[0][0].decode('utf-8')
    cursor.close()
    cnn.close()
    # 传参给clickhouse查询用
    return res[0][0]


def call(N):
    print("开始第"+str(N))
    token = "c6024cb9-346b-4ef0-ada9-d0c193145673"
    id = sql_query(N)
    formdata = {
    "iotPointList": [
            {
                "acquisitionMethod": 0,
                "agentItemIndex": "anylink&3701290&3701290_"+str(N),
                "cim": "testitem"+str(N),
                "decimalPlace": "1",
                "itemId": id,
                "ratio": 1
            }
        ],
        "subjectId": '228375'
    }

    url = "http://test.venus.wxhundun.com/service-da-cim/mgnt/subject-directory/item/config/itemInfo"

    headers = {'Content-Type': 'application/json;charset=UTF-8',
               "Authorization": "bearer " + token}
    print(formdata)
    res = requests.request("post", url, json=formdata, headers=headers)
    # return res

def call1(N):
    id = sql_query(N)
    formdata = {
                "acquisitionMethod": 0,
                "agentItemIndex": "anylink&3701290&3701290_" + str(N),
                "cim": "testitem" + str(N),
                "decimalPlace": "1",
                "itemId": id,
                "ratio": 1
            }
    print(str(formdata)+',')

if __name__ == '__main__':
    for x in range(500):
        call1(x+1)

    # print(sql_query(1))