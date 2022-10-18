cook_book = {}
dish_list = []
with open('recipes.txt', 'w', encoding='utf-8') as file:
    for l in file:
        dish_name = l.strip()
        ingredients_list = []
        count = file.readline()
        for i in range(int(count)):
            dish = file.readline().strip().split(' | ')
            ingredients_list.append({'ingredient_name': dish[0],
                                     'quantity': dish[1],
                                     'measure': dish[2]})
            dish_list.append(dish)
        recipe = file.readline()
        cook_book.update(dish)
print(cook_book)
        # for l in file:
        #     dish_name = l.strip()
        #     ingredients_list = []
        #     dish = {dish_name: ingredients_list}
        #     dish_count = file.readline()
        #     for i in range(int(dish_count)):
        #         dsh = file.readline().strip().split(' | ')
        #         ingredients_list.append({'ingredient_name': dsh[0],
        #                                  'quantity': int(dsh[1]),
        #                                  'measure': dsh[2]})
        #         dish_list.append(dish)
        #     blank_line = file.readline()
        #     cook_book.update(dish)
        # cook_book = {
        #     'Омлет': [
        #         {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
        #         {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
        #         {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
        #     ],
        #     'Утка по-пекински': [
        #         {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
        #         {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
        #         {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
        #         {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
        #     ],
        #     'Запеченный картофель': [
        #         {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
        #         {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
        #         {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
        #     ]
        # }