from classes import Card, Account

card_db = [
        Card({
            'name': "Jene's Credit Card",
            'number': "1111 1111 1111 1111",
            'pin_number': "1234",
            'accounts': ["123-456-789", "234-567-890",]
        }),
        Card({
            'name': "A's Debit Card",
            'number': "2222 2222 2222 2222",
            'pin_number': "2222",
            'accounts': ["345-678-901", "456-789-012", "567-890-123"]
        })
    ]


account_db = [
    Account({
        'name': "Checking Account",
        'number': "123-456-789",
        'balance': 12000,
    }),
    Account({
        'name': "Savings Account",
        'number': "234-567-890",
        'balance': 50000,
    }),
    Account({
        'name': "Checking Account 1",
        'number': "345-678-901",
        'balance': 10000,
    }),
    Account({
        'name': "Checking Account 2",
        'number': "456-789-012",
        'balance': 45000,
    }),
    Account({
        'name': "Savings Account",
        'number': "567-890-123",
        'balance': 1000000,
    })
]