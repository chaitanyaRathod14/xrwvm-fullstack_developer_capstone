from .models import CarMake, CarModel


def initiate():
    """Populate the database with initial car makes and models."""
    car_make_data = [
        {"name": "Toyota", "description": "Japanese multinational automotive manufacturer", "country_of_origin": "Japan"},
        {"name": "Honda", "description": "Japanese public multinational conglomerate", "country_of_origin": "Japan"},
        {"name": "Ford", "description": "American multinational automobile manufacturer", "country_of_origin": "USA"},
        {"name": "Chevrolet", "description": "American automobile division of General Motors", "country_of_origin": "USA"},
        {"name": "BMW", "description": "German multinational corporation producing luxury vehicles", "country_of_origin": "Germany"},
        {"name": "Nissan", "description": "Japanese multinational automobile manufacturer", "country_of_origin": "Japan"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make, _ = CarMake.objects.get_or_create(
            name=data['name'],
            defaults={
                'description': data['description'],
                'country_of_origin': data['country_of_origin']
            }
        )
        car_make_instances.append(car_make)

    car_model_data = [
        {"name": "Camry", "car_make": car_make_instances[0], "car_type": "SEDAN", "year": 2021},
        {"name": "Corolla", "car_make": car_make_instances[0], "car_type": "SEDAN", "year": 2022},
        {"name": "RAV4", "car_make": car_make_instances[0], "car_type": "SUV", "year": 2023},
        {"name": "Highlander", "car_make": car_make_instances[0], "car_type": "SUV", "year": 2020},
        {"name": "Civic", "car_make": car_make_instances[1], "car_type": "SEDAN", "year": 2022},
        {"name": "Accord", "car_make": car_make_instances[1], "car_type": "SEDAN", "year": 2021},
        {"name": "CR-V", "car_make": car_make_instances[1], "car_type": "SUV", "year": 2023},
        {"name": "Pilot", "car_make": car_make_instances[1], "car_type": "SUV", "year": 2019},
        {"name": "Mustang", "car_make": car_make_instances[2], "car_type": "COUPE", "year": 2022},
        {"name": "F-150", "car_make": car_make_instances[2], "car_type": "TRUCK", "year": 2023},
        {"name": "Explorer", "car_make": car_make_instances[2], "car_type": "SUV", "year": 2021},
        {"name": "Escape", "car_make": car_make_instances[2], "car_type": "SUV", "year": 2020},
        {"name": "Silverado", "car_make": car_make_instances[3], "car_type": "TRUCK", "year": 2022},
        {"name": "Malibu", "car_make": car_make_instances[3], "car_type": "SEDAN", "year": 2021},
        {"name": "Equinox", "car_make": car_make_instances[3], "car_type": "SUV", "year": 2023},
        {"name": "3 Series", "car_make": car_make_instances[4], "car_type": "SEDAN", "year": 2022},
        {"name": "X5", "car_make": car_make_instances[4], "car_type": "SUV", "year": 2023},
        {"name": "Altima", "car_make": car_make_instances[5], "car_type": "SEDAN", "year": 2021},
        {"name": "Rogue", "car_make": car_make_instances[5], "car_type": "SUV", "year": 2022},
    ]

    for data in car_model_data:
        CarModel.objects.get_or_create(
            name=data['name'],
            car_make=data['car_make'],
            defaults={
                'car_type': data['car_type'],
                'year': data['year'],
            }
        )

    print("Database populated successfully!")
