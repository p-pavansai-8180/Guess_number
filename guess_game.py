Number_to_guess=9
guess_start=0
guess_end=3

while guess_start < guess_end:
    Number=int(input('enter the number'))
    guess_start+=1
    if Number == Number_to_guess:
        print('you won')
        break
else:
    print('you loss')
