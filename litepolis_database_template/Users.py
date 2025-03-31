from typing import Optional

from sqlmodel import Field, Session, SQLModel, select

from .utils import with_session, create_db_and_tables

# Define the SQLModel for users
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    password: str
    privilege: str = "user"


class UserManager:
    @staticmethod
    def create_user(email: str, password: str, privilege: str = "user"):
        for session in with_session():
            user = User(email=email, password=password, privilege=privilege)
            session.add(user)
            session.commit()
            session.refresh(user)
        return user

    @staticmethod
    def read_user(user_id: int):
        for session in with_session():
            user = session.get(User, user_id)
        return user

    @staticmethod
    def read_users():
        for session in with_session():
            users = session.exec(select(User)).all()
        return users

    @staticmethod
    def update_user(user_id: int, email: str, password: str, privilege: str):
        for session in with_session():
            db_user = session.get(User, user_id)
            if not db_user:
                return None

            db_user.email = email
            db_user.password = password
            db_user.privilege = privilege

            session.add(db_user)
            session.commit()
            session.refresh(db_user)
        return db_user

    @staticmethod
    def delete_user(user_id: int):
        for session in with_session():
            user = session.get(User, user_id)
            if not user:
                return False

            session.delete(user)
            session.commit()
        return True

# Run this once to create the database and tables
create_db_and_tables()
