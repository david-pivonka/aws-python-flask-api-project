import pandas
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def post_file_upload():
    file = request.files.get("file")
    excel = pandas.read_excel(file)
    worksheet_names = list(excel.keys())

    return jsonify({
        "body": "Hello from root",
        "worksheet_names": worksheet_names
    })
