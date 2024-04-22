total_1 = input('Enter your string: ')
total_2 = input('Enter your string: ')
total_3 = input('Enter your string: ')
total_4 = input('Enter your string: ')
with open('Hw.txt', 'w') as f:
    f.write(f'{total_1}\n')
    f.write(f'{total_2}\n')
f = open('Hw.txt', 'a')
f.write(f'{total_3}\n')
f.write(f'{total_4}\n')
f.close()

