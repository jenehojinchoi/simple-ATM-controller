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
    
    def get_accounts(self):
        return self.accounts

class ATM_controller(object):
    def __init__(self):
        #self.db = db
        self.card_pin = {
            '1111 1111 1111 1111' : '1234'
        }
        self.card_accounts = {
            '1111 1111 1111 1111' : ['123-456-789', '234-567-890']
        }
        self.start()

    def select_account(self, card_number): 
        if len(self.card_accounts[card_number]) == 0:
            print("There is no account connected to this card. \n")
            return
        print("Please select your account to progress transaction.")
        for account in self.card_accounts[card_number]:
            print(account)

    def start(self):
        print("Please insert your card.")
        card_number = sys.stdin.readline().strip()
        if card_number:
            print("Please enter your pin number")
            pin_number = sys.stdin.readline().strip()
        if not self.check_pin_number(card_number, pin_number):
            print('Wrong pin number. Please restart. \n')
        else:
            print("Correct pin number.")
            self.select_account(card_number)
    
    def check_pin_number(self, card_number, pin_number):
        if card_number in self.card_pin:
            if self.card_pin[card_number] == pin_number:
                return True
            else:
                return False

def main():
    # db = {
    #     card_number: '1111 1111 1111 1111'
    # }
    ATM_controller()

main()