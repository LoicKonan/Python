def pay(Hours, rate):
    if(Hours < 41) and Hours > 0:
        return Hours * rate
    elif (Hours > 40) and Hours > 0:
        return (40 * rate) + ((Hours - 40) * 15)
    else:
        return('Invalid hours')
    
print(pay(45,10))