import sys
import re
import db

class ATM_controller(object):
    def __init__(self, card_db, account_db):
        self.card_db = card_db
        self.account_db = account_db
        self.curr_card = None
        self.curr_account = None
        self.start()

    def start(self):
        print("--------------------------------")
        print("System started. Please insert your card.")
        card_number = sys.stdin.readline().strip()
        if not self.validate_inserted_card(card_number):
            return

        print("Please enter your pin number")
        pin_number = sys.stdin.readline().strip()
        print("--------------------------------")

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
        if re.match(r"\b\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}\b", card_number) and self.curr_card:
            print("--------------------------------")
            print("[SUCCESS] Card Inserted")
            return True
        print("[FAIL] Invalid Card Inserted. Please try again. \n")
        return False

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

        while not self.curr_account: 
            print("--------------------------------")
            if len(self.curr_card.accounts) == 0:
                print("There is no account connected to this card. \n")
                return
            print("Please select your account to progress transaction. Enter the number. ")
            
            for i, account_number in enumerate(self.curr_card.accounts):
                account = find_account(account_number)
                print("{}. {}: {}".format(i+1, account.name, account.number))
            
            account_index = int(sys.stdin.readline().strip())-1
            if 0 <= account_index < len(self.curr_card.accounts):
                self.curr_account = find_account(self.curr_card.accounts[account_index])

            print("--------------------------------")
            if not self.curr_account:
                print("[FAIL] Invalid Account Number. Please select valid account.")
        
        print("[SUCCESS] Valid Account Number.")
        self.progress_transaction()


    def progress_transaction(self):
        print("--------------------------------")
        print("Please select transaction. Enter the number. ")

        transactions = ["Check Balance", "Deposit", "Withdraw", "Quit"]
        for i, transaction in enumerate(transactions):
            print("{}: {}".format(i+1, transaction))
            
        transaction_selected = int(sys.stdin.readline().strip())
        print("--------------------------------")
        print("{} selected.".format(transactions[transaction_selected-1]))

        if transaction_selected == 1:
            print("Current Balance: ", self.curr_account.get_balance())
            
        elif transaction_selected == 2:
            print("Enter how much you want to deposit. ")
            deposit_amount = int(sys.stdin.readline().strip())
            curr_balance = self.curr_account.get_balance()
            self.curr_account.set_balance(curr_balance + deposit_amount)
            11
            print("Deposit: ", deposit_amount)
            print("Current Balance: ", self.curr_account.get_balance())

        elif transaction_selected == 3:
            print("Enter how much you want to withdraw. ")
            withdrawal_amount = int(sys.stdin.readline().strip())
            curr_balance = self.curr_account.get_balance()
            self.curr_account.set_balance(curr_balance - withdrawal_amount)

            print("Withdrawal: ", withdrawal_amount)
            print("Current Balance: ", self.curr_account.get_balance())

        elif transaction_selected == 4:
            print("--------------------------------")
            print("End of transaction. \n")
            return

        else:
            print("Invalid transaction. Please retry.")
            self.progress_transaction()

        print("--------------------------------")
        print("Do you want to continue with another transaction? Enter 1 for yes, 2 for no. ")
        want_continue = sys.stdin.readline().strip()
        if want_continue == "1":
            self.progress_transaction()
        else: 
            print("--------------------------------")
            print("End of transaction. \n")
            return

def main():
    ATM_controller(db.card_db, db.account_db)

main()