from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def health():
    return jsonify({
        "service": "flask-gke-ci-cd-v2",
        "status": "ok"
    })

@app.route("/hello")
def hello():
    return jsonify({
        "message": "Hello from CI/CD pipeline v2"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)  # nosec B104

