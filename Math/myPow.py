def myPow(self, x: float, n: int) -> float:

    # if the base is 0, return 0 since 0*anything is 0
    if x == 0:
        return 0

    # if the exponent is 0, then return 1 since a^0 = 1
    if n == 0:
        return 1

    # starting number (can't be 0 since x*0=0 but x*1=x to start out)
    res = 1
    # get the absolute value of the power to know our value
    power = abs(n)

    # while power is positive
    while power > 0:
        # essentially checking if its odd (power % 2 == 1)
        if power & 1:
            # if so, then multiply the result by the
            res = res * x

        # regardless if the power is even or not, square it each time
        # allows to halve the time it takes to calculate
        x = x * x

        # divide power by 2 (power = power // 2)
        # loop will stop after the power of 1 is complete since 0 // 2 = 1
        power >>= 1

    # return multiplied total, change to 1/result if it is negative exponent
    return res if n >= 0 else 1 / res
