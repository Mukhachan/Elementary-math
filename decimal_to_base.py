def decimal_to_base(n, b):
    if n == 0:
        return '0'

    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = []

    while n > 0:
        res.append(digits[n % b])
        n //= b

    return ''.join(res[::-1])