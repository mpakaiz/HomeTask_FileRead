from pprint import pprint
with open('data.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ing_count = int(file.readline())
        ingredients = []
        for _ in range(ing_count):
            ingredient, quantity, measure = file.readline().strip().split(" | ")
            ingredients.append({
                'ingredient_name': ingredient,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[dish_name] = ingredients
    # pprint(cook_book, sort_dicts=False)

def get_shop_list_by_dishes(dishes, person_count):
    total = {}
    for dish, ingrs in cook_book.items():
        if dish in dishes:
            for q in ingrs:
                if q.get('ingredient_name') not in total.keys():
                    total[q.get('ingredient_name')] = {
                                                        'measure': q.get('measure'),
                                                        'quantity': int(q.get('quantity')) * person_count
                    }
                else:
                    total[q.get('ingredient_name')] = {
                                                        'measure': q.get('measure'),
                                                        'quantity': int(q.get('quantity')) * person_count
                                                                    + int(total[q.get('ingredient_name')]['quantity'])
                    }
    pprint(total)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print('___________')
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 3)


