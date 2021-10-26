# The program searches for prime numbers through dividing with previous ones.

numbers = [2, 3, 4]
prime_numbers = [2, 3]

while 1:
    try:
        
        # Add numbers to the numbers list.
        numbers += [numbers[-1] + 1]

        for i in range(1, len(numbers) - 1):
            
            # Check whether the current number is dividable by previous numbers.
            if numbers[-1] / numbers[i] == int(numbers[-1] / numbers[i]):
                break
                
            # Add a prime number to the list.
            elif i == len(numbers) - 2:
                prime_numbers += [numbers[-1]]

    except KeyboardInterrupt:
        
        # Write prime numbers to a text file when CTRL-C is pressed.
        with open('Prime numbers.txt', 'w') as output_file:
            output_file.write(f'PYTHON OVERWRITES THIS FILE EACH TIME.\n\nThere are {len(prime_numbers)} prime numbers till number {numbers[-1]}:')
            for number in prime_numbers:
                output_file.write(f'\n{number}')
        
        break
            
        
