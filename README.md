#Compartilhamentos

#Instalar requerimentos (Django>=2.2,<2.3): 
pip install -r requirements.txt

#Criar o banco de dados:
python manage.py migrate

#Indexar as pastas estaticas:
python manage.py collectstatic

#Rodar Servidor:
python manage.py runserver

#Acessar com:
http://localhost:8000/
