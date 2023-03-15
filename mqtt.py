import paho.mqtt.client as mqtt
import json

HOST = "172.19.100.4"
PORT = 1883

mqttClient = mqtt.Client()

# 网关编号
agentCode = "5000040"
# 指令结果
rs = 0


# 连接MQTT服务器
def on_mqtt_connect():
    mqttClient.connect(HOST, PORT, 60)
    mqttClient.loop_start()


# publish 消息
def on_publish(topic, payload, qos):
    mqttClient.publish(topic, payload, qos)


# 消息处理函数
def on_message_come(lient, userdata, msg):
    print("subscribe %s: %s" % (msg.topic, str(msg.payload)))
    print("\n")
    print("---------------------------------------")
    request = json.loads(msg.payload)

    # 获取userId
    userid = request['c'][0]['cmds'][0]['userid']
    response = {
        "resps": [
            {
                "rs": rs,
                "userid": userid
            }
        ]
    }

    # 发送响应
    mqttClient.publish("/at/" + agentCode + "/[62]", "[62]" + json.dumps(response), 2)
    print("publish /at/%s/[62]: [62]%s" % (agentCode, json.dumps(response)))
    print("\n")
    print("---------------------------------------")


# subscribe 消息
def on_subscribe():
    mqttClient.subscribe(agentCode + "/COMMAND", 2)
    # 消息到来处理函数
    mqttClient.on_message = on_message_come


def main():
    on_mqtt_connect()
    on_subscribe()
    while True:
        pass


if __name__ == '__main__':
    main()
