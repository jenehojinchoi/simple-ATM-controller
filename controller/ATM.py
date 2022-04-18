import sys
import db
from classes import ATM_controller

def main():
    ATM_controller(db.card_db, db.account_db)
    
main()