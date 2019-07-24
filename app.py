from flask import Flask ,request
from middleware import Middleware

app = Flask(__name__)
app.wsgi_app = Middleware(app.wsgi_app)

@app.route('/home')
def home():
    return 'Hello'

@app.route('/contacto')
def contacto():
    return 'contacto'

if __name__ == '__main__':
    app.run(ssl_context='adhoc')
