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

card_db = [
        Card({
            'name': "Jene's Credit Card",
            'number': "1111 1111 1111 1111",
            'pin_number': "1234",
            'accounts': ["123-456-789", "234-567-890",]
        })
    ]

account_db = [
    Account({
        'name': "Checkings Account",
        'number': "123-456-789",
        'balance': 12000,
    }),
    Account({
        'name': "Savings Account",
        'number': "234-567-890",
        'balance': 50000,
    })
]