import smtplib
from email.utils import formataddr
from email.mime.text import MIMEText
from email.header import Header
from QueryScript import query
from config import config


def send_email(subject: str, content: str) -> None:
    smtp_config = config["smtp"]
    msg = MIMEText(content, "html", "utf-8")

    from_name = "宿舍电量警告"
    msg["From"] = formataddr((
        str(Header(from_name, "utf-8")),
        smtp_config["sender"],
    ))

    receivers = smtp_config["receiver"]
    if isinstance(receivers, list):
        msg["To"] = ",".join(receivers)
        to_addrs = receivers
    else:
        msg["To"] = receivers
        to_addrs = [receivers]

    msg["Subject"] = str(Header(subject, "utf-8"))

    with smtplib.SMTP_SSL(smtp_config["server"], int(smtp_config["port"])) as smtp:
        smtp.login(smtp_config["sender"], smtp_config["auth_code"])
        smtp.sendmail(smtp_config["sender"], to_addrs, msg.as_string())


if __name__ == "__main__":
    subject = "宿舍电量提醒"

    Synjones_Auth = config["Synjones-Auth"]
    dorm = config["dorm"]
    room = config["room"]

    last = query(dorm, room, Synjones_Auth=Synjones_Auth)
    print(f"Query result: {last}")  # 添加调试信息

    try:
        last_value = float(last)
        body = f"byd同学：<br><br>您好！<br><br>您的宿舍{dorm} {room}电量不足，仅剩{last_value}，请及时充值。"
        # last_value 为宿舍剩余电量，低于{threshold}度时发送邮件提醒，可根据实际情况修改，默认为10
        if last_value < config.get("threshold", 10):
            send_email(subject, body)
    except ValueError as e:
        print(f"Error converting query result to float: {e}")
