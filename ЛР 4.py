
# coding: utf-8

# In[24]:


from pickle import dumps, load
import json
import csv

def __save_txt__():
    print("Put filename: ", end=' ')
    while True:
        filename = input()+".txt"
        deletechars='\/:*?"<>|'
        for c in deletechars:
            filename = filename.replace(c,'')
        if filename == ".txt":
            print("Please, rename file")
            continue
        break
    f = open(filename, 'wb')
    f.write(dumps(Structure))
    f.close()
    print("Saved as: ", filename)

def __open_txt__():
    print("Put filename: ", end=' ')
    filename = input()+".txt"
    f = open(filename, 'rb')
    data = load(f)
    f.close()
    return data

def __save_json__():
    print("Put filename: ", end=' ')
    while True:
        filename = input()+".json"
        deletechars='\/:*?"<>|'
        for c in deletechars:
            filename = filename.replace(c,'')
        if filename == ".json":
            print("Please, rename file")
            continue
        break
    f = open(filename, 'w')
    f.write(json.dumps(Structure))
    f.close()
    print("Saved as: ", filename)

def __open_json__():
    print("Put filename: ", end=' ')
    filename = input()+".json"
    f = open(filename, 'r')
    data = json.load(f)
    f.close()
    return data

def __save_csv__():
    print("Put filename: ", end=' ')
    while True:
        filename = input()+".csv"
        deletechars='\/:*?"<>|'
        for c in deletechars:
            filename = filename.replace(c,'')
        if filename == ".csv":
            print("Please, rename file")
            continue
        break
    with open(filename, mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(Structure[0])
        writer.writerow(Structure[1])
        writer.writerow(Structure[2])
    f.close()
    print("Saved as: ", filename)
    
def __open_csv__():
    print("Put filename: ", end=' ')
    filename = input()+".csv"
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
    f.close()
    #return data    

client_1 = {
    'id': 1,  # Уникальный идентификатор 
    'last_name': u'Петров',  # Фамилия
    'first_name': u'Петр',  # Имя
    'Patronymic': u'Петрович',
    'birth_date': '1990, 1, 1'  # Дата рождения
}

client_2 = {
    'id': 2,
    'last_name': u'Иванов',
    'first_name': u'Иван',
    'Patronymic': u'Иванович',
    'birth_date': '1990, 7, 5'
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

Structure = [clients, tarifs, marks]

for i in Structure[2]:
     for n in Structure[2][i]:
            print("Клиент:", Structure[0][n-1]['last_name'], "Тариф:", Structure[1][i-1]['name'], "Сумма:", Structure[2][i][n] ,"Процентная ставка:", Structure[1][i-1]['percent'], "%")

a = int(input())
in a == 1:
    __save_txt__()
if a == 2:
    __save_json__()
if a == 3:
    __save_csv__()
if a == 4:
    Structure[1][0]['name'] = 'Бред'
    Structure = __open_txt__()
if a == 5:
    Structure[1][0]['name'] = 'Бред'
    Structure == __open_json__()
if a == 6:
    Structure[1][0]['name'] = 'Бред'
    __open_csv__()
print(Structure[1][0]['name'])

