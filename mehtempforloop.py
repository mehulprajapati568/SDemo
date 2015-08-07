temp =eval(raw_input("enter value"))
while True:
    if temp > 31 and temp < 35:
        print 'sunny day'
        break
    elif temp > 35 and temp < 40:
        print 'warm day'
        break
    elif temp > 40 and temp < 45:
        print 'high temperature'
        break
    else:
        print 'value Invalid'
        break
