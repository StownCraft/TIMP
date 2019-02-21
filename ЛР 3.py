
# coding: utf-8

# In[17]:


from datetime import datetime, date

class Client():
    def __init__(self, id=1,  last_name = "Петров", first_name = "Петр", patronymic = "Петрович", birth_date = date(1990, 1, 1), money = 4000000):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.birth_date = birth_date
        self.money = money

Client_1 = Client()
Client_2 = Client(2, "Иванов", "Иван", "Иванович", date(1990, 7, 5), 50000) 
Client_3 = Client(2, "Семенов", "Семен", "Семенович", date(1990, 7, 5), 50000) 
Client_4 = Client(2, "Волков", "Анатолий", "Александрович", date(1990, 7, 5), 50000) 
Client_5 = Client(2, "Иванов", "Иван", "Иванович", date(1990, 7, 5), 50000) 
Clients = [Client_1, Client_2, Client_3, Client_4, Client_5]

def sort_client_by_name(clients_list):
    data = sorted(clients_list, key=lambda d: d.first_name)
    for i in range(len(data)):
        data[i]=data[i].first_name
    return data
print(sort_client_by_name(Clients))

