from flask import Flask,render_template

app = Flask(__name__)

app.config['EXPLAIN_TEMPLATE_LOADING'] = True

@app.route("/")
def hello_page():
    return render_template("cv.html")

if __name__ == "__main__":
    app.run(debug=True)

#flask template leri adi template olan bir dosyadan almali onemli!!!