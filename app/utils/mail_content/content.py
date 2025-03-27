


class MailContent:

    @staticmethod
    def get_login_content(mail: str, username: str) -> dict:
        return {
            "to_mail": mail,
            "subject": f"{username}, new login in your account from device",
            "message": ""
        }

    @staticmethod
    def get_reg_content(mail: str, username: str) -> dict:
        return {
            "to_mail": mail,
            "subject": f"{username}, congratulations!!!",
            "message": f"{username}, thank's for registration in our service;)"
        }