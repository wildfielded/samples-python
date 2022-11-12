#!/usr/bin/python3

import json
import uuid

import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, Session

import api_validations as v_


''' =====----- Global variables -----===== '''
DB_PATH = 'sqlite:///sqlite/db.sqlite3'
Base = declarative_base()
ENGINE = sa.create_engine(DB_PATH)


''' =====----- Classes -----===== '''
class User(Base):
    __tablename__ = 'Users'
    uid = sa.Column(sa.String(36), primary_key=True)
    name = sa.Column(sa.String(1024))
    birth = sa.Column(sa.String(10))
    login = sa.Column(sa.String(1024))
    password = sa.Column(sa.String(1024))
    phone = sa.Column(sa.String(12))
    email = sa.Column(sa.String(1024))
    tg = sa.Column(sa.String(1024))


class Error(Base):
    __tablename__ = 'Errors'
    code = sa.Column(sa.Integer, primary_key=True)
    text = sa.Column(sa.Text(1024))


''' =====----- API methods -----===== '''
def register_post(userdata_: dict) -> dict:
    ''' The first API method (new user registration)
    Arguments:
        userdata_ [dict] -- JSON with obligatory 'name', 'birth', 'login',
            'password', 'phone', and with optional 'email', 'tg' fields
    Returns:
        [dict] -- JSON with user ID field 'uid' on success, or with
            'code' and 'text' fields on error
    '''
    err_code = v_.validate_all(userdata_)
    if err_code == 0:
        new_user = User(uid=str(uuid.uuid4()),
                        name=userdata_.get('name'),
                        birth=userdata_.get('birth'),
                        login=userdata_.get('login'),
                        password=userdata_.get('password'),
                        phone=userdata_.get('phone'),
                        email=userdata_.get('email'),
                        tg=userdata_.get('tg')
                       )
        with Session(ENGINE) as add_session:
            output_ = dict(uid=new_user.uid)
            add_session.add(new_user)
            add_session.commit()
    else:
        with Session(ENGINE) as err_session:
            error_ = err_session.query(Error).filter(Error.code == err_code).first()
            output_ = dict(code=error_.code, text=error_.text)
    return json.dumps(output_, ensure_ascii=False, indent=4)


def login_post(credentials_: dict) -> dict:
    ''' The second API method (authorization)
    Arguments:
        credentials_ [dict] -- JSON with 'login' and 'password' fields
    Returns:
        [dict] -- JSON with user ID field 'uid' on success, or with
            'code' and 'text' fields on error
    '''
    login_ = credentials_.get('login')
    password_ = credentials_.get('password')
    with Session(ENGINE) as auth_session:
        try:
            user_ = auth_session.query(User).filter(User.login == login_).first()
            if user_.password == password_:
                output_ = dict(uid=user_.uid)
            else:
                error_ = auth_session.query(Error).filter(Error.code == 800).first()
                output_ = dict(code=error_.code, text=error_.text)
        except:
            error_ = auth_session.query(Error).filter(Error.code == 800).first()
            output_ = dict(code=error_.code, text=error_.text)
    return json.dumps(output_, ensure_ascii=False, indent=4)


def user_get(uid_: str) -> dict:
    ''' The third API method (id request)
    Arguments:
        uid_ [str] -- User ID
    Returns:
        [dict] -- JSON with all user fields except 'password' and 'uid'
            self on success, or with 'code' and 'text' fields on error
    '''
    with Session(ENGINE) as q_session:
        try:
            user_ = q_session.query(User).filter(User.uid == uid_).first()
            output_ = dict(name=user_.name,
                           birth=user_.birth,
                           login=user_.login,
                           phone=user_.phone,
                           email=user_.email,
                           tg=user_.tg
                          )
        except:
            error_ = q_session.query(Error).filter(Error.code == 900).first()
            output_ = dict(code=error_.code, text=error_.text)
    return json.dumps(output_, ensure_ascii=False, indent=4)

#####=====----- THE END -----=====#########################################