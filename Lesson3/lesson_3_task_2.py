from smartphone import Smartphone

catalog = []
#Пять разных экземпляров класса Smartphone
phone1 = Smartphone("Apple", "iPhone 8+", "89996978947")
phone2 = Smartphone("Infinix", "SMART 8", "89507664749")
phone3 = Smartphone("Tecno", "SPARK GO", "89081234561")
phone4 = Smartphone("HUAWEI", "nova Y61", "89071234567")
phone5 = Smartphone("Samsung", "Galaxy A14", "89087654323")

#Добавить каждый экземпляр в список catalog
catalog.append(phone1)
catalog.append(phone2)   
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print (f"{phone.brand} - {phone.model}. {phone.phone_number}")