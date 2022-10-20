 # pip install mimesis

 from datetime import date
 from random import choice
 from mimesis import Person, Address, Finance
 from mimesis.builtins import RussiaSpecProvider
 from mimesis.enums import Gender
 from mimesis.locales import Locale


 def create_fake_person():
     address = Address(Locale.RU)
     fin = Finance(Locale.RU)
     person = Person(Locale.RU)
     ru_spec = RussiaSpecProvider()

     mail_dict = ['mail.ru', 'gmail.com', 'rambler.ru', 'yandex.ru', 'hotmail.com', 'outlook.com', 'ya.ru', 'yahoo.com',
                  'mail.com', 'protonmail.com']
     age_pers = person.age(minimum=22, maximum=66)

     list_person = [person.first_name(gender=Gender.MALE), ru_spec.patronymic(gender=Gender.MALE), person.last_name(gender=Gender.MALE), date.today().year - age_pers, age_pers, address.postal_code(
     )+' '+address.city() + ' '+address.address(), person.telephone(mask='8-9##-###-####'), person.email(domains=[choice(mail_dict)]), fin.company(), person.occupation().lower()]
     return list_person
