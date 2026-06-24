from fastapi import APIRouter, HTTPException, Depends

import database
import schemas
import auth

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(user: schemas.UserCreate):

    conn = database.get_connection()
    cur = conn.cursor()

    existing = cur.execute(
        "SELECT * FROM users WHERE email=?",
        (user.email,)
    ).fetchone()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    hashed = auth.hash_password(user.password)

    cur.execute(
        "INSERT INTO users(email,password) VALUES (?,?)",
        (user.email, hashed)
    )

    conn.commit()
    conn.close()

    return {"message": "User registered"}


@router.post("/login")
def login(data: schemas.LoginRequest):

    conn = database.get_connection()
    cur = conn.cursor()

    user = cur.execute(
        "SELECT * FROM users WHERE email=?",
        (data.email,)
    ).fetchone()

    conn.close()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not auth.verify_password(
        data.password,
        user["password"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = auth.create_token(data.email)

    return {"token": token}


@router.get("/me")
def me(
    email: str = Depends(auth.get_current_user)
):
    return {"email": email}