import csv
import fnmatch

from handle_excel_xlrd import HandExcel
import os
from openpyxl import Workbook


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False


def type_one(data):
    real_data = data.split('\n')
    """"清理列表中单个回车以及格式化回车符号"""
    list1 = []
    for i in real_data:
        if i == "":
            continue
        if i[0].isdigit():
            list1.append(i + "\n")
        else:
            i = list1[-1].replace('\n', ';') + i + "\n"
            list1[-1] = i
    # a = ''.join(list1)
    # print(a)
    """"格式化子层级：若第三位是空格则认为其为父层级"""
    list2 = []
    for i in list1:
        if is_number(i[0]) and "." in i[-2:]:
            list2.append(i)
            continue
        if i[2] is " ":
            list2.append(i)
        else:
            i = list2[-1].replace('\n', ';') + i
            list2[-1] = i
    done_text = ''.join(list2)
    return done_text[:-1]


def type_two(data):
    real_data = data.split('\n')
    """"清理列表中单个回车以及格式化回车符号"""
    list1 = []
    for i in real_data:
        if i == "":
            continue
        if i[0].isdigit():
            list1.append(i + "\n")
        else:
            i = list1[-1].replace('\n', ';') + i + "\n"
            list1[-1] = i
    """"若第五位字符为空格则判定为子层级"""
    list2 = []
    for i in list1:
        if i[1] == ".":
            if is_number(i[0]) and "." in i[-2:]:
                list2.append(i)
                continue
            if len(i) == 2 and is_number(i[0]) and i[1] == ".":
                list2.append(i)
                continue
            if i[2] is " ":
                list2.append(i)
                continue
            if i[4] is " ":
                list2.append(i)
                val1 = "→" + i[2:].replace('\n', ';') + "\n"
                list2[-1] = val1
                continue
            if i[2] is not " " and i[4] is not " ":
                val = list2[-1].replace('\n', ';') + i
                list2[-1] = val
        if i[2] == ".":
            if is_number(i[0]) and "." in i[-2:]:
                list2.append(i)
                continue
            if len(i) == 3 and is_number(i[0]) and i[2] == ".":
                list2.append(i)
                continue
            if i[3] is " ":
                list2.append(i)
                continue
            if i[5] is " ":
                list2.append(i)
                val1 = "→" + i[3:].replace('\n', ';') + "\n"
                list2[-1] = val1
                continue
            if i[3] is not " " and i[5] is not " ":
                val = list2[-1].replace('\n', ';') + i
                list2[-1] = val
    done_text = ''.join(list2)
    return done_text[:-1]


def read_data_excel():
    file_type = "*.csv"
    # 获取当前目录
    current_dir = os.getcwd()
    # 遍历当前目录下的所有文件
    for file in os.listdir(current_dir):
        # 判断文件名是否匹配所需文件类型
        if fnmatch.fnmatch(file, file_type):
            return file


if __name__ == '__main__':
    """初始化excel表格"""
    filename = "pingcode.xlsx"
    # 检查当前目录下是否存在指定的Excel文件
    if not os.path.isfile(filename):
        print("未检测到excel，立即新建")
        # 如果文件不存在，则创建新的Excel文件
        wb = Workbook()
        wb.save(filename)
        print(f"{filename} 文件已创建")
        data_excel = read_data_excel()
        print(f"已读取到来源文件为 {data_excel}")
    else:
        # 如果文件已经存在，则输出信息
        print(f"{filename} 文件已存在，正在初始化")
        os.remove(filename)
        data_excel = read_data_excel()
        print(f"已读取到来源文件为 {data_excel}")
        wb = Workbook()
        wb.save(filename)
        print(f"{filename} 文件已创建")
    print(f"{filename} 文件已初始化完成")

    # all_data = HandExcel().get_excel_data(data_excel)
    # 打开CSV文件
    all_data = []
    with open(data_excel, 'r') as file:
        # 创建CSV读取器
        reader = csv.reader(file)
        # 跳过标题行
        next(reader)
        # 逐行读取CSV文件中的数据
        for row in reader:
            # 打印每一行数据
            all_data.append(row)

    all_list = [[], ["模块", "编号", '*标题', '维护人', '用例类型', '重要程度', '测试类型', '预估工时', '关联项目需求', '前置条件', '步骤描述', '预期结果', '关注人', '备注', '步骤数']]
    for row in all_data:
        temporary_list = []
        """"开始组装临时列表"""
        temporary_list.append("")  # 模块
        temporary_list.append("")  # 编号
        temporary_list.append(row[4])  # 标题
        temporary_list.append("")  # 维护人
        temporary_list.append(row[11])  # 用例类型
        temporary_list.append(("P" + str(row[10]))[:2])  # 重要程度
        temporary_list.append("手动")  # 测试类型
        temporary_list.append("")  # 预估工时
        temporary_list.append("")  # 关联项目需求
        temporary_list.append(row[5])  # 前置条件

        old_steps_list = row[6]  # 步骤（原始数据）

        case_steps = row[7]
        steps_num = row[16]  # 对应步骤数
        real_steps_list = row[8]  # 对应正式步骤数
        if case_steps is not "":
            if len(real_steps_list.split('\n')) == steps_num:
                case_steps_list = type_one(case_steps)
                new_steps_list = type_one(old_steps_list)
            else:
                case_steps_list = type_two(case_steps)
                new_steps_list = type_two(old_steps_list)
            temporary_list.append(new_steps_list)  # 步骤描述
            temporary_list.append(case_steps_list)  # 预期结果
        else:
            temporary_list.append("")  # 步骤描述
            temporary_list.append("")  # 预期结果

        temporary_list.append("")  # 关注人
        temporary_list.append("")  # 备注
        temporary_list.append(row[16])  # 步骤数

        all_list.append(temporary_list)

    HandExcel().write_list_data("result", all_list)
    print("格式化完毕")

