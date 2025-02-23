from app.utils.exceptions.base import BaseException



class AuthException(BaseException):
    def __init__(self, status: int = 400, detail: str = "Authorization error"):
        super().__init__(status, detail)


class BadPassword(AuthException):
    def __init__(self, status = 400, detail = "Incorrect password"):
        super().__init__(status, detail)

class UserAlreadyExists(AuthException):
    def __init__(self, status = 400, detail = "Authorization error"):
        super().__init__(status, detail)