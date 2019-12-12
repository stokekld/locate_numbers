from flask import Flask, request
import csv

app = Flask(__name__)

@app.route('/locate_numbers', methods = ['POST'])
def hello_world():

    inputFile = request.files["numbers"]
    inputFile.save("input.csv")

    with open("input.csv") as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            print(row[0])

    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9000, debug=True)