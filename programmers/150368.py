from itertools import product

def solution(users, emoticons):
    discounts = [10, 20, 30, 40]
    m = len(emoticons)
    max_plus = 0
    max_sales = 0
    
    for rates in product(discounts, repeat=m):
        sales = 0
        plus = 0
        
        for user in users:
            min_disc, min_price = user
            total = 0
            
            for i in range(m):
                if rates[i] >= min_disc:
                    price = emoticons[i] * (100 - rates[i]) // 100
                    total += price
            
            if total >= min_price:
                sales += 1
            else:
                sales += total
        
        if plus > max_plus or (plus == max_plus and sales > max_sales):
            max_plus = plus
            max_sales = sales
        
    answer = [max_plus, max_sales] 
    return answer