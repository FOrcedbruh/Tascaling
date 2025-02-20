


class BaseException(Exception):
    
    def __init__(self, status: int, detail: str):
        self.status: int = status
        self.detail: str = detail
