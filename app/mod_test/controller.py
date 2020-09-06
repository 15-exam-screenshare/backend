#!/bin/env python
from flask import render_template, session, redirect, url_for,  request
from flask_socketio import emit, join_room, leave_room
from .. import socketio
from . import mod_test

@mod_test.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        name =  request.form['name']
        if name is not None:
            session['name'] = name
            return redirect(url_for('test.chat'))
    return render_template('test-index.html')

@mod_test.route('/chat')
def chat():
    name = session.get('name', '')
    if name == '':
        return redirect(url_for('test.index'))
    return render_template('test-chat.html', name=name)


@socketio.on('joined', namespace='/chat')
def enter(message):
    room = 1
    join_room(room)


@socketio.on('text', namespace='/chat')
def text(message):
    room = 1
    emit('message', {'message': session.get('name') + ':' + message['message']}, room=room)


@socketio.on('left', namespace='/chat')
def leave(message):
    room = 1
    leave_room(room)

