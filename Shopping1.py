import sys



User = input('Enter Your Username: ')
Pass = input('Enter Your Password: ')
ConfirmPass = input('Confirm Password:')


class Bank_Account:
	def __init__(self):
		self.balance=0
		print("IMine Bank ")

	def deposit(self):
		amount=float(input("Enter amount to be Deposited: "))
		self.balance += amount
		print("\n Amount Deposited:",amount)

	def withdraw(self):
		amount = float(input("Enter amount to be Withdrawn: "))
		if self.balance>=amount:
			self.balance-=amount
			print("\n You Withdrew:", amount)
		else:
			print("\n Insufficient balance ")

	def display(self):
		print("\n Net Available Balance=",self.balance)


s = Bank_Account()
s.deposit()
s.withdraw()
s.display()

if Pass == ConfirmPass:
    print('Successful')
else :
    print('Not Found Password')
    sys.exit()
print('Welcome ',User, 'to the Market')
shop = input('Enter the request: ')
print('Here you are Request: ',shop)


