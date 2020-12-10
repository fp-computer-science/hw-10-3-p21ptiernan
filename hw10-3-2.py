# Author PT 12/9/20

# Problem 3

def three_letter_words(lst):
    three_ltr = len(lst)
    three = 1
    while three_ltr < three+1:
        if len(lst) == 3:
            x = int(len(lst)) == 3
            three_ltr += x
            three += x
        return three_ltr


result = three_letter_words(["cat", "bat", "apple"])
print(result)
