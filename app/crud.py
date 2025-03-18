from sqlalchemy.orm import Session
from model import UserProfile, UserCredential
from schemas import CreateUserProfileRequest
import util

# Create a new User Profile and User Credential
def create_user(db:Session, req = CreateUserProfileRequest):

    # Save the User Profile Information
    _user_profile = UserProfile(
        user_name=req.user_name,
        first_name=req.first_name,
        last_name=req.last_name,
        email=req.email,
        age=req.age,
        height=req.height,
        weight=req.weight,
    )
    db.add(_user_profile)
    db.commit()
    db.refresh(_user_profile)
    user_id = _user_profile.user_id

    # Save the User Credential
    _user_credential = UserCredential(user_id=user_id, hashed_password=util.hash_password(req.password))
    db.add(_user_credential)
    db.commit()
    db.refresh(_user_credential)
    return _user_profile