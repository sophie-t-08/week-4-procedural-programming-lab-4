word1 = input("Enter a word: ")
word2 = input("Enter another word: ")

list1 =list(word1)
list2 = list(word2)

def check_lists(list1, list2):
    list1.sort()
    list2.sort()
    return list1 == list2

print(check_lists(list1, list2))