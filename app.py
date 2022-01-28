from flask import Flask
app = Flask("Ola-MUNDO")
@app.route("/", methods=['GET'])

def respond():
    return {"dizendo": "olá mundo"}

app.run(threaded=True, port=5000)
