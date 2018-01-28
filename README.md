# Matik NoHa
Django projekt pre korešpondenčné semináre. Nočná hra na zimný Matik 2018.

## Požiadavky

 - Python (3 alebo vyšší, verzia 3.6.0 odporúčaná)
 - Django (verzia 2.0)
 - virtuálne prostredie

## Spustenie

Prvýkrát:
```cmd
manage.py makemigrations cmn
```
```cmd
manage.py migrate
```
a stále:
```cmd
manage.py runserver 0.0.0.0:PORT_NUMBER
```

## Prístup k aplikácii

Po tomto sa na admin stránku dostaneš ak do prehliadača zadáš `localhost:PORT_NUMBER/admin` a do aplikácie ak zadáš `localhost:PORT_NUMBER/pokemoni` (`localhost` môže byť nahradený IP adresou servera, napríklad `192.168.1.47`).
