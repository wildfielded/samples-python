#!/usr/bin/python3

from bottle import HTTPError, get, post, request, run

import api_module as api_


''' =====----- Global variables -----===== '''
ROOT_INDEX_FILE = 'ADDS/index.html'


''' =====----- Bottle resources -----===== '''
@get('/')
def server_root() -> str:
    ''' Analogue of Apache's "It works!" page for testing Bottle performance
    Returns:
        [str] -- contents of HTML file specified in the global variable
            ROOT_INDEX_FILE
    '''
    with open(ROOT_INDEX_FILE, 'r', encoding='utf-8') as f_:
        return f_.read()

@post('/v1/auth/register')
def register_post():
    ''' The first API method
    '''
    return api_.register_post(request.json)

@post('/v1/auth/login')
def login_post():
    ''' The second API method
    '''
    return api_.login_post(request.json)

@get('/v1/user')
def user_get():
    ''' The third API method
    '''
    uid_ = request.query.id
    return api_.user_get(uid_)


''' =====----- MAIN -----===== '''
if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)

#####=====----- THE END -----=====#########################################