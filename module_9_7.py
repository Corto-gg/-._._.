
def is_prime(fanc):

    def wrapper(*args,**kwargs):
        resault = fanc(*args,**kwargs)
        sum_1 = sum(args)
        j = 0
        for i in range(2, sum_1 // 2 + 1):
            if sum_1 % i == 0:
                j = j + 1
        if j <= 0:
            print('Простое')
        else:
            print('Состовное')
        return resault
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)

