#!/usr/bin/python3

from time import strftime


def is_valid_name(name_: str) -> int:
    ''' User name validation.
        Now the presence and length of the string only.
    Arguments:
        name_ [str] -- 'name' field of json
    Returns:
        [int] -- '0' on success, or error code according to the
            'Errors' table
    '''
    if name_ is not None and 0 < len(name_) <= 1024:
        return 0
    else:
        return 100


def is_valid_birth(birth_: str) -> int:
    ''' Birth date validation.
        Now the presence and length of the string, as well as the age of
        majority (16 y.o. or more at the moment).
    Arguments:
        birth_ [str] -- 'birth' field of json
    Returns:
        [int] -- '0' on success, or error code according to the
            'Errors' table
    '''
    if birth_ is not None and len(birth_) == 10:
        birth_date = int(birth_.replace('-', ''))
        current_date = int(strftime('%Y%m%d'))
        if birth_date + 160000 > current_date:
            return 210
        else:
            return 0
    else:
        return 200


def is_valid_login(login_: str) -> int:
    ''' Login name validation.
        Now the presence and length of the string only.
    Arguments:
        login_ [str] -- 'login' field of json
    Returns:
        [int] -- '0' on success, or error code according to the
            'Errors' table
    '''
    if login_ is not None and 0 < len(login_) <= 1024:
        return 0
    else:
        return 300


def is_valid_password(password_: str) -> int:
    ''' Password validation.
        Now the presence and length of the string only.
    Arguments:
        password_ [str] -- 'password' field of json
    Returns:
        [int] -- '0' on success, or error code according to the
            'Errors' table
    '''
    if password_ is not None and 0 < len(password_) <= 1024:
        return 0
    else:
        return 400


def is_valid_phone(phone_: str) -> int:
    ''' Phone number validation.
        Now the presence and length of the string only.
    Arguments:
        phone_ [str] -- 'phone' field of json
    Returns:
        [int] -- '0' on success, or error code according to the
            'Errors' table
    '''
    if phone_ is not None and len(phone_) == 12:
        return 0
    else:
        return 500


def is_valid_email(email_: str) -> int:
    ''' Email address (optional) validation.
        It can be 'None', otherwise, the length of the string and the presence
        of at least one dot after '@' (second-level mail domain or more).
    Arguments:
        email_ [str] -- 'email' field of json
    Returns:
        [int] -- '0' on success, or error code according to the
            'Errors' table
    '''
    if email_ is None:
        return 0
    try:
        if 0 < len(email_) <= 1024:
            if '@' in email_ and '.' in email_.split('@')[1]:
                return 0
            else:
                return 600
        else:
            return 600
    except:
        return 600


def is_valid_tg(tg_: str) -> int:
    ''' Telegram login (optional) validation.
        It can be 'None', otherwise, the length of the string and the presence
        of '@' as first symbol.
    Arguments:
        email_ [str] -- 'tg' field of json
    Returns:
        [int] -- '0' on success, or error code according to the
            'Errors' table
    '''
    if tg_ is None:
        return 0
    try:
        if 0 < len(tg_) <= 1024:
            if tg_[0] == '@':
                return 0
            else:
                return 700
        else:
            return 700
    except:
        return 700


def validate_all(userdata_: dict) -> int:
    ''' The main function of input data validation. Checks all fields
        sequentially. At the first detected error, returns its code.
    Arguments:
        userdata_ [dict] -- json with user data
    Returns:
        [int] -- '0' on success, or code of first detected error according to
            the 'Errors' table
    '''
    code_list = [is_valid_name(userdata_.get('name')),
                 is_valid_birth(userdata_.get('birth')),
                 is_valid_login(userdata_.get('login')),
                 is_valid_password(userdata_.get('password')),
                 is_valid_phone(userdata_.get('phone')),
                 is_valid_email(userdata_.get('email')),
                 is_valid_tg(userdata_.get('tg')),
                ]
    for code_ in code_list:
        if code_ != 0:
            return code_
    return 0

#####=====----- THE END -----=====#########################################