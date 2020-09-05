from flask import Flask , render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route("/")
def main():
     return render_template("index.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('chat client')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('chat client: ' + str(json))
    socketio.emit('chat server', json, callback=messageReceived)
    
if __name__ == '__main__':
    socketio.run(app)