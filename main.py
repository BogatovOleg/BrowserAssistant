from flask import Flask

application = Flask(__name__)
app = application


@application.route('/')
def hello_world():
    return 'Sup. Subscribe'

app.run( host='0.0.0.0', port=8080)
