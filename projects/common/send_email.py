from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


# 邮件发送者
from_addr = 'from_addr@gmail.com'
password = 'password'

to_addr = 'to_addr@qq.com'

# 发送者使用对
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# 邮件内容
msg = MIMEText('hello, send by Python……', 'plain', 'utf-8')
msg['From'] = _format_addr('briskwind <%s>' % from_addr)

# 邮件摘要
msg['Subject'] = Header('来自python SMTP……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, smtp_port)
# into TLS mode
server.starttls()
server.set_debuglevel(1)

# 登陆发送者邮箱
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
