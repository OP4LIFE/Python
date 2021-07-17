# NAVODILA:
# Vprašaj 'Who are you?'.
# Če ime ni Joe, ponovno vprašaj who are you.
# Če ime je Joe, ga pozdravi in vprašaj za geslo.
# Če je geslo swordfish, izpiši 'Access granted'.
# Če geslo ni swordfish, ponovi vsa vprašanja od začetka.
# Nikoli se ne udaj.

while True:
	print('Who are you?')
	name = input()
	if name != 'Joe':
		continue
	print('Welcome Joe, what is the password?')
	password = input()
	if password == 'swordfish':
		break
print('Access granted')
