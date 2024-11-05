# Napíšte skript, ktorý importuje modul math a vypočíta druhú odmocninu zo 64. Výsledok vytlačte na obrazovku.
# Použite funkciu sqrt. Vypíšte aj výsledok.

#Z modulu random importujte iba funkciu randint a použite ju na vygenerovanie náhodného celého čísla medzi 1 a 10.
# Výsledok vytlačte.

# Importujte modul datetime ako dt apoužite hona vytlačenie aktuálneho dátumu a času. Použite funkciu datetime.now()
#
# import math
# from random import randint
# import datetime as dt
#
# print(math.sqrt(64))
# print(randint(1,10))
# print(dt.datetime.now())
#


#
# Napíšte príkaz pip, ktorý nainštaluje balík requests.
# Po inštalácii balíka requests napíšte skript, ktorý ho importuje a pošle GET požiadavku na
# https://google.com. Vytlačte status kód odpovede.

import requests

print(requests.get("https://google.com"))