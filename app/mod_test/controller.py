from flask import Blueprint, render_template
from app import socketio
from . import mod_test

@mod_test.route("/chat")
def chat():
    return render_template("chat.html")

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('chat client')
def handle_chat(json, methods=['GET', 'POST']):
    print('chat client: ' + str(json))
    socketio.emit('chat server', json, callback=messageReceived)

################################################################################

@mod_test.route("/videochat")
def videochat():
    return render_template("videochat.html")

@socketio.on('video')
def handle_vdieo(data_video):
    pass

################################################################################

@mod_test.route("/streamingauido")
def streamingaudio():
    return render_template("streamingaudio.html")
# @socketio.on('image')
# def image(data_image):
#     sbuf = StringIO()
#     sbuf.write(data_image)

#     # decode and convert into image
#     b = io.BytesIO(base64.b64decode(data_image))
#     pimg = Image.open(b)

#     # Process the image frame
#     frame = imutils.resize(frame, width=700)
#     frame = cv2.flip(frame, 1)
#     imgencode = cv2.imencode('.jpg', frame)[1]

#     # base64 encode
#     stringData = base64.b64encode(imgencode).decode('utf-8')
#     b64_src = 'data:image/jpg;base64,'
#     stringData = b64_src + stringData

#     # emit the frame back
#     emit('response_back', stringData)