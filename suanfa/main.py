from handle_excel_xlrd import HandExcel
from call import Call


def read_excel(row):
    row_data = HandExcel().get_rows_value("data", row)
    return row_data


def mape(real, result):
    mape_value = round((abs(real - float(result)) / real), 5)
    return mape_value


def rows(row):
    rows_num = HandExcel().get_cells_num("data", row)
    return rows_num


rows_long = HandExcel().get_rows("data")


def run_TCS():
    ficq452b = rows('ficq452b')
    tcs_sort = [rows('ficq452b'), rows('fiq460b'), rows('ti451b'), rows('or1_cur_b3')]

    for i in range(rows_long-31):
        print("开始运行第" + str(i + 1) + "条数据")
        data = read_excel(i+2)
        result = Call().TCS_call(data, tcs_sort)
        print(result[0])
        real_data = read_excel(i + 2 + 30)

        format_mape = mape(real_data[ficq452b], result[0])
        print("本条数据偏差率" + str(format_mape))

        # 写入
        HandExcel().write_list_data("result", [[i + 1, real_data[ficq452b], result[0],
                                               format_mape]])


def run_H2():
    ficq451b = rows('ficq451b')
    h2_sort = [rows('ficq452b'), rows('ti451b'), rows('or1_cur_b3'), rows('ficq451b')]

    for i in range(rows_long-31):
        print("开始运行第" + str(i + 1) + "条数据")
        data = read_excel(i+2)
        result = Call().H2_call(data, h2_sort)
        real_data = read_excel(i + 2 + 30)

        format_mape = mape(real_data[ficq451b], result[0])
        # print("本条数据偏差率" + str(format_mape) + "%")
        print("本条偏差率 %.4f" % format_mape)

        # 写入
        HandExcel().write_list_data("result", [[i + 1, real_data[ficq451b], result[0],
                                                format_mape]])


def run_Ele():
    or1_cur_b3 = rows('or1_cur_b3')
    or2_cur_b3 = rows('or2_cur_b3')
    or3_cur_b3 = rows('or3_cur_b3')
    mr1_cur_b3 = rows('mr1_cur_b3')
    mr2_cur_b3 = rows('mr2_cur_b3')
    ir_cur_b3 = rows('ir_cur_b3')
    h2_sort = [rows('ficq452b'),
               rows('ficq451b'),
               rows('pi454b'),
               rows('tic453b'),
               rows('ti452b'),
               rows('pi452b'),
               rows('ti451b'),
               rows('tic457b'),
               rows('fiq455b'),
               rows('fiq454b'),
               rows('or1_cur_b3'),
               rows('or2_cur_b3'),
               rows('mr2_cur_b3'),
               rows('ir_cur_b3')]

    for i in range(rows_long-31):
        print("开始运行第" + str(i+1) + "条数据")
        data = read_excel(i+2)
        result = Call().elec_call(data, h2_sort)
        real_data = read_excel(i + 2 + 30)

        or1_mape = mape(or1_cur_b3, result[0])
        or2_mape = mape(or2_cur_b3, result[1])
        or3_mape = mape(or3_cur_b3, result[2])
        mr1_mape = mape(mr1_cur_b3, result[3])
        mr2_mape = mape(mr2_cur_b3, result[4])
        ir_mape = mape(ir_cur_b3, result[5])

        print("or1偏差率 %.4f, or2偏差率 %.4f, or3偏差率 %.4f, mr1偏差率 %.4f, mr2偏差率 %.4f, ir偏差率 %.4f" %(or1_mape, or2_mape, or3_mape, mr1_mape, mr2_mape, ir_mape))

        # 数据组装 并 写入
        list_data = [[i+1,
                      real_data[or1_cur_b3], result[0], or1_mape,
                      real_data[or2_cur_b3], result[1], or2_mape,
                      real_data[or3_cur_b3], result[2], or3_mape,
                      real_data[mr1_cur_b3], result[3], mr1_mape,
                      real_data[mr2_cur_b3], result[4], mr2_mape,
                      real_data[ir_cur_b3], result[5], ir_mape]]
        HandExcel().write_list_data("result", list_data)


if __name__ == '__main__':
    run_Ele()
