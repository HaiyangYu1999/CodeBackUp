#!/root/Python-3.6.0 python3
from email.mime.text import MIMEText
from smtplib import SMTP_SSL


def send_mail(username, passwd, recv, title, content, mail_host='smtp.qq.com', port=465):
    msg = MIMEText(content)
    msg['Subject'] = title
    msg['From'] = username
    msg['To'] = recv
    print('Begin Connect...')
    smtp = SMTP_SSL(mail_host, port=port)
    print('Begin Login...')
    smtp.login(username, passwd)
    print('Begin Send...')
    smtp.sendmail(username, recv, msg.as_string())
    smtp.quit()
    print('email send success.')



title="英雄难度副本:专业课, 期末，保研"
content="笨猪加油~"
email_user = '1572808459@qq.com'
email_pwd = 'txmeskvtpydujgij'
maillist1 = '1572808459@qq.com'
maillist2 = '676393790@qq.com'
send_mail(email_user, email_pwd, maillist1, title, content)
send_mail(email_user, email_pwd, maillist2, title, content)
