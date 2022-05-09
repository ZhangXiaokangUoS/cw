# coding=utf-8

import smtplib

HOST = "smtp.office365.com"
PORT = 587
FROM_USER = "zxk18840831142@outlook.com"
PASSWORD = "a2762789.0"


class MailBase:

    def __init__(self, to_user, subject="", content=""):
        self.to_user = to_user
        self.subject = subject
        self.content = content

    def __str__(self):
        return "\r\n".join([
            "from: {}".format(FROM_USER),
            "to: {}".format(self.to_user),
            "Subject: {}".format(self.subject),
            "",
            self.content
        ])

    def __len__(self):
        return len(str(self))


class RegisterSuccessMail(MailBase):

    def __init__(self, to_user, user_name):
        super().__init__(to_user=to_user, subject="Do not reply -- Register successfully!")

        self.user_name = user_name

        self.content = "Dear {},"\
                       "\n\n"\
                       "Welcome to join 3ZL Q&A platform. Hope you can enjoy your every question and answer."\
                       "\n\n"\
                       "Please click the link http://8.208.90.158/activate/{} to activate your account, " \
                       "otherwise you will not be able to log in to the platform normally."\
                       "\n\n"\
                       "Kind regards,"\
                       "\n"\
                       "3ZL Team".format(user_name, user_name)


def send_mail(to_user, body):
    server = smtplib.SMTP(HOST, PORT)
    server.starttls()
    # print(body)
    for i in range(5):
        try:
            server.login(FROM_USER, PASSWORD)
            server.sendmail(FROM_USER, to_user, body)
            server.close()
            return 0
        except Exception as e:
            print("[SEND MAIL ERROR] ", e)
    # if i == 4:
    #     return -1


if __name__ == "__main__":
    to = "xz1a21@soton.ac.uk"
    data = str(RegisterSuccessMail(to, "ZXK"))
    send_mail(to, data)
