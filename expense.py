from PyInquirer import prompt
import csv

def get_list_users():
    with open('user.csv', 'r') as f:
        reader = csv.reader(f)
        list_users = list(reader)
        for i in range(len(list_users)):
            list_users[i] = list_users[i][0]
    return list_users

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
        "type":"rawlist",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": get_list_users()
    }
]



def new_expense(*args):
    expense_questions[2]['choices'] = get_list_users()
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