from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>🎯 Mon quiz multi fonctionne !</h1>"

if __name__ == "__main__":
    app.run()
