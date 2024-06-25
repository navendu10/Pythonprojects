import smtplib, ssl


def send_email1(message):
    host = "smtp.gmail.com"
    port = 465

    username = "nav.vyas1005@gmail.com"
    password = "xuyg brxt bvti nrzn"

    receiver = "nav.vyas1005@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
