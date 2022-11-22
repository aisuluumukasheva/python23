# banned = input("Ведите запрещенные слова через запятую: ").split(", ")
# text = input("Введите текст: ").lower()

# for word in banned:
#     if word in text:
#         # word = "привет"
#         # len(word) = 6
#         # word.replace("риве", "****")
#         # correct = "п****т"
#         correct = word.replace(word[1: -1], "*" * (len(word) -2))
#         text = text.replace(word, "*"*len(word))
# print("Исправленный текст: ")
# print(text)


def isPalindrome(self, x: int) -> bool:
    if str(x) == str(x[::-1]):
        print(True)
        return True
    else:
        return False
        
isPalindrome(121)