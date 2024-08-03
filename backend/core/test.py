from core.models import *

meals = [
    {
        "name": "Спагетти Болоньезе",
        "description": "Классическое итальянское блюдо с пастой и сытным мясным соусом.",
        "price": 350,
        "categories": ["Паста", "Итальянская кухня"],
        "ingredients": ["Молотый говяжий фарш", "Лук", "Чеснок", "Томатный соус", "Томаты", "Итальянские специи", "Спагетти"],
        "image": "https://kremlin-product.ru/upload/medialibrary/241/jfw6bequvf8s8mcum1npqc0jx1v1ngad/grilled_vegetables.jpg"
    },
    {
        "name": "Цезарь с курицей",
        "description": "Освежающий салат с жареной курицей, хрустящим салатом и соусом Цезарь.",
        "price": 280,
        "categories": ["Салаты", "Американская кухня"],
        "ingredients": ["Жареная куринная грудка", "Салат романо", "Крутоны", "Пармезан", "Соус Цезарь", "Лимонный сок", "Оливковое масло"],
        "image": "https://s.restorating.ru/w/1920x1080/articles/2920/None-111028.jpeg",
    },
    {
        "name": "Овощной вок",
        "description": "Быстрый и красочный вок с овощами и тофу или выбранным вами видом белка.",
        "price": 300,
        "categories": ["Овощи", "Азиатская кухня"],
        "ingredients": ["Тофу", "Брокколи", "Болгарский перец", "Морковь", "Снеговые горошинки", "Соевый соус", "Имбирь", "Чеснок", "Соевое масло"],
        "image": "https://gotovim-doma.ru/images/recipe/e/ce/eceb453fefbab09075a8c779712e52f8.jpg",
    },
    {
        "name": "Такос с говядиной",
        "description": "Ароматная приправленная говядина в тортильях с начинкой.",
        "price": 320,
        "categories": ["Мексиканская кухня"],
        "ingredients": ["Молотая говядина", "Приправа для тако", "Тортильи", "Салат", "Помидоры", "Сыр", "Сальса", "Сметана"],
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNVW3bTlMbUA_8-fbvHUgW1KaIEKaLANG0dg&usqp=CAU",
    },
    {
        "name": "Грибной ризотто",
        "description": "Кремовое итальянское блюдо с жареными грибами и пармезаном.",
        "price": 380,
        "categories": ["Ризотто", "Итальянская кухня"],
        "ingredients": ["Рис арборио", "Грибы", "Лук", "Белое вино", "Куриный бульон", "Пармезан", "Масло"],
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBsyitq8OdeFsdjKzPHO_ntFd0k9HnlM1NvA&usqp=CAU",
    },
    {
        "name": "Лосось с лимонно-укропным соусом",
        "description": "Жареный или запеченный лосось подается с ароматным соусом из лимона и укропа.",
        "price": 420,
        "categories": ["Рыба", "Скандинавская кухня"],
        "ingredients": ["Филе лосося", "Лимон", "Свежий укроп", "Оливковое масло", "Чеснок", "Соль и перец"],
        "image": "https://kandbi.com/image/catalog/blog/firmennoe-blyudo-v-restorane-chto-eto-i-kakim-ono-byvaet-2.jpg",
    },
    {
        "name": "Капрезе Панини",
        "description": "Жареный бутерброд с моцареллой, помидорами и базиликом.",
        "price": 250,
        "categories": ["Панини", "Итальянская кухня"],
        "ingredients": ["Хлеб чиабатта", "Моцарелла", "Помидоры", "Свежие листья базилика", "Бальзамический глазурь", "Оливковое масло"],
        "image": "https://cdn.lifehacker.ru/wp-content/uploads/2020/04/5e95669b997f5_j3hekga7e3r41__700_1587380182-e1587380213139.jpg",
    },
    {
        "name": "Овощное Карри",
        "description": "Острое и ароматное карри с разнообразными овощами.",
        "price": 290,
        "categories": ["Карри", "Азиатская кухня"],
        "ingredients": ["Смешанные овощи", "Карри-паста", "Кокосовое молоко", "Лук", "Чеснок", "Имбирь", "Рис басмати"],
        "image": "https://e0.edimdoma.ru/data/posts/0002/1936/21936-ed4_wide.jpg?1679398231",
    },
    {
        "name": "Куриное Альфредо Паста",
        "description": "Кремовый соус Альфредо с жареной куриной грудкой над лапшой феттучини.",
        "price": 360,
        "categories": ["Паста", "Итальянская кухня"],
        "ingredients": ["Лапша феттучини", "Куриная грудка", "Тяжелая сливка", "Пармезан", "Масло", "Чеснок", "Соль и перец"],
        "image": "https://hip2go.ru/api2/images/IikoProducts26/c1c668e7c6-1_500x353.jpg",
    },
    {
        "name": "Салат с киноа, авокадо и чёрными бобами",
        "description": "Питательный салат с киноа, авокадо, чёрными бобами и лаймовым винегретом.",
        "price": 310,
        "image": "https://takethemameal.com/files_images_v2/stam.jpg",
        "categories": ["Салаты", "Здоровое питание"],
        "ingredients": ["Киноа", "Чёрные бобы", "Авокадо", "Вишня томаты", "Красный лук", "Кинза", "Сок лайма", "Оливковое масло", "Соль и перец"],
    }
]

for i in meals:
    for r in Restaurant.objects.all():
        meal = Meal.objects.create(
            name=i['name'], description=i['description'], price=i['price'], image=i['image'], restaurant=r)
        for cat in i['categories']:
            category, _ = Category.objects.get_or_create(
                name=cat, defaults={'name': cat})
            meal.categories.add(category)
        for ing in i['ingredients']:
            ing, _ = Ingredient.objects.get_or_create(
                name=ing, defaults={'name': ing})
            meal.ingredients.add(ing)


restaurants = [
    {
        "name": "Итальянская Гастрономия",
        "description": "Приглашаем вас насладиться аутентичной итальянской кухней.",
        "image": "https://gotovim-doma.ru/images/recipe/e/ce/eceb453fefbab09075a8c779712e52f8.jpg",
        "address": "ул. Итальянская, 123",
        "categories": ["Паста", "Итальянская кухня"]
    },
    {
        "name": "Салатная Оазис",
        "description": "Здесь вы найдете разнообразные свежие салаты для здорового питания.",
        "image": "https://www.tokyo-city.ru/images/interesno/ot-edy-bednyakov-do-izyskannykh.jpg",
        "address": "пр. Здоровья, 456",
        "categories": ["Салаты", "Здоровое питание"]
    },
    {
        "name": "Американский Дайнер",
        "description": "Погрузитесь в атмосферу настоящего американского дайнера с классическими блюдами.",
        "image": "https://www.bahroma1.ru/templates/bahroma1/img/slider/2300x1500_61b11ccbd3b30.jpg",
        "address": "ул. Американская, 789",
        "categories": ["Американская кухня"]
    },
    {
        "name": "Азиатский Уголок",
        "description": "Приготовлено с любовью — азиатские блюда с использованием свежих овощей и традиционных приправ.",
        "image": "https://www.edimdoma.ru/data/posts/0002/1061/21061-ed4_wide.jpg?1631187425",
        "address": "пр. Востока, 101",
        "categories": ["Овощи", "Азиатская кухня"]
    },
    {
        "name": "Мексиканский Рай",
        "description": "Острые и сочные вкусы Мексики ждут вас в нашем ресторане.",
        "image": "https://e2.edimdoma.ru/data/fat_tags/0000/1463/1463-ed4_wide.jpg?1515755509",
        "address": "ул. Тако, 567",
        "categories": ["Мексиканская кухня"]
    },
    {
        "name": "Ризотто Мастер",
        "description": "Изысканные ризотто, приготовленные с использованием только лучших ингредиентов.",
        "image": "https://s.restorating.ru/w/1920x1080/articles/2920/None-111028.jpeg",
        "address": "пл. Ризотто, 234",
        "categories": ["Ризотто"]
    },
    {
        "name": "Морская Симфония",
        "description": "Погрузитесь в мир свежих морепродуктов и уютной скандинавской атмосферы.",
        "image": "https://s1.eda.ru/StaticContent/Photos/170304161224/210406204345/p_O.jpg",
        "address": "ул. Скандинавская, 876",
        "categories": ["Рыба", "Скандинавская кухня"]
    },
    {
        "name": "Панини Королевство",
        "description": "Бутерброды панини с различными начинками, созданные для настоящих гурманов.",
        "image": "https://e0.edimdoma.ru/data/posts/0002/1936/21936-ed4_wide.jpg?1679398231",
        "address": "пр. Панини, 345",
        "categories": ["Панини"]
    },
    {
        "name": "Карри Уголок",
        "description": "Ароматные блюда карри, приготовленные с использованием специй прямо из Индии.",
        "image": "https://cdn.lifehacker.ru/wp-content/uploads/2020/04/5e95669b997f5_j3hekga7e3r41__700_1587380182-e1587380213139.jpg",
        "address": "ул. Карри, 678",
        "categories": ["Карри"]
    },
    {
        "name": "Зеленый Дом",
        "description": "Здесь вы найдете богатый выбор блюд для здорового образа жизни и долголетия.",
        "image": "https://raw.githubusercontent.com/Wulfram8/storage/main/chech_rest_logo.png",
        "address": "пл. Здоровья, 987",
        "categories": ["Здоровое питание"]
    }
]


for i in restaurants:
    re = Restaurant.objects.create(
        name=i['name'], description=i['description'], address=i['address'], image=i['image'])
    for cat in i['categories']:
        category, _ = Category.objects.get_or_create(
            name=cat, defaults={'name': cat})
        re.categories.add(category)


[
    {
        "id": 11,
        "categories": [
            {
                "id": 13,
                "name": "Здоровое питание"
            }
        ],
        "meals": [
            {
                "id": 221,
                "ingredients": [
                    {
                        "id": 7,
                        "name": "Молотый говяжий фарш"
                    },
                    {
                        "id": 8,
                        "name": "Лук"
                    },
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 10,
                        "name": "Томатный соус"
                    },
                    {
                        "id": 11,
                        "name": "Томаты"
                    },
                    {
                        "id": 12,
                        "name": "Итальянские специи"
                    },
                    {
                        "id": 13,
                        "name": "Спагетти"
                    }
                ],
                "categories": [
                    {
                        "id": 1,
                        "name": "Паста"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Спагетти Болоньезе",
                "description": "Классическое итальянское блюдо с пастой и сытным мясным соусом.",
                "image": "https://kremlin-product.ru/upload/medialibrary/241/jfw6bequvf8s8mcum1npqc0jx1v1ngad/grilled_vegetables.jpg",
                "price": 350,
                "restaurant": 11
            },
            {
                "id": 231,
                "ingredients": [
                    {
                        "id": 14,
                        "name": "Жареная куринная грудка"
                    },
                    {
                        "id": 15,
                        "name": "Салат романо"
                    },
                    {
                        "id": 16,
                        "name": "Крутоны"
                    },
                    {
                        "id": 17,
                        "name": "Пармезан"
                    },
                    {
                        "id": 18,
                        "name": "Соус Цезарь"
                    },
                    {
                        "id": 19,
                        "name": "Лимонный сок"
                    },
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    }
                ],
                "categories": [
                    {
                        "id": 3,
                        "name": "Салаты"
                    },
                    {
                        "id": 4,
                        "name": "Американская кухня"
                    }
                ],
                "name": "Цезарь с курицей",
                "description": "Освежающий салат с жареной курицей, хрустящим салатом и соусом Цезарь.",
                "image": "https://s.restorating.ru/w/1920x1080/articles/2920/None-111028.jpeg",
                "price": 280,
                "restaurant": 11
            },
            {
                "id": 241,
                "ingredients": [
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 21,
                        "name": "Тофу"
                    },
                    {
                        "id": 22,
                        "name": "Брокколи"
                    },
                    {
                        "id": 23,
                        "name": "Болгарский перец"
                    },
                    {
                        "id": 24,
                        "name": "Морковь"
                    },
                    {
                        "id": 25,
                        "name": "Снеговые горошинки"
                    },
                    {
                        "id": 26,
                        "name": "Соевый соус"
                    },
                    {
                        "id": 27,
                        "name": "Имбирь"
                    },
                    {
                        "id": 28,
                        "name": "Соевое масло"
                    }
                ],
                "categories": [
                    {
                        "id": 5,
                        "name": "Овощи"
                    },
                    {
                        "id": 6,
                        "name": "Азиатская кухня"
                    }
                ],
                "name": "Овощной вок",
                "description": "Быстрый и красочный вок с овощами и тофу или выбранным вами видом белка.",
                "image": "https://gotovim-doma.ru/images/recipe/e/ce/eceb453fefbab09075a8c779712e52f8.jpg",
                "price": 300,
                "restaurant": 11
            },
            {
                "id": 251,
                "ingredients": [
                    {
                        "id": 29,
                        "name": "Молотая говядина"
                    },
                    {
                        "id": 30,
                        "name": "Приправа для тако"
                    },
                    {
                        "id": 31,
                        "name": "Тортильи"
                    },
                    {
                        "id": 32,
                        "name": "Салат"
                    },
                    {
                        "id": 33,
                        "name": "Помидоры"
                    },
                    {
                        "id": 34,
                        "name": "Сыр"
                    },
                    {
                        "id": 35,
                        "name": "Сальса"
                    },
                    {
                        "id": 36,
                        "name": "Сметана"
                    }
                ],
                "categories": [
                    {
                        "id": 7,
                        "name": "Мексиканская кухня"
                    }
                ],
                "name": "Такос с говядиной",
                "description": "Ароматная приправленная говядина в тортильях с начинкой.",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNVW3bTlMbUA_8-fbvHUgW1KaIEKaLANG0dg&usqp=CAU",
                "price": 320,
                "restaurant": 11
            },
            {
                "id": 261,
                "ingredients": [
                    {
                        "id": 8,
                        "name": "Лук"
                    },
                    {
                        "id": 17,
                        "name": "Пармезан"
                    },
                    {
                        "id": 37,
                        "name": "Рис арборио"
                    },
                    {
                        "id": 38,
                        "name": "Грибы"
                    },
                    {
                        "id": 39,
                        "name": "Белое вино"
                    },
                    {
                        "id": 40,
                        "name": "Куриный бульон"
                    },
                    {
                        "id": 41,
                        "name": "Масло"
                    }
                ],
                "categories": [
                    {
                        "id": 8,
                        "name": "Ризотто"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Грибной ризотто",
                "description": "Кремовое итальянское блюдо с жареными грибами и пармезаном.",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBsyitq8OdeFsdjKzPHO_ntFd0k9HnlM1NvA&usqp=CAU",
                "price": 380,
                "restaurant": 11
            },
            {
                "id": 271,
                "ingredients": [
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    },
                    {
                        "id": 42,
                        "name": "Филе лосося"
                    },
                    {
                        "id": 43,
                        "name": "Лимон"
                    },
                    {
                        "id": 44,
                        "name": "Свежий укроп"
                    },
                    {
                        "id": 45,
                        "name": "Соль и перец"
                    }
                ],
                "categories": [
                    {
                        "id": 9,
                        "name": "Рыба"
                    },
                    {
                        "id": 10,
                        "name": "Скандинавская кухня"
                    }
                ],
                "name": "Лосось с лимонно-укропным соусом",
                "description": "Жареный или запеченный лосось подается с ароматным соусом из лимона и укропа.",
                "image": "https://kandbi.com/image/catalog/blog/firmennoe-blyudo-v-restorane-chto-eto-i-kakim-ono-byvaet-2.jpg",
                "price": 420,
                "restaurant": 11
            },
            {
                "id": 281,
                "ingredients": [
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    },
                    {
                        "id": 33,
                        "name": "Помидоры"
                    },
                    {
                        "id": 46,
                        "name": "Хлеб чиабатта"
                    },
                    {
                        "id": 47,
                        "name": "Моцарелла"
                    },
                    {
                        "id": 48,
                        "name": "Свежие листья базилика"
                    },
                    {
                        "id": 49,
                        "name": "Бальзамический глазурь"
                    }
                ],
                "categories": [
                    {
                        "id": 11,
                        "name": "Панини"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Капрезе Панини",
                "description": "Жареный бутерброд с моцареллой, помидорами и базиликом.",
                "image": "https://cdn.lifehacker.ru/wp-content/uploads/2020/04/5e95669b997f5_j3hekga7e3r41__700_1587380182-e1587380213139.jpg",
                "price": 250,
                "restaurant": 11
            },
            {
                "id": 291,
                "ingredients": [
                    {
                        "id": 8,
                        "name": "Лук"
                    },
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 27,
                        "name": "Имбирь"
                    },
                    {
                        "id": 50,
                        "name": "Смешанные овощи"
                    },
                    {
                        "id": 51,
                        "name": "Карри-паста"
                    },
                    {
                        "id": 52,
                        "name": "Кокосовое молоко"
                    },
                    {
                        "id": 53,
                        "name": "Рис басмати"
                    }
                ],
                "categories": [
                    {
                        "id": 12,
                        "name": "Карри"
                    },
                    {
                        "id": 6,
                        "name": "Азиатская кухня"
                    }
                ],
                "name": "Овощное Карри",
                "description": "Острое и ароматное карри с разнообразными овощами.",
                "image": "https://e0.edimdoma.ru/data/posts/0002/1936/21936-ed4_wide.jpg?1679398231",
                "price": 290,
                "restaurant": 11
            },
            {
                "id": 301,
                "ingredients": [
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 17,
                        "name": "Пармезан"
                    },
                    {
                        "id": 41,
                        "name": "Масло"
                    },
                    {
                        "id": 45,
                        "name": "Соль и перец"
                    },
                    {
                        "id": 54,
                        "name": "Лапша феттучини"
                    },
                    {
                        "id": 55,
                        "name": "Куриная грудка"
                    },
                    {
                        "id": 56,
                        "name": "Тяжелая сливка"
                    }
                ],
                "categories": [
                    {
                        "id": 1,
                        "name": "Паста"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Куриное Альфредо Паста",
                "description": "Кремовый соус Альфредо с жареной куриной грудкой над лапшой феттучини.",
                "image": "https://hip2go.ru/api2/images/IikoProducts26/c1c668e7c6-1_500x353.jpg",
                "price": 360,
                "restaurant": 11
            },
            {
                "id": 311,
                "ingredients": [
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    },
                    {
                        "id": 45,
                        "name": "Соль и перец"
                    },
                    {
                        "id": 57,
                        "name": "Киноа"
                    },
                    {
                        "id": 58,
                        "name": "Чёрные бобы"
                    },
                    {
                        "id": 59,
                        "name": "Авокадо"
                    },
                    {
                        "id": 60,
                        "name": "Вишня томаты"
                    },
                    {
                        "id": 61,
                        "name": "Красный лук"
                    },
                    {
                        "id": 62,
                        "name": "Кинза"
                    },
                    {
                        "id": 63,
                        "name": "Сок лайма"
                    }
                ],
                "categories": [
                    {
                        "id": 3,
                        "name": "Салаты"
                    },
                    {
                        "id": 13,
                        "name": "Здоровое питание"
                    }
                ],
                "name": "Салат с киноа, авокадо и чёрными бобами",
                "description": "Питательный салат с киноа, авокадо, чёрными бобами и лаймовым винегретом.",
                "image": "https://takethemameal.com/files_images_v2/stam.jpg",
                "price": 310,
                "restaurant": 11
            }
        ],
        "name": "Зеленый Дом",
        "description": "Здесь вы найдете богатый выбор блюд для здорового образа жизни и долголетия.",
        "image": "https://raw.githubusercontent.com/Wulfram8/storage/main/chech_rest_logo.png",
        "address": "пл. Здоровья, 987",
        "created_at": "2023-12-29T02:10:39.206967Z",
        "updated_at": "2023-12-29T02:10:39.206967Z"
    },
    {
        "id": 10,
        "categories": [
            {
                "id": 12,
                "name": "Карри"
            }
        ],
        "meals": [
            {
                "id": 222,
                "ingredients": [
                    {
                        "id": 7,
                        "name": "Молотый говяжий фарш"
                    },
                    {
                        "id": 8,
                        "name": "Лук"
                    },
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 10,
                        "name": "Томатный соус"
                    },
                    {
                        "id": 11,
                        "name": "Томаты"
                    },
                    {
                        "id": 12,
                        "name": "Итальянские специи"
                    },
                    {
                        "id": 13,
                        "name": "Спагетти"
                    }
                ],
                "categories": [
                    {
                        "id": 1,
                        "name": "Паста"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Спагетти Болоньезе",
                "description": "Классическое итальянское блюдо с пастой и сытным мясным соусом.",
                "image": "https://kremlin-product.ru/upload/medialibrary/241/jfw6bequvf8s8mcum1npqc0jx1v1ngad/grilled_vegetables.jpg",
                "price": 350,
                "restaurant": 10
            },
            {
                "id": 232,
                "ingredients": [
                    {
                        "id": 14,
                        "name": "Жареная куринная грудка"
                    },
                    {
                        "id": 15,
                        "name": "Салат романо"
                    },
                    {
                        "id": 16,
                        "name": "Крутоны"
                    },
                    {
                        "id": 17,
                        "name": "Пармезан"
                    },
                    {
                        "id": 18,
                        "name": "Соус Цезарь"
                    },
                    {
                        "id": 19,
                        "name": "Лимонный сок"
                    },
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    }
                ],
                "categories": [
                    {
                        "id": 3,
                        "name": "Салаты"
                    },
                    {
                        "id": 4,
                        "name": "Американская кухня"
                    }
                ],
                "name": "Цезарь с курицей",
                "description": "Освежающий салат с жареной курицей, хрустящим салатом и соусом Цезарь.",
                "image": "https://s.restorating.ru/w/1920x1080/articles/2920/None-111028.jpeg",
                "price": 280,
                "restaurant": 10
            },
            {
                "id": 242,
                "ingredients": [
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 21,
                        "name": "Тофу"
                    },
                    {
                        "id": 22,
                        "name": "Брокколи"
                    },
                    {
                        "id": 23,
                        "name": "Болгарский перец"
                    },
                    {
                        "id": 24,
                        "name": "Морковь"
                    },
                    {
                        "id": 25,
                        "name": "Снеговые горошинки"
                    },
                    {
                        "id": 26,
                        "name": "Соевый соус"
                    },
                    {
                        "id": 27,
                        "name": "Имбирь"
                    },
                    {
                        "id": 28,
                        "name": "Соевое масло"
                    }
                ],
                "categories": [
                    {
                        "id": 5,
                        "name": "Овощи"
                    },
                    {
                        "id": 6,
                        "name": "Азиатская кухня"
                    }
                ],
                "name": "Овощной вок",
                "description": "Быстрый и красочный вок с овощами и тофу или выбранным вами видом белка.",
                "image": "https://gotovim-doma.ru/images/recipe/e/ce/eceb453fefbab09075a8c779712e52f8.jpg",
                "price": 300,
                "restaurant": 10
            },
            {
                "id": 252,
                "ingredients": [
                    {
                        "id": 29,
                        "name": "Молотая говядина"
                    },
                    {
                        "id": 30,
                        "name": "Приправа для тако"
                    },
                    {
                        "id": 31,
                        "name": "Тортильи"
                    },
                    {
                        "id": 32,
                        "name": "Салат"
                    },
                    {
                        "id": 33,
                        "name": "Помидоры"
                    },
                    {
                        "id": 34,
                        "name": "Сыр"
                    },
                    {
                        "id": 35,
                        "name": "Сальса"
                    },
                    {
                        "id": 36,
                        "name": "Сметана"
                    }
                ],
                "categories": [
                    {
                        "id": 7,
                        "name": "Мексиканская кухня"
                    }
                ],
                "name": "Такос с говядиной",
                "description": "Ароматная приправленная говядина в тортильях с начинкой.",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNVW3bTlMbUA_8-fbvHUgW1KaIEKaLANG0dg&usqp=CAU",
                "price": 320,
                "restaurant": 10
            },
            {
                "id": 262,
                "ingredients": [
                    {
                        "id": 8,
                        "name": "Лук"
                    },
                    {
                        "id": 17,
                        "name": "Пармезан"
                    },
                    {
                        "id": 37,
                        "name": "Рис арборио"
                    },
                    {
                        "id": 38,
                        "name": "Грибы"
                    },
                    {
                        "id": 39,
                        "name": "Белое вино"
                    },
                    {
                        "id": 40,
                        "name": "Куриный бульон"
                    },
                    {
                        "id": 41,
                        "name": "Масло"
                    }
                ],
                "categories": [
                    {
                        "id": 8,
                        "name": "Ризотто"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Грибной ризотто",
                "description": "Кремовое итальянское блюдо с жареными грибами и пармезаном.",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBsyitq8OdeFsdjKzPHO_ntFd0k9HnlM1NvA&usqp=CAU",
                "price": 380,
                "restaurant": 10
            },
            {
                "id": 272,
                "ingredients": [
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    },
                    {
                        "id": 42,
                        "name": "Филе лосося"
                    },
                    {
                        "id": 43,
                        "name": "Лимон"
                    },
                    {
                        "id": 44,
                        "name": "Свежий укроп"
                    },
                    {
                        "id": 45,
                        "name": "Соль и перец"
                    }
                ],
                "categories": [
                    {
                        "id": 9,
                        "name": "Рыба"
                    },
                    {
                        "id": 10,
                        "name": "Скандинавская кухня"
                    }
                ],
                "name": "Лосось с лимонно-укропным соусом",
                "description": "Жареный или запеченный лосось подается с ароматным соусом из лимона и укропа.",
                "image": "https://kandbi.com/image/catalog/blog/firmennoe-blyudo-v-restorane-chto-eto-i-kakim-ono-byvaet-2.jpg",
                "price": 420,
                "restaurant": 10
            },
            {
                "id": 282,
                "ingredients": [
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    },
                    {
                        "id": 33,
                        "name": "Помидоры"
                    },
                    {
                        "id": 46,
                        "name": "Хлеб чиабатта"
                    },
                    {
                        "id": 47,
                        "name": "Моцарелла"
                    },
                    {
                        "id": 48,
                        "name": "Свежие листья базилика"
                    },
                    {
                        "id": 49,
                        "name": "Бальзамический глазурь"
                    }
                ],
                "categories": [
                    {
                        "id": 11,
                        "name": "Панини"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Капрезе Панини",
                "description": "Жареный бутерброд с моцареллой, помидорами и базиликом.",
                "image": "https://cdn.lifehacker.ru/wp-content/uploads/2020/04/5e95669b997f5_j3hekga7e3r41__700_1587380182-e1587380213139.jpg",
                "price": 250,
                "restaurant": 10
            },
            {
                "id": 292,
                "ingredients": [
                    {
                        "id": 8,
                        "name": "Лук"
                    },
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 27,
                        "name": "Имбирь"
                    },
                    {
                        "id": 50,
                        "name": "Смешанные овощи"
                    },
                    {
                        "id": 51,
                        "name": "Карри-паста"
                    },
                    {
                        "id": 52,
                        "name": "Кокосовое молоко"
                    },
                    {
                        "id": 53,
                        "name": "Рис басмати"
                    }
                ],
                "categories": [
                    {
                        "id": 12,
                        "name": "Карри"
                    },
                    {
                        "id": 6,
                        "name": "Азиатская кухня"
                    }
                ],
                "name": "Овощное Карри",
                "description": "Острое и ароматное карри с разнообразными овощами.",
                "image": "https://e0.edimdoma.ru/data/posts/0002/1936/21936-ed4_wide.jpg?1679398231",
                "price": 290,
                "restaurant": 10
            },
            {
                "id": 302,
                "ingredients": [
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 17,
                        "name": "Пармезан"
                    },
                    {
                        "id": 41,
                        "name": "Масло"
                    },
                    {
                        "id": 45,
                        "name": "Соль и перец"
                    },
                    {
                        "id": 54,
                        "name": "Лапша феттучини"
                    },
                    {
                        "id": 55,
                        "name": "Куриная грудка"
                    },
                    {
                        "id": 56,
                        "name": "Тяжелая сливка"
                    }
                ],
                "categories": [
                    {
                        "id": 1,
                        "name": "Паста"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Куриное Альфредо Паста",
                "description": "Кремовый соус Альфредо с жареной куриной грудкой над лапшой феттучини.",
                "image": "https://hip2go.ru/api2/images/IikoProducts26/c1c668e7c6-1_500x353.jpg",
                "price": 360,
                "restaurant": 10
            },
            {
                "id": 312,
                "ingredients": [
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    },
                    {
                        "id": 45,
                        "name": "Соль и перец"
                    },
                    {
                        "id": 57,
                        "name": "Киноа"
                    },
                    {
                        "id": 58,
                        "name": "Чёрные бобы"
                    },
                    {
                        "id": 59,
                        "name": "Авокадо"
                    },
                    {
                        "id": 60,
                        "name": "Вишня томаты"
                    },
                    {
                        "id": 61,
                        "name": "Красный лук"
                    },
                    {
                        "id": 62,
                        "name": "Кинза"
                    },
                    {
                        "id": 63,
                        "name": "Сок лайма"
                    }
                ],
                "categories": [
                    {
                        "id": 3,
                        "name": "Салаты"
                    },
                    {
                        "id": 13,
                        "name": "Здоровое питание"
                    }
                ],
                "name": "Салат с киноа, авокадо и чёрными бобами",
                "description": "Питательный салат с киноа, авокадо, чёрными бобами и лаймовым винегретом.",
                "image": "https://takethemameal.com/files_images_v2/stam.jpg",
                "price": 310,
                "restaurant": 10
            }
        ],
        "name": "Карри Уголок",
        "description": "Ароматные блюда карри, приготовленные с использованием специй прямо из Индии.",
        "image": "https://zg-brand.ru/upload/images/5e71478a893aea91ff1be84f6e1042eb--restaurant-logos-tulip.jpg",
        "address": "ул. Карри, 678",
        "created_at": "2023-12-29T02:10:39.198623Z",
        "updated_at": "2023-12-29T05:20:08.748009Z"
    },
    {
        "id": 9,
        "categories": [
            {
                "id": 11,
                "name": "Панини"
            }
        ],
        "meals": [
            {
                "id": 223,
                "ingredients": [
                    {
                        "id": 7,
                        "name": "Молотый говяжий фарш"
                    },
                    {
                        "id": 8,
                        "name": "Лук"
                    },
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 10,
                        "name": "Томатный соус"
                    },
                    {
                        "id": 11,
                        "name": "Томаты"
                    },
                    {
                        "id": 12,
                        "name": "Итальянские специи"
                    },
                    {
                        "id": 13,
                        "name": "Спагетти"
                    }
                ],
                "categories": [
                    {
                        "id": 1,
                        "name": "Паста"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Спагетти Болоньезе",
                "description": "Классическое итальянское блюдо с пастой и сытным мясным соусом.",
                "image": "https://kremlin-product.ru/upload/medialibrary/241/jfw6bequvf8s8mcum1npqc0jx1v1ngad/grilled_vegetables.jpg",
                "price": 350,
                "restaurant": 9
            },
            {
                "id": 233,
                "ingredients": [
                    {
                        "id": 14,
                        "name": "Жареная куринная грудка"
                    },
                    {
                        "id": 15,
                        "name": "Салат романо"
                    },
                    {
                        "id": 16,
                        "name": "Крутоны"
                    },
                    {
                        "id": 17,
                        "name": "Пармезан"
                    },
                    {
                        "id": 18,
                        "name": "Соус Цезарь"
                    },
                    {
                        "id": 19,
                        "name": "Лимонный сок"
                    },
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    }
                ],
                "categories": [
                    {
                        "id": 3,
                        "name": "Салаты"
                    },
                    {
                        "id": 4,
                        "name": "Американская кухня"
                    }
                ],
                "name": "Цезарь с курицей",
                "description": "Освежающий салат с жареной курицей, хрустящим салатом и соусом Цезарь.",
                "image": "https://s.restorating.ru/w/1920x1080/articles/2920/None-111028.jpeg",
                "price": 280,
                "restaurant": 9
            },
            {
                "id": 243,
                "ingredients": [
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 21,
                        "name": "Тофу"
                    },
                    {
                        "id": 22,
                        "name": "Брокколи"
                    },
                    {
                        "id": 23,
                        "name": "Болгарский перец"
                    },
                    {
                        "id": 24,
                        "name": "Морковь"
                    },
                    {
                        "id": 25,
                        "name": "Снеговые горошинки"
                    },
                    {
                        "id": 26,
                        "name": "Соевый соус"
                    },
                    {
                        "id": 27,
                        "name": "Имбирь"
                    },
                    {
                        "id": 28,
                        "name": "Соевое масло"
                    }
                ],
                "categories": [
                    {
                        "id": 5,
                        "name": "Овощи"
                    },
                    {
                        "id": 6,
                        "name": "Азиатская кухня"
                    }
                ],
                "name": "Овощной вок",
                "description": "Быстрый и красочный вок с овощами и тофу или выбранным вами видом белка.",
                "image": "https://gotovim-doma.ru/images/recipe/e/ce/eceb453fefbab09075a8c779712e52f8.jpg",
                "price": 300,
                "restaurant": 9
            },
            {
                "id": 253,
                "ingredients": [
                    {
                        "id": 29,
                        "name": "Молотая говядина"
                    },
                    {
                        "id": 30,
                        "name": "Приправа для тако"
                    },
                    {
                        "id": 31,
                        "name": "Тортильи"
                    },
                    {
                        "id": 32,
                        "name": "Салат"
                    },
                    {
                        "id": 33,
                        "name": "Помидоры"
                    },
                    {
                        "id": 34,
                        "name": "Сыр"
                    },
                    {
                        "id": 35,
                        "name": "Сальса"
                    },
                    {
                        "id": 36,
                        "name": "Сметана"
                    }
                ],
                "categories": [
                    {
                        "id": 7,
                        "name": "Мексиканская кухня"
                    }
                ],
                "name": "Такос с говядиной",
                "description": "Ароматная приправленная говядина в тортильях с начинкой.",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNVW3bTlMbUA_8-fbvHUgW1KaIEKaLANG0dg&usqp=CAU",
                "price": 320,
                "restaurant": 9
            },
            {
                "id": 263,
                "ingredients": [
                    {
                        "id": 8,
                        "name": "Лук"
                    },
                    {
                        "id": 17,
                        "name": "Пармезан"
                    },
                    {
                        "id": 37,
                        "name": "Рис арборио"
                    },
                    {
                        "id": 38,
                        "name": "Грибы"
                    },
                    {
                        "id": 39,
                        "name": "Белое вино"
                    },
                    {
                        "id": 40,
                        "name": "Куриный бульон"
                    },
                    {
                        "id": 41,
                        "name": "Масло"
                    }
                ],
                "categories": [
                    {
                        "id": 8,
                        "name": "Ризотто"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Грибной ризотто",
                "description": "Кремовое итальянское блюдо с жареными грибами и пармезаном.",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBsyitq8OdeFsdjKzPHO_ntFd0k9HnlM1NvA&usqp=CAU",
                "price": 380,
                "restaurant": 9
            },
            {
                "id": 273,
                "ingredients": [
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    },
                    {
                        "id": 42,
                        "name": "Филе лосося"
                    },
                    {
                        "id": 43,
                        "name": "Лимон"
                    },
                    {
                        "id": 44,
                        "name": "Свежий укроп"
                    },
                    {
                        "id": 45,
                        "name": "Соль и перец"
                    }
                ],
                "categories": [
                    {
                        "id": 9,
                        "name": "Рыба"
                    },
                    {
                        "id": 10,
                        "name": "Скандинавская кухня"
                    }
                ],
                "name": "Лосось с лимонно-укропным соусом",
                "description": "Жареный или запеченный лосось подается с ароматным соусом из лимона и укропа.",
                "image": "https://kandbi.com/image/catalog/blog/firmennoe-blyudo-v-restorane-chto-eto-i-kakim-ono-byvaet-2.jpg",
                "price": 420,
                "restaurant": 9
            },
            {
                "id": 283,
                "ingredients": [
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    },
                    {
                        "id": 33,
                        "name": "Помидоры"
                    },
                    {
                        "id": 46,
                        "name": "Хлеб чиабатта"
                    },
                    {
                        "id": 47,
                        "name": "Моцарелла"
                    },
                    {
                        "id": 48,
                        "name": "Свежие листья базилика"
                    },
                    {
                        "id": 49,
                        "name": "Бальзамический глазурь"
                    }
                ],
                "categories": [
                    {
                        "id": 11,
                        "name": "Панини"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Капрезе Панини",
                "description": "Жареный бутерброд с моцареллой, помидорами и базиликом.",
                "image": "https://cdn.lifehacker.ru/wp-content/uploads/2020/04/5e95669b997f5_j3hekga7e3r41__700_1587380182-e1587380213139.jpg",
                "price": 250,
                "restaurant": 9
            },
            {
                "id": 293,
                "ingredients": [
                    {
                        "id": 8,
                        "name": "Лук"
                    },
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 27,
                        "name": "Имбирь"
                    },
                    {
                        "id": 50,
                        "name": "Смешанные овощи"
                    },
                    {
                        "id": 51,
                        "name": "Карри-паста"
                    },
                    {
                        "id": 52,
                        "name": "Кокосовое молоко"
                    },
                    {
                        "id": 53,
                        "name": "Рис басмати"
                    }
                ],
                "categories": [
                    {
                        "id": 12,
                        "name": "Карри"
                    },
                    {
                        "id": 6,
                        "name": "Азиатская кухня"
                    }
                ],
                "name": "Овощное Карри",
                "description": "Острое и ароматное карри с разнообразными овощами.",
                "image": "https://e0.edimdoma.ru/data/posts/0002/1936/21936-ed4_wide.jpg?1679398231",
                "price": 290,
                "restaurant": 9
            },
            {
                "id": 303,
                "ingredients": [
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 17,
                        "name": "Пармезан"
                    },
                    {
                        "id": 41,
                        "name": "Масло"
                    },
                    {
                        "id": 45,
                        "name": "Соль и перец"
                    },
                    {
                        "id": 54,
                        "name": "Лапша феттучини"
                    },
                    {
                        "id": 55,
                        "name": "Куриная грудка"
                    },
                    {
                        "id": 56,
                        "name": "Тяжелая сливка"
                    }
                ],
                "categories": [
                    {
                        "id": 1,
                        "name": "Паста"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Куриное Альфредо Паста",
                "description": "Кремовый соус Альфредо с жареной куриной грудкой над лапшой феттучини.",
                "image": "https://hip2go.ru/api2/images/IikoProducts26/c1c668e7c6-1_500x353.jpg",
                "price": 360,
                "restaurant": 9
            },
            {
                "id": 313,
                "ingredients": [
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    },
                    {
                        "id": 45,
                        "name": "Соль и перец"
                    },
                    {
                        "id": 57,
                        "name": "Киноа"
                    },
                    {
                        "id": 58,
                        "name": "Чёрные бобы"
                    },
                    {
                        "id": 59,
                        "name": "Авокадо"
                    },
                    {
                        "id": 60,
                        "name": "Вишня томаты"
                    },
                    {
                        "id": 61,
                        "name": "Красный лук"
                    },
                    {
                        "id": 62,
                        "name": "Кинза"
                    },
                    {
                        "id": 63,
                        "name": "Сок лайма"
                    }
                ],
                "categories": [
                    {
                        "id": 3,
                        "name": "Салаты"
                    },
                    {
                        "id": 13,
                        "name": "Здоровое питание"
                    }
                ],
                "name": "Салат с киноа, авокадо и чёрными бобами",
                "description": "Питательный салат с киноа, авокадо, чёрными бобами и лаймовым винегретом.",
                "image": "https://takethemameal.com/files_images_v2/stam.jpg",
                "price": 310,
                "restaurant": 9
            }
        ],
        "name": "Панини Королевство",
        "description": "Бутерброды панини с различными начинками, созданные для настоящих гурманов.",
        "image": "https://zg-brand.ru/upload/images/5e71478a893aea91ff1be84f6e1042eb--restaurant-logos-tulip.jpg",
        "address": "пр. Панини, 345",
        "created_at": "2023-12-29T02:10:39.189539Z",
        "updated_at": "2023-12-29T05:17:19.948206Z"
    },
    {
        "id": 8,
        "categories": [
            {
                "id": 9,
                "name": "Рыба"
            },
            {
                "id": 10,
                "name": "Скандинавская кухня"
            }
        ],
        "meals": [
            {
                "id": 224,
                "ingredients": [
                    {
                        "id": 7,
                        "name": "Молотый говяжий фарш"
                    },
                    {
                        "id": 8,
                        "name": "Лук"
                    },
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 10,
                        "name": "Томатный соус"
                    },
                    {
                        "id": 11,
                        "name": "Томаты"
                    },
                    {
                        "id": 12,
                        "name": "Итальянские специи"
                    },
                    {
                        "id": 13,
                        "name": "Спагетти"
                    }
                ],
                "categories": [
                    {
                        "id": 1,
                        "name": "Паста"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Спагетти Болоньезе",
                "description": "Классическое итальянское блюдо с пастой и сытным мясным соусом.",
                "image": "https://kremlin-product.ru/upload/medialibrary/241/jfw6bequvf8s8mcum1npqc0jx1v1ngad/grilled_vegetables.jpg",
                "price": 350,
                "restaurant": 8
            },
            {
                "id": 234,
                "ingredients": [
                    {
                        "id": 14,
                        "name": "Жареная куринная грудка"
                    },
                    {
                        "id": 15,
                        "name": "Салат романо"
                    },
                    {
                        "id": 16,
                        "name": "Крутоны"
                    },
                    {
                        "id": 17,
                        "name": "Пармезан"
                    },
                    {
                        "id": 18,
                        "name": "Соус Цезарь"
                    },
                    {
                        "id": 19,
                        "name": "Лимонный сок"
                    },
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    }
                ],
                "categories": [
                    {
                        "id": 3,
                        "name": "Салаты"
                    },
                    {
                        "id": 4,
                        "name": "Американская кухня"
                    }
                ],
                "name": "Цезарь с курицей",
                "description": "Освежающий салат с жареной курицей, хрустящим салатом и соусом Цезарь.",
                "image": "https://s.restorating.ru/w/1920x1080/articles/2920/None-111028.jpeg",
                "price": 280,
                "restaurant": 8
            },
            {
                "id": 244,
                "ingredients": [
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 21,
                        "name": "Тофу"
                    },
                    {
                        "id": 22,
                        "name": "Брокколи"
                    },
                    {
                        "id": 23,
                        "name": "Болгарский перец"
                    },
                    {
                        "id": 24,
                        "name": "Морковь"
                    },
                    {
                        "id": 25,
                        "name": "Снеговые горошинки"
                    },
                    {
                        "id": 26,
                        "name": "Соевый соус"
                    },
                    {
                        "id": 27,
                        "name": "Имбирь"
                    },
                    {
                        "id": 28,
                        "name": "Соевое масло"
                    }
                ],
                "categories": [
                    {
                        "id": 5,
                        "name": "Овощи"
                    },
                    {
                        "id": 6,
                        "name": "Азиатская кухня"
                    }
                ],
                "name": "Овощной вок",
                "description": "Быстрый и красочный вок с овощами и тофу или выбранным вами видом белка.",
                "image": "https://gotovim-doma.ru/images/recipe/e/ce/eceb453fefbab09075a8c779712e52f8.jpg",
                "price": 300,
                "restaurant": 8
            },
            {
                "id": 254,
                "ingredients": [
                    {
                        "id": 29,
                        "name": "Молотая говядина"
                    },
                    {
                        "id": 30,
                        "name": "Приправа для тако"
                    },
                    {
                        "id": 31,
                        "name": "Тортильи"
                    },
                    {
                        "id": 32,
                        "name": "Салат"
                    },
                    {
                        "id": 33,
                        "name": "Помидоры"
                    },
                    {
                        "id": 34,
                        "name": "Сыр"
                    },
                    {
                        "id": 35,
                        "name": "Сальса"
                    },
                    {
                        "id": 36,
                        "name": "Сметана"
                    }
                ],
                "categories": [
                    {
                        "id": 7,
                        "name": "Мексиканская кухня"
                    }
                ],
                "name": "Такос с говядиной",
                "description": "Ароматная приправленная говядина в тортильях с начинкой.",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNVW3bTlMbUA_8-fbvHUgW1KaIEKaLANG0dg&usqp=CAU",
                "price": 320,
                "restaurant": 8
            },
            {
                "id": 264,
                "ingredients": [
                    {
                        "id": 8,
                        "name": "Лук"
                    },
                    {
                        "id": 17,
                        "name": "Пармезан"
                    },
                    {
                        "id": 37,
                        "name": "Рис арборио"
                    },
                    {
                        "id": 38,
                        "name": "Грибы"
                    },
                    {
                        "id": 39,
                        "name": "Белое вино"
                    },
                    {
                        "id": 40,
                        "name": "Куриный бульон"
                    },
                    {
                        "id": 41,
                        "name": "Масло"
                    }
                ],
                "categories": [
                    {
                        "id": 8,
                        "name": "Ризотто"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Грибной ризотто",
                "description": "Кремовое итальянское блюдо с жареными грибами и пармезаном.",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBsyitq8OdeFsdjKzPHO_ntFd0k9HnlM1NvA&usqp=CAU",
                "price": 380,
                "restaurant": 8
            },
            {
                "id": 274,
                "ingredients": [
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    },
                    {
                        "id": 42,
                        "name": "Филе лосося"
                    },
                    {
                        "id": 43,
                        "name": "Лимон"
                    },
                    {
                        "id": 44,
                        "name": "Свежий укроп"
                    },
                    {
                        "id": 45,
                        "name": "Соль и перец"
                    }
                ],
                "categories": [
                    {
                        "id": 9,
                        "name": "Рыба"
                    },
                    {
                        "id": 10,
                        "name": "Скандинавская кухня"
                    }
                ],
                "name": "Лосось с лимонно-укропным соусом",
                "description": "Жареный или запеченный лосось подается с ароматным соусом из лимона и укропа.",
                "image": "https://kandbi.com/image/catalog/blog/firmennoe-blyudo-v-restorane-chto-eto-i-kakim-ono-byvaet-2.jpg",
                "price": 420,
                "restaurant": 8
            },
            {
                "id": 284,
                "ingredients": [
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    },
                    {
                        "id": 33,
                        "name": "Помидоры"
                    },
                    {
                        "id": 46,
                        "name": "Хлеб чиабатта"
                    },
                    {
                        "id": 47,
                        "name": "Моцарелла"
                    },
                    {
                        "id": 48,
                        "name": "Свежие листья базилика"
                    },
                    {
                        "id": 49,
                        "name": "Бальзамический глазурь"
                    }
                ],
                "categories": [
                    {
                        "id": 11,
                        "name": "Панини"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Капрезе Панини",
                "description": "Жареный бутерброд с моцареллой, помидорами и базиликом.",
                "image": "https://cdn.lifehacker.ru/wp-content/uploads/2020/04/5e95669b997f5_j3hekga7e3r41__700_1587380182-e1587380213139.jpg",
                "price": 250,
                "restaurant": 8
            },
            {
                "id": 294,
                "ingredients": [
                    {
                        "id": 8,
                        "name": "Лук"
                    },
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 27,
                        "name": "Имбирь"
                    },
                    {
                        "id": 50,
                        "name": "Смешанные овощи"
                    },
                    {
                        "id": 51,
                        "name": "Карри-паста"
                    },
                    {
                        "id": 52,
                        "name": "Кокосовое молоко"
                    },
                    {
                        "id": 53,
                        "name": "Рис басмати"
                    }
                ],
                "categories": [
                    {
                        "id": 12,
                        "name": "Карри"
                    },
                    {
                        "id": 6,
                        "name": "Азиатская кухня"
                    }
                ],
                "name": "Овощное Карри",
                "description": "Острое и ароматное карри с разнообразными овощами.",
                "image": "https://e0.edimdoma.ru/data/posts/0002/1936/21936-ed4_wide.jpg?1679398231",
                "price": 290,
                "restaurant": 8
            },
            {
                "id": 304,
                "ingredients": [
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 17,
                        "name": "Пармезан"
                    },
                    {
                        "id": 41,
                        "name": "Масло"
                    },
                    {
                        "id": 45,
                        "name": "Соль и перец"
                    },
                    {
                        "id": 54,
                        "name": "Лапша феттучини"
                    },
                    {
                        "id": 55,
                        "name": "Куриная грудка"
                    },
                    {
                        "id": 56,
                        "name": "Тяжелая сливка"
                    }
                ],
                "categories": [
                    {
                        "id": 1,
                        "name": "Паста"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Куриное Альфредо Паста",
                "description": "Кремовый соус Альфредо с жареной куриной грудкой над лапшой феттучини.",
                "image": "https://hip2go.ru/api2/images/IikoProducts26/c1c668e7c6-1_500x353.jpg",
                "price": 360,
                "restaurant": 8
            },
            {
                "id": 314,
                "ingredients": [
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    },
                    {
                        "id": 45,
                        "name": "Соль и перец"
                    },
                    {
                        "id": 57,
                        "name": "Киноа"
                    },
                    {
                        "id": 58,
                        "name": "Чёрные бобы"
                    },
                    {
                        "id": 59,
                        "name": "Авокадо"
                    },
                    {
                        "id": 60,
                        "name": "Вишня томаты"
                    },
                    {
                        "id": 61,
                        "name": "Красный лук"
                    },
                    {
                        "id": 62,
                        "name": "Кинза"
                    },
                    {
                        "id": 63,
                        "name": "Сок лайма"
                    }
                ],
                "categories": [
                    {
                        "id": 3,
                        "name": "Салаты"
                    },
                    {
                        "id": 13,
                        "name": "Здоровое питание"
                    }
                ],
                "name": "Салат с киноа, авокадо и чёрными бобами",
                "description": "Питательный салат с киноа, авокадо, чёрными бобами и лаймовым винегретом.",
                "image": "https://takethemameal.com/files_images_v2/stam.jpg",
                "price": 310,
                "restaurant": 8
            }
        ],
        "name": "Морская Симфония",
        "description": "Погрузитесь в мир свежих морепродуктов и уютной скандинавской атмосферы.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJA7cpTj-UUuCjH2U6fHp6DBYNjs2R-IAJTQ&usqp=CAU",
        "address": "ул. Скандинавская, 876",
        "created_at": "2023-12-29T02:10:39.174486Z",
        "updated_at": "2023-12-29T05:14:20.598851Z"
    },
    {
        "id": 7,
        "categories": [
            {
                "id": 8,
                "name": "Ризотто"
            }
        ],
        "meals": [
            {
                "id": 225,
                "ingredients": [
                    {
                        "id": 7,
                        "name": "Молотый говяжий фарш"
                    },
                    {
                        "id": 8,
                        "name": "Лук"
                    },
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 10,
                        "name": "Томатный соус"
                    },
                    {
                        "id": 11,
                        "name": "Томаты"
                    },
                    {
                        "id": 12,
                        "name": "Итальянские специи"
                    },
                    {
                        "id": 13,
                        "name": "Спагетти"
                    }
                ],
                "categories": [
                    {
                        "id": 1,
                        "name": "Паста"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Спагетти Болоньезе",
                "description": "Классическое итальянское блюдо с пастой и сытным мясным соусом.",
                "image": "https://kremlin-product.ru/upload/medialibrary/241/jfw6bequvf8s8mcum1npqc0jx1v1ngad/grilled_vegetables.jpg",
                "price": 350,
                "restaurant": 7
            },
            {
                "id": 235,
                "ingredients": [
                    {
                        "id": 14,
                        "name": "Жареная куринная грудка"
                    },
                    {
                        "id": 15,
                        "name": "Салат романо"
                    },
                    {
                        "id": 16,
                        "name": "Крутоны"
                    },
                    {
                        "id": 17,
                        "name": "Пармезан"
                    },
                    {
                        "id": 18,
                        "name": "Соус Цезарь"
                    },
                    {
                        "id": 19,
                        "name": "Лимонный сок"
                    },
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    }
                ],
                "categories": [
                    {
                        "id": 3,
                        "name": "Салаты"
                    },
                    {
                        "id": 4,
                        "name": "Американская кухня"
                    }
                ],
                "name": "Цезарь с курицей",
                "description": "Освежающий салат с жареной курицей, хрустящим салатом и соусом Цезарь.",
                "image": "https://s.restorating.ru/w/1920x1080/articles/2920/None-111028.jpeg",
                "price": 280,
                "restaurant": 7
            },
            {
                "id": 245,
                "ingredients": [
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 21,
                        "name": "Тофу"
                    },
                    {
                        "id": 22,
                        "name": "Брокколи"
                    },
                    {
                        "id": 23,
                        "name": "Болгарский перец"
                    },
                    {
                        "id": 24,
                        "name": "Морковь"
                    },
                    {
                        "id": 25,
                        "name": "Снеговые горошинки"
                    },
                    {
                        "id": 26,
                        "name": "Соевый соус"
                    },
                    {
                        "id": 27,
                        "name": "Имбирь"
                    },
                    {
                        "id": 28,
                        "name": "Соевое масло"
                    }
                ],
                "categories": [
                    {
                        "id": 5,
                        "name": "Овощи"
                    },
                    {
                        "id": 6,
                        "name": "Азиатская кухня"
                    }
                ],
                "name": "Овощной вок",
                "description": "Быстрый и красочный вок с овощами и тофу или выбранным вами видом белка.",
                "image": "https://gotovim-doma.ru/images/recipe/e/ce/eceb453fefbab09075a8c779712e52f8.jpg",
                "price": 300,
                "restaurant": 7
            },
            {
                "id": 255,
                "ingredients": [
                    {
                        "id": 29,
                        "name": "Молотая говядина"
                    },
                    {
                        "id": 30,
                        "name": "Приправа для тако"
                    },
                    {
                        "id": 31,
                        "name": "Тортильи"
                    },
                    {
                        "id": 32,
                        "name": "Салат"
                    },
                    {
                        "id": 33,
                        "name": "Помидоры"
                    },
                    {
                        "id": 34,
                        "name": "Сыр"
                    },
                    {
                        "id": 35,
                        "name": "Сальса"
                    },
                    {
                        "id": 36,
                        "name": "Сметана"
                    }
                ],
                "categories": [
                    {
                        "id": 7,
                        "name": "Мексиканская кухня"
                    }
                ],
                "name": "Такос с говядиной",
                "description": "Ароматная приправленная говядина в тортильях с начинкой.",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNVW3bTlMbUA_8-fbvHUgW1KaIEKaLANG0dg&usqp=CAU",
                "price": 320,
                "restaurant": 7
            },
            {
                "id": 265,
                "ingredients": [
                    {
                        "id": 8,
                        "name": "Лук"
                    },
                    {
                        "id": 17,
                        "name": "Пармезан"
                    },
                    {
                        "id": 37,
                        "name": "Рис арборио"
                    },
                    {
                        "id": 38,
                        "name": "Грибы"
                    },
                    {
                        "id": 39,
                        "name": "Белое вино"
                    },
                    {
                        "id": 40,
                        "name": "Куриный бульон"
                    },
                    {
                        "id": 41,
                        "name": "Масло"
                    }
                ],
                "categories": [
                    {
                        "id": 8,
                        "name": "Ризотто"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Грибной ризотто",
                "description": "Кремовое итальянское блюдо с жареными грибами и пармезаном.",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBsyitq8OdeFsdjKzPHO_ntFd0k9HnlM1NvA&usqp=CAU",
                "price": 380,
                "restaurant": 7
            },
            {
                "id": 275,
                "ingredients": [
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    },
                    {
                        "id": 42,
                        "name": "Филе лосося"
                    },
                    {
                        "id": 43,
                        "name": "Лимон"
                    },
                    {
                        "id": 44,
                        "name": "Свежий укроп"
                    },
                    {
                        "id": 45,
                        "name": "Соль и перец"
                    }
                ],
                "categories": [
                    {
                        "id": 9,
                        "name": "Рыба"
                    },
                    {
                        "id": 10,
                        "name": "Скандинавская кухня"
                    }
                ],
                "name": "Лосось с лимонно-укропным соусом",
                "description": "Жареный или запеченный лосось подается с ароматным соусом из лимона и укропа.",
                "image": "https://kandbi.com/image/catalog/blog/firmennoe-blyudo-v-restorane-chto-eto-i-kakim-ono-byvaet-2.jpg",
                "price": 420,
                "restaurant": 7
            },
            {
                "id": 285,
                "ingredients": [
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    },
                    {
                        "id": 33,
                        "name": "Помидоры"
                    },
                    {
                        "id": 46,
                        "name": "Хлеб чиабатта"
                    },
                    {
                        "id": 47,
                        "name": "Моцарелла"
                    },
                    {
                        "id": 48,
                        "name": "Свежие листья базилика"
                    },
                    {
                        "id": 49,
                        "name": "Бальзамический глазурь"
                    }
                ],
                "categories": [
                    {
                        "id": 11,
                        "name": "Панини"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Капрезе Панини",
                "description": "Жареный бутерброд с моцареллой, помидорами и базиликом.",
                "image": "https://cdn.lifehacker.ru/wp-content/uploads/2020/04/5e95669b997f5_j3hekga7e3r41__700_1587380182-e1587380213139.jpg",
                "price": 250,
                "restaurant": 7
            },
            {
                "id": 295,
                "ingredients": [
                    {
                        "id": 8,
                        "name": "Лук"
                    },
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 27,
                        "name": "Имбирь"
                    },
                    {
                        "id": 50,
                        "name": "Смешанные овощи"
                    },
                    {
                        "id": 51,
                        "name": "Карри-паста"
                    },
                    {
                        "id": 52,
                        "name": "Кокосовое молоко"
                    },
                    {
                        "id": 53,
                        "name": "Рис басмати"
                    }
                ],
                "categories": [
                    {
                        "id": 12,
                        "name": "Карри"
                    },
                    {
                        "id": 6,
                        "name": "Азиатская кухня"
                    }
                ],
                "name": "Овощное Карри",
                "description": "Острое и ароматное карри с разнообразными овощами.",
                "image": "https://e0.edimdoma.ru/data/posts/0002/1936/21936-ed4_wide.jpg?1679398231",
                "price": 290,
                "restaurant": 7
            },
            {
                "id": 305,
                "ingredients": [
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 17,
                        "name": "Пармезан"
                    },
                    {
                        "id": 41,
                        "name": "Масло"
                    },
                    {
                        "id": 45,
                        "name": "Соль и перец"
                    },
                    {
                        "id": 54,
                        "name": "Лапша феттучини"
                    },
                    {
                        "id": 55,
                        "name": "Куриная грудка"
                    },
                    {
                        "id": 56,
                        "name": "Тяжелая сливка"
                    }
                ],
                "categories": [
                    {
                        "id": 1,
                        "name": "Паста"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Куриное Альфредо Паста",
                "description": "Кремовый соус Альфредо с жареной куриной грудкой над лапшой феттучини.",
                "image": "https://hip2go.ru/api2/images/IikoProducts26/c1c668e7c6-1_500x353.jpg",
                "price": 360,
                "restaurant": 7
            },
            {
                "id": 315,
                "ingredients": [
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    },
                    {
                        "id": 45,
                        "name": "Соль и перец"
                    },
                    {
                        "id": 57,
                        "name": "Киноа"
                    },
                    {
                        "id": 58,
                        "name": "Чёрные бобы"
                    },
                    {
                        "id": 59,
                        "name": "Авокадо"
                    },
                    {
                        "id": 60,
                        "name": "Вишня томаты"
                    },
                    {
                        "id": 61,
                        "name": "Красный лук"
                    },
                    {
                        "id": 62,
                        "name": "Кинза"
                    },
                    {
                        "id": 63,
                        "name": "Сок лайма"
                    }
                ],
                "categories": [
                    {
                        "id": 3,
                        "name": "Салаты"
                    },
                    {
                        "id": 13,
                        "name": "Здоровое питание"
                    }
                ],
                "name": "Салат с киноа, авокадо и чёрными бобами",
                "description": "Питательный салат с киноа, авокадо, чёрными бобами и лаймовым винегретом.",
                "image": "https://takethemameal.com/files_images_v2/stam.jpg",
                "price": 310,
                "restaurant": 7
            }
        ],
        "name": "Ризотто Мастер",
        "description": "Изысканные ризотто, приготовленные с использованием только лучших ингредиентов.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSpXxAHGJ3jCBSSJrTI_7kqwAw0BayBNvk6eA&usqp=CAU",
        "address": "пл. Ризотто, 234",
        "created_at": "2023-12-29T02:10:39.164768Z",
        "updated_at": "2023-12-29T05:14:11.748054Z"
    },
    {
        "id": 6,
        "categories": [
            {
                "id": 7,
                "name": "Мексиканская кухня"
            }
        ],
        "meals": [
            {
                "id": 226,
                "ingredients": [
                    {
                        "id": 7,
                        "name": "Молотый говяжий фарш"
                    },
                    {
                        "id": 8,
                        "name": "Лук"
                    },
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 10,
                        "name": "Томатный соус"
                    },
                    {
                        "id": 11,
                        "name": "Томаты"
                    },
                    {
                        "id": 12,
                        "name": "Итальянские специи"
                    },
                    {
                        "id": 13,
                        "name": "Спагетти"
                    }
                ],
                "categories": [
                    {
                        "id": 1,
                        "name": "Паста"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Спагетти Болоньезе",
                "description": "Классическое итальянское блюдо с пастой и сытным мясным соусом.",
                "image": "https://kremlin-product.ru/upload/medialibrary/241/jfw6bequvf8s8mcum1npqc0jx1v1ngad/grilled_vegetables.jpg",
                "price": 350,
                "restaurant": 6
            },
            {
                "id": 236,
                "ingredients": [
                    {
                        "id": 14,
                        "name": "Жареная куринная грудка"
                    },
                    {
                        "id": 15,
                        "name": "Салат романо"
                    },
                    {
                        "id": 16,
                        "name": "Крутоны"
                    },
                    {
                        "id": 17,
                        "name": "Пармезан"
                    },
                    {
                        "id": 18,
                        "name": "Соус Цезарь"
                    },
                    {
                        "id": 19,
                        "name": "Лимонный сок"
                    },
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    }
                ],
                "categories": [
                    {
                        "id": 3,
                        "name": "Салаты"
                    },
                    {
                        "id": 4,
                        "name": "Американская кухня"
                    }
                ],
                "name": "Цезарь с курицей",
                "description": "Освежающий салат с жареной курицей, хрустящим салатом и соусом Цезарь.",
                "image": "https://s.restorating.ru/w/1920x1080/articles/2920/None-111028.jpeg",
                "price": 280,
                "restaurant": 6
            },
            {
                "id": 246,
                "ingredients": [
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 21,
                        "name": "Тофу"
                    },
                    {
                        "id": 22,
                        "name": "Брокколи"
                    },
                    {
                        "id": 23,
                        "name": "Болгарский перец"
                    },
                    {
                        "id": 24,
                        "name": "Морковь"
                    },
                    {
                        "id": 25,
                        "name": "Снеговые горошинки"
                    },
                    {
                        "id": 26,
                        "name": "Соевый соус"
                    },
                    {
                        "id": 27,
                        "name": "Имбирь"
                    },
                    {
                        "id": 28,
                        "name": "Соевое масло"
                    }
                ],
                "categories": [
                    {
                        "id": 5,
                        "name": "Овощи"
                    },
                    {
                        "id": 6,
                        "name": "Азиатская кухня"
                    }
                ],
                "name": "Овощной вок",
                "description": "Быстрый и красочный вок с овощами и тофу или выбранным вами видом белка.",
                "image": "https://gotovim-doma.ru/images/recipe/e/ce/eceb453fefbab09075a8c779712e52f8.jpg",
                "price": 300,
                "restaurant": 6
            },
            {
                "id": 256,
                "ingredients": [
                    {
                        "id": 29,
                        "name": "Молотая говядина"
                    },
                    {
                        "id": 30,
                        "name": "Приправа для тако"
                    },
                    {
                        "id": 31,
                        "name": "Тортильи"
                    },
                    {
                        "id": 32,
                        "name": "Салат"
                    },
                    {
                        "id": 33,
                        "name": "Помидоры"
                    },
                    {
                        "id": 34,
                        "name": "Сыр"
                    },
                    {
                        "id": 35,
                        "name": "Сальса"
                    },
                    {
                        "id": 36,
                        "name": "Сметана"
                    }
                ],
                "categories": [
                    {
                        "id": 7,
                        "name": "Мексиканская кухня"
                    }
                ],
                "name": "Такос с говядиной",
                "description": "Ароматная приправленная говядина в тортильях с начинкой.",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNVW3bTlMbUA_8-fbvHUgW1KaIEKaLANG0dg&usqp=CAU",
                "price": 320,
                "restaurant": 6
            },
            {
                "id": 266,
                "ingredients": [
                    {
                        "id": 8,
                        "name": "Лук"
                    },
                    {
                        "id": 17,
                        "name": "Пармезан"
                    },
                    {
                        "id": 37,
                        "name": "Рис арборио"
                    },
                    {
                        "id": 38,
                        "name": "Грибы"
                    },
                    {
                        "id": 39,
                        "name": "Белое вино"
                    },
                    {
                        "id": 40,
                        "name": "Куриный бульон"
                    },
                    {
                        "id": 41,
                        "name": "Масло"
                    }
                ],
                "categories": [
                    {
                        "id": 8,
                        "name": "Ризотто"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Грибной ризотто",
                "description": "Кремовое итальянское блюдо с жареными грибами и пармезаном.",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBsyitq8OdeFsdjKzPHO_ntFd0k9HnlM1NvA&usqp=CAU",
                "price": 380,
                "restaurant": 6
            },
            {
                "id": 276,
                "ingredients": [
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    },
                    {
                        "id": 42,
                        "name": "Филе лосося"
                    },
                    {
                        "id": 43,
                        "name": "Лимон"
                    },
                    {
                        "id": 44,
                        "name": "Свежий укроп"
                    },
                    {
                        "id": 45,
                        "name": "Соль и перец"
                    }
                ],
                "categories": [
                    {
                        "id": 9,
                        "name": "Рыба"
                    },
                    {
                        "id": 10,
                        "name": "Скандинавская кухня"
                    }
                ],
                "name": "Лосось с лимонно-укропным соусом",
                "description": "Жареный или запеченный лосось подается с ароматным соусом из лимона и укропа.",
                "image": "https://kandbi.com/image/catalog/blog/firmennoe-blyudo-v-restorane-chto-eto-i-kakim-ono-byvaet-2.jpg",
                "price": 420,
                "restaurant": 6
            },
            {
                "id": 286,
                "ingredients": [
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    },
                    {
                        "id": 33,
                        "name": "Помидоры"
                    },
                    {
                        "id": 46,
                        "name": "Хлеб чиабатта"
                    },
                    {
                        "id": 47,
                        "name": "Моцарелла"
                    },
                    {
                        "id": 48,
                        "name": "Свежие листья базилика"
                    },
                    {
                        "id": 49,
                        "name": "Бальзамический глазурь"
                    }
                ],
                "categories": [
                    {
                        "id": 11,
                        "name": "Панини"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Капрезе Панини",
                "description": "Жареный бутерброд с моцареллой, помидорами и базиликом.",
                "image": "https://cdn.lifehacker.ru/wp-content/uploads/2020/04/5e95669b997f5_j3hekga7e3r41__700_1587380182-e1587380213139.jpg",
                "price": 250,
                "restaurant": 6
            },
            {
                "id": 296,
                "ingredients": [
                    {
                        "id": 8,
                        "name": "Лук"
                    },
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 27,
                        "name": "Имбирь"
                    },
                    {
                        "id": 50,
                        "name": "Смешанные овощи"
                    },
                    {
                        "id": 51,
                        "name": "Карри-паста"
                    },
                    {
                        "id": 52,
                        "name": "Кокосовое молоко"
                    },
                    {
                        "id": 53,
                        "name": "Рис басмати"
                    }
                ],
                "categories": [
                    {
                        "id": 12,
                        "name": "Карри"
                    },
                    {
                        "id": 6,
                        "name": "Азиатская кухня"
                    }
                ],
                "name": "Овощное Карри",
                "description": "Острое и ароматное карри с разнообразными овощами.",
                "image": "https://e0.edimdoma.ru/data/posts/0002/1936/21936-ed4_wide.jpg?1679398231",
                "price": 290,
                "restaurant": 6
            },
            {
                "id": 306,
                "ingredients": [
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 17,
                        "name": "Пармезан"
                    },
                    {
                        "id": 41,
                        "name": "Масло"
                    },
                    {
                        "id": 45,
                        "name": "Соль и перец"
                    },
                    {
                        "id": 54,
                        "name": "Лапша феттучини"
                    },
                    {
                        "id": 55,
                        "name": "Куриная грудка"
                    },
                    {
                        "id": 56,
                        "name": "Тяжелая сливка"
                    }
                ],
                "categories": [
                    {
                        "id": 1,
                        "name": "Паста"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Куриное Альфредо Паста",
                "description": "Кремовый соус Альфредо с жареной куриной грудкой над лапшой феттучини.",
                "image": "https://hip2go.ru/api2/images/IikoProducts26/c1c668e7c6-1_500x353.jpg",
                "price": 360,
                "restaurant": 6
            },
            {
                "id": 316,
                "ingredients": [
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    },
                    {
                        "id": 45,
                        "name": "Соль и перец"
                    },
                    {
                        "id": 57,
                        "name": "Киноа"
                    },
                    {
                        "id": 58,
                        "name": "Чёрные бобы"
                    },
                    {
                        "id": 59,
                        "name": "Авокадо"
                    },
                    {
                        "id": 60,
                        "name": "Вишня томаты"
                    },
                    {
                        "id": 61,
                        "name": "Красный лук"
                    },
                    {
                        "id": 62,
                        "name": "Кинза"
                    },
                    {
                        "id": 63,
                        "name": "Сок лайма"
                    }
                ],
                "categories": [
                    {
                        "id": 3,
                        "name": "Салаты"
                    },
                    {
                        "id": 13,
                        "name": "Здоровое питание"
                    }
                ],
                "name": "Салат с киноа, авокадо и чёрными бобами",
                "description": "Питательный салат с киноа, авокадо, чёрными бобами и лаймовым винегретом.",
                "image": "https://takethemameal.com/files_images_v2/stam.jpg",
                "price": 310,
                "restaurant": 6
            }
        ],
        "name": "Мексиканский Рай",
        "description": "Острые и сочные вкусы Мексики ждут вас в нашем ресторане.",
        "image": "https://img.freepik.com/premium-vector/restaurant-logo_1078-387.jpg",
        "address": "ул. Тако, 567",
        "created_at": "2023-12-29T02:10:39.156512Z",
        "updated_at": "2023-12-29T05:13:59.900479Z"
    },
    {
        "id": 5,
        "categories": [
            {
                "id": 5,
                "name": "Овощи"
            },
            {
                "id": 6,
                "name": "Азиатская кухня"
            }
        ],
        "meals": [
            {
                "id": 227,
                "ingredients": [
                    {
                        "id": 7,
                        "name": "Молотый говяжий фарш"
                    },
                    {
                        "id": 8,
                        "name": "Лук"
                    },
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 10,
                        "name": "Томатный соус"
                    },
                    {
                        "id": 11,
                        "name": "Томаты"
                    },
                    {
                        "id": 12,
                        "name": "Итальянские специи"
                    },
                    {
                        "id": 13,
                        "name": "Спагетти"
                    }
                ],
                "categories": [
                    {
                        "id": 1,
                        "name": "Паста"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Спагетти Болоньезе",
                "description": "Классическое итальянское блюдо с пастой и сытным мясным соусом.",
                "image": "https://kremlin-product.ru/upload/medialibrary/241/jfw6bequvf8s8mcum1npqc0jx1v1ngad/grilled_vegetables.jpg",
                "price": 350,
                "restaurant": 5
            },
            {
                "id": 237,
                "ingredients": [
                    {
                        "id": 14,
                        "name": "Жареная куринная грудка"
                    },
                    {
                        "id": 15,
                        "name": "Салат романо"
                    },
                    {
                        "id": 16,
                        "name": "Крутоны"
                    },
                    {
                        "id": 17,
                        "name": "Пармезан"
                    },
                    {
                        "id": 18,
                        "name": "Соус Цезарь"
                    },
                    {
                        "id": 19,
                        "name": "Лимонный сок"
                    },
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    }
                ],
                "categories": [
                    {
                        "id": 3,
                        "name": "Салаты"
                    },
                    {
                        "id": 4,
                        "name": "Американская кухня"
                    }
                ],
                "name": "Цезарь с курицей",
                "description": "Освежающий салат с жареной курицей, хрустящим салатом и соусом Цезарь.",
                "image": "https://s.restorating.ru/w/1920x1080/articles/2920/None-111028.jpeg",
                "price": 280,
                "restaurant": 5
            },
            {
                "id": 247,
                "ingredients": [
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 21,
                        "name": "Тофу"
                    },
                    {
                        "id": 22,
                        "name": "Брокколи"
                    },
                    {
                        "id": 23,
                        "name": "Болгарский перец"
                    },
                    {
                        "id": 24,
                        "name": "Морковь"
                    },
                    {
                        "id": 25,
                        "name": "Снеговые горошинки"
                    },
                    {
                        "id": 26,
                        "name": "Соевый соус"
                    },
                    {
                        "id": 27,
                        "name": "Имбирь"
                    },
                    {
                        "id": 28,
                        "name": "Соевое масло"
                    }
                ],
                "categories": [
                    {
                        "id": 5,
                        "name": "Овощи"
                    },
                    {
                        "id": 6,
                        "name": "Азиатская кухня"
                    }
                ],
                "name": "Овощной вок",
                "description": "Быстрый и красочный вок с овощами и тофу или выбранным вами видом белка.",
                "image": "https://gotovim-doma.ru/images/recipe/e/ce/eceb453fefbab09075a8c779712e52f8.jpg",
                "price": 300,
                "restaurant": 5
            },
            {
                "id": 257,
                "ingredients": [
                    {
                        "id": 29,
                        "name": "Молотая говядина"
                    },
                    {
                        "id": 30,
                        "name": "Приправа для тако"
                    },
                    {
                        "id": 31,
                        "name": "Тортильи"
                    },
                    {
                        "id": 32,
                        "name": "Салат"
                    },
                    {
                        "id": 33,
                        "name": "Помидоры"
                    },
                    {
                        "id": 34,
                        "name": "Сыр"
                    },
                    {
                        "id": 35,
                        "name": "Сальса"
                    },
                    {
                        "id": 36,
                        "name": "Сметана"
                    }
                ],
                "categories": [
                    {
                        "id": 7,
                        "name": "Мексиканская кухня"
                    }
                ],
                "name": "Такос с говядиной",
                "description": "Ароматная приправленная говядина в тортильях с начинкой.",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNVW3bTlMbUA_8-fbvHUgW1KaIEKaLANG0dg&usqp=CAU",
                "price": 320,
                "restaurant": 5
            },
            {
                "id": 267,
                "ingredients": [
                    {
                        "id": 8,
                        "name": "Лук"
                    },
                    {
                        "id": 17,
                        "name": "Пармезан"
                    },
                    {
                        "id": 37,
                        "name": "Рис арборио"
                    },
                    {
                        "id": 38,
                        "name": "Грибы"
                    },
                    {
                        "id": 39,
                        "name": "Белое вино"
                    },
                    {
                        "id": 40,
                        "name": "Куриный бульон"
                    },
                    {
                        "id": 41,
                        "name": "Масло"
                    }
                ],
                "categories": [
                    {
                        "id": 8,
                        "name": "Ризотто"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Грибной ризотто",
                "description": "Кремовое итальянское блюдо с жареными грибами и пармезаном.",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBsyitq8OdeFsdjKzPHO_ntFd0k9HnlM1NvA&usqp=CAU",
                "price": 380,
                "restaurant": 5
            },
            {
                "id": 277,
                "ingredients": [
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    },
                    {
                        "id": 42,
                        "name": "Филе лосося"
                    },
                    {
                        "id": 43,
                        "name": "Лимон"
                    },
                    {
                        "id": 44,
                        "name": "Свежий укроп"
                    },
                    {
                        "id": 45,
                        "name": "Соль и перец"
                    }
                ],
                "categories": [
                    {
                        "id": 9,
                        "name": "Рыба"
                    },
                    {
                        "id": 10,
                        "name": "Скандинавская кухня"
                    }
                ],
                "name": "Лосось с лимонно-укропным соусом",
                "description": "Жареный или запеченный лосось подается с ароматным соусом из лимона и укропа.",
                "image": "https://kandbi.com/image/catalog/blog/firmennoe-blyudo-v-restorane-chto-eto-i-kakim-ono-byvaet-2.jpg",
                "price": 420,
                "restaurant": 5
            },
            {
                "id": 287,
                "ingredients": [
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    },
                    {
                        "id": 33,
                        "name": "Помидоры"
                    },
                    {
                        "id": 46,
                        "name": "Хлеб чиабатта"
                    },
                    {
                        "id": 47,
                        "name": "Моцарелла"
                    },
                    {
                        "id": 48,
                        "name": "Свежие листья базилика"
                    },
                    {
                        "id": 49,
                        "name": "Бальзамический глазурь"
                    }
                ],
                "categories": [
                    {
                        "id": 11,
                        "name": "Панини"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Капрезе Панини",
                "description": "Жареный бутерброд с моцареллой, помидорами и базиликом.",
                "image": "https://cdn.lifehacker.ru/wp-content/uploads/2020/04/5e95669b997f5_j3hekga7e3r41__700_1587380182-e1587380213139.jpg",
                "price": 250,
                "restaurant": 5
            },
            {
                "id": 297,
                "ingredients": [
                    {
                        "id": 8,
                        "name": "Лук"
                    },
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 27,
                        "name": "Имбирь"
                    },
                    {
                        "id": 50,
                        "name": "Смешанные овощи"
                    },
                    {
                        "id": 51,
                        "name": "Карри-паста"
                    },
                    {
                        "id": 52,
                        "name": "Кокосовое молоко"
                    },
                    {
                        "id": 53,
                        "name": "Рис басмати"
                    }
                ],
                "categories": [
                    {
                        "id": 12,
                        "name": "Карри"
                    },
                    {
                        "id": 6,
                        "name": "Азиатская кухня"
                    }
                ],
                "name": "Овощное Карри",
                "description": "Острое и ароматное карри с разнообразными овощами.",
                "image": "https://e0.edimdoma.ru/data/posts/0002/1936/21936-ed4_wide.jpg?1679398231",
                "price": 290,
                "restaurant": 5
            },
            {
                "id": 307,
                "ingredients": [
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 17,
                        "name": "Пармезан"
                    },
                    {
                        "id": 41,
                        "name": "Масло"
                    },
                    {
                        "id": 45,
                        "name": "Соль и перец"
                    },
                    {
                        "id": 54,
                        "name": "Лапша феттучини"
                    },
                    {
                        "id": 55,
                        "name": "Куриная грудка"
                    },
                    {
                        "id": 56,
                        "name": "Тяжелая сливка"
                    }
                ],
                "categories": [
                    {
                        "id": 1,
                        "name": "Паста"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Куриное Альфредо Паста",
                "description": "Кремовый соус Альфредо с жареной куриной грудкой над лапшой феттучини.",
                "image": "https://hip2go.ru/api2/images/IikoProducts26/c1c668e7c6-1_500x353.jpg",
                "price": 360,
                "restaurant": 5
            },
            {
                "id": 317,
                "ingredients": [
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    },
                    {
                        "id": 45,
                        "name": "Соль и перец"
                    },
                    {
                        "id": 57,
                        "name": "Киноа"
                    },
                    {
                        "id": 58,
                        "name": "Чёрные бобы"
                    },
                    {
                        "id": 59,
                        "name": "Авокадо"
                    },
                    {
                        "id": 60,
                        "name": "Вишня томаты"
                    },
                    {
                        "id": 61,
                        "name": "Красный лук"
                    },
                    {
                        "id": 62,
                        "name": "Кинза"
                    },
                    {
                        "id": 63,
                        "name": "Сок лайма"
                    }
                ],
                "categories": [
                    {
                        "id": 3,
                        "name": "Салаты"
                    },
                    {
                        "id": 13,
                        "name": "Здоровое питание"
                    }
                ],
                "name": "Салат с киноа, авокадо и чёрными бобами",
                "description": "Питательный салат с киноа, авокадо, чёрными бобами и лаймовым винегретом.",
                "image": "https://takethemameal.com/files_images_v2/stam.jpg",
                "price": 310,
                "restaurant": 5
            }
        ],
        "name": "Азиатский Уголок",
        "description": "Приготовлено с любовью — азиатские блюда с использованием свежих овощей и традиционных приправ.",
        "image": "https://d1csarkz8obe9u.cloudfront.net/posterpreviews/cafe-restaurant-logo-design-template-36687c31a16c5e4a27cad5fc058dcebb_screen.jpg?ts=1561470662",
        "address": "пр. Востока, 101",
        "created_at": "2023-12-29T02:10:39.140885Z",
        "updated_at": "2023-12-29T05:13:49.914776Z"
    },
    {
        "id": 4,
        "categories": [
            {
                "id": 4,
                "name": "Американская кухня"
            }
        ],
        "meals": [
            {
                "id": 228,
                "ingredients": [
                    {
                        "id": 7,
                        "name": "Молотый говяжий фарш"
                    },
                    {
                        "id": 8,
                        "name": "Лук"
                    },
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 10,
                        "name": "Томатный соус"
                    },
                    {
                        "id": 11,
                        "name": "Томаты"
                    },
                    {
                        "id": 12,
                        "name": "Итальянские специи"
                    },
                    {
                        "id": 13,
                        "name": "Спагетти"
                    }
                ],
                "categories": [
                    {
                        "id": 1,
                        "name": "Паста"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Спагетти Болоньезе",
                "description": "Классическое итальянское блюдо с пастой и сытным мясным соусом.",
                "image": "https://kremlin-product.ru/upload/medialibrary/241/jfw6bequvf8s8mcum1npqc0jx1v1ngad/grilled_vegetables.jpg",
                "price": 350,
                "restaurant": 4
            },
            {
                "id": 238,
                "ingredients": [
                    {
                        "id": 14,
                        "name": "Жареная куринная грудка"
                    },
                    {
                        "id": 15,
                        "name": "Салат романо"
                    },
                    {
                        "id": 16,
                        "name": "Крутоны"
                    },
                    {
                        "id": 17,
                        "name": "Пармезан"
                    },
                    {
                        "id": 18,
                        "name": "Соус Цезарь"
                    },
                    {
                        "id": 19,
                        "name": "Лимонный сок"
                    },
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    }
                ],
                "categories": [
                    {
                        "id": 3,
                        "name": "Салаты"
                    },
                    {
                        "id": 4,
                        "name": "Американская кухня"
                    }
                ],
                "name": "Цезарь с курицей",
                "description": "Освежающий салат с жареной курицей, хрустящим салатом и соусом Цезарь.",
                "image": "https://s.restorating.ru/w/1920x1080/articles/2920/None-111028.jpeg",
                "price": 280,
                "restaurant": 4
            },
            {
                "id": 248,
                "ingredients": [
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 21,
                        "name": "Тофу"
                    },
                    {
                        "id": 22,
                        "name": "Брокколи"
                    },
                    {
                        "id": 23,
                        "name": "Болгарский перец"
                    },
                    {
                        "id": 24,
                        "name": "Морковь"
                    },
                    {
                        "id": 25,
                        "name": "Снеговые горошинки"
                    },
                    {
                        "id": 26,
                        "name": "Соевый соус"
                    },
                    {
                        "id": 27,
                        "name": "Имбирь"
                    },
                    {
                        "id": 28,
                        "name": "Соевое масло"
                    }
                ],
                "categories": [
                    {
                        "id": 5,
                        "name": "Овощи"
                    },
                    {
                        "id": 6,
                        "name": "Азиатская кухня"
                    }
                ],
                "name": "Овощной вок",
                "description": "Быстрый и красочный вок с овощами и тофу или выбранным вами видом белка.",
                "image": "https://gotovim-doma.ru/images/recipe/e/ce/eceb453fefbab09075a8c779712e52f8.jpg",
                "price": 300,
                "restaurant": 4
            },
            {
                "id": 258,
                "ingredients": [
                    {
                        "id": 29,
                        "name": "Молотая говядина"
                    },
                    {
                        "id": 30,
                        "name": "Приправа для тако"
                    },
                    {
                        "id": 31,
                        "name": "Тортильи"
                    },
                    {
                        "id": 32,
                        "name": "Салат"
                    },
                    {
                        "id": 33,
                        "name": "Помидоры"
                    },
                    {
                        "id": 34,
                        "name": "Сыр"
                    },
                    {
                        "id": 35,
                        "name": "Сальса"
                    },
                    {
                        "id": 36,
                        "name": "Сметана"
                    }
                ],
                "categories": [
                    {
                        "id": 7,
                        "name": "Мексиканская кухня"
                    }
                ],
                "name": "Такос с говядиной",
                "description": "Ароматная приправленная говядина в тортильях с начинкой.",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNVW3bTlMbUA_8-fbvHUgW1KaIEKaLANG0dg&usqp=CAU",
                "price": 320,
                "restaurant": 4
            },
            {
                "id": 268,
                "ingredients": [
                    {
                        "id": 8,
                        "name": "Лук"
                    },
                    {
                        "id": 17,
                        "name": "Пармезан"
                    },
                    {
                        "id": 37,
                        "name": "Рис арборио"
                    },
                    {
                        "id": 38,
                        "name": "Грибы"
                    },
                    {
                        "id": 39,
                        "name": "Белое вино"
                    },
                    {
                        "id": 40,
                        "name": "Куриный бульон"
                    },
                    {
                        "id": 41,
                        "name": "Масло"
                    }
                ],
                "categories": [
                    {
                        "id": 8,
                        "name": "Ризотто"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Грибной ризотто",
                "description": "Кремовое итальянское блюдо с жареными грибами и пармезаном.",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBsyitq8OdeFsdjKzPHO_ntFd0k9HnlM1NvA&usqp=CAU",
                "price": 380,
                "restaurant": 4
            },
            {
                "id": 278,
                "ingredients": [
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    },
                    {
                        "id": 42,
                        "name": "Филе лосося"
                    },
                    {
                        "id": 43,
                        "name": "Лимон"
                    },
                    {
                        "id": 44,
                        "name": "Свежий укроп"
                    },
                    {
                        "id": 45,
                        "name": "Соль и перец"
                    }
                ],
                "categories": [
                    {
                        "id": 9,
                        "name": "Рыба"
                    },
                    {
                        "id": 10,
                        "name": "Скандинавская кухня"
                    }
                ],
                "name": "Лосось с лимонно-укропным соусом",
                "description": "Жареный или запеченный лосось подается с ароматным соусом из лимона и укропа.",
                "image": "https://kandbi.com/image/catalog/blog/firmennoe-blyudo-v-restorane-chto-eto-i-kakim-ono-byvaet-2.jpg",
                "price": 420,
                "restaurant": 4
            },
            {
                "id": 288,
                "ingredients": [
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    },
                    {
                        "id": 33,
                        "name": "Помидоры"
                    },
                    {
                        "id": 46,
                        "name": "Хлеб чиабатта"
                    },
                    {
                        "id": 47,
                        "name": "Моцарелла"
                    },
                    {
                        "id": 48,
                        "name": "Свежие листья базилика"
                    },
                    {
                        "id": 49,
                        "name": "Бальзамический глазурь"
                    }
                ],
                "categories": [
                    {
                        "id": 11,
                        "name": "Панини"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Капрезе Панини",
                "description": "Жареный бутерброд с моцареллой, помидорами и базиликом.",
                "image": "https://cdn.lifehacker.ru/wp-content/uploads/2020/04/5e95669b997f5_j3hekga7e3r41__700_1587380182-e1587380213139.jpg",
                "price": 250,
                "restaurant": 4
            },
            {
                "id": 298,
                "ingredients": [
                    {
                        "id": 8,
                        "name": "Лук"
                    },
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 27,
                        "name": "Имбирь"
                    },
                    {
                        "id": 50,
                        "name": "Смешанные овощи"
                    },
                    {
                        "id": 51,
                        "name": "Карри-паста"
                    },
                    {
                        "id": 52,
                        "name": "Кокосовое молоко"
                    },
                    {
                        "id": 53,
                        "name": "Рис басмати"
                    }
                ],
                "categories": [
                    {
                        "id": 12,
                        "name": "Карри"
                    },
                    {
                        "id": 6,
                        "name": "Азиатская кухня"
                    }
                ],
                "name": "Овощное Карри",
                "description": "Острое и ароматное карри с разнообразными овощами.",
                "image": "https://e0.edimdoma.ru/data/posts/0002/1936/21936-ed4_wide.jpg?1679398231",
                "price": 290,
                "restaurant": 4
            },
            {
                "id": 308,
                "ingredients": [
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 17,
                        "name": "Пармезан"
                    },
                    {
                        "id": 41,
                        "name": "Масло"
                    },
                    {
                        "id": 45,
                        "name": "Соль и перец"
                    },
                    {
                        "id": 54,
                        "name": "Лапша феттучини"
                    },
                    {
                        "id": 55,
                        "name": "Куриная грудка"
                    },
                    {
                        "id": 56,
                        "name": "Тяжелая сливка"
                    }
                ],
                "categories": [
                    {
                        "id": 1,
                        "name": "Паста"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Куриное Альфредо Паста",
                "description": "Кремовый соус Альфредо с жареной куриной грудкой над лапшой феттучини.",
                "image": "https://hip2go.ru/api2/images/IikoProducts26/c1c668e7c6-1_500x353.jpg",
                "price": 360,
                "restaurant": 4
            },
            {
                "id": 318,
                "ingredients": [
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    },
                    {
                        "id": 45,
                        "name": "Соль и перец"
                    },
                    {
                        "id": 57,
                        "name": "Киноа"
                    },
                    {
                        "id": 58,
                        "name": "Чёрные бобы"
                    },
                    {
                        "id": 59,
                        "name": "Авокадо"
                    },
                    {
                        "id": 60,
                        "name": "Вишня томаты"
                    },
                    {
                        "id": 61,
                        "name": "Красный лук"
                    },
                    {
                        "id": 62,
                        "name": "Кинза"
                    },
                    {
                        "id": 63,
                        "name": "Сок лайма"
                    }
                ],
                "categories": [
                    {
                        "id": 3,
                        "name": "Салаты"
                    },
                    {
                        "id": 13,
                        "name": "Здоровое питание"
                    }
                ],
                "name": "Салат с киноа, авокадо и чёрными бобами",
                "description": "Питательный салат с киноа, авокадо, чёрными бобами и лаймовым винегретом.",
                "image": "https://takethemameal.com/files_images_v2/stam.jpg",
                "price": 310,
                "restaurant": 4
            }
        ],
        "name": "Американский Дайнер",
        "description": "Погрузитесь в атмосферу настоящего американского дайнера с классическими блюдами.",
        "image": "https://static.rfstat.com/logo-presets/815/thumbnail_663f51850657_1x.webp",
        "address": "ул. Американская, 789",
        "created_at": "2023-12-29T02:10:39.131752Z",
        "updated_at": "2023-12-29T05:13:31.383269Z"
    },
    {
        "id": 3,
        "categories": [
            {
                "id": 3,
                "name": "Салаты"
            },
            {
                "id": 13,
                "name": "Здоровое питание"
            }
        ],
        "meals": [
            {
                "id": 229,
                "ingredients": [
                    {
                        "id": 7,
                        "name": "Молотый говяжий фарш"
                    },
                    {
                        "id": 8,
                        "name": "Лук"
                    },
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 10,
                        "name": "Томатный соус"
                    },
                    {
                        "id": 11,
                        "name": "Томаты"
                    },
                    {
                        "id": 12,
                        "name": "Итальянские специи"
                    },
                    {
                        "id": 13,
                        "name": "Спагетти"
                    }
                ],
                "categories": [
                    {
                        "id": 1,
                        "name": "Паста"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Спагетти Болоньезе",
                "description": "Классическое итальянское блюдо с пастой и сытным мясным соусом.",
                "image": "https://kremlin-product.ru/upload/medialibrary/241/jfw6bequvf8s8mcum1npqc0jx1v1ngad/grilled_vegetables.jpg",
                "price": 350,
                "restaurant": 3
            },
            {
                "id": 239,
                "ingredients": [
                    {
                        "id": 14,
                        "name": "Жареная куринная грудка"
                    },
                    {
                        "id": 15,
                        "name": "Салат романо"
                    },
                    {
                        "id": 16,
                        "name": "Крутоны"
                    },
                    {
                        "id": 17,
                        "name": "Пармезан"
                    },
                    {
                        "id": 18,
                        "name": "Соус Цезарь"
                    },
                    {
                        "id": 19,
                        "name": "Лимонный сок"
                    },
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    }
                ],
                "categories": [
                    {
                        "id": 3,
                        "name": "Салаты"
                    },
                    {
                        "id": 4,
                        "name": "Американская кухня"
                    }
                ],
                "name": "Цезарь с курицей",
                "description": "Освежающий салат с жареной курицей, хрустящим салатом и соусом Цезарь.",
                "image": "https://s.restorating.ru/w/1920x1080/articles/2920/None-111028.jpeg",
                "price": 280,
                "restaurant": 3
            },
            {
                "id": 249,
                "ingredients": [
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 21,
                        "name": "Тофу"
                    },
                    {
                        "id": 22,
                        "name": "Брокколи"
                    },
                    {
                        "id": 23,
                        "name": "Болгарский перец"
                    },
                    {
                        "id": 24,
                        "name": "Морковь"
                    },
                    {
                        "id": 25,
                        "name": "Снеговые горошинки"
                    },
                    {
                        "id": 26,
                        "name": "Соевый соус"
                    },
                    {
                        "id": 27,
                        "name": "Имбирь"
                    },
                    {
                        "id": 28,
                        "name": "Соевое масло"
                    }
                ],
                "categories": [
                    {
                        "id": 5,
                        "name": "Овощи"
                    },
                    {
                        "id": 6,
                        "name": "Азиатская кухня"
                    }
                ],
                "name": "Овощной вок",
                "description": "Быстрый и красочный вок с овощами и тофу или выбранным вами видом белка.",
                "image": "https://gotovim-doma.ru/images/recipe/e/ce/eceb453fefbab09075a8c779712e52f8.jpg",
                "price": 300,
                "restaurant": 3
            },
            {
                "id": 259,
                "ingredients": [
                    {
                        "id": 29,
                        "name": "Молотая говядина"
                    },
                    {
                        "id": 30,
                        "name": "Приправа для тако"
                    },
                    {
                        "id": 31,
                        "name": "Тортильи"
                    },
                    {
                        "id": 32,
                        "name": "Салат"
                    },
                    {
                        "id": 33,
                        "name": "Помидоры"
                    },
                    {
                        "id": 34,
                        "name": "Сыр"
                    },
                    {
                        "id": 35,
                        "name": "Сальса"
                    },
                    {
                        "id": 36,
                        "name": "Сметана"
                    }
                ],
                "categories": [
                    {
                        "id": 7,
                        "name": "Мексиканская кухня"
                    }
                ],
                "name": "Такос с говядиной",
                "description": "Ароматная приправленная говядина в тортильях с начинкой.",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNVW3bTlMbUA_8-fbvHUgW1KaIEKaLANG0dg&usqp=CAU",
                "price": 320,
                "restaurant": 3
            },
            {
                "id": 269,
                "ingredients": [
                    {
                        "id": 8,
                        "name": "Лук"
                    },
                    {
                        "id": 17,
                        "name": "Пармезан"
                    },
                    {
                        "id": 37,
                        "name": "Рис арборио"
                    },
                    {
                        "id": 38,
                        "name": "Грибы"
                    },
                    {
                        "id": 39,
                        "name": "Белое вино"
                    },
                    {
                        "id": 40,
                        "name": "Куриный бульон"
                    },
                    {
                        "id": 41,
                        "name": "Масло"
                    }
                ],
                "categories": [
                    {
                        "id": 8,
                        "name": "Ризотто"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Грибной ризотто",
                "description": "Кремовое итальянское блюдо с жареными грибами и пармезаном.",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBsyitq8OdeFsdjKzPHO_ntFd0k9HnlM1NvA&usqp=CAU",
                "price": 380,
                "restaurant": 3
            },
            {
                "id": 279,
                "ingredients": [
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    },
                    {
                        "id": 42,
                        "name": "Филе лосося"
                    },
                    {
                        "id": 43,
                        "name": "Лимон"
                    },
                    {
                        "id": 44,
                        "name": "Свежий укроп"
                    },
                    {
                        "id": 45,
                        "name": "Соль и перец"
                    }
                ],
                "categories": [
                    {
                        "id": 9,
                        "name": "Рыба"
                    },
                    {
                        "id": 10,
                        "name": "Скандинавская кухня"
                    }
                ],
                "name": "Лосось с лимонно-укропным соусом",
                "description": "Жареный или запеченный лосось подается с ароматным соусом из лимона и укропа.",
                "image": "https://kandbi.com/image/catalog/blog/firmennoe-blyudo-v-restorane-chto-eto-i-kakim-ono-byvaet-2.jpg",
                "price": 420,
                "restaurant": 3
            },
            {
                "id": 289,
                "ingredients": [
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    },
                    {
                        "id": 33,
                        "name": "Помидоры"
                    },
                    {
                        "id": 46,
                        "name": "Хлеб чиабатта"
                    },
                    {
                        "id": 47,
                        "name": "Моцарелла"
                    },
                    {
                        "id": 48,
                        "name": "Свежие листья базилика"
                    },
                    {
                        "id": 49,
                        "name": "Бальзамический глазурь"
                    }
                ],
                "categories": [
                    {
                        "id": 11,
                        "name": "Панини"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Капрезе Панини",
                "description": "Жареный бутерброд с моцареллой, помидорами и базиликом.",
                "image": "https://cdn.lifehacker.ru/wp-content/uploads/2020/04/5e95669b997f5_j3hekga7e3r41__700_1587380182-e1587380213139.jpg",
                "price": 250,
                "restaurant": 3
            },
            {
                "id": 299,
                "ingredients": [
                    {
                        "id": 8,
                        "name": "Лук"
                    },
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 27,
                        "name": "Имбирь"
                    },
                    {
                        "id": 50,
                        "name": "Смешанные овощи"
                    },
                    {
                        "id": 51,
                        "name": "Карри-паста"
                    },
                    {
                        "id": 52,
                        "name": "Кокосовое молоко"
                    },
                    {
                        "id": 53,
                        "name": "Рис басмати"
                    }
                ],
                "categories": [
                    {
                        "id": 12,
                        "name": "Карри"
                    },
                    {
                        "id": 6,
                        "name": "Азиатская кухня"
                    }
                ],
                "name": "Овощное Карри",
                "description": "Острое и ароматное карри с разнообразными овощами.",
                "image": "https://e0.edimdoma.ru/data/posts/0002/1936/21936-ed4_wide.jpg?1679398231",
                "price": 290,
                "restaurant": 3
            },
            {
                "id": 309,
                "ingredients": [
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 17,
                        "name": "Пармезан"
                    },
                    {
                        "id": 41,
                        "name": "Масло"
                    },
                    {
                        "id": 45,
                        "name": "Соль и перец"
                    },
                    {
                        "id": 54,
                        "name": "Лапша феттучини"
                    },
                    {
                        "id": 55,
                        "name": "Куриная грудка"
                    },
                    {
                        "id": 56,
                        "name": "Тяжелая сливка"
                    }
                ],
                "categories": [
                    {
                        "id": 1,
                        "name": "Паста"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Куриное Альфредо Паста",
                "description": "Кремовый соус Альфредо с жареной куриной грудкой над лапшой феттучини.",
                "image": "https://hip2go.ru/api2/images/IikoProducts26/c1c668e7c6-1_500x353.jpg",
                "price": 360,
                "restaurant": 3
            },
            {
                "id": 319,
                "ingredients": [
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    },
                    {
                        "id": 45,
                        "name": "Соль и перец"
                    },
                    {
                        "id": 57,
                        "name": "Киноа"
                    },
                    {
                        "id": 58,
                        "name": "Чёрные бобы"
                    },
                    {
                        "id": 59,
                        "name": "Авокадо"
                    },
                    {
                        "id": 60,
                        "name": "Вишня томаты"
                    },
                    {
                        "id": 61,
                        "name": "Красный лук"
                    },
                    {
                        "id": 62,
                        "name": "Кинза"
                    },
                    {
                        "id": 63,
                        "name": "Сок лайма"
                    }
                ],
                "categories": [
                    {
                        "id": 3,
                        "name": "Салаты"
                    },
                    {
                        "id": 13,
                        "name": "Здоровое питание"
                    }
                ],
                "name": "Салат с киноа, авокадо и чёрными бобами",
                "description": "Питательный салат с киноа, авокадо, чёрными бобами и лаймовым винегретом.",
                "image": "https://takethemameal.com/files_images_v2/stam.jpg",
                "price": 310,
                "restaurant": 3
            }
        ],
        "name": "Салатная Оазис",
        "description": "Здесь вы найдете разнообразные свежие салаты для здорового питания.",
        "image": "https://static.rfstat.com/logo-presets/4522/thumbnail_63a6c7e4a1df_1x.webp",
        "address": "пр. Здоровья, 456",
        "created_at": "2023-12-29T02:10:39.116866Z",
        "updated_at": "2023-12-29T05:13:16.251947Z"
    },
    {
        "id": 2,
        "categories": [
            {
                "id": 1,
                "name": "Паста"
            },
            {
                "id": 2,
                "name": "Итальянская кухня"
            }
        ],
        "meals": [
            {
                "id": 230,
                "ingredients": [
                    {
                        "id": 7,
                        "name": "Молотый говяжий фарш"
                    },
                    {
                        "id": 8,
                        "name": "Лук"
                    },
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 10,
                        "name": "Томатный соус"
                    },
                    {
                        "id": 11,
                        "name": "Томаты"
                    },
                    {
                        "id": 12,
                        "name": "Итальянские специи"
                    },
                    {
                        "id": 13,
                        "name": "Спагетти"
                    }
                ],
                "categories": [
                    {
                        "id": 1,
                        "name": "Паста"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Спагетти Болоньезе",
                "description": "Классическое итальянское блюдо с пастой и сытным мясным соусом.",
                "image": "https://kremlin-product.ru/upload/medialibrary/241/jfw6bequvf8s8mcum1npqc0jx1v1ngad/grilled_vegetables.jpg",
                "price": 350,
                "restaurant": 2
            },
            {
                "id": 240,
                "ingredients": [
                    {
                        "id": 14,
                        "name": "Жареная куринная грудка"
                    },
                    {
                        "id": 15,
                        "name": "Салат романо"
                    },
                    {
                        "id": 16,
                        "name": "Крутоны"
                    },
                    {
                        "id": 17,
                        "name": "Пармезан"
                    },
                    {
                        "id": 18,
                        "name": "Соус Цезарь"
                    },
                    {
                        "id": 19,
                        "name": "Лимонный сок"
                    },
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    }
                ],
                "categories": [
                    {
                        "id": 3,
                        "name": "Салаты"
                    },
                    {
                        "id": 4,
                        "name": "Американская кухня"
                    }
                ],
                "name": "Цезарь с курицей",
                "description": "Освежающий салат с жареной курицей, хрустящим салатом и соусом Цезарь.",
                "image": "https://s.restorating.ru/w/1920x1080/articles/2920/None-111028.jpeg",
                "price": 280,
                "restaurant": 2
            },
            {
                "id": 250,
                "ingredients": [
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 21,
                        "name": "Тофу"
                    },
                    {
                        "id": 22,
                        "name": "Брокколи"
                    },
                    {
                        "id": 23,
                        "name": "Болгарский перец"
                    },
                    {
                        "id": 24,
                        "name": "Морковь"
                    },
                    {
                        "id": 25,
                        "name": "Снеговые горошинки"
                    },
                    {
                        "id": 26,
                        "name": "Соевый соус"
                    },
                    {
                        "id": 27,
                        "name": "Имбирь"
                    },
                    {
                        "id": 28,
                        "name": "Соевое масло"
                    }
                ],
                "categories": [
                    {
                        "id": 5,
                        "name": "Овощи"
                    },
                    {
                        "id": 6,
                        "name": "Азиатская кухня"
                    }
                ],
                "name": "Овощной вок",
                "description": "Быстрый и красочный вок с овощами и тофу или выбранным вами видом белка.",
                "image": "https://gotovim-doma.ru/images/recipe/e/ce/eceb453fefbab09075a8c779712e52f8.jpg",
                "price": 300,
                "restaurant": 2
            },
            {
                "id": 260,
                "ingredients": [
                    {
                        "id": 29,
                        "name": "Молотая говядина"
                    },
                    {
                        "id": 30,
                        "name": "Приправа для тако"
                    },
                    {
                        "id": 31,
                        "name": "Тортильи"
                    },
                    {
                        "id": 32,
                        "name": "Салат"
                    },
                    {
                        "id": 33,
                        "name": "Помидоры"
                    },
                    {
                        "id": 34,
                        "name": "Сыр"
                    },
                    {
                        "id": 35,
                        "name": "Сальса"
                    },
                    {
                        "id": 36,
                        "name": "Сметана"
                    }
                ],
                "categories": [
                    {
                        "id": 7,
                        "name": "Мексиканская кухня"
                    }
                ],
                "name": "Такос с говядиной",
                "description": "Ароматная приправленная говядина в тортильях с начинкой.",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNVW3bTlMbUA_8-fbvHUgW1KaIEKaLANG0dg&usqp=CAU",
                "price": 320,
                "restaurant": 2
            },
            {
                "id": 270,
                "ingredients": [
                    {
                        "id": 8,
                        "name": "Лук"
                    },
                    {
                        "id": 17,
                        "name": "Пармезан"
                    },
                    {
                        "id": 37,
                        "name": "Рис арборио"
                    },
                    {
                        "id": 38,
                        "name": "Грибы"
                    },
                    {
                        "id": 39,
                        "name": "Белое вино"
                    },
                    {
                        "id": 40,
                        "name": "Куриный бульон"
                    },
                    {
                        "id": 41,
                        "name": "Масло"
                    }
                ],
                "categories": [
                    {
                        "id": 8,
                        "name": "Ризотто"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Грибной ризотто",
                "description": "Кремовое итальянское блюдо с жареными грибами и пармезаном.",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBsyitq8OdeFsdjKzPHO_ntFd0k9HnlM1NvA&usqp=CAU",
                "price": 380,
                "restaurant": 2
            },
            {
                "id": 280,
                "ingredients": [
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    },
                    {
                        "id": 42,
                        "name": "Филе лосося"
                    },
                    {
                        "id": 43,
                        "name": "Лимон"
                    },
                    {
                        "id": 44,
                        "name": "Свежий укроп"
                    },
                    {
                        "id": 45,
                        "name": "Соль и перец"
                    }
                ],
                "categories": [
                    {
                        "id": 9,
                        "name": "Рыба"
                    },
                    {
                        "id": 10,
                        "name": "Скандинавская кухня"
                    }
                ],
                "name": "Лосось с лимонно-укропным соусом",
                "description": "Жареный или запеченный лосось подается с ароматным соусом из лимона и укропа.",
                "image": "https://kandbi.com/image/catalog/blog/firmennoe-blyudo-v-restorane-chto-eto-i-kakim-ono-byvaet-2.jpg",
                "price": 420,
                "restaurant": 2
            },
            {
                "id": 290,
                "ingredients": [
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    },
                    {
                        "id": 33,
                        "name": "Помидоры"
                    },
                    {
                        "id": 46,
                        "name": "Хлеб чиабатта"
                    },
                    {
                        "id": 47,
                        "name": "Моцарелла"
                    },
                    {
                        "id": 48,
                        "name": "Свежие листья базилика"
                    },
                    {
                        "id": 49,
                        "name": "Бальзамический глазурь"
                    }
                ],
                "categories": [
                    {
                        "id": 11,
                        "name": "Панини"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Капрезе Панини",
                "description": "Жареный бутерброд с моцареллой, помидорами и базиликом.",
                "image": "https://cdn.lifehacker.ru/wp-content/uploads/2020/04/5e95669b997f5_j3hekga7e3r41__700_1587380182-e1587380213139.jpg",
                "price": 250,
                "restaurant": 2
            },
            {
                "id": 300,
                "ingredients": [
                    {
                        "id": 8,
                        "name": "Лук"
                    },
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 27,
                        "name": "Имбирь"
                    },
                    {
                        "id": 50,
                        "name": "Смешанные овощи"
                    },
                    {
                        "id": 51,
                        "name": "Карри-паста"
                    },
                    {
                        "id": 52,
                        "name": "Кокосовое молоко"
                    },
                    {
                        "id": 53,
                        "name": "Рис басмати"
                    }
                ],
                "categories": [
                    {
                        "id": 12,
                        "name": "Карри"
                    },
                    {
                        "id": 6,
                        "name": "Азиатская кухня"
                    }
                ],
                "name": "Овощное Карри",
                "description": "Острое и ароматное карри с разнообразными овощами.",
                "image": "https://e0.edimdoma.ru/data/posts/0002/1936/21936-ed4_wide.jpg?1679398231",
                "price": 290,
                "restaurant": 2
            },
            {
                "id": 310,
                "ingredients": [
                    {
                        "id": 9,
                        "name": "Чеснок"
                    },
                    {
                        "id": 17,
                        "name": "Пармезан"
                    },
                    {
                        "id": 41,
                        "name": "Масло"
                    },
                    {
                        "id": 45,
                        "name": "Соль и перец"
                    },
                    {
                        "id": 54,
                        "name": "Лапша феттучини"
                    },
                    {
                        "id": 55,
                        "name": "Куриная грудка"
                    },
                    {
                        "id": 56,
                        "name": "Тяжелая сливка"
                    }
                ],
                "categories": [
                    {
                        "id": 1,
                        "name": "Паста"
                    },
                    {
                        "id": 2,
                        "name": "Итальянская кухня"
                    }
                ],
                "name": "Куриное Альфредо Паста",
                "description": "Кремовый соус Альфредо с жареной куриной грудкой над лапшой феттучини.",
                "image": "https://hip2go.ru/api2/images/IikoProducts26/c1c668e7c6-1_500x353.jpg",
                "price": 360,
                "restaurant": 2
            },
            {
                "id": 320,
                "ingredients": [
                    {
                        "id": 20,
                        "name": "Оливковое масло"
                    },
                    {
                        "id": 45,
                        "name": "Соль и перец"
                    },
                    {
                        "id": 57,
                        "name": "Киноа"
                    },
                    {
                        "id": 58,
                        "name": "Чёрные бобы"
                    },
                    {
                        "id": 59,
                        "name": "Авокадо"
                    },
                    {
                        "id": 60,
                        "name": "Вишня томаты"
                    },
                    {
                        "id": 61,
                        "name": "Красный лук"
                    },
                    {
                        "id": 62,
                        "name": "Кинза"
                    },
                    {
                        "id": 63,
                        "name": "Сок лайма"
                    }
                ],
                "categories": [
                    {
                        "id": 3,
                        "name": "Салаты"
                    },
                    {
                        "id": 13,
                        "name": "Здоровое питание"
                    }
                ],
                "name": "Салат с киноа, авокадо и чёрными бобами",
                "description": "Питательный салат с киноа, авокадо, чёрными бобами и лаймовым винегретом.",
                "image": "https://takethemameal.com/files_images_v2/stam.jpg",
                "price": 310,
                "restaurant": 2
            }
        ],
        "name": "Итальянская Гастрономия",
        "description": "Приглашаем вас насладиться аутентичной итальянской кухней.",
        "image": "https://takethemameal.com/files_images_v2/stam.jpg",
        "address": "ул. Итальянская, 123",
        "created_at": "2023-12-29T02:10:39.096441Z",
        "updated_at": "2023-12-29T02:10:39.096441Z"
    }
]
