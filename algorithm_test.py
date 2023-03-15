import requests

def script():
    null = None
    count = 1
    for i in range(49):
        count += 1
        print(count)
        url = 'http://10.88.36.13:8080/os-script/script/save'
        headers = {'Content-Type': 'application/json;charset=UTF-8',
                   "Authorization": "61230428d49d4eae8ce1c06550a54906"}
        formdata = {
                        "processType": "4",
                        "scriptName": str(count),
                        "content": "#jiaoben"+str(count)+"=#60dianwei1000+#60dianwei999+#60dianwei998+#60dianwei997+#60dianwei996+#60dianwei995+#60dianwei994+#60dianwei993+#60dianwei992+#60dianwei991+#60dianwei990",
                        "intervalTime": "5000",
                        "language": "CN"
                    }
        print(formdata)
        res = requests.request("post", url, json=formdata, headers=headers)
        print(res)


if __name__ == '__main__':
    script()
