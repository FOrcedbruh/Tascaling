from app.repositories import UsersRepository


class UsersService:
    
    def __init__(self, repository: UsersRepository):
        self.repository = repository