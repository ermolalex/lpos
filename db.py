db = [
    {'plu': 1, 'name': 'Молоко', 'unit_price': 65},
    {'plu': 2, 'name': 'Сыр', 'unit_price': 980},
    {'plu': 3, 'name': 'Колбаса', 'unit_price': 348},
    {'plu': 4, 'name': 'Вино', 'unit_price': 2065},
    {'plu': 5, 'name': 'Водка', 'unit_price': 765},
]

def search(plu):
    res = None
    for item in db:
        if item['plu'] == plu:
            res = item
            break
    return res