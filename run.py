from flaskblog import app
from flask import Flask

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
