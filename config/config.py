"""项目配置文件"""
import os
import logging

#项目路径
prj_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path=os.path.join(prj_path,"data")
testcase_path=os.path.join(prj_path,"testcase")
report_file=os.path.join(prj_path,"report","report.html")
log_file=os.path.join(prj_path,"log","log.txt")

#日志的配置
logging.basicConfig(level=logging.INFO,
                   format='[%(asctime)s]-%(message)s',
                   datefmt="%Y-%m-%d %H:%M:%S",
                   filename=log_file,
                   filemode="a")

#数据库配置
db_host = "115.28.108.130"
db_port = 3306
db_user = "test"
db_password = "123456"
db = "api_test"

#email配置
smtp_server = "smtp.163.com"  # smtp服务器地址
smtp_user="ivan-me@163.com"
smtp_password="hanzhichao123"

subject="接口测试报告"
sender = smtp_user#邮件发送人
receiver = "343480288@qq.com"#邮件接收人
is_send_email=False#是否发送邮件



if __name__=="__main__":
    print(prj_path)
    print(data_path)
    print(report_file)
    print(log_file)
    print(testcase_path)