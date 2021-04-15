def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(surname='Semenov', name='Boris', year='1990', city='Saint-Petersburg', email='b.semenov@corp.vk.com',
              telephone='+7-921-575-95-69'))