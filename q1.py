def intersection_finder(list1, list2):
    list3 = []

    for item in list1:
        if item in list2:
            list3.append(item)

    return list3


print("**************part1****************")


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [6, 7, 8, 9, 10, 11, 12, 13]
print("list1:", list1)
print("list2:", list2)
print("intersection  'list1' and 'list2':", intersection_finder(list1, list2))


print("**************part2****************")

def palindromes_maker(list):
    palindromes = []

    for words in list:
        if words == words[::-1]:
            palindromes.append(words)

    return palindromes


random_list = ["level", "redder", "noon", "stats", "kian", "python"]
print("initial list:",random_list)
print(" palindromes :", palindromes_maker(random_list))

print("**************part3****************")


def prime_finder(list):
    primeList = list.copy()

    for i in range(2, max(primeList) + 1):
        if i in primeList:
            for j in range(i * 2, max(primeList) + 1, i):
                if j in primeList:
                    primeList.remove(j)

    return primeList


numberList = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
print(" prime numbers :", prime_finder(numberList))

print("**************part4****************")


def anagrams(word, word_list):
    output = []
    word = word.lower().replace(" ", "")
    sorted_input = sorted(word)

    for goal_words in word_list:
        goal_words = goal_words.lower().replace(" ", "")
        sorted_goal_words = sorted(goal_words)

        if sorted_input == sorted_goal_words:
            output.append(goal_words)

    return output


input = "heart"
print(" anagram  of:", input, ":",
      anagrams(input, ["earth", "threa", "tear", "hater", "rathe"]))
