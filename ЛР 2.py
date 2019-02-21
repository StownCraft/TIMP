
# coding: utf-8

# In[36]:


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
Clients = [Client_1, Client_2]

def search_client_by_name(first_name, clients_list):
    for client in clients_list:
        if client.first_name == first_name:
            return client.last_name
    return None

def filtrate_clients_by_money(money, clients_list):
    result = []
    for client in clients_list:
        if client.money == money:
            result.append(client.first_name)
    return result

print(search_client_by_name(u'Толстой', Clients))
print(search_client_by_name(u'Иван', Clients))

fil = filtrate_clients_by_money(50000, Clients)
for i in range(len(fil)):
    print(fil[i])

