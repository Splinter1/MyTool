import csv
import requests


if __name__ == '__main__':
    all_data = []
    with open("data.csv", 'r') as file:
        # 创建CSV读取器
        reader = csv.reader(file)
        # 跳过标题行
        next(reader)
        # 逐行读取CSV文件中的数据
        for row in reader:
            # 打印每一行数据
            all_data.append(row)
    print(all_data)

    for i in range(300):
        url = 'http://test.venus.wxhundun.com/service-da-cim/mgnt/subject-directory/item/config/itemInfo'
        headers = {'Content-Type': 'application/json;charset=UTF-8',
                   "Authorization": "bearer 084750fe-c785-4295-a729-22d6e98aed8e"}
        formdata = {
                        "iotPointList": [
                            {
                                "itemName": "水表总量统计",
                                "itemId": "47183",
                                "id": "47183",
                                "thingModelCode": "Water",
                                "cim": "WATER",
                                "name": "水表总量统计",
                                "alias": "water",
                                "unit": "unit016",
                                "description": "",
                                "decimalPlace": "2",
                                "sequence": 1,
                                "modeType": "READ",
                                "itemType": "IOT_NUMERICAL",
                                "dataType": "ACCUMULATE",
                                "attributesType": "OPTIONAL",
                                "itemSourceType": "NORMAL",
                                "ratio": 1,
                                "type": "2",
                                "agentItemName": "1",
                                "agentItemIndex": "anylink&3701558&3701558_"+str(i+301),
                                "acquisitionMethod": 0
                            }
                        ],
                        "subjectId": str(all_data[i][0])
                    }
        print(formdata)
        res = requests.request("post", url, json=formdata, headers=headers)
        print(res)

