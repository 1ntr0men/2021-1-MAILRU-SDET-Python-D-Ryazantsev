import faker

fake = faker.Faker()


def get_valid_name():
    while True:
        name = fake.first_name()
        if 5 < len(name) < 17:
            return name


def get_invalid_name():
    while True:
        name = fake.first_name()
        if 5 > len(name):
            return name
