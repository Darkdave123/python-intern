from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from routers.auth import sessions

router = APIRouter()

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials

    if token not in sessions:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    return sessions[token]


@router.get("/")
def get_tasks(
    current_user: str = Depends(get_current_user)
):
    return {
        "message": "Protected Route",
        "user": current_user
    }