import uuid
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import CookieTransport, JWTStrategy, AuthenticationBackend

from src.config import SECRET_PHRASE
from src.auth.models import User
from src.auth.manager import get_user_manager

cookie_transport = CookieTransport(cookie_max_age=3600, cookie_name="TheMostDeliciousCookies")

SECRET = SECRET_PHRASE


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()