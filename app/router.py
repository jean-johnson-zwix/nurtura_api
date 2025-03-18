from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import CreateUserProfileRequest, CreateUserProfileResponse, Response
import crud

router = APIRouter()

def get_database_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/create-profile')
async def create_user_profile(req:CreateUserProfileRequest,db:Session=Depends(get_database_session)):
    _user_profile = crud.create_user(db, req)
    response = CreateUserProfileResponse(user_name=_user_profile.user_name, user_id=_user_profile.user_id)
    return Response(status_code=200,message=f"User profile created successfully for {_user_profile.first_name} {_user_profile.last_name}", result=response).dict(exclude_none=True)

