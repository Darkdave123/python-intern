from fastapi import APIRouter, HTTPException, Depends
from database import get_connection
from schemas import UserRegister, UserLogin
from auth import (
    hash_password,
    verify_password,
    sessions,
    get_current_user
)

import uuid

router = APIRouter()


@router.post("/register")
def register(user: UserRegister):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (user.email,)
    )

    if cursor.fetchone():
        conn.close()
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    cursor.execute(
        """
        INSERT INTO users(email, hashed_password)
        VALUES (?,?)
        """,
        (
            user.email,
            hash_password(user.password)
        )
    )

    conn.commit()
    conn.close()

    return {"message": "User registered"}


@router.post("/login")
def login(user: UserLogin):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (user.email,)
    )

    db_user = cursor.fetchone()

    conn.close()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        user.password,
        db_user["hashed_password"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = str(uuid.uuid4())

    sessions[token] = user.email

    return {"token": token}


@router.get("/me")
def me(
    current_user: str = Depends(get_current_user)
):
    return {
        "email": current_user
    }