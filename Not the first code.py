# # first ex.
# print("What's up World?")
#
# # ex01
# dict_1 = {"Family":
#         {"Dad": "Kuvanish",
#          "Mom": "Salima",
#          "Sister": "Sevara",
#          "Me": "Sanjar"},
#           "Age":
#         {"Dad": 1975,
#          "Mom": 1978,
#          "Sister": 2003,
#          "Me": 2007}}
# print(f"My dad's name is {dict_1['Family']['Dad']} and he is {dict_1['Age']['Dad']}\n")
#
# # ex03
# dict_2 = {"first": "первый", "second": "второй", "third": "третий"}
# print(">>> Enter your the word you wanna to translate: ")
# input_1 = input(">>> ")
# if input_1.lower() not in dict_2:
#     print(">>> Error!\n")
# else:
#     print(dict_2[input_1],"\n")
#
# # ex04
# dict_3 = {"Dict": "словарь", "Int": "целое число", "Float": "число сплывающей точкой"}
# for i, k in dict_3.items():
#     print(f"{i} : {k}")
# print("\n")
#
# # ex05
# dict_foods = {"stake": "50$", "burger": "10$", "taco": "20$."}
# print(">>> Enter the food:")
#
# input_food = input(">>> ")
#
# if input_food.lower() in dict_foods:
#     print(f">>> {input_food.lower()} is {dict_foods[input_food]}")
# else:
#     print(">>> Error!")
#
# # ex06
# dict_info = {"name": "Sanjar", "w.b.": [21, 10, 2007], "study": "Astrum academy"}
# dict_info_2 = {"name": "Sevara", "w.b.": [1, 8, 2003], "study": "Yojou University"}
#
# list_info = []
# list_info.append(dict_info)
# list_info.append(dict_info_2)
# for p in list_info:
#     # print(f"Name: {p['name']}, was born in {p['w.b.']}, study at {p['study']}")
#     pass
#
# # ex07
# dict_info["direction"] = "Data science"
# dict_info_2["direction"] = "Medicine"
# for p in list_info:
#     print(f"Name: {p['name']}, was born in {p['w.b.']}, study at {p['study']}, direction {p['direction']}")
#
# # ex08
#
# books = []
# print("\n>>> Your favorite book:")
# input_book = ''
# while input_book.lower() != "end":
#     input_book = input("\n>>> ")
#     books.append(input_book.title())
#     if input_food.lower() == "end":
#         break
# for q in books:
#     if q == "End":
#         books.remove(q)
# print(books)
# print(">>> Ended")
# books.clear()
# # To save answers, remove the top code(74)
#
# # ex09
#
# while True:
#     input_age_to_ticket = input("\n>>> Your age: ")
#     if input_age_to_ticket.lower() == 'stop':
#         true_false_age = "stop"
#         print(">>> Stop!")
#         break
#     elif int(input_age_to_ticket) <= 7:
#         print(">>> Ticked price: 2$")
#     elif 7 < int(input_age_to_ticket) and int(input_age_to_ticket) <= 18:
#         print(">>> Ticked price: 3$")
#     elif 18 < int(input_age_to_ticket) and int(input_age_to_ticket) <= 65:
#         print(">>> Ticked price: 10$")
#     elif 65 < int(input_age_to_ticket):
#         print(">>> Ticked price: free!")
#     else:
#         print(">>> Error!")
#
# # ex10
#
# list_product = []
# number = 1
#
# while True:
#     input_input = input(f">>> {number} - product: ")
#     list_product.append(input_input)
#     yes_or_no = input(">>> Do you wanna continue? (yes / no): ")
#     number += 1
#     if yes_or_no != "yes":
#         break
#
# number_2 = 1
# for p in range(len(list_product)):
#     print(f"{number_2} - product : {list_product[p]}")
#     number_2 += 1

# ex11

def rand(p1):
    global result

    if p1[0].lower() and p1[1].lower() in "qwrtypsdfghjklzxcvbnm":
        first_letters = p1[:2]
        result = p1[2:] + first_letters + "ay"

    elif p1[0].lower() in "qwrtypsdfghjklzxcvbnm":
        first_letters_ = p1[0]
        result = p1[1:] + first_letters_ + "ay"

    else:
        result = p1 + "ay"
    return result

while True:
    input_word = input(">>> Enter word: ")
    print(rand(input_word))
    iuiua = input(">>> Push 'ENTER' if you wanna continue!")
    if iuiua == "no":
        break