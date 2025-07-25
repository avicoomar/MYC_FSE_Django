**DB Setup notes for Testing/Development:**
1. config/fixtures/initial_data.json is intended to be used to populate the db used in test/dev environment with the production db's data
2. Only auth app's data is crucial for Django's authentication/authorization to function properly. Rest of the data is either created automatically by Django or not required for test/dev.
3. To replicate the production's data at any given time, run:
   ```bash
   python manage.py dumpdata \
   auth \
   --natural-foreign \
   --natural-primary \
   --database=mysql_db \
   --settings=config.settings_prod \
   --indent=2 \
   > config/fixtures/initial_data.json
   ```
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Testing:

After DB setup, run either:  
```bash
python manage.py test --settings=config.settings_test
```
OR 
```bash
python manage.py migrate --settings=config.settings_test  
python manage.py loaddata config/fixtures/initial_data.json --settings=config.settings_test  
python manage.py test --settings=config.settings_test
```

------------------------------------------------------------------------------------------------------

## Development:

Perform DB setup as described above if needed, then run:  
```bash
python manage.py makemigrations  
python manage.py migrate --database=mysql_db  
python manage.py migrate --database=sqlite_db #optional  
python manage.py loaddata config/fixtures/initial_data.json #warning - run only when dev db is different from prod db  
python manage.py [command]
```
If needed, insert an admin user too using this command:  
```bash
python manage.py shell -c "MyUser.objects.create_superuser(username='admin', password='admin', role='ADMIN', phone_no='123')"
```

------------------------------------------------------------------------------------------------------

## Production(tentative):
```bash
python manage.py makemigrations --settings=config.settings_prod #optional  
python manage.py migrate --database=mysql_db --settings=config.settings_prod  
python manage.py migrate --database=sqlite_db --settings=config.settings_prod #optional  
uvicorn config.asgi:application --host 0.0.0.0 --port 8000
```
