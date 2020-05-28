from flask import Flask, __main__
app = Flask(__name__)

@app.route('/')
def helloworld():
    return ('Hello-World')

if __main__ == "__main__":
    app.run()