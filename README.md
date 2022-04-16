# Simple ATM controller
## Requirements
At least the following flow should be implemented:
Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw
## Description
This program can be executed by running `python ATM.py` in terminal.

There is `DB.py`, which contains a class named `Account` and `Card`. `DB.py` has all cards and accounts information. 

In `DB.py`, there is only one card, of which card number is `1111 1111 1111 1111`.
The card is connected to two accounts: `123-456-789`, `234-567-890`.
More cards and accounts can be added in `DB.py`.