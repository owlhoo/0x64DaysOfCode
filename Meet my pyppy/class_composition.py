# composition allows explicit relationships between objects, as follows


class Country(object):
    def __init__(self):
        self.cities = []

    def add_city(self, city):
        if isinstance(city, City):
            self.cities.append(city)
        else:
            raise TypeError("You've tried to add something "
                            "which is not of class City as city to country.." + str(self.__class__))


class City(object):
    def __init__(self, num_people):
        self.people = []
        self.num_people = num_people

    def add_person(self, person):
        self.people.append(person)

    def join_country(self, country):
        self.country = country
        country.add_city(self)

        for i in range(self.num_people):
            Person(i).join_city(self)


class Person(object):
    def __init__(self, ID):
        self.ID = ID

    def join_city(self, city):
        self.city = city
        city.add_person(self)

    def people_in_my_country(self):
        x = sum([len(c.people) for c in self.city.country.cities])
        return x


US = Country()
# US.add_city(20)
NYC = City(10).join_country(US)
SF = City(5).join_country(US)


print(US.cities[0].people[0].people_in_my_country())
