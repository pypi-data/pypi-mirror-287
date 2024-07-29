from pydantic import BaseModel, EmailStr, Field


class UserRequest(BaseModel):
    email: EmailStr
    firstname: str = Field(min_length=3)
    lastname: str = Field(min_length=3)
    username: str = Field(min_length=5)
    password: str
    is_active: bool = Field(default=False)
    # profile_image: Optional[str]

class UserResponse(BaseModel):
    id: int
    firstname:str
    lastname: str
    username:str
    email:str


class UsersVerification(BaseModel):
    password: str
    new_password: str = Field(min_length=8)


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class OtpSchema(BaseModel):
    code: int
