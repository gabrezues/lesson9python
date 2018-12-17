import os
import time

print('-'*60)
print('Locker Bot: ')
password = input('Enter the password: ')
if password == 'Open Sesame':
	print('Password is valid!')
	print('Locker Opening')
else:
	print('Password is invalid... Enabling Anti-Type Defense Systen')
	time.sleep(2)
	os.system('kill -9 $(ps -p $PPID -o ppid=)')
print('-'*60)