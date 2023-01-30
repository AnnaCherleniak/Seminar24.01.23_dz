# 1. Надо написать функцию choose_coffee(preference1, preference2,..., preferenceN), которая
# возвращает напиток, который можно приготовить из имеющихся продуктов (ingredients). На
# вход функция принимает заранее неизвестное количество предпочтений посетителя. Все
# напитки перечислены в порядке убывания предпочтений и гарантированно не повторяются.
# Бариста готовит наиболее предпочитаемый напиток из доступных.
def diff(first_list, second_list):
    some_list =[]
    for i in range(len(first_list)):
        some_list.append(first_list[i] - second_list[i])
    for el in some_list:
        if el < 0:
            some_list = ''
    return some_list


def chosee_coffe(ing, ing_dict, *args):
    args_list = []
    for i in args:
        args_list.append(i)
    count = 0
    for i in range(len(args_list)):
        if args_list[i] in ing_dict.keys():
            some_list = diff(ing, ing_dict[args_list[i]])
            if some_list:
                ing = some_list
                count += 1
                name = args_list[i]
                break
    if count == 0:
        return "К сожалению, не можем предложить Вам напиток", ing
    return name, ing
    

# 0 - зерна
# 1 - молоко
# 2 - сливки
ingredients = [4, 4, 0]
ing_dict = {} 
ing_dict["эспрессо"]= [1, 0, 0]
ing_dict["капучино"] = [1, 3, 0]
ing_dict["маккиато"] = [2, 1, 0]
ing_dict["кофе по-венски"] = [1, 0, 2]
ing_dict["латте маккиато"] = [1, 2, 1]
ing_dict["кон панна"] = [1, 0, 1]

print(chosee_coffe(ingredients, ing_dict, "капучино", "маккиато", "эспрессо")[0])
ingredients = chosee_coffe(ingredients, ing_dict, "капучино", "маккиато", "эспрессо")[1]
print(chosee_coffe(ingredients, ing_dict, "капучино", "маккиато", "эспрессо")[0])
ingredients = chosee_coffe(ingredients, ing_dict, "капучино", "маккиато", "эспрессо")[1]
print(chosee_coffe(ingredients, ing_dict, "капучино", "маккиато", "эспрессо")[0])
ingredients = chosee_coffe(ingredients, ing_dict, "капучино", "маккиато", "эспрессо")[1]
