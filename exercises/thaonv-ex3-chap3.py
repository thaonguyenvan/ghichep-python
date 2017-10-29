try:
    score = float(input('Enter score (0.0 - 1.0): '))
except:
    print('Error, please enter numeric number')
    score = float(input('Enter score (0.0 - 1.0): '))
if 0.0 < score < 1.0 :
    if score >= 0.9 :
        print('A')
    elif 0.8 <= score < 0.9 :
        print('B')
    elif 0.7 <= score < 0.9 :
        print('C')
    elif 0.6 <= score < 0.7 :
        print('C')
    else:
        print('F')
else:
    print('Bad score')