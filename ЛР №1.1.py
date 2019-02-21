
# coding: utf-8

# In[3]:


from datetime import datetime, date

class Client():
    def __init__(self, id=1,  last_name = "Петров", first_name = "Петр", patronymic = "Петрович", birth_date = date(1990, 1, 1), money = 4000000):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.birth_date = birth_date
        self.money = money

class Tarif():
    def __init__(self, name=None,  percent=2000):
        self.name = name
        self.percent = percent
     
Tarif_1 = Tarif('Базовый', 5.5)
Tarif_2 = Tarif('Не базовый', 7.5)
Tarifs = [Tarif_1, Tarif_2]

Client_1 = Client()
Client_2 = Client(2, "Иванов", "Иван", "Иванович", date(1990, 7, 5), 50000) 
Clients = [Client_1, Client_2]

class association():
    def __init__(self, client_id = 0,  tarif_id = 0):
        self.client_id = client_id
        self.tarif_id = tarif_id

Check_1 = association()
Check_2 = association(1, 1)
Checks = [Check_1, Check_2]

for i in range(len(Checks)):
    print("Клиент:", Clients[Checks[i].client_id].last_name, "Тариф:", Tarifs[Checks[i].tarif_id].name, "Сумма:", Clients[Checks[i].client_id].money ,"Процентная ставка:", Tarifs[Checks[i].tarif_id].percent, "%")

