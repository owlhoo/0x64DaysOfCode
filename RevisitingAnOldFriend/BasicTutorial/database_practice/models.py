from django.db import models

# Create your models here.


class CommonInfo(models.Model):
    name = models.CharField(max_length=50, null=True)
    surname = models.CharField(max_length=50, null=True)

    class Meta:
        abstract = True


class Musician (CommonInfo):
    instrument = models.CharField(max_length=50)


class Album(CommonInfo):
    artist = models.CharField(max_length=50)
    release_date = models.DateField()
    num_stars = models.IntegerField()


class Person(CommonInfo):
    SHIRT_SIZES = (
        ('S', 'SMALL'),
        ('M', 'MEDIUM'),
        ('L', 'LARGE'),
    )
    shirt_size = models.CharField(max_length=6, choices=SHIRT_SIZES)
# get_shirt_size_display() will show full length choice
# while the S, M or L will be saved in the database

    @property
    def person_name(self):
        """Returns name of the person :D"""
        return f"{str(self.name)} {str(self.shirt_size)}"

    @person_name.setter
    def person_name(self, name):
        self.name = name

    @person_name.deleter
    def person_name(self):
        del self.name

    def __str__(self):
        return self.name


class Group(CommonInfo):
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name


class Membership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=256)


class Man(CommonInfo):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.person.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print("Done saving..", end="hehe\n")
        return self.__str__()


class Room(models.Model):
    wall_color = models.CharField(max_length=50)
    volume = models.IntegerField(default=2)


class Corridor(Room):
    has_furniture = models.BooleanField(default=False)
