
# coding: utf-8

# In[37]:


from datetime import datetime, date
client_1 = {
    'id': 1,  # Уникальный идентификатор 
    'last_name': u'Петров',  # Фамилия
    'first_name': u'Петр',  # Имя
    'Patronymic': u'Петрович'
    'birth_date': date(1990, 1, 1),  # Дата рождения
}

client_2 = {
    'id': 2,
    'last_name': u'Иванов',
    'first_name': u'Иван',
    'Patronymic': u'Иванович'
    'birth_date': date(1990, 7, 5),
}

clients = [client_1, client_2]

tarif_1 = {
    'id': 1,  # Уникальный идентификатор 
    'name': u'Базовый',  # Наименование 
    'percent': 5.5  # ставка
}

tarif_2 = {
    'id': 2,  # Уникальный идентификатор 
    'name': u'Не базовый',  # Наименование 
    'percent': 7.5  # ставка
}

tarifs = [tarif_1, tarif_2]

marks = {
    tarif_1['id']: {
        client_1['id']: 4000000
    },
   tarif_2['id']: {
        client_2['id']: 50000
    }
}

for i in marks:
     for n in marks[i]:
            print("Клиент:", clients[n-1]['last_name'], "Тариф:", tarifs[i-1]['name'], "Сумма:", marks[i][n] ,"Процентная ставка:", tarifs[i-1]['percent'], "%")

