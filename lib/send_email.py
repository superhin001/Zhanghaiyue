"""发送邮件"""
import smtplib
from email.mime.text import MIMEText #邮件正文
from email.mime.multipart import MIMEMultipart #上传附件
import sys
sys.path.append("..")  # 提升包搜索路径到项目路径
from config import config as cf

def send_report():
    msg=MIMEMultipart()#混合格式的邮件
    #邮件正文
    body=MIMEText("测试报告","html","utf-8")#plain是普通文本，可以换成html
    msg.attach(body)#添加到正文里
    #邮件头
    msg['From'] = cf.sender
    msg["To"] = cf.receiver
    msg['Subject'] = cf.subject
    #报告附件
    with open (cf.report_file,"rb") as f:
        att_file=f.read()
    att1 = MIMEText(att_file, 'base64', 'utf-8')#转换成base64格式的，对一些非文本的传输
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="report.html"'
    msg.attach(att1)
    #发送邮件
    smtp = smtplib.SMTP_SSL(cf.smtp_server)
    smtp.login(cf.smtp_user, cf.smtp_password)
    smtp.sendmail(cf.sender,cf.receiver, msg.as_string())
    cf.logging.info("发送完成")
    smtp.quit()

if __name__=="__main__":
    send_report()


'''
"""发送邮件"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
sys.path.append("..")  # 提升包搜索路径到项目路径
from config import config as cf

# 发送报告
def send_report():
    msg = MIMEMultipart() # 混合格式的邮件
    # 邮件正文
    body = MIMEText('测试报告', 'html', 'utf-8')
    msg.attach(body)
    # 邮件头
    msg['From'] = cf.sender
    msg['To'] = cf.receiver
    msg['Subject'] = cf.subject
    # 报告附件
    with open(cf.report_file,'rb') as f:
        att_file = f.read()
    att1 = MIMEText(att_file, 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="report.html"'
    msg.attach(att1)
    # 发送邮件
    smtp = smtplib.SMTP_SSL(cf.smtp_server)
    smtp.login(cf.smtp_user, cf.smtp_password)
    smtp.sendmail(cf.sender, cf.receiver, msg.as_string())
    cf.logging.info("send email done")

if __name__ == "__main__":
    send_report()
    '''