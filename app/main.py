# build fa5a63b77a
# (auto) 08719b
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'ok'
