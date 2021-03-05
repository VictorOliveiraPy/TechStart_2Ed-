# OLIST

aplicativo para armazenar dados de vendedores, produtos, marketplaces e categorias.

## Como desenvolver ?

1. Clone o repositório.
2. Crie um virtualenv com python 3.8
3. Ative o virtualenv.
4. Instale as  depedencias.
5.Configure a instancia com o .env
6. Execute os testes.

````console
git clone https://github.com/VictorOliveiraPy/TechStart_2Ed-.git 
cd venv
python -m venv .venv
source .venv/bin/activate
pip install -r requirementes-dev.txt
cp contrib/env-sample .env
python manage.py test

````

## Como fazer o deploy ?
1. Crie um instancia  no heroku.
2. Envie as configuracoes para o heroku.
3. Define uma SECRET_KEY segura para instância.
4. Define DEBUG=False.
5. Configure o serviço de email.
6. Envie o código para o heroku

````console
heroku create minha instancia
heroko config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
git push heroku master --force

````
