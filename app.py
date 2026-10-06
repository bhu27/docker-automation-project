from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Docker CI/CD Project</title>
        </head>
        <body>
            <h1>Docker CI/CD Automation Project</h1>
            <p>Application successfully deployed using Docker!</p>
            <p>Pipeline: GitHub → Docker → Trivy → Docker Hub</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
