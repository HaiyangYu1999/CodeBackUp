import smtplib

from email.mime.text import MIMEText


def send_mail(username, passwd, recv, title, content, mail_host='smtp.qq.com', port=465):
    msg = MIMEText(content)

    msg['Subject'] = title

    msg['From'] = username

    msg['To'] = recv

    print('Begin Connect...')

    smtp = smtplib.SMTP_SSL(mail_host, port=port)

    print('Begin Login...')

    smtp.login(username, passwd)

    print('Begin Send...')

    smtp.sendmail(username, recv, msg.as_string())

    smtp.quit()

    print('email send success.')


if __name__ == '__main__':
    email_user = '1572808459@qq.com'

    email_pwd = 'txmeskvtpydujgij'

    maillist = '1572808459@qq.com'

    title = '长沙市岳麓区 10月24日20时 周三  小雨转中雨  18/23°C'

    content = '24日夜间:小雨,18℃\n25日白天:中雨,23℃\n穿衣指数:建议穿薄外套或牛仔裤等服装。'

    send_mail(email_user, email_pwd, maillist, title, content)
