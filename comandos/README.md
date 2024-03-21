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
git remote add origin URL_DO_GIT

# Migrando a base de dados do Django
python manage.py makemigrations
python manage.py migrate

# Criando e modificando a senha de um super usuário Django
python manage.py createsuperuser
python manage.py changepassword USERNAME