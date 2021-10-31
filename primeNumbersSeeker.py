# The program searches for prime numbers through dividing with previous ones.

numbers = [2, 3, 4]
prime_numbers = [2, 3]

while 1:
    try: 
        # Add a new number to the numbers list.
        numbers += [numbers[-1] + 1]

        for p in prime_numbers:           
            # Check whether the current number is dividable by previous prime numbers.
            if numbers[-1] % p == 0:
                break
                
        # Add a prime number to the list if the loop was not broken.
        else:
            prime_numbers += [numbers[-1]]       


    # Write prime numbers to a text file when CTRL-C is pressed.
    except KeyboardInterrupt:       
        with open('Prime numbers.txt', 'w') as output_file:
            output_file.write(f'PYTHON OVERWRITES THIS FILE EACH TIME.\n\nThere are {len(prime_numbers)} prime numbers till number {numbers[-1]}:')
            for number in prime_numbers:
                output_file.write(f'\n{number}')
        break
 
