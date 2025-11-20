from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello World!</h1><p>Flask app deployed successfully on Azure Web App</p>"

@app.route("/health")
def health():
    return {"status": "healthy", "message": "App is running"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
