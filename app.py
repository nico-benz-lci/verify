from flask import Flask, render_template, request, flash
import csv

with open("output/results.csv") as f:
    test_data = [{k:v for k, v in row.items()} for row in csv.DictReader(f, skipinitialspace=True)]

app = Flask(__name__)
app.secret_key = "abcdefg"
app.debug = True

@app.route("/index")
def index():
    flash("Enter verification code!")
    return render_template("index.html", test_data=test_data)

@app.route("/verify", methods=["POST", "GET"])
def verify():
    counter = 0
    for i in test_data:
        if str(request.form["name_input"]) in i.values():
            name = "Name: " + i["Name"]
            first_name = "First Name: " + i["First Name"]
            date_of_birth = "Date of Birth: " + i["Date of Birth"]
            city = "City: " + i["City"]
            country = "Country: " + i["Country"]
            date_of_exam = "Date of Exam: " + i["Date of Exam"]
            date_of_issue = "Date of Issue: " + i["Date of Issue"]
        else:
            counter += 1

    flash("Code entered: " + str(request.form["name_input"]))
    if counter >= len(test_data):
        flash("Code not found")
    else:
        flash("Successfully verified!")
        flash(f"{name}")
        flash(f"{first_name}")
        flash(f"{date_of_birth}")
        flash(f"{city}")
        flash(f"{country}")
        flash(f"{date_of_exam}")
        flash(f"{date_of_issue}")
    return render_template("index.html")
