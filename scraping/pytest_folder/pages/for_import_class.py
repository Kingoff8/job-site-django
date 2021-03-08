def import_class(request):

    if request == 'hh':
        from pages.locators import HhRuLocators as Locators
    else:
        from pages.locators import other_site_Locators as Locators
    return print(Locators)
