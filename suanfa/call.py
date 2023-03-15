import requests
import jsonpath


class Call:
    def TCS_call(self, data, sort):
        ficq452b = data[sort[0]]
        fiq460b = data[sort[1]]
        ti451b = data[sort[2]]
        or1_cur_b3 = data[sort[3]]

        format_data = {
            "runStatus": 0,
            "timestamp": 1647246489,
            "params": {
                "15100FICQ452B.PIDA.PV": ficq452b,
                "15100FIQ460B.PVALGO.PV": fiq460b,
                "15100Ti451b.DACA.PV": ti451b,
                "15100OR1_CUR_B3.daca.pv": or1_cur_b3,
                "dcs": 1.1
                },
            "times": 0
        }
        url = "http://10.88.36.227:5000/api/v1/tcs_model"
        headers = {'Content-Type': 'application/json'}

        res = requests.request("post", url, json=format_data, headers=headers)
        body_json = res.json()
        value = jsonpath.jsonpath(body_json, '$..body')[0]

        return value

    def H2_call(self, data, sort):
        ficq452b = data[sort[0]]
        ti451b = data[sort[1]]
        or1_cur_b3 = data[sort[2]]
        ficq451b = data[sort[3]]

        format_data = {
            "runStatus": 0,
            "timestamp": 1647246489,
            "params": {
                "15100FICQ452B.PIDA.PV": ficq452b,
                "15100FICQ451B.PIDA.PV": ficq451b,
                "15100Ti451b.DACA.PV": ti451b,
                "15100OR1_CUR_B3.daca.pv": or1_cur_b3
            },
            "times": 0
        }
        url = "http://10.88.36.227:5000/api/v1/h2_model"
        headers = {'Content-Type': 'application/json'}

        res = requests.request("post", url, json=format_data, headers=headers)
        body_json = res.json()
        value = jsonpath.jsonpath(body_json, '$..body')[0]

        return value

    def elec_call(self, data, sort):
        format_data = {
            "runStatus": 0,
            "timestamp": 1647246489,
            "params": {
                "15100FICQ452B.PIDA.PV": data[sort[0]],
                "15100FICQ451B.PIDA.PV": data[sort[1]],
                "15100PI454B.DACA.PV": data[sort[2]],
                "15100TIC453B.PIDA.PV": data[sort[3]],
                "15100Ti452b.DACA.PV": data[sort[4]],
                "15100Pi452b.DACA.PV": data[sort[5]],
                "15100Ti451b.DACA.PV": data[sort[6]],
                "15100Tic457b.pida.pv": data[sort[7]],
                "15100Fiq455b.PVALGO.PV": data[sort[8]],
                "15100Fiq454b.PVALGO.pv": data[sort[9]],
                "15100OR1_CUR_B3.DACA.pv": data[sort[10]],
                "15100OR2_CUR_B3.DACA.PV": data[sort[11]],
                "15100mr2_CUR_B3.DACA.PV": data[sort[12]],
                "15100ir_CUR_B3.DACA.PV": data[sort[13]],
                "dcs": 1.1
            },
            "times": 0
        }
        url = "http://10.88.36.227:5000/api/v1/elec_model"
        headers = {'Content-Type': 'application/json'}
        # print(format_data)
        res = requests.request("post", url, json=format_data, headers=headers)
        # print(res)
        body_json = res.json()
        # print(body_json)
        value = jsonpath.jsonpath(body_json, '$..body')[0]
        # print(value)
        return value
