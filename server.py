from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def store_data(data):
    with open("database.txt", mode="a") as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        print(email)
        file = database.write(f'\n{email},{subject},{message}')

        print("yeah ")
def store_data_csv(data):
    with open("database.csv", mode="a", newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        print(email)
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
        print("yeah ")


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            store_data_csv(data)
            return redirect("/thankyou.html")
        except:
            return "did not save to database"
    return 'something went wrong'

