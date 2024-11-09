"""
The payment card is secured with a four-digit PIN code (0805). The program that checks if the PIN code entered
in the payment terminal is correct. The user has up to three possibilities for entering a PIN code. In case of three
unsuccessful attempts, the card is blocked.

Sample result:
Enter the PIN code: 2398
Incorrect...
Enter the PIN code: 0912
Incorrect...
Enter the PIN code: 7860
Incorrect...
Sorry, your payment card has been blocked
"""

max_attempts = 3
attempts = 1

code_input = input('Enter the PIN code: ')
if code_input == '0805':
    print("Success!")
else:
    while attempts < max_attempts:
        print('Incorrect...')
        code_input = input('Enter the PIN code: ')
        attempts +=1
    print('Sorry, your payment card has been blocked')



