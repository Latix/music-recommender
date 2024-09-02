# try:
#     number = int(input("Enter Number"))
#     print(number)
# except ValueError:
#     print("Invalid Number")

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print(f"You are moving {self.x}")
#
# point1 = Point(10, 21)
# point1.move()

import converters
from shopping import cart

# import random
#
# print(random.randint(10, 30))

# from pathlib import Path
# path = Path("shopping")
# print(path.exists())

# """
#     Approach: Iteration 1
#
#     1. Get the domains of each email
#     input: ['www.a.com', 'www.b.com']
#     output: ['a.com', 'b.com']
#
#     Approach: Iteration 2
# """
# urls = ['www.a.com', 'www.b.com']
#
# for i in urls:
#     print(i[4:])
#
# print(4 + "Cool")

# import openpyxl as xl
# from openpyxl.chart import BarChart, Reference
#
# def process_work_book(file_name):
#     wb = xl.load_workbook(file_name)
#     sheet = wb['Sheet1']
#     # cell = sheet['a1']
#     # cell = sheet.cell(1, 1)
#
#     # print(sheet.max_row)
#
#     for row in range(2, sheet.max_row + 1):
#         cell = sheet.cell(row, 3)
#         corrected_price = cell.value * 0.9
#         print(corrected_price)
#         corrected_price_cell = sheet.cell(row, 4)
#         corrected_price_cell.value = corrected_price
#
#     values = Reference(sheet,
#               min_row=2,
#               max_row=sheet.max_row,
#               min_col=4,
#               max_col=4)
#
#     chart = BarChart()
#     chart.add_data(values)
#     sheet.add_chart(chart)
#     wb.save(file_name)
#
# process_work_book('transactions.xlsx')

from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os  # Import os to access environment variables

app = Flask(__name__)

# Load the model
model = joblib.load('music-recommendations.joblib')

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        # Get input data
        data = request.json
        expected_features = ['age', 'gender']  # List all features expected by the model
        df = pd.DataFrame(data, columns=expected_features)

        # Check if all required columns are present
        if not all(col in df.columns for col in expected_features):
            raise ValueError(f"Missing one or more required features: {expected_features}")

        # Make predictions
        predictions = model.predict(df)

        # Return predictions as JSON
        return jsonify(predictions.tolist())
    except Exception as e:
        print('Error....', e)
        return str(e), 400

if __name__ == '__main__':
    port = int(os.getenv('PORT', 4040))  # Use environment variable, default to 4040 if not set
    print(f'App Started...listening on: {port}')
    app.run(host='0.0.0.0', port=port)
