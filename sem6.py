# def more_five(x):
#     if x > 5:
#         return True

# print(more_five(10))  

# def summ(x):
#     return x +2 


# func = lambda x: x+2    


from random import randint


lst = ['3', '5', '7', '4']
res = map(int, lst)



# print(list(res))     #  На печать выводится список: [3, 5, 7, 4]
# print(tuple(res))    #  на печать выодится кортеж: (3, 5, 7, 4)

# res2 = map(summ, res)
# res2 = map(lambda x: x*2, res)
# print(tuple(res2))


def more_five(x):
    if x > 5:
        return True
 

# res_map = map(more_five, res)
#print(list(res_map))
# res_filter = filter(more_five, res)
# print(list(res_filter))


# ====================
# list compehention, set comprih. (множества)
# ====================

res_range = []
for i in range(10):
    res_range.append(randint(0, 10))

# print(res_range)

# то же, но короче:

new_list = [randint(0, 10) for i in range(10) if i % 2 == 0] # список
# print(rand_list)


set_cmp = {randint(0, 10) for i in range(10)} # множество (только уникальные элементы)
# print(set_cmp)


dict_cmp = {i: randint(0, 10) for i in range(10)} # словарь
# print(dict_cmp)

rand_list = (randint(0, 10) for i in range(10)) # генератор
# print(list(rand_list))

# ================
# несколько способов перебора:

# for i in range(5):
#     rand_list[i]

# for i in rand_list:

# for i, a in enumerate(rand_list):  # множественное присвоение
#     print(f'{i = }, {a = }')

# for w in enumerate(rand_list):    # кортежи
    # print(w)

s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::7])