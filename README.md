# Ekko WIP
Intern SMS-tjeneste for IT-Hjelp
Utviklet slik at vaktledere/fagansvarlige på USIT IT-hjelp enkelt kan sende felles SMS til alle på IT-hjelp avdelingen


## Hvordan kjøre prosjektet lokalt

1. Klon repoet/last ned ZIP
```bash
git clone https://github.uio.no/kevil/Ekko.git
cd ekko
```

2. Opprett og aktiver et virtuelt miljø
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate
```

3. Installer avhengigheter
```bash
pip install -r requirements.txt
```

4. Kjør migrasjoner
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Start serveren
```bash
python manage.py runserver
```

Åpne `http://127.0.0.1:8000` i nettleseren (evt. hvor enn du velger å hoste den)
