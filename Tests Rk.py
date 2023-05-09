# print("\n\tHello World!")
# print()
#
# # List check
# lst1 = [1, 3, 5, 6, 7, 8]
# lst2 = [1, 2, 3, 4, 5, 7]
#
# lista3 = list(set(lst1) & set(lst2))
#
# print("\t", lista3, "\n")
#
#
# # String index - powinno rozlozyc text na kolejne linie w print
#
# text_to_index = input("Podaj teks do rozbicia: ")
# #len(text_to_index)
# # print(len(text_to_index))
# b = len(text_to_index)
# print(b, "\n")
#
# # number = 0
# # a = text_to_index[number]
# # print(a)
# # number = number + 1
# # a = text_to_index[number]
# # print(a,"\n")
#
# number = 0
# # number = int(number)
#
# while number < b:
#     a = text_to_index[number]
#     print(a)
#     number = number + 1
#     if number == b:
#         print()
#
# lcz = input("Lista: ").split(" ")
# # lcz = lcz.split(" ")
# for i in lcz:
#     print(i)
# #print(lcz)
#
# choice_list = [1, 2, 3, 4, 6, 7, 8, 0]
#
# for i in choice_list:
#     print(i)


# symbole = {1: "a", 2: "b", 3: "c"}
#
# for a in symbole:
#     print(symbole[a])
#
# symbole.pop(3)
# print()
# for a in symbole:
#     print(symbole[a])
#
# print()
# print(1 in symbole)
# print(3 in symbole)
# print()
#
# for key, value in symbole.items():
#     print(key,value)

n1 = 1
n2 = 2
def add():
    print(n1 + n2)


add()


def my_mood(answear):
    print("My mood today")
    print(answear)

resp = input("How are You?")
my_mood(resp)


def my_mood2(answear):
    return answear * 2

resp = input("How are You?")
twiced = my_mood2(resp)
print("My mood is like", twiced)