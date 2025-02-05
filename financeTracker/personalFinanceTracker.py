"""For this script to work, you'll need to add a CSV file named Transactions.csv in the same directory as this script.
 The CSV file should have the following columns: 
    Date,
    Description,
    Amount,
    Balance,
    Transaction Type,
    and Status.
The script will read the CSV file and calculate the total expenses for a given month. 
It will then update a JSON file named monthly_expenses.json with the total expenses for that month.
The JSON file will store the total expenses for each month in the format: {"MM-YYYY": total_expenses}.
"""

import csv
import json
import os

def monthly_expenses_sum(csv_file_path):
    totalExpenses = 0.0
    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            date, _, amount, _, transaction_type, status = row
            amount = amount.replace(',', '')
            if transaction_type.lower() == "debit":
                totalExpenses += float(amount)
    return totalExpenses

def update_expenses_json(json_file_path, month, total_expenses):
    expensesData = {}
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as json_file:
            expensesData = json.load(json_file)

    expensesData[month] = total_expenses

    with open(json_file_path, 'w') as json_file:
        json.dump(expensesData, json_file, indent=4)

monthInput = input("Please enter the month (MM-YYYY): ")
csvFileName = "Transactions.csv"
jsonFileName = "monthly_expenses.json"
totalMonthExpenses = monthly_expenses_sum(csvFileName)
print(f"Total expenses for {monthInput}: ${totalMonthExpenses}")

update_expenses_json(jsonFileName, monthInput, totalMonthExpenses)