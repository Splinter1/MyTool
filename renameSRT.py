import os
import ftplib


def ftpCon():
    host = 'lzzhome.top'
    f = ftplib.FTP()
    f.encoding = 'UTF-8'
    f.connect(host, 6001)
    f.login('file', 'file5733607')

    print("FTP服务器已经成功登录")
    f.cwd("/娱乐/电视剧/最后生还者 (2023)/Season 1/")
    print('当前工作目录：', f.pwd())

    dir_list = []
    for i in f.nlst():
        if i[-3:] == "mkv":
            dir_list.append(i)
    print(dir_list)

    f.quit()
    print("FTP服务器已断开")

    return dir_list


def reName(dirname):
    count = 0
    dir_list = os.listdir(dirname)
    try:
        dir_list.remove(".DS_Store")
    except:
        print("直接开始")
    dir_list.sort()
    print(dir_list)
    movie_list = ftpCon()
    for cur_file in dir_list:
        old_dir = os.path.join(dirname, cur_file)
        filetype = os.path.splitext(cur_file)[1]  # 文件类型
        # if count < 10:
        #     str_count = "0" + str(count)
        # else:
        #     str_count = str(count)
        new_dir = os.path.join(dirname, (movie_list[count][:-4]+".force.chi") + filetype)  # 新文件
        os.rename(old_dir, new_dir)
        print(old_dir, new_dir)
        count += 1

if __name__ == "__main__":
    dirname = r"/Users/lizongzheng/Downloads/S01"
    reName(dirname)



