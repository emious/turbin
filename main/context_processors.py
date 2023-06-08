from product.models import Category
from main.models import NavMenu, WebsiteSetting


def add_variable_to_context(request):
    menu = []
    nav_menu = NavMenu.objects.all()
    category = Category.objects.all()
    website_setting = WebsiteSetting.objects.first()

    for each in nav_menu:
        dict_cat = dict()
        dict_cat['id'] = each.id
        dict_cat['name'] = each.name
        dict_cat['link'] = each.link
        if each.name == 'محصولات':
            dict_cat['product'] = category
        menu.append(dict_cat)

    return {
        'nav_menu': menu,
        'WebsiteSetting': website_setting
    }
