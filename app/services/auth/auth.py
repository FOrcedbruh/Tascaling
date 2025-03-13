from app.repositories import UsersRepository
from app.dto.auth.auth import LoginSchema, RegistrationSchema, LoginSuccessSchema, JWTPayloadAccessSchema, JWTPayloadRefreshSchema
from app.utils.jwt.hash_password import hash_password, validate_password
from app.utils.exceptions.AuthExceptions import BadPassword, UserAlreadyExists, InvalidToken
from app.utils.jwt.create import create_access_token, create_refresh_token
from app.utils.jwt.encode_decode import decode_jwt

class AuthService():

    def __init__(self, repository: UsersRepository):
        self.repository: UsersRepository = repository

    def check_password(self, password: str, hashed: bytes) -> bool:
        res = validate_password(password=password, hashed=hashed)
        if not res:
            raise BadPassword()

    async def login(self, data: LoginSchema) -> LoginSuccessSchema:
        user = await self.repository.get_user_by_username(data=data.username)
        self.check_password(password=data.password, hashed=user.password)

        payload_access_data = JWTPayloadAccessSchema(age=user.age, username=user.username, sub=str(user.id))
        payload_refresh_data = JWTPayloadRefreshSchema(sub=str(user.id))

        access_token: str = create_access_token(data=payload_access_data)
        refresh_token: str = create_refresh_token(data=payload_refresh_data)

        return LoginSuccessSchema(
            access_token=access_token,
            refresh_token=refresh_token
        )
    
    async def registration(self, data: RegistrationSchema) -> LoginSuccessSchema:
        user = await self.repository.get_user_for_create(data=data.username)
        if user:
            raise UserAlreadyExists(detail=f"User with username {data.username} already exists")
        
        hashed_password: bytes = hash_password(password=data.password)

        data_dict = data.model_dump(exclude_none=True)
        data_dict["password"] = hashed_password

        user = await self.repository.create_one(data=data_dict)

        payload_access_data = JWTPayloadAccessSchema(age=user.age, username=user.username, sub=str(user.id))
        payload_refresh_data = JWTPayloadRefreshSchema(sub=str(user.id))

        access_token: str = create_access_token(data=payload_access_data)
        refresh_token: str = create_refresh_token(data=payload_refresh_data)

        return LoginSuccessSchema(
            access_token=access_token,
            refresh_token=refresh_token
        )
    
    async def refresh(self, refresh_token: str) -> str:
        payload_data: dict = decode_jwt(token=refresh_token)

        user = await self.repository.get_one_by_id(id=payload_data["sub"])
    
        if not user:
            raise InvalidToken()
        
        access_token: str = create_access_token(data=JWTPayloadAccessSchema(age=user.age, username=user.username, sub=str(user.id)))

        return LoginSuccessSchema(
            access_token=access_token
        )