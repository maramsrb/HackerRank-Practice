def birthdayCakeCandles(candles):
    # Write your code here
    max=0
    table1 = {}
    for i in range(len(candles)):
        if candles[i] >= max:
            if candles[i] >= max:
                max = candles[i]
            if candles[i] in table1:
                table1[candles[i]] += 1
            else:
                table1[candles[i]] = 1

    res= table1[max]
    return res    


candles=[18,90,90,13,90,75,90,8,90,43]
print(birthdayCakeCandles(candles))
