from PyInquirer import prompt
import csv

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },

]



def new_expense(*args):
    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    print("Expense Added !")
    return register_expense(infos['amount'], infos['label'], infos['spender'])

# register expense in csv file
def register_expense(amount, label, spender):
    with open('expense.csv', 'a') as f:
        spamwriter = csv.writer(f, delimiter=' ')
        spamwriter.writerow([amount, label, spender])
    return True

