import random

import factory
from faker import Faker

from apps.core.models import Image, Person, Role
from apps.core.utils import get_picsum_image, slugify

fake = Faker(locale="ru_RU")


class PersonFactory(factory.django.DjangoModelFactory):
    """Create Person objects.

    The behavior is different based on params:
        - `add_image`: create Person with fake not empty image
        - `add_real_image`: create Person with real image. Requires internet.
        - `add_city`: create Person with fake not empty city
        - `add_email`: create Person with fake email link nikolaykiryanov@lubimovka.ru
    """

    class Meta:
        model = Person

    first_name = factory.Faker("first_name", locale="ru_RU")
    last_name = factory.Faker("last_name", locale="ru_RU")
    middle_name = factory.Faker("middle_name", locale="ru_RU")
    email = None
    image = ""
    city = ""

    class Params:
        add_image = factory.Trait(
            image=factory.django.ImageField(color=factory.Faker("color")),
        )
        add_real_image = factory.Trait(
            image=factory.django.ImageField(from_func=get_picsum_image),
        )
        add_city = factory.Trait(
            city=factory.Faker("city_name", locale="ru_RU"),
        )
        add_email = factory.Trait(
            email=factory.LazyAttribute(lambda person: slugify(person.first_name + person.last_name) + "@lubimovka.ru"),
        )


class ImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Image
        django_get_or_create = ("image",)

    image = factory.django.ImageField(
        color=factory.LazyFunction(lambda: random.choice(["blue", "yellow", "green", "orange"])),
        width=factory.LazyFunction(lambda: random.randint(10, 1000)),
        height=factory.SelfAttribute("width"),
    )


class RoleFactory(factory.django.DjangoModelFactory):
    """This factory can be used only inside TeamMemberFactory."""

    class Meta:
        model = Role
        django_get_or_create = ["slug"]
