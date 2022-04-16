# Simple ATM controller
## Requirements
At least the following flow should be implemented:
Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw
## Description
This program can be executed by running `python ATM.py` in terminal.

There is `DB.py`, which contains a class named `Account` and `Card`. <br>
`DB.py` has information of all cards and accounts connected to the cards.

In `DB.py`, there is only one card, of which card number is `1111 1111 1111 1111`.<br>
The pin number of the card is `1234`. <br>
The card is connected to two accounts: `123-456-789`, `234-567-890`. <br>

To add or update card/account information,`DB.py` can be edited. <br>

## Demos
### 1. When an invalid card is inserted
This is when an entered card number does not consist of 16 digits. 
![](https://github.com/jenehojinchoi/simple-ATM-controller/blob/main/Demos/Invalid_card_inserted.png)

### 2. When a pin number is incorrect
This is when an entered pin number and the pin number corresponding to the card are different.
![](https://github.com/jenehojinchoi/simple-ATM-controller/blob/main/Demos/Wrong_pin_number.png)

### 3. When an invalid account is selected
This is when a user selects an invalid account. (Numbers that are out of range)
![](https://github.com/jenehojinchoi/simple-ATM-controller/blob/main/Demos/Invalid_account_selected.png)



