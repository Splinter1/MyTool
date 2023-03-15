import math


def dcs(data):
    scm_b3_cm = data[20]
    ti004a = data[18]
    pic007a = data[19]

    dcs_comp_params = {
        888: [11.567, 2.42365],
        887: [11.561, 2.4226],
        886: [11.556, 2.42177],
        885: [11.55, 2.42],
        884: [14.9103, 3.1253],
        883: [11.54, 2.41907],
        882: [14.71, 3.08386],
        881: [11.529, 2.41721],
        880: [16.097, 3.375],
        879: [11.518, 2.41533],
        878: [14.862, 3.11685],
        877: [11.508, 2.41368],
        876: [11.501, 2.41242],
        875: [11.496, 2.4116],
        874: [11.491, 2.41077],
        873: [11.485, 2.40973]
    }

    if scm_b3_cm >= 403:
        # tcs
        temp = ti004a
        press = pic007a
        key = press*1000
        if key not in dcs_comp_params:
            x = abs(key - 888)
            n = abs(key - 872)
            if x > n:
                key = 872
            else:
                key = 888
        data_dcs = dcs_comp_params[key][0] - dcs_comp_params[key][1]*math.log(temp)
        return data_dcs
    else:
        return None


