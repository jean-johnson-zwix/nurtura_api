from sqlalchemy.orm import Session
from model import UserProfile, UserCredential 
from schemas import CreateUserProfileRequest, UserLogin
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

def userlogin(db: Session, req: UserLogin):
    username = req.user_name
    password = req.password
    ##return {password}       ##Uncomment this to see the password being inconsistently hashed.
    # Get user profile by username
    user_profile = db.query(UserProfile).filter(UserProfile.user_name == username).first()

    if not user_profile:
        return {"message": "User does not exist"}

    user_id = user_profile.user_id

    # Get credentials for the user ID
    credentials = db.query(UserCredential).filter(UserCredential.user_id == user_id).first()

    ##return {credentials.hashed_password}
    if util.verify_password(password,credentials.hashed_password):
        # Login successful, return user profile
        return user_profile

    return {"message": "Incorrect password"}

     
    