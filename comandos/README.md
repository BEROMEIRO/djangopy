# Iniciando projeto Django
python -m venv venv (cria a pasta venv)
.\venv\Scripts\activate (ativa ambiente virtual)
pip install django (só precisa disso no começo)
django-admin startproject project . (método para criar seu projeto inicial)
python manage.py startapp contact

# Configurar o git
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main

# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git push
git remote add origin URL_DO_GIT

# Migrando a base de dados do Django
python manage.py makemigrations
python manage.py migrate

# Criando e modificando a senha de um super usuário Django
python manage.py createsuperuser
python manage.py changepassword USERNAME

# Django Shell
python manage.py shell

# Trabalhando com o model do Django

# Importe o módulo
from contact.models import Contact
# Cria um contato (Lazy)
# Retorna o contato
contact = Contact(**fields)
contact.save()
# Cria um contato (Não lazy)
# Retorna o contato
contact = Contact.objects.create(**fields)
# Seleciona um contato com id 5
# Retorna o contato
contact = Contact.objects.get(pk=5)
# Edita um contato
# Retorna o contato
contact.field_name1 = 'Novo valor 1'
contact.field_name2 = 'Novo valor 2'
contact.save()
# Apaga um contato
# Depende da base de dados, geralmente retorna o número
# de valores manipulados na base de dados
contact.delete()
# Seleciona todos os contatos ordenando por id DESC
# Retorna QuerySet[]
contacts = Contact.objects.all().order_by('-id')
# Seleciona contatos usando filtros
# Retorna QuerySet[]
contacts = Contact.objects.filter(**filters).order_by('-id')
print(contacts)

