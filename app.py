from flask import *

app = Flask(__name__)


@app.route('/')
def Hello():
    return "Hello world"



if __name__=="__main__":
    app.run()

