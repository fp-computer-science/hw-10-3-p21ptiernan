# Author PT 12/9/20

# Problem 5

def no_odds(lst):
    num_odds = 0
    num = 1
    while num < lst+1:
        if num % 2 == 0:
            num_odds += num
            num += 1
    return num_odds


result = no_odds([2, 4, 6, 8, 9])
print(result)
