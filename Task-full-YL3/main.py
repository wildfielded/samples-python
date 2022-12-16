#!/usr/bin/python3

from string import Template

from bottle import route, run, request, redirect, HTTPError

import FigClasses as fc_
import HTML_Templates as ht_

#####=====----- Variables -----=====#####

#####=====----- Classes -----=====#####

#####=====----- Functions -----=====#####

@route('/')
def server_root():
    return ht_.HEADER + ht_.FORM_INI + ht_.FOOTER

@route('/figure', method='POST')
def figure():
    input_encoding = 'utf-8'
    suburl_ = '/' + str(request.forms.get('figtype'))
    redirect('/figure' + suburl_)

@route('/figure/<class_>')
def figure_class(class_):
    if class_ == 'Quadro':
        new_form_ = ht_.FORM_QUADRO
    if class_ == 'Cone':
        new_form_ = ht_.FORM_CONE
    if class_ == 'Circle':
        new_form_ = ht_.FORM_CIRCLE
    if class_ == 'Cube':
        new_form_ = ht_.FORM_CUBE
    if class_ == 'Parallelepiped':
        new_form_ = ht_.FORM_PARALLELEPIPED
    if class_ == 'Pyramid3F':
        new_form_ = ht_.FORM_PYRAMID3F
    if class_ == 'Pyramid4F':
        new_form_ = ht_.FORM_PYRAMID4F
    if class_ == 'Rectangle':
        new_form_ = ht_.FORM_RECTANGLE
    if class_ == 'Rhombus':
        new_form_ = ht_.FORM_RHOMBUS
    if class_ == 'Sphere':
        new_form_ = ht_.FORM_SPHERE
    if class_ == 'Trapezoid':
        new_form_ = ht_.FORM_TRAPEZOID
    if class_ == 'Triangle':
        new_form_ = ht_.FORM_TRIANGLE
    if class_ == 'Cylinder':
        new_form_ = ht_.FORM_CYLINDER
    return ht_.HEADER + new_form_ + ht_.FOOTER

@route('/result', method='POST')
def result(**kwargs):
    return ht_.HEADER + ht_.FOOTER

#####=====----- MAIN -----=====#####

if __name__ == '__main__':
    run(host='127.0.0.1', port=8080, debug=True)

#####=====----- THE END -----=====########################################