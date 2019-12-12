from flask import Flask, request, send_file
from phonenumbers import parse, is_valid_number, geocoder
import csv, phonenumbers

app = Flask(__name__)

@app.route('/locate_numbers', methods = ['POST'])
def hello_world():

    if not "numbers" in request.files:
        return "No file", 400

    request.files["numbers"].save("input.csv")

    # creating file
    with open('output.csv', mode='w') as csv_outputFile:
        csv_outputFile.write("numbers,valid,location\n")
    
    with open("input.csv") as csv_inputFile:
        csv_reader = csv.reader(csv_inputFile)

        for row in csv_reader:
            try:
                number = parse(row[0], "US")

                if is_valid_number(number):
                    valid = 'true'
                else:
                    valid = 'false'

                if geocoder.description_for_number(number, "en") == '':
                    where = 'n/a'
                else:
                    where = geocoder.description_for_number(number, "en")

                with open('output.csv', mode='a') as csv_outputFile:
                    csv_writer = csv.writer(csv_outputFile, delimiter=',')
                    csv_writer.writerow([row[0], valid, where])
            except:
                print("Bad number")
                pass

    return send_file("output.csv", as_attachment=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9000, debug=True)