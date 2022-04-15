import sys

class Account(object):
    def __init__(self, account_dict):
        self.name = account_dict['name']
        self.number = account_dict['number']
        self.balance = account_dict['balance']
    
    def in_dict(self):
        account_dict = {}
        account_dict['name'] = self.name
        account_dict['number'] = self.number
        account_dict['balance'] = self.balance
        return account_dict

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance

class Card(object):
    def __init__(self, card_dict):
        self.name = card_dict['name']
        self.number = card_dict['number']
        self.pin_number = card_dict['pin_number']
        self.accounts = []
        for account in card_dict['accounts']:
            self.accounts.append(Account(account))
    
    def in_dict(self):
        card_dict = {}
        card_dict['name'] = self.name
        card_dict['number'] = self.number
        card_dict['pin_number'] = self.pin_number
        card_dict['accounts'] = []
        for account in self.accounts:
            card_dict['accounts'].append(account.in_dict())
        return card_dict

class ATM_controller(object):
    def __init__(self):
        #self.db = db
        self.card_number = ''
        self.start()

    def start(self):
        print("Please insert your card.")
        card_number = sys.stdin.readline().strip()
        if card_number:
            print("Please enter your pin number")
            pin_number = sys.stdin.readline().strip()
        if not self.check_pin_number(card_number, pin_number):
            print("card_number: ", card_number)
            print("pin_number: ", pin_number)
            print('Wrong pin number. Please restart. \n')
        else:
            print("Correct pin number.")
    
    def check_pin_number(self, card_number, pin_number):
        print("checking pin number?")
        return True

def main():
    # db = {
    #     card_number: '1111 1111 1111 1111'
    # }
    ATM_controller()

main()