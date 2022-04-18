# Simple ATM controller
## Requirements
At least the following flow should be implemented:
Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw
## Description
The project structure looks like the following:
```
├── README.md
├── Demos
└── controller
    ├── ATM.py
    ├── classes.py
    └── db.py
```

This program can be executed by running `python ./controller/ATM.py` in terminal.<br>
or move to `controller` directory and run `python ATM.py`. <br>

`ATM.py`contains `main` function. <br>
`classes.py`contains a class named `ATM_controller`, `Account`, and `Card`. <br>
`DB.py` has information of all cards and accounts connected to the cards.

In `DB.py`, there are two cards: `1111 1111 1111 1111`, `2222 2222 2222 2222`.<br>

| Card Number                    |  Pin Number       |  Accounts       |
| -----------                    | -----------       | -----------        |
| 1111 1111 1111 1111            | 1234              | 123-456-789, 234-567-890       |
| 2222 2222 2222 2222            | 2222              | 345-678-901, 456-789-012, 567-890-123     |

To add or update card/account information,`DB.py` can be edited. <br>

## Demos
### 0. Demo Video
![](https://github.com/jenehojinchoi/simple-ATM-controller/blob/main/Demos/Demo.gif)

### 1-1. When an invalid card is inserted
This is when an entered card number does not consist of 4 groups of 4 digits and spaces in between each group. For example, the card number entered in the image below does not have a space between the third and fourth group. 
![](https://github.com/jenehojinchoi/simple-ATM-controller/blob/main/Demos/Invalid_card.png)

### 1-2. When there is no card with the card number
This is when the format of the card number is correct but there exists no card with the card number. 
![](https://github.com/jenehojinchoi/simple-ATM-controller/blob/main/Demos/Valid_card_no_card_number.png)

### 2. When a pin number is incorrect
This is when an entered pin number and the pin number corresponding to the card are different.
![](https://github.com/jenehojinchoi/simple-ATM-controller/blob/main/Demos/Wrong_pin_number.png)

### 3. When an invalid account is selected
This is when a user selects an invalid account. (Numbers that are out of range or the number is not a digit). The user is prompted to select an account again.
![](https://github.com/jenehojinchoi/simple-ATM-controller/blob/main/Demos/Invalid_account_selected.png)



