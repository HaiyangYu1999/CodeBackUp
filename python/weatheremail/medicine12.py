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



title="午饭时间到啦，笨猪早上有没有按时吃药呢"
content="午饭要吃的清淡一点，少吃辛辣的东西多吃蔬菜水果\\n如果早上没有吃药记得中午补上呀~"
email_user = '1572808459@qq.com'
email_pwd = 'txmeskvtpydujgij'
maillist1 = '1572808459@qq.com'
maillist2 = '676393790@qq.com'
send_mail(email_user, email_pwd, maillist1, title, content)
send_mail(email_user, email_pwd, maillist2, title, content)
