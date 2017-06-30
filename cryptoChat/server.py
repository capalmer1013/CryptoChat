""" Http server for serving the chat clients
"""

from flask import Flask, jsonify
from flask_restful import reqparse
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def viewUsers():
    pass
    
@app.route("/<user>/chat")
def getChatFromUser(roomNumber=None):
    pass
    
@app.route("/<user>/send", methods=['POST'])
def sendChatToUser(roomNumber=None):
    pass

@app.route("/<user>/publicKey")
def getUsersPublicKey(user=None)
    pass
    
@app.route("/createUser/<username>", methods=['POST'])
def createUser(username=None):
    # args with publicKey
    pass

if __name__ == "__main__":
    app,run(host="0.0.0.0", port='8080')
