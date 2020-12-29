# 使用 yagmail 自动发送测试报告邮件
import os
import time
import yagmail
import zipfile


# 注意需要先开启邮箱 POP3/SMTP 服务
def send_email(report):
    yag = yagmail.SMTP(user='xx@163.com', password='授权码', host='smtp.163.com')

    # 邮件正文
    contents = [
        "测试已完成，请查看附件",
    ]
    # subject 主题  attachments 附件
    yag.send(to='yy@qq.com', subject='自动化测试报告', contents=contents,
             attachments=report)


# 使用 zipfile 压缩文件夹
def zip_dir(directory):
    zip_file = directory + '.zip'
    z = zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(directory):
        f_path = root.replace(directory, '')
        f_path = f_path and f_path + os.sep or ''
        for file in files:
            z.write(os.path.join(root, file), f_path + file)
    z.close()
    return zip_file


if __name__ == '__main__':

    current_time = time.strftime('%Y%m%d%H%M%S')
    os.system('pytest --alluredir=./{}-allure ./test_baidu_parametrize.py'.format(current_time))
    os.system('allure generate ./{0}-allure -o ./{0}-report'.format(current_time))
    zip_path = zip_dir('./{0}-report'.format(current_time))
    send_email(zip_path)

