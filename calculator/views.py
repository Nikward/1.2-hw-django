from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },

}


def calculate_recipe(request, recipe):
    # Количество порций из запроса. По умолчаний количество порций = 1
    servings = int(request.GET.get('servings', 1))
    # Список ингредиентов из DATA
    recipe_ingr = DATA.get(recipe)
    # Вычисляем ингредиенты в зависимости от кол-ва порций
    recipe_result = {}
    for name, value in recipe_ingr.items():
        recipe_result[name] = value * servings

    context = {
        'recipe': recipe_result
    }
    return render(request, 'calculator/index.html', context)
