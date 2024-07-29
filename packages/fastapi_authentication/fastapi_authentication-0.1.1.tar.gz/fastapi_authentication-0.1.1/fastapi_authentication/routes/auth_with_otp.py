from datetime import datetime, timedelta, timezone
from fastapi import APIRouter, Depends, HTTPException, status, Path

from typing import List

from fastapi.security import OAuth2PasswordRequestForm

from fastapi_auth import models, schemas
from fastapi_auth.con import db_dependency

from fastapi_auth.config import ALGORITHM, SECRET_KEY
from fastapi_auth.services.security import authenticate_user, create_access_token, user_dependency
from fastapi_auth.services.email import otp_generator, send_verification_email
from fastapi_auth.services.security import bcrypt_context
from jose import jwt, JWTError

# router = APIRouter(
#     prefix="/users",
#     tags=["users"]
# )


# @router.post("/new_user", status_code=status.HTTP_201_CREATED, summary="Create new user account / sign up")
async def create_new_user(userrequest, db, otp):
    '''  ## Sign Up

    This endpoint is used for creating a new user account.
    '''

    # Check if the user already exists based on email or username
    existing_user = db.query(models.User).filter((models.User.email == userrequest.email) | (
        models.User.username == userrequest.username)).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="User already registered with the given email or username")

    # try:
    create_user_model = models.User(
        firstname=userrequest.firstname,
        lastname=userrequest.lastname,
        email=userrequest.email,
        username=userrequest.username,
        hashed_password=bcrypt_context.hash(userrequest.password),
        is_active=False
    )
    db.add(create_user_model)
    db.commit()

    await send_verification_email(create_user_model.email, otp)

    # Store the OTP and email in your database with an expiration time
    otp_record = models.OTPRecord(email=userrequest.email, otp=otp)
    db.add(otp_record)
    db.commit()

    return {"message": "Email sent successfully with OTP!"}
    # except Exception as e:
    #     db.rollback()  # Rollback changes if any exception occurs
    #     # For debugging purposes, you might want to log the exception here
    #     raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to create user and send email")


# @router.post("/resend_otp", status_code=status.HTTP_200_OK, summary="Resend OTP to user's email")
async def resend_otp(email, db):
    """
    ## resend otp code
    this endpoint is for resending the otp code and  cancels the previous one so the second code will be walid
    > it has email parameter"""

    # Verify if user email exists in the database
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Cancel the previous OTP by deleting or invalidating it
    previous_otp_record = db.query(models.OTPRecord).filter(
        models.OTPRecord.email == email).first()
    if previous_otp_record:
        db.delete(previous_otp_record)
        db.commit()

    # Generate a new OTP
    new_otp = otp_generator()

    # Send the new OTP via email
    try:
        await send_verification_email(email, new_otp)

        # Store the new OTP in the database
        new_otp_record = models.OTPRecord(email=email, otp=new_otp)
        db.add(new_otp_record)
        db.commit()

        return {"message": "New OTP sent successfully!"}
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500, detail=f"Failed to resend OTP: {str(e)}")


# @router.post("/verify/{code}", summary="Verify that the email used to sign up is yours")
async def enter_the_code(code, db):
    """
    ## Verification page
    
    > Allow the user a place to enter 6 integer digits

    ** Note: ** otp code is valid around 10 minutes
    """
    otp_validity_duration = timedelta(minutes=10)

    # Retrieve the stored OTP and timestamp from the database using the code
    otp_record = db.query(models.OTPRecord).filter(
        models.OTPRecord.otp == str(code)).first()

    if not otp_record:
        raise HTTPException(
            status_code=404, detail="OTP record not found or already used")

    # Make current_time timezone-aware (assuming UTC)
    current_time = datetime.now(timezone.utc)

    # Convert otp_creation_time to be timezone-aware if it is naive
    otp_creation_time = otp_record.created_at
    if otp_creation_time.tzinfo is None:
        otp_creation_time = otp_creation_time.replace(tzinfo=timezone.utc)

    otp_expiry_time = otp_creation_time + otp_validity_duration

    if current_time > otp_expiry_time:
        raise HTTPException(status_code=410, detail="OTP has expired")

    # Use the email from the OTP record to find the corresponding user
    user = db.query(models.User).filter(
        models.User.email == otp_record.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    try:
        user.is_active = True
        # Delete OTP record after successful verification
        db.delete(otp_record)
        db.commit()
        return {"message": "Verification successful and user activated"}
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500, detail=f"Internal server error: {str(e)}")

'''-----------------------------------------------------------------------------------------------------------------'''


# login
# Assuming authenticate_user expects parameters like (username_or_email, password, db)
# @router.post("/token", response_model=schemas.TokenResponse, summary="Login endpoint")
async def login_for_access_token(db, form_data):
    '''
    ## Login
    #### It can verify both:
    - Username
    - Email
    ** with password **
    '''

    # Since OAuth2PasswordRequestForm does not directly provide a 'username' field,
    # we assume 'username' is used here to mean either an actual username or email.
    # So, the form_data.username will contain either the username or the email.
    user = authenticate_user(
        username_or_email=form_data.username, password=form_data.password, db=db)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password")

    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Please activate your account")

    access_token, refresh_token = create_access_token(
        username=user.username, user_id=user.id)

    return schemas.TokenResponse(access_token=access_token, refresh_token=refresh_token, token_type="bearer")


# @router.post("/refresh", summary="Refresh access token")
async def refresh_token(refresh_token, db):
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        if username is None or user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

        new_access_token, new_refresh_token = create_access_token(
            username, user_id)
        return schemas.TokenResponse(access_token=new_access_token, refresh_token=new_refresh_token, token_type="bearer")
    except jwt.JWTError:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Invalid token or expired token")


# @router.get("/user_info", response_model=schemas.UserResponse, summary="Get user information")
async def get_user_info(db, user):
    """
    Retrieve the information of the authenticated user.
    Returns the user information as a UserResponse object.
    Raises HTTPException for unauthorized access.
    """
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed")
    user_model = db.query(models.User).filter(models.User.id == user.get('id')).first()
    return user_model

# @router.put('/change_password', status_code=status.HTTP_200_OK, summary="Change user password")
async def change_password(db: db_dependency, user: user_dependency, user_verify: schemas.UsersVerification):
    """
    Allows the user to change their password.
    Requires the current and new password.
    Raises HTTPException for invalid current password or unauthorized access.
    """
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed")
    user_model = db.query(models.User).filter(models.User.id == user.get('id')).first()
    if not bcrypt_context.verify(user_verify.password, user_model.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid current password")
    user_model.hashed_password = bcrypt_context.hash(user_verify.new_password)
    db.add(user_model)
    db.commit()
    return {"message": "Password changed successfully"}

# @router.delete("/delete_account", summary="Delete user account")
async def delete_account(db , user):
    """
    Delete the authenticated user's account and all related data (projects, todos, resources, profile picture).
    Raises HTTPException for unauthorized access.
    """
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed")

    # Deleting associated resources, todos, and projects
    db.query(models.Resource).join(models.Todo).join(models.Project).filter(models.Project.user_id == user.get('id')).delete(synchronize_session=False)
    db.query(models.Todo).join(models.Project).filter(models.Project.user_id == user.get('id')).delete(synchronize_session=False)
    db.query(models.Project).filter(models.Project.user_id == user.get('id')).delete(synchronize_session=False)

    # Delete profile picture and user account
    db.query(models.ImageModel).filter(models.ImageModel.user_id == user.get('id')).delete(synchronize_session=False)
    db.query(models.User).filter(models.User.id == user.get('id')).delete(synchronize_session=False)

    db.commit()
    return {"message": "User account and all related data deleted successfully"}

