from flask import Flask

from pollen.pollen import pollen_bp

app = Flask(__name__)

app.register_blueprint(pollen_bp, url_prefix='/pollen')

if __name__ == '__main__':
    app.run(debug=True)
