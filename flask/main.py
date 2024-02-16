from distutils.log import debug
from fileinput import filename
from flask import *
from converter import js_to_python, indentToNbsp
from readability import analyze_code
from open import getComment
from os.path import join

app = Flask(__name__, template_folder="template")
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["POST", "GET"])
def main():
    if request.method == "POST":
        f = request.files["js-file"]
        f.save(join(app.config["UPLOAD_FOLDER"], f.filename))
        js_path = join(app.config["UPLOAD_FOLDER"], f.filename)
        with open(js_path) as f:
            js_code = f.read()
        python_code = js_to_python(js_code)
        js = js_code
        # python_code = indentToNbsp(python_code)
        py = python_code
        print(py)
        return render_template("index.html", js=js, py=py)
    return render_template("index.html")


@app.route("/comment", methods=["POST", "GET"])
def comment():
    if request.method == "POST":
        f = request.files["js-file"]
        f.save(join(app.config["UPLOAD_FOLDER"], f.filename))
        js_path = join(app.config["UPLOAD_FOLDER"], f.filename)
        with open(js_path) as f:
            js_code = f.read()
        python_code = getComment(js_code)
        js = js_code
        py = python_code
        print(py)
        return render_template("comment.html", js=js, py=py)
    return render_template("comment.html")


@app.route("/codeindex", methods=["POST", "GET"])
def codeindex():
    if request.method == "POST":
        f = request.files["js-file"]
        f.save(join(app.config["UPLOAD_FOLDER"], f.filename))
        py_path = join(app.config["UPLOAD_FOLDER"], f.filename)
        (
            total_variables,
            meaningful_variables,
            total_class,
            meaningful_class,
            meaningful_functions,
            total_functions,
            functions_with_docstrings,
            meaningful_comments,
            readability_index,
        ) = analyze_code(py_path)
        with open(py_path) as f:
            py_code = f.read()
            # py = py_code.split("\n")
            py = py_code

        return render_template(
            "codeindex.html",
            py=py,
            total_variables=total_variables,
            meaningful_variables=meaningful_variables,
            total_class=total_class,
            meaningful_class=meaningful_class,
            meaningful_functions=meaningful_functions,
            total_functions=total_functions,
            functions_with_docstrings=functions_with_docstrings,
            meaningful_comments=meaningful_comments,
            readability_index=readability_index,
        )
    return render_template("codeindex.html")


if __name__ == "__main__":
    app.run(debug=True)
