import os
from flask import Flask
from popular_artifacts import popular_artifact_generator

app = Flask(__name__)

@app.route("/")
def generate_buzz():
    page = '<html><body><p>'
    first, second = popular_artifact_generator.main()
    page += str(first)
    page += '</p><p>'
    page += str(second)
    page += '</p></body></html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))