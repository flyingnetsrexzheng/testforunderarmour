from flask import Flask

app = Flask(__name__)

@app.route('/v1')
def hello_word():
    return "SH There is Under Armour in Flyingnets AWS-2-7 NewCMP-remote\n"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
