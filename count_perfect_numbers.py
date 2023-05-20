def count_perfect_numbers(start, end):
    count = 0 # счетчик совершенных чисел, изначально равен нулю
    
    for num in range(start, end+1): # перебираем все числа от start до end
        sum_divisors = 0 # сумма делителей числа, изначально равна нулю
        
        for divisor in range(1, num): # перебираем все возможные делители числа
            if num % divisor == 0: # если divisor делит num без остатка,
                sum_divisors += divisor # то добавляем divisor к сумме делителей
                
        if sum_divisors == num: # если сумма делителей равна самому числу,
            count += 1 # то это совершенное число, увеличиваем счетчик
            
    return count # возвращаем количество совершенных чисел