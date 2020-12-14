# PT 12/9/20

# Question 1


def count_odds(lst):
    num_odds = 0
    num = 0
    while num < len(lst):
        if lst[num] % 2 != 0:
            num_odds += 1
            num += 1
    return num_odds


result = count_odds([1, 2, 3, 4, 5, 6])
print(result)
