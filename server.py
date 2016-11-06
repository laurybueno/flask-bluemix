import os
from flask import Flask, request, send_from_directory

# {
#   "url": "https://gateway.watsonplatform.net/conversation/api",
#   "password": "dEhUVszahZAU",
#   "username": "6382d1d9-ebbe-4637-aac3-79f340dd009c"
# }

app = Flask(__name__)


@app.route('/stylesheets/<path:path>')
def send_css(path):
    return send_from_directory('static/stylesheets', path)


@app.route('/images/<path:path>')
def send_img(path):
    return send_from_directory('static/images', path)


@app.route('/')
def root():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    # Bind to PORT/HOST if defined, otherwise default to 5050/localhost.
    PORT = int(os.getenv('VCAP_APP_PORT', 8000))
    # HOST = str(os.getenv('VCAP_APP_HOST', 'localhost'))
    app.run(host='0.0.0.0', port=PORT)
