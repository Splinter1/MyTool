import os
import sys
import time
import tkinter
import tkinter.font as tkFont

import gitlab
import yaml


class Text():

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("版本查询小工具")
        self.root['width'] = 500
        self.root['height'] = 400

        #窗口布局
        self.frame = [tkinter.Frame(), tkinter.Frame(), tkinter.Frame()]

        #输入消息Text的滚动条
        self.inputTextScrollBar = tkinter.Scrollbar(self.frame[0])
        self.inputTextScrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        #输入消息Text，并与滚动条绑定
        ft = tkFont.Font(family='Fixdsys', size=11)
        self.inputText = tkinter.Text(self.frame[0], width=70, height=18, font=ft)
        self.inputText['yscrollcommand'] = self.inputTextScrollBar.set
        self.inputText.pack(expand=1, fill=tkinter.BOTH)
        self.inputTextScrollBar['command'] = self.inputText.yview()
        self.frame[0].pack(expand=1, fill=tkinter.BOTH)

        #”查询“按钮
        self.queryButton = tkinter.Button(self.frame[1], text='查询', width=10, command=self.Query)
        # self.queryButton = tkinter.Button(self.frame[1], text='查询', width=10)
        self.queryButton.pack(expand=1, side=tkinter.BOTTOM and tkinter.RIGHT, padx=25, pady=5)

        #“关闭”按钮
        self.closeButton = tkinter.Button(self.frame[1], text='关闭', width=10, command=self.close)
        # self.closeButton = tkinter.Button(self.frame[1], text='关闭', width=10)
        # self.closeButton.pack(expand=1, fill=tkinter.BOTH)
        self.frame[1].pack(expand=1, fill=tkinter.BOTH)
        self.closeButton.pack(expand=1, side=tkinter.BOTTOM and tkinter.RIGHT, padx=25, pady=5)


        # 显示消息Text右边的滚动条
        self.chatTextScrollBar = tkinter.Scrollbar(self.frame[2])
        self.chatTextScrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        # 显示消息Text，并绑定上面的滚动条
        ft = tkFont.Font(family='Fixdsys', size=11)
        self.chatText = tkinter.Listbox(self.frame[2], width=70, height=18, font=ft)
        self.chatText['yscrollcommand'] = self.chatTextScrollBar.set
        self.chatText.pack(expand=1, fill=tkinter.BOTH)
        self.chatTextScrollBar['command'] = self.chatText.yview()
        self.frame[2].pack(expand=1, fill=tkinter.BOTH)

        self.root.mainloop()
        # #标签，分开消息显示Text和消息输入Text
        # label = tkinter.Label(self.frame[3], height=2)
        # label.pack(fill=tkinter.BOTH)
        # self.frame[3].pack(expand=1, fill=tkinter.BOTH)

    def prod(self, services):
        # 1、通过gitlab库访问gitlab项目地址
        GITURL = "http://172.19.32.226:8900/"  # gitlab的域名
        GITTOKEN = "8fo1t76T5PoxnidtyET9"  # 用户访问的token
        GITORG = "devops"  # 项目所有者
        project_name = "kubernetes-workloads"  # 要访问的项目名

        # 2、获取项目文件中的内容保存到临时yml文件中
        gl = gitlab.Gitlab(GITURL, GITTOKEN)
        project = gl.projects.get(GITORG + '/' + project_name)
        # 3、获取文件中文件名称
        # services = ["auth-service","auth-se rvice-web"]
        # for i in items:
        #     m = '-'.join(i['name'].split("-")[:-2])
        #     services.append(m)
        # services.pop(0)

        # services = []
        Prod_line = ["venus-2.0", "iheatlab-2.0", "aircooling-2.0", "pms-2.0"]
        for j in Prod_line:
            for u in services:
                git_path = j + "/prod/" + u + "-prod-dep.yml"  # 要读取的文件相对路径
                try:
                    f = project.files.get(file_path=git_path, ref='master')
                except Exception as err:
                    print( j + " not find " + u)
                    continue
                # 第一次decode获得bytes格式的内容
                file_content = f.decode()
                # 第二次decode获得str
                file_content = file_content.decode()
                s = open("test3.yml", "w")  # 把读取的结果保存起来
                s.write(file_content)
                s.close()

                # 3、对yml文件进行操作获取到想要的字段
                # f = open('D:/WebContent/venus-2.0/pre/authentication-center-pre-dep.yml','r', encoding='utf-8')
                f = open('test3.yml', 'r', encoding='utf-8')
                f_data = f.read()
                f.close()
                data = yaml.load_all(f_data, Loader=yaml.Loader)
                a = data.__next__()
                b = data.__next__()
                c = b["spec"]['template']['spec']['containers'][0]
                d = c['image']
                e = d.split("/", 2)[2]
                if e == "nginx-vts-exporter:0.10.4":
                    with open('test3.yml', 'r') as file:
                        text = file.readline()
                        counts = 1
                        while text:
                            if counts >= 110:
                                break
                            text = file.readline()
                            counts += 1
                        tmp = text.split("/", 2)[2]
                        print(tmp)
                        image = open("prod_1.txt", "a+")  # 把读取的结果保存起来
                        image.write(tmp)
                        image.close()
                else:
                    print(e)
                    image = open("prod_1.txt", "a+")  # 把读取的结果保存起来
                    image.write(e)
                    image.write('\n')
                    image.close()


    #查询当前对应服务版本
    def Query(self):
        #得到用户在Text中输入的消息
        message = self.inputText.get('1.0', tkinter.END)
        services = message.split("\n")[:-1]
        self.prod(services)
        #格式化当前的时间
        theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        f = open('prod_1.txt', 'r', encoding='utf-8')
        f_data = f.read().split("\n")[:-1]
        f.close()
        print(f_data)
        self.chatText.insert(tkinter.END, '当前生产版本结果如下 ' + theTime + ' ：\n')
        for i in f_data:
            self.chatText.insert(tkinter.END, i + '\n')

        file = open('prod_1.txt', 'w')
        file = open("prod_1.txt", 'w').close()

        self.inputText.delete(0.0, message.__len__()-1.0)
    #关闭消息窗口并退出
    def close(self):
        sys.exit()

if __name__ == '__main__':
    start = Text()
