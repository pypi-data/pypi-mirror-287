# from typing import Sequence, Callable, Any, Dict
# from pydantic import BaseModel
# from fastapi import Depends
# from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
# from ashtree.errors import ConfigurationError, Forbidden, Unauthorized
# from app.context import ctx

# bearer = HTTPBearer()


# class AuthData(BaseModel):
#     token: str
#     payload: Dict[str, Any]


# def jwt_required(*, audience: Sequence[str]) -> Callable[..., Any]:
    
#     try:
#         import jwt # type: ignore (optional dependency)
#     except ImportError:
#         raise RuntimeError("jwt_required needs pyjwt package to be installed")
#     if not ctx.cfg.jwt.enabled:
#         raise ConfigurationError("jwt is disabled in config")
#     if ctx.cfg.jwt.secret_key is None:
#         raise ConfigurationError("jwt.secret_key must be configured to use jwt_required")
    
#     async def get_auth_data(credentials: HTTPAuthorizationCredentials = Depends(bearer)) -> AuthData:
#         if credentials.scheme != "Bearer":
#             raise Forbidden(f"scheme {credentials.scheme} is not supported")
        
#         token = credentials.credentials
#         try:
#             payload = jwt.decode(
#                 token,
#                 ctx.cfg.jwt.secret_key,
#                 audience=audience,
#                 options={"require": ["aud", "exp", "iat"]},
#                 algorithms=["HS256"]
#             )
#         except jwt.InvalidSignatureError:
#             raise Forbidden("token signature verification failed")
#         except jwt.ExpiredSignatureError:
#             raise Forbidden("token expired")
#         except jwt.MissingRequiredClaimError as e:
#             raise Forbidden(f"token is missing claim {e.claim}")
#         except jwt.InvalidAudienceError:
#             raise Forbidden(f"token audience {audience} is missing")
        
#         return AuthData(token=token, payload=payload)
    
#     return get_auth_data


from typing import Sequence, List, Callable, Optional, Awaitable
from fastapi import Depends, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.models import User, Session

bearer = HTTPBearer(auto_error=False)


class AuthData:
    user: User
    aud: List[str]

    def __init__(self, user: User, aud: Sequence[str]):
        self.user = user
        self.aud = list(aud)


async def current_session(request: Request) -> Session:
    return request.state.session


def auth_required(aud: Sequence[str]) -> Callable[..., Awaitable[AuthData]]:
    async def inner(
        session: Session = Depends(current_session),
        credentials: Optional[HTTPAuthorizationCredentials] = Depends(bearer)
    ) -> AuthData:
        user = await User.get("viert")
        if user is None:
            raise Unauthorized("authentication required")
        return AuthData(user=user, aud=[])

    return inner
