from django.shortcuts import render


def maindndpage(request):
    return render(request, "dndpage/main_dnd_page.html",)


def lvdndpage(request):
    lv = [i + 1 for i in range(20)]
    return render(request, "dndpage/lv_dnd_page.html", {"lv": lv})

def geardndpage(request):
    gear = [
        {"name": "item1", "description": "item1 description", "quantity" : 1},
        {"name": "item2", "description": "item2 description", "quantity" : 1},
        {"name": "item3", "description": "item3 description", "quantity" : 1},
        {"name": "item4", "description": "item4 description", "quantity" : 1},
        {"name": "item5", "description": "item5 description", "quantity" : 1},
    ]
    return render(request, "dndpage/gear_dnd_page.html", {"gear": gear})


