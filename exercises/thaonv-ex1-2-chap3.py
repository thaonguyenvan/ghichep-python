while True :

    try:
        hour = float(input('Enter hours: '))
    except:
        print('Error, enter numeric input')
        hour = float(input('Enter hours: '))
    try:
        rate = float(input('Enter rate: '))
    except:
        print('Error, enter numeric input')
        rate = float(input('Enter rate: '))
    if hour > 40:
        above = hour - 40
        pay = (40 * rate) + (above * (rate * 1.5))
    else:
        pay = hour * rate
        
    print('Pay: ', pay)
    cont = input('Do you want to calculate more? (yes/no)')
    if cont == 'yes' :
        continue
    elif cont == 'no' :
        break
    else :
        print('Please enter "yes" or "no"')
        cont = input('Do you want to calculate more? (yes/no)')