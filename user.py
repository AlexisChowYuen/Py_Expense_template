from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    }
]   

def add_user():
    infos = prompt(user_questions)
    print("User Added !")
    return register_user(infos['name'])

# register user in csv file
def register_user(name):
    with open('user.csv', 'a') as f:
        spamwriter = csv.writer(f, delimiter=' ')
        spamwriter.writerow([name])
    return True