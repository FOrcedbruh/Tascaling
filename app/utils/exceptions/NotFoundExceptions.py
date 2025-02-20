from app.utils.exceptions.base import BaseException
from fastapi import status

class NotFound(BaseException):

    def __init__(
            self, 
            detail: str,
            status: int = status.HTTP_404_NOT_FOUND
        ):
        super().__init__(
            status=status,
            detail=detail
        )


class UserNotFound(NotFound): ... 

class TaskNotFound(NotFound): ...

class IdeaNotFound(NotFound): ...

