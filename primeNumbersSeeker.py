# The program searches for prime numbers through dividing with previous ones.

number = 1
prime_numbers = []

while 1:
    try:
        number += 1

        for p in prime_numbers:           
            # Check whether the current number is dividable by previous prime numbers.
            if number % p == 0:
                break
                
        # Add a prime number to the list if the loop was not broken.
        else:
            prime_numbers += [number]       


    # Write prime numbers to a text file when CTRL-C is pressed.
    except KeyboardInterrupt:       
        with open('Prime numbers.txt', 'w') as output_file:
            output_file.write(f'PYTHON OVERWRITES THIS FILE EACH TIME.\n\nThere are {len(prime_numbers)} prime numbers till number {number}:')
            for p in prime_numbers:
                output_file.write(f'\n{p}')
        break
 
