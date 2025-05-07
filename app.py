from ast import main
from doctest import debug
from flask import Flask
from controllers.main_controller import mainAppController


app = Flask(__name__)

@app.route('/')
def index():
    return mainAppController.home()

@app.route('/sign-in', methods=['POST', 'GET'])
def sign_in():
    return mainAppController.sign_in()

@app.route('/sign-up', methods=['POST','GET'])
def sign_up():
    return mainAppController.sign_up()

@app.route('/chat', methods=['POST', 'GET'])
def chat():
    return mainAppController.chat()


@app.route('/profile')
def profile():
    return mainAppController.profile()

@app.route('/logout')
def logout():
    return mainAppController.logout()




if __name__ =="__main__":
    app.run(debug=True)