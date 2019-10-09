from flask import Flask

app = Flask(__name__)

@api.route("/",methods=['POST'])
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()
