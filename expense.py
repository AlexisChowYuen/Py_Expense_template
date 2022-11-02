from PyInquirer import prompt
import csv

def get_list_users():
    with open('user.csv', 'r') as f:
        reader = csv.reader(f)
        list_users = list(reader)
        for i in range(len(list_users)):
            list_users[i] = { "name": list_users[i][0] }
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
        "type":"checkbox",
        'qmark': '😃',
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": get_list_users(),
        'validate': lambda answer: 'You must choose at least one user.' \
            if len(answer) == 0 else True
    }
]



def new_expense(*args):
    expense_questions[2]['choices'] = get_list_users()
    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    print("Expense Added !")
    
    amount = infos['amount']
    spender = infos['spender']

    new_amount = int(amount) / len(spender)
    res = True
    for i in range(len(spender)):
        # Create list without item at index i
        others_involved = spender[:i] + spender[i+1:]
        res = res and register_expense(new_amount, infos['label'], spender[i], others_involved)
    return res

# register expense in csv file
def register_expense(amount, label, spender, others_involved=[]):
    with open('expense.csv', 'a') as f:
        spamwriter = csv.writer(f, delimiter=' ')
        spamwriter.writerow([amount, label, spender, others_involved])
    return True