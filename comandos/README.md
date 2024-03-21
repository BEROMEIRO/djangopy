Iniciar o projeto Django

Iniciando projeto Django
python -m venv venv (cria a pasta venv)
.\venv\Scripts\activate (ativa ambiente virtual)
pip install django (só precisa disso no começo)
django-admin startproject project . (método para criar seu projeto inicial)

Configurar o git

git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT