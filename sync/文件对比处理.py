import difflib
import argparse
import sys
import gitlab
import yaml

def pre():
    GITURL = "http://172.19.32.226:8900/"  # gitlab的域名
    GITTOKEN = "8fo1t76T5PoxnidtyET9"  # 用户访问的token
    GITORG = "devops"  # 项目所有者
    project_name = "kubernetes-workloads-pre"  # 要访问的项目名

    # 2、获取项目文件中的内容保存到临时yml文件中
    gl = gitlab.Gitlab(GITURL, GITTOKEN)
    project = gl.projects.get(GITORG + '/' + project_name)

    # 3、获取文件中文件名称
    items = project.repository_tree(path='venus-2.0/pre', ref='master', recursive=True, all=True)
    services = []
    for i in items:
        m = '-'.join(i['name'].split("-")[:-2])
        services.append(m)
    services.pop(0)
    for u in services:
        git_path = "venus-2.0/pre/" + u + "-pre-dep.yml"  # 要读取的文件相对路径
        f = project.files.get(file_path=git_path, ref='master')
        file_content = f.decode()
        file_content = file_content.decode()
        s = open("test.yml", "w")  # 把读取的结果保存起来
        s.write(file_content)
        s.close()

        # 3、对yml文件进行操作获取到想要的字段
        f = open('test.yml', 'r', encoding='utf-8')
        f_data = f.read()
        f.close()
        data = yaml.load_all(f_data, Loader=yaml.Loader)
        a = data.__next__()
        b = data.__next__()
        c = b["spec"]['template']['spec']['containers'][0]
        d = c['image']
        e = d.split("/", 2)[2]
        if e == "nginx-vts-exporter:0.10.4":
            # text = linecache.getline('test.yml', 106)
            # tmp = text.split("/", 2)[2]
            # print(tmp)
            # image = open("pre.txt", "a+")  # 把读取的结果保存起来
            # image.write(tmp)
            # image.close()
            with open('test.yml', 'r') as file:
                text = file.readline()
                counts = 1
                while text:
                    if counts >= 106:
                        break
                    text = file.readline()
                    counts += 1
                tmp = text.split("/", 2)[2]
                print(tmp)
                image = open("pre.txt", "a+")  # 把读取的结果保存起来
                image.write(tmp)
                image.close()
        else:
            print(e)
            image = open("pre.txt", "a+")  # 把读取的结果保存起来
            image.write(e)
            image.write('\n')
            image.close()

def prod():
    # 1、通过gitlab库访问gitlab项目地址
    GITURL = "http://172.19.32.226:8900/"  # gitlab的域名
    GITTOKEN = "8fo1t76T5PoxnidtyET9"  # 用户访问的token
    GITORG = "devops"  # 项目所有者
    project_name = "kubernetes-workloads"  # 要访问的项目名

    # 2、获取项目文件中的内容保存到临时yml文件中
    gl = gitlab.Gitlab(GITURL, GITTOKEN)
    project = gl.projects.get(GITORG + '/' + project_name)
    project1 = gl.projects.get(GITORG + '/' + "kubernetes-workloads-pre")
    # 3、获取文件中文件名称
    items = project1.repository_tree(path='venus-2.0/pre', ref='master', recursive=True, all=True)
    services = []
    for i in items:
        m = '-'.join(i['name'].split("-")[:-2])
        services.append(m)
    services.pop(0)
    for u in services:
        git_path = "venus-2.0/prod/" + u + "-prod-dep.yml"  # 要读取的文件相对路径
        # git_path = "venus-2.0/pre/web-screen-pre-dep.yml"  # 要读取的文件相对路径
        try:
            f = project.files.get(file_path=git_path, ref='master')
        except Exception as err:
            print("not find" + u)
            a = "not find" + u
            image = open("prod.txt", "a+")  # 把读取的结果保存起来
            image.write(a)
            image.write('\n')
            image.close()
            continue
        # 第一次decode获得bytes格式的内容
        file_content = f.decode()
        # 第二次decode获得str
        file_content = file_content.decode()
        s = open("test2.yml", "w")  # 把读取的结果保存起来
        s.write(file_content)
        s.close()

        # 3、对yml文件进行操作获取到想要的字段
        # f = open('D:/WebContent/venus-2.0/pre/authentication-center-pre-dep.yml','r', encoding='utf-8')
        f = open('test2.yml', 'r', encoding='utf-8')
        f_data = f.read()
        f.close()
        data = yaml.load_all(f_data, Loader=yaml.Loader)
        a = data.__next__()
        b = data.__next__()
        c = b["spec"]['template']['spec']['containers'][0]
        d = c['image']
        e = d.split("/", 2)[2]
        if e == "nginx-vts-exporter:0.10.4":
            with open('test2.yml', 'r') as file:
                text = file.readline()
                counts = 1
                while text:
                    if counts >= 110:
                        break
                    text = file.readline()
                    counts += 1
                tmp = text.split("/", 2)[2]
                print(tmp)
                image = open("prod.txt", "a+")  # 把读取的结果保存起来
                image.write(tmp)
                image.close()
        else:
            print(e)
            image = open("prod.txt", "a+")  # 把读取的结果保存起来
            image.write(e)
            image.write('\n')
            image.close()





# 创建打开文件函数，并按换行符分割内容
def readfile(filename):
    try:
        with open(filename, 'r') as fileHandle:
            text = fileHandle.read().splitlines()
        return text
    except IOError as e:
        print("Read file Error:", e)
        sys.exit()
# 比较两个文件并输出到html文件中
def diff_file(filename1, filename2):
    text1_lines = readfile(filename1)
    text2_lines = readfile(filename2)
    d = difflib.HtmlDiff()
    # context=True时只显示差异的上下文，默认显示5行，由numlines参数控制，context=False显示全文，差异部分颜色高亮，默认为显示全文
    result = d.make_file(text1_lines, text2_lines, filename1, filename2, context=True)
    # 内容保存到result.txt文件中
    with open('result.html', 'w') as resultfile:
        resultfile.write(result)
    # print(result)
if __name__ == '__main__':
    pre()
    prod()
    # 定义必须传入两个参数，使用格式-f1 filename1 -f2 filename
    # parser = argparse.ArgumentParser(description="传入两个文件参数")
    # parser.add_argument('-f1', action='store', dest='filename1', required=True)
    # parser.add_argument('-f2', action='store', dest='filename2', required=True)
    # given_args = parser.parse_args()
    # filename1 = given_args.filename1
    # filename2 = given_args.filename2
    diff_file("pre.txt", "prod.txt")
    file = open('pre.txt','w')
    file = open("pre.txt", 'w').close()
    file1 = open('prod.txt', 'w')
    file1 = open("prod.txt", 'w').close()
