#Control Structures
# If....Else
years = 17
if years>=18:
    print('Your are an adult.')
    print('you have',years,'Years.')
else:
    print('Your are a child.')
    print('you have', years, 'Years.')

n = int(input('Enter a number:'))
if n>0:
    print(n,'is a positive number')
elif n==0:
    print(n,'is a zero.')
else:
    print(n,'is a negative number')
