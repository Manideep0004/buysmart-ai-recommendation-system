from fastapi import APIRouter, HTTPException, status
from ..schemas.user import UserAuth, UserOut, TokenSchema
from ..services.user import UserService
from ..auth.utils import verify_password, create_access_token, create_refresh_token

auth_router = APIRouter()

@auth_router.post('/signup', summary="Create new user", response_model=UserOut)
async def create_user(data: UserAuth):
    # Check if user already exists
    user = await UserService.get_user_by_email(data.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )
    
    new_user = await UserService.create_user(data)
    return new_user

@auth_router.post('/login', summary="Create access and refresh tokens for user", response_model=TokenSchema)
async def login(data: UserAuth):
    user = await UserService.get_user_by_email(data.email)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    hashed_pass = user['password']
    if not verify_password(data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    
    return {
        "access_token": create_access_token(user['email']),
        "refresh_token": create_refresh_token(user['email']),
    }
