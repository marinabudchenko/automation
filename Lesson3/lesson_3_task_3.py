from address import Address
from mailing import Mailing

to_address = Address("11111", "Ростов-на-Дону", "Ткачева", "12", "55")
from_address = Address("22222", "Москва", "Московская", "8", "7")
mailing = Mailing(to_address, from_address, 300, "LOL777")

print(f"Отправление {mailing.track} из {mailing.from_address.index},{mailing.from_address.city},"
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} " 
      f" в{mailing.to_address.index}, {mailing.to_address.city},{mailing.to_address.street}, " 
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")   

                                 