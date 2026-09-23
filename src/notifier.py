"""외부 알림 전송 관련 함수 (STEP 17에서 Notebook으로 검증한 로직을 그대로 옮김).

이 모듈은 환경변수(.env)를 직접 읽지 않습니다.
Webhook URL, Gmail 주소/앱 비밀번호 같은 비밀값은 항상 호출하는 쪽(상위 계층)에서
인자로 전달받습니다.
"""

import smtplib
from email.message import EmailMessage

import requests


def send_slack_message(webhook_url, message_text):
    """
    Slack Incoming Webhook(webhook_url)으로 message_text를 전송하고 응답을 반환합니다.
    (STEP 15 로직과 동일)

    주의: 실제로 호출하면 진짜 Slack 메시지가 발송됩니다.
    """
    response = requests.post(
        webhook_url,
        json={"text": message_text},
        timeout=10,
    )
    return response


def send_gmail(gmail_address, gmail_app_password, gmail_to, subject, body):
    """
    Gmail SMTP(smtp.gmail.com:465)로 메일 1건을 발송합니다. (STEP 16 로직과 동일)

    주의: 실제로 호출하면 진짜 메일이 발송됩니다.
    """
    msg = EmailMessage()
    msg["From"] = gmail_address
    msg["To"] = gmail_to
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=20) as smtp:
        smtp.login(gmail_address, gmail_app_password)
        smtp.send_message(msg)

    return True
