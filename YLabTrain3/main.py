#!/usr/bin/python3

from bottle import route, run, request, redirect, HTTPError

import FigClasses as fc_

#####=====----- Variables -----=====#####

#####=====----- Classes -----=====#####

#####=====----- Functions -----=====#####

@route('/')
def server_root():
    with open('web/index.html', 'r', encoding='utf-8') as f_:
        output_ = f_.read()
    return output_

@route('/figure', method='POST')
def figure():
    input_encoding = 'utf-8'
    suburl_ = '/' + str(request.forms.get('figtype'))
    redirect('/figure' + suburl_)

@route('/figure/<class_>')
def figure_class(class_):
    return 'It works'

#####=====----- MAIN -----=====#####

if __name__ == '__main__':
    run(host='127.0.0.1', port=8080, debug=True)

#####=====----- THE END -----=====########################################