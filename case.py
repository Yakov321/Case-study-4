
'''
   Part of case-study #4
   
   Developers: Saipulaev A., Batrakova K., Tolstov J.

'''
import art_local as art
day = int(input(art.date)) 
temp = int(input(art.temperature)) 
money = 10000000000 
broken = False 
match day: 
    case 1: 
        t = 10 
        if (t - 2) <= temp <= (t + 2): 
            print(art.good) 
        elif (t - 4) <= temp <= (t - 2) or (t + 2) <= temp <= (t + 4): 
            print(art.failure) 
        elif temp < (t - 4) or (t + 4) < temp: 
            print(art.damage) 
            broken = True 
    case 2: 
        t = 20 
        if (t - 2) <= temp <= (t + 2): 
            print(art.good) 
        elif (t - 4) <= temp <= (t - 2) or (t + 2) <= temp <= (t + 4): 
            print(art.failure) 
        elif temp < (t - 4) or (t + 4) < temp: 
            print(art.damage) 
            broken = True 
    case 3: 
        t = 17 
        if (t - 2) <= temp <= (t + 2): 
            print(art.good) 
        elif (t - 4) <= temp <= (t - 2) or (t + 2) <= temp <= (t + 4): 
            print(art.failure) 
        elif temp < (t - 4) or (t + 4) < temp: 
            print(art.damage) 
            broken = True 
    case 4: 
        t = 14 
        if (t - 2) <= temp <= (t + 2): 
            print(art.good) 
        elif (t - 4) <= temp <= (t - 2) or (t + 2) <= temp <= (t + 4): 
            print(art.failure) 
        elif temp < (t - 4) or (t + 4) < temp: 
            print(art.damage) 
            broken = True 
    case 5: 
        t = 6 
        if (t - 2) <= temp <= (t + 2): 
            print(art.good) 
        elif (t - 4) <= temp <= (t - 2) or (t + 2) <= temp <= (t + 4): 
            print(art.failure) 
        elif temp < (t - 4) or (t + 4) < temp: 
            print(art.damage) 
            broken = True 
    case 6: 
        t = 9 
        if (t - 2) <= temp <= (t + 2): 
            print(art.good) 
        elif (t - 4) <= temp <= (t - 2) or (t + 2) <= temp <= (t + 4): 
            print(art.failure) 
        elif temp < (t - 4) or (t + 4) < temp: 
            print(art.damage) 
            broken = True 
    case 7: 
        t = 25 
        if (t - 2) <= temp <= (t + 2): 
            print(art.good) 
        elif (t - 4) <= temp <= (t - 2) or (t + 2) <= temp <= (t + 4): 
            print(art.failure) 
        elif temp < (t - 4) or (t + 4) < temp: 
            print(art.damage) 
            broken = True 
    case 8: 
        t = 11 
        if (t - 2) <= temp <= (t + 2): 
            print(art.good) 
        elif (t - 4) <= temp <= (t - 2) or (t + 2) <= temp <= (t + 4): 
            print(art.failure) 
        elif temp < (t - 4) or (t + 4) < temp: 
            print(art.damage) 
            broken = True 
    case 9: 
        t = 17 
        if (t - 2) <= temp <= (t + 2): 
            print(art.good) 
        elif (t - 4) <= temp <= (t - 2) or (t + 2) <= temp <= (t + 4): 
            print(art.failure) 
        elif temp < (t - 4) or (t + 4) < temp: 
            print(art.damage) 
            broken = True 
    case 10: 
        t = 7 
        if (t - 2) <= temp <= (t + 2): 
            print(art.good) 
        elif (t - 4) <= temp <= (t - 2) or (t + 2) <= temp <= (t + 4): 
            print(art.failure) 
        elif temp < (t - 4) or (t + 4) < temp: 
            print(art.damage) 
            broken = True 
    case 11: 
        t = 5 
        if (t - 2) <= temp <= (t + 2): 
            print(art.good) 
        elif (t - 4) <= temp <= (t - 2) or (t + 2) <= temp <= (t + 4): 
            print(art.failure) 
        elif temp < (t - 4) or (t + 4) < temp: 
            print(art.damage) 
            broken = True 
    case 12: 
        t = 16 
        if (t - 2) <= temp <= (t + 2): 
            print(art.good) 
        elif (t - 4) <= temp <= (t - 2) or (t + 2) <= temp <= (t + 4): 
            print(art.failure)
        elif temp < (t - 4) or (t + 4) < temp: 
            print(art.damage) 
            broken = True 
    case 13: 
        t = 22 
        if (t - 2) <= temp <= (t + 2): 
            print(art.good) 
        elif (t - 4) <= temp <= (t - 2) or (t + 2) <= temp <= (t + 4): 
            print(art.failure) 
        elif temp < (t - 4) or (t + 4) < temp: 
            print(art.damage) 
            broken = True 
    case 14: 
        t = 8 
        if (t - 2) <= temp <= (t + 2): 
            print(art.good) 
        elif (t - 4) <= temp <= (t - 2) or (t + 2) <= temp <= (t + 4): 
            print(art.failure) 
        elif temp < (t - 4) or (t + 4) < temp: 
            print(art.damage) 
            broken = True 
    case 15: 
        t = 15 
        if (t - 2) <= temp <= (t + 2): 
            print(art.good) 
        elif (t - 4) <= temp <= (t - 2) or (t + 2) <= temp <= (t + 4): 
            print(art.failure) 
        elif temp < (t - 4) or (t + 4) < temp: 
            print(art.damage) 
            broken = True 
    case 16: 
        t = 8 
        if (t - 2) <= temp <= (t + 2): 
            print(art.good) 
        elif (t - 4) <= temp <= (t - 2) or (t + 2) <= temp <= (t + 4): 
            print(art.failure) 
        elif temp < (t - 4) or (t + 4) < temp: 
            print(art.damage) 
            broken = True 
    case 17: 
        t = 21 
        if (t - 2) <= temp <= (t + 2): 
            print(art.good) 
        elif (t - 4) <= temp <= (t - 2) or (t + 2) <= temp <= (t + 4): 
            print(art.failure) 
        elif temp < (t - 4) or (t + 4) < temp: 
            print(art.damage) 
            broken = True 
    case 18: 
        t = 25 
        if (t - 2) <= temp <= (t + 2): 
            print(art.good) 
        elif (t - 4) <= temp <= (t - 2) or (t + 2) <= temp <= (t + 4): 
            print(art.failure) 
        elif temp < (t - 4) or (t + 4) < temp: 
            print(art.damage) 
            broken = True 
    case 19: 
        t = 24 
        if (t - 2) <= temp <= (t + 2): 
            print(art.good) 
        elif (t - 4) <= temp <= (t - 2) or (t + 2) <= temp <= (t + 4): 
            print(art.failure) 
        elif temp < (t - 4) or (t + 4) < temp: 
            print(art.damage) 
            broken = True 
    case 20: 
        t = 13 
        if (t - 2) <= temp <= (t + 2): 
            print(art.good) 
        elif (t - 4) <= temp <= (t - 2) or (t + 2) <= temp <= (t + 4): 
            print(art.failure) 
        elif temp < (t - 4) or (t + 4) < temp: 
            print(art.damage) 
            broken = True 
    case 21: 
        t = 8 
        if (t - 2) <= temp <= (t + 2): 
            print(art.good) 
        elif (t - 4) <= temp <= (t - 2) or (t + 2) <= temp <= (t + 4): 
            print(art.failure) 
        elif temp < (t - 4) or (t + 4) < temp: 
            print(art.damage) 
            broken = True 
    case 22:
        t = 15
        if (t - 2) <= temp <= (t + 2):
            print(art.good) 
        elif (t - 4) <= temp <= (t - 2) or (t + 2) <= temp <= (t + 4):
            print(art.failure) 
        elif temp < (t - 4) or (t + 4) < temp:
            print(art.damage) 
            broken = True 
    case 23: 
        t = 5 
        if (t - 2) <= temp <= (t + 2): 
            print(art.good) 
        elif (t - 4) <= temp <= (t - 2) or (t + 2) <= temp <= (t + 4): 
            print(art.failure) 
        elif temp < (t - 4) or (t + 4) < temp: 
            print(art.damage) 
            broken = True 
    case 24: 
        t = 19 
        if (t - 2) <= temp <= (t + 2): 
            print(art.good) 
        elif (t - 4) <= temp <= (t - 2) or (t + 2) <= temp <= (t + 4): 
            print(art.failure) 
        elif temp < (t - 4) or (t + 4) < temp: 
            print(art.damage) 
            broken = True
    case 25: 
        t = 22 
        if (t - 2) <= temp <= (t + 2): 
            print(art.good) 
        elif (t - 4) <= temp <= (t - 2) or (t + 2) <= temp <= (t + 4): 
            print(art.failure) 
        elif temp < (t - 4) or (t + 4) < temp: 
            print(art.damage) 
            broken = True 
    case 26: 
        t = 10 
        if (t - 2) <= temp <= (t + 2): 
            print(art.good) 
        elif (t - 4) <= temp <= (t - 2) or (t + 2) <= temp <= (t + 4): 
            print(art.failure) 
        elif temp < (t - 4) or (t + 4) < temp: 
            print(art.damage) 
            broken = True 
    case 27: 
        t = 11 
        if (t - 2) <= temp <= (t + 2): 
            print(art.good) 
        elif (t - 4) <= temp <= (t - 2) or (t + 2) <= temp <= (t + 4): 
            print(art.failure) 
        elif temp < (t - 4) or (t + 4) < temp: 
            print(art.damage) 
            broken = True 
    case 28: 
        t = 12 
        if (t - 2) <= temp <= (t + 2): 
            print(art.good) 
        elif (t - 4) <= temp <= (t - 2) or (t + 2) <= temp <= (t + 4): 
            print(art.failure) 
        elif temp < (t - 4) or (t + 4) < temp: 
            print(art.damage) 
            broken = True 
    case 29: 
        t = 9 
        if (t - 2) <= temp <= (t + 2): 
            print(art.good) 
        elif (t - 4) <= temp <= (t - 2) or (t + 2) <= temp <= (t + 4): 
            print(art.failure) 
        elif temp < (t - 4) or (t + 4) < temp: 
            print(art.damage) 
            broken = True 
    case 30: 
        t = 8 
        if (t - 2) <= temp <= (t + 2): 
            print(art.good) 
        elif (t - 4) <= temp <= (t - 2) or (t + 2) <= temp <= (t + 4): 
            print(art.failure) 
        elif temp < (t - 4) or (t + 4) < temp: 
            print(art.damage) 
            broken = True 
    case _: 
        print(art.error) 
if broken is True: 
    print(art.option_1_price) 
    print(art.option_1_repair)
    print(art.option_2_price) 
    print(art.option_2_repair)
    print(art.option_3_price) 
    print(art.option_3_repair) 
     
    way = int(input(art.option)) 
match way: 
    case 1: 
        money -= 1000000000 
        print(f'У вас осталось {money} тенге') 
        print(art.diamond) 
    case 2: 
        money -= 100000000 
        print(f'У вас осталось {money} тенге') 
        print(art.platinum) 
    case 3: 
        money -= 10000000 
        print(f'У вас осталось {money} тенге') 
        print(art.done)
