secret_number = 5
guess_limit = 3
guess_count = 0
while guess_count <= guess_limit:
    number = int(input("Enter number  "))
    guess_count += 1
    if number == secret_number:
        print('You won')
        break
    else:
        print('You lose')

    
