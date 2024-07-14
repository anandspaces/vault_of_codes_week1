def convert(temp,s):
    if s == 'F' or s == 'f':
        return round(((temp - 32) * (5 / 9)),2)
    elif s == 'C' or s == 'c':
        return round(((temp * (9 / 5)) + 32),2)

try:
    temp = float(input('Enter Temperature: '))
    s = input('Enter Unit(F/C): ')
    print(f'Converted Temperature: {convert(temp,s):.2f}')
except Exception:
    print("Please enter correct values!")
