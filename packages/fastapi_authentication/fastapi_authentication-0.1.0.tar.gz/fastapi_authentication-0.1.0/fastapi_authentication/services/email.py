'''-------------------------------------------------otp start---with sign up----------------------------------------------------------'''


from email.message import EmailMessage
import smtplib
import ssl
from fastapi import HTTPException
import pyotp
from fastapi_authentication.config import EMAIL_PASSWORD, EMAIL_SENDER, OTP_SECRET_KEY


email_sender = EMAIL_SENDER
email_password = EMAIL_PASSWORD
otp_secret_key =  OTP_SECRET_KEY


def otp_generator():
    totp = pyotp.TOTP(otp_secret_key)
    return totp.now()

async def send_verification_email(receiver_email, otp):
    subject = f'{otp} is your ideamentor code'
    body = f"""
    ideamentor is your ideamentor code

        Log in to ideamentor
        Welcome back! Enter this code within the next 10 minutes to log in:

                        {otp}
    """
    em = EmailMessage()
    em["from"] = email_sender
    em["to"] = receiver_email
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, receiver_email, em.as_string())
    except smtplib.SMTPException as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to send email: {str(e)}")
