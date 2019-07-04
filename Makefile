PORT=7000
CD=cd src &&


start:
	@echo "starting development server"
	$(CD) python3 manage.py runserver $(PORT)

install: 
	@echo "installing all dependencies"
	$(CD) pip install -r requirements.txt

migrate:
	@echo "migrating into the db"
	$(CD) python3 manage.py migrate

freeze:
	@echo "updating requirements.txt"
	$(CD) rm requirements.txt
	$(CD) pip freeze >> requirements.txt

migrations:
	@echo "creating migrations"
	$(CD) python3 manage.py makemigrations

action:
	@echo "executing command"
	$(CD) python3 manage.py $(ARGS)

