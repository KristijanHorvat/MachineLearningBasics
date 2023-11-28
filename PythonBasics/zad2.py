while True:
    
    try:
        value = float(input('Value between 0.0 and 1.0:'))
        if 0.0 <= value <= 1.0:
            break
        else:
            raise ValueError
    except ValueError:
       print("izvan granica")

if value>=0.9:
    print("A")
elif value>=0.8:
    print("B")
elif value>=0.7:
    print("C")
elif value>=0.6:
    print("D")
elif value>=0.5:
    print("F")
