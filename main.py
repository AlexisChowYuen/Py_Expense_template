from examples import custom_style_2
from expense import expense_questions,new_expense,get_list_users
from user import user_questions,add_user
from PyInquirer import prompt

def ask_option():
    main_option = {
        "type":"list",
        "name":"main_options",
        "message":"Expense Tracker v0.1",
        "choices": ["New Expense","Show Status","New User"]
    }
    option = prompt(main_option)
    if (option['main_options']) == "New Expense":
        new_expense()
        ask_option()
    elif (option['main_options']) == "Show Status":
        print("Show Status")
        ask_option()
    elif (option['main_options']) == "New User":
        add_user()
        ask_option()

def main():
    ask_option()

main()