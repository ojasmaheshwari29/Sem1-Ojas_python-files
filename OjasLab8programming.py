# #1
# s = input()
# vowels = "aeiouAEIOU"
# v_count = c_count = d_count = s_count = o_count = 0

# for ch in s:
#   if ch in vowels:
#     v_count += 1
#   elif ch.isalpha():
#     c_count += 1
#   elif ch.isdigit():
#     d_count += 1
#   elif ch.isspace():
#     s_count += 1
#   else:
#     o_count += 1

# print(f"Vowels: {v_count}")
# print(f"Consonants: {c_count}")
# print(f"Digits: {d_count}")
# print(f"Spaces: {s_count}")
# print(f"Others: {o_count}")
# #2
# text = input("Enter string: ")
# result = ""
# for i in range(len(text)):
#     if i % 2 == 0:
#         result += text[i].upper()
#     else:
#         result += text[i].lower()
# print(result)
# #3
# password = input("Enter password: ")
# if len(password) < 8:
#     print("WEAK")
# else:
#     has_upper = 0
#     has_lower = 0
#     has_digit = 0
#     has_special = 0
#     for char in password:
#         if char.isupper():
#             has_upper = 1
#         elif char.islower():
#             has_lower = 1
#         elif char.isdigit():
#             has_digit = 1
#         elif char != " ":  # Not a letter, digit, or space
#             has_special = 1

#     kinds = has_upper + has_lower + has_digit + has_special
#     if kinds == 4:
#         print("STRONG")
#     elif kinds == 2 or kinds == 3:
#         print("MODERATE")
#     else:
#         print("WEAK")
# #4
# text = input("Enter string: ")
# target = input("Enter character to count: ")
# count = 0
# positions = ""
# for i in range(len(text)):
#     if text[i] == target:
#         count += 1
#         positions += str(i) + " "
# print("Count:", count)
# if count > 0:
#     print("Positions:", positions.strip())
# else:
#     print("Positions: -1")
# #5
# sentence = input("Enter sentence: ")
# words = sentence.split()
# for word in words:
#     print(len(word), end=" ")
# print() 
# #7
# text = input("Enter string: ")
# changes = 0
# n = len(text)
# for i in range(n // 2):
#     if text[i] != text[n - 1 - i]:
#         changes += 1
# print("Changes needed:", changes)
#8
# text = input("Enter string: ")
# result = ""
# for char in text:
#     if char not in result:
#         result += char
# print(result)

