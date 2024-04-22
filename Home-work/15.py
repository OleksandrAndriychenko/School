def func_2():
    if num.isdigit():
        total = (f'Ви ввели позитивне ціле число: {num}')
    elif num.startswith('-'):
        num_1 = num.strip('-')
        if num_1.isdigit():
            total = (f"Ви ввели від'ємне ціле число: {num}")
        else:
            num_2 = num_1.replace('.','')
            if num_2.isdigit():
                total = (f"Ви ввели від'ємне  дробове число: {num}")
    else:
        num_3 = num.replace('.', '')
        if num_3.isdigit():
            total = (f'Ви ввели позитивне дробове число: {num}')
        else:
            total = (f'Ви ввели не коректне число: {num}')

    return total


while True:
    num = input('Enter a number to continue, if you want to leave enter(вихід, exit, quit, e, q): ')
    if num.lower() in ("вихід", "exit", "quit", "e", "q"):
        break
    else:
        a = func_2()
    print(a)


