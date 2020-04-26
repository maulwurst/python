def make_car(manufacturer,model_name,**car_info):
    profile = {}
    profile['manufacturer'] = manufacturer
    profile['model_name'] = model_name
    for key, value in car_info.items():
        profile[key] = value
    return profile
car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)
