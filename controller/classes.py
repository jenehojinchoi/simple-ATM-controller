import sys 
import re

class ATM_controller(object):
    def __init__(self, card_db, account_db):
        self.card_db = card_db
        self.account_db = account_db
        self.curr_card = None
        self.curr_account = None
        self.start()

    def start(self):
        print("----------------------------------------------------------------")
        print("System started. Please insert your card. The card number should consist of 4 groups of 4 digits and space in between them. e.g.) 1111 1111 1111 1111")
        card_number = sys.stdin.readline().strip()
        if not self.validate_inserted_card(card_number):
            return

        print("Please enter your 4-digit pin number.")
        pin_number = sys.stdin.readline().strip()
        print("----------------------------------------------------------------")

        if not self.check_pin_number(pin_number):
            print('[FAIL] Wrong pin number. Please restart. \n')
            return
        else:
            print("[SUCCESS] Correct pin number.")
            self.select_account()

    def validate_inserted_card(self, card_number):
        def find_card(card_number):
            for card in self.card_db:
                if card.number == card_number:
                    return card
            return None

        self.curr_card = find_card(card_number)
        card_format_matched = re.match(r"\b\d{4}[ ]\d{4}[ ]\d{4}[ ]\d{4}\b", card_number)

        if not card_format_matched:
            print("[FAIL] Invalid Card Inserted. Please try again. \n")
            return False
            
        if not self.curr_card:
            print("[FAIL] There is no card with this card number. Please try again. \n")
            return False

        if re.match(r"\b\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}\b", card_number) and self.curr_card:
            print("----------------------------------------------------------------")
            print("[SUCCESS] Card Inserted")
            return True

    def check_pin_number(self, pin_number):
        if self.curr_card.pin_number == pin_number:
            return True
        else:
            return False

    def select_account(self): 
        def find_account(account_number):
            for account in self.account_db:
                if account.number == account_number:
                    return account
            return None

        print("----------------------------------------------------------------")
        if len(self.curr_card.accounts) == 0:
            print("There is no account connected to this card. \n")
            return

        print("Please select your account to progress transaction. Enter the number: {} to {}".format(1, len(self.curr_card.accounts)))
        
        for i, account_number in enumerate(self.curr_card.accounts):
            account = find_account(account_number)
            print("{}. {}: {}".format(i+1, account.name, account.number))
        
        account_index = ''
        account_index = sys.stdin.readline().strip()
        if not re.match(r'^\d$', account_index):
            print("[FAIL] Invalid Account Number. Please select a valid account.")
            return self.select_account()

        account_index = int(account_index)-1

        if 0 <= account_index < len(self.curr_card.accounts):
            self.curr_account = find_account(self.curr_card.accounts[account_index])
            print("[SUCCESS] Valid Account Number.")
            return self.progress_transaction()

        else: 
            print("[FAIL] Account number out of range. Please select a valid account.")
            return self.select_account()

    def progress_transaction(self):
        print("----------------------------------------------------------------")
        print("Please select transaction. Enter the number. ")

        transactions = ["Check Balance", "Deposit", "Withdraw", "Quit"]
        for i, transaction in enumerate(transactions):
            print("{}: {}".format(i+1, transaction))

        transaction_selected = sys.stdin.readline().strip()
        if not re.match(r'^[1-4]$', transaction_selected):
            print("[FAIL] Invalid Transaction Selected. Please try again. ")
            return self.progress_transaction()

        else:
            print("----------------------------------------------------------------")
            print("{} selected.".format(transactions[int(transaction_selected)-1]))

            if transaction_selected == '1':
                print("Current Balance: {0:.2f}".format(self.curr_account.get_balance()))
                
            elif transaction_selected == '2':
                print("Enter how much you want to deposit. ")
                deposit_amount = float(sys.stdin.readline().strip())
                curr_balance = self.curr_account.get_balance()
                self.curr_account.set_balance(curr_balance + deposit_amount)
                print("Deposit: ", deposit_amount)
                print("Current Balance: {0:.2f}".format(self.curr_account.get_balance()))

            elif transaction_selected == '3':
                print("Enter how much you want to withdraw. ")
                withdrawal_amount = float(sys.stdin.readline().strip())
                curr_balance = self.curr_account.get_balance()
                self.curr_account.set_balance(curr_balance - withdrawal_amount)

                print("Withdrawal: ", withdrawal_amount)
                print("Current Balance: {0:.2f}".format(self.curr_account.get_balance()))

            elif transaction_selected == '4':
                print("----------------------------------------------------------------")
                print("End of transaction. \n")
                return
        
            return self.continue_or_quit()

    def continue_or_quit(self):
        print("----------------------------------------------------------------")
        print("Do you want to continue with another transaction? Enter 1 for yes, 2 for no. ")
        continue_or_quit_option = sys.stdin.readline().strip()
        if continue_or_quit_option == '1':
            self.progress_transaction()
        elif continue_or_quit_option == '2': 
            print("----------------------------------------------------------------")
            print("End of transaction. \n")
            return
        else:
            print("----------------------------------------------------------------")
            print("[FAIL] Invalid option. Please try again. ")
            return self.continue_or_quit()
        
        
class Account(object):
    def __init__(self, account_dict):
        self.name = account_dict['name']
        self.number = account_dict['number']
        self.balance = account_dict['balance']

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance


class Card(object):
    def __init__(self, card_dict):
        self.name = card_dict['name']
        self.number = card_dict['number']
        self.pin_number = card_dict['pin_number']
        self.accounts = card_dict['accounts']

    def get_accounts(self):
        return self.accounts