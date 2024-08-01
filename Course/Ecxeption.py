

try: 
    print(1/0)
except (ZeroDivisionError, IndexError) as e:
    print("Message")
    print(e)
