from flask import Flask, render_template, request, flash

import pandas as pd


url = "https://raw.githubusercontent.com/nico-benz-lci/verify/29e6e47fccd000732e8b66f01782a317d5f1ce92/output/results.csv"

test_data = pd.io.parsers.read_csv(url, sep='\s*,\s*',engine='python')

app = Flask(__name__)
app.secret_key = "abcdefg"
app.debug = True

@app.route("/index")
def index():
    flash("Enter verification code!")
    return render_template("index.html", test_data=test_data)

@app.route("/verify", methods=["POST", "GET"])
def verify():
    search = str(request.form["name_input"])
    if str(request.form["name_input"]) in test_data.values:
        index = test_data.index
        condition = test_data["Verification Code"] == search
        code_indice = index[condition]
        code_indice_list = code_indice.tolist()

        fname = test_data.loc[code_indice_list[0], "First Name"]
        name = test_data.loc[code_indice_list[0], "Name"]
        bday = test_data.loc[code_indice_list[0], "Date of Birth"]
        city = test_data.loc[code_indice_list[0], "City"]
        country = test_data.loc[code_indice_list[0], "Country"]
        doe = test_data.loc[code_indice_list[0], "Date of Exam"]
        flash("Code entered: " + str(request.form["name_input"]))
        flash("Successfully verified!")
        flash(fname + " " + name + " from " + city + " (" + country + "), born on " + bday + ", took part in this exam on " + doe + ". ")
    else:
        flash("Code entered: " + str(request.form["name_input"]))
        flash("Code not found in database!")

    return render_template("index.html")
