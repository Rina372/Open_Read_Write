cook_book = {}
dish_list = []
with open('recipes.txt', 'rt', encoding='utf-8') as file:
    for l in file:
        dish_name = l.strip()
        ingredients_list = []
        dish = {dish_name: ingredients_list}
        count = file.readline()
        for i in range(int(count)):
            dish1 = file.readline().strip().split(' | ')
            ingredients_list.append({'ingredient_name': dish1[0],
                                     'quantity': int(dish1[1]),
                                     'measure': dish1[2]})
            dish_list.append(dish)
        recipe = file.readline()
        cook_book.update(dish)
# print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for l in cook_book[dish]:
                person_c = int(l['quantity']) * person_count
                dishes_list = {l['ingredient_name']: {'measure':l['measure'], 'quantity': person_c}}
                shop_list.update(dishes_list)
        return shop_list
# print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
