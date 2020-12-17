import os
from flask import Flask 
from flask import request, render_template

app = Flask(__name__)
UPLOAD_FOLDER = "/usr/src/app/static"

@app.route("/", methods=["GET", "POST"])
def upload_predict():
    if request.method == "POST":
        image_file = request.files["image"]
        if image_file:
            image_location = os.path.join(UPLOAD_FOLDER, 
                                image_file.filename)
            image_file.save(image_location)
            return render_template("index.html", image_loc=image_file.filename)
    return render_template("index.html", image_loc=None)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9001, debug=True)