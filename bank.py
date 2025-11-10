# Importing all necessary modules
import random
import string

# Storing all numbers in numbers for ID
numbers = string.digits

# A dict where all the data will be saved
account_details = {}
# A list for transactions notes
notes = []
# A list for transactions history
transaction_history = []

# Function to create an account
def create_account():
    print('\n|---CREATING_ACCOUNT---|')
 
    name = input('\nEnter your name: ')
    account_details['Name'] = name

    while True:

        gmail = input('\nEnter your email: ')

        if not gmail.endswith('@gmail.com'):
            print('\n❌ Error: Email must end with @gmail.com')
        else:
            account_details['Mail'] = gmail
            break

    while True:
        password = input('\nCreate a password: ')
        
        if len(password) < 8:
            print('\n❌ Error: Password must be atleast 8 characters long!')
        else:
            account_details['Password'] = password
            break
    
    id = ''.join(random.sample(numbers, 8))   
    account_details['ID'] = id
    
    print('\n|-✅ Your account has been created succesfully! ✅-|\n')

    for i,(key, value) in enumerate(account_details.items(),start=1):
        print(f'{i} - {key}: {value}')
    
# Function to deposit money
def deposit_money():
    print('\n|---DEPOSIT_MONEY---|')

    while True:
        password_check = input('\nEnter account password: ')

        if password_check in account_details['Password']:
            try:

                amount_to_add = int(input('\nEnter the amount: '))

                if amount_to_add == 0:
                    account_details['Amount'] = 0
                    print('\n🛑 Stop depositing money!')
                    break

                note = input('\nEnter a Note: ').title()
                if note == '0':
                    print('\n🛑 No note add!')
                notes.append(note)
                
                account_details['Amount'] = amount_to_add
                print('\n')
                result = f'Amount: ${amount_to_add} deposited successfully!'
                transaction_history.append(result)
                print(result)
                break

            except ValueError:
                print('\n❌ Error: Invalid amount!')

        else:
            print('\n❌ Error: Incorrect password!')

# Funtion to withdraw money
def withdraw_money():
    print('\n|---WITHDRAW_MONEY---|')

    while True:
        password_check = input('\nEnter account password: ')

        if password_check in account_details['Password']:
            try:

                total_amount = account_details['Amount']
                print(f'\nTotal amount present: ${total_amount}')

                amount_to_withdraw = int(input('\nEnter the amount: '))

                if amount_to_withdraw > total_amount:
                    print(f'\n❌ Error: ${amount_to_withdraw} is higher then actual amount!')
                    continue

                elif total_amount == 0:
                    print('\n❌ Error: No amount deposited yet!')
                    break

                elif amount_to_withdraw == 0:
                    print('\n🛑 Stop withdrawing money!')
                    break

                else:
                    note = input('\nEnter a Note: ').title()

                    if note == '0':
                        print('\n🛑 No note added')
                    notes.append(note)

                    remaining_amount = total_amount - amount_to_withdraw
                    print('\n')
                    result = f'Amount: ${amount_to_withdraw} withdrew successfully!'
                    transaction_history.append(result)
                    print(result)
                    print(f'Remainig amount: ${remaining_amount}')
                    break

            except ValueError:
                print('\n❌ Error: Invalid amount!')
        
        else:
            print('\n❌ Error: Incorrect password!')

# Function to view all transaction
def view_transaction_history():
    print('\n|---TRANSACTION_HISTORY---|\n')

    if not transaction_history:
        print('\n🛑 No transaction history avalible!')

    for i,(transaction, note) in enumerate(zip(transaction_history,notes),start=1):
        print(f'{i}: {transaction.replace('successfully!','')} - {note}')
        
# Function for all type of account settings
def account_settings():
    print('\n|---ACCOUNT_SETTINGS---|')

    while True:  
        print('\n1. View account')
        print('2. Change settings')
        print('3. Exit settings')

        user_input = input('\nEnter (1/2/3): ')
        
        if user_input == '1':
            print('\n--VIEW_ACCOUNT--\n')
            for i,(key, value) in enumerate(account_details.items(),start=1):
                print(f'{i} - {key}: {value}')
        
        elif user_input == '2':
            print('\n--SETTINGS--')
            
            password_check = input('\nEnter you password: ')
            password = account_details['Password']

            if password_check == password:

                print('\n1 - Change name')
                print('2 - Change gmail')
                print('3 - Change password')
                print('4 - Get new ID')

                user_input = int(input('\nEnter (1/2/3/4): '))

                if user_input == 1:
                    
                    new_name = input('\nEnter new name: ')

                    account_details['Name'] = new_name
                    print(f'\n✅ Name changed to [{new_name}] successfully!')
                
                elif user_input == 2:
                    new_gmail = input('\nEnter new gmail: ')

                    if not new_gmail.endswith('@gmail.com'):
                        print('\n❌ Error: Email must end with @gmail.com')
                    else:
                        account_details['Mail'] = new_gmail
                        print(f'\n✅ Gmail changed to [{new_gmail}] successfully!')

                elif user_input == 3:
                    new_password = input('\nEnter new password: ')

                    if len(new_password) < 8:
                        print('\n❌ Error: Password must be atleast 8 characters long!')
                    else:
                        account_details['Password'] = new_password
                        print(f'\n✅ Password changed to [{new_password}] successfully!')
                
                elif user_input == 4: 
                    new_id = ''.join(random.sample(numbers, 8))
                    account_details['ID'] = new_id
                    print('\n✅ ID changed successfully!')
                    print(f'New ID: {new_id}')

                else:
                    print('\n❌ Error: Incorred ID!')
                    continue
            
            else:
                print('\n❌ Error: Incorrect password!')

        elif user_input == '3':
            print('\n🛑 Settings Exited!')
            break

        else:
            print('\n❌ Error: Please enter (1/2/3)!')

# An intro function
def intro():
    print("\n" + "="*50)
    print("          WELCOME TO BANK ACCOUNT SYSTEM")
    print("="*50)
    print("\n   Manage your account, deposits, withdrawals,")
    print("  and track all your  transactions in one place!")
    print("\n" + "-"*50)

# Instruction manual
def instruction_manual():
    print("\n" + "="*50)
    print("              INSTRUCTION MANUAL")
    print("="*50)
    print("\n1. First, create your account")
    print("2. Deposit money to add funds")
    print("3. Withdraw money when needed") 
    print("4. Check transaction history anytime")
    print("5. Modify settings in Account Settings")
    print('6. Enter 0 anytime to stop any deposit or withdrawl!')
    print("\nNote: Remember your Password and ID!")
    print("-"*50)

# Main loop to run the whole program
intro()
create_account()

while True:
    print('\n1. Instruction Manual')
    print('2. Straight to bank account')
    print('3. Exit')

    user_choice = input('\nEnter you choice (1/2/3): ')

    if user_choice == '1':
        instruction_manual()

    elif user_choice == '2':
        print('\n1. Deposit Money')
        print('2. Withdraw Money')
        print('3. View Transaction History')
        print('4. Account Settings')
        print('5. Exit')

        user_choice = input('\nEnter you chioce (1-5): ')

        if user_choice == '1':
            deposit_money()

        elif user_choice == '2':
            withdraw_money()
        
        elif user_choice == '3':
            view_transaction_history()
        
        elif user_choice == '4':
            account_settings()

        elif user_choice == '5':
            print('\nSystem was stopped!')
            break
            
    elif user_choice == '3':
        print('\nSystem was stopped!')
        break

    else:
        print('\n❌ Error: Please enter (1/2/3)')

#____________________________________________________________________________________________________
# Create by: Izram Khan
# Date Created: 10-Nov-2025 (11:53 pm)
# AI usage: 2%
# All credit goes to Izram Khan(98%) and Deepseek(2%)
