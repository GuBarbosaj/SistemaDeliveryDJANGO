# Sistema de delivery - DJANGO

Aplicação de delivery desenvolvida durante a Imersão Python, utilizando o framework Django.

# Detalhes

Nesta aplicação, pelo lado do administrador, é possível realizar o cadastro e gerenciamento de produtos e pedidos, além de ser possível cadastrar outros administradores com funções específicas de acordo com a problemática. Já pelo lado do cliente, é possível escolher produtos e adiciona-los ao carrinho, ao fim confirmar o pedido através do preenchimento de um formulário com informações sobre o endereço de entrega e forma de pagamento.

Durante a imersão foi ensinado conceitos básicos sobre o funcionamento e arquitetura do framework Django, como por exemplo, o seu o padrão model-template-view. Além de utilizar o ORM do Django que possibilita a construções especiais de abstração que podem ser usadas para criar consultas complexas ao banco de dados.

# Execução

Para executar o projeto a partir da linha de comando, vá para a pasta root do projeto e execute o comando:

```bash
python manage.py runserver
```

Depois basta acessar o endereço que será exibido no terminal. 

Para acessar a pagina de administrador utilize o caminho (/admin). 

A criação de um super usuario segue o padrão do framework DJANGO.

```bash
python3 manage.py createsuperuser
```

# Observaçao

Para o funcionamento da aplicação é necessario que todas as bibliotecas utilizadas no mesmo estejam instaladas na maquína. A fim de testes, recomendo a utilização de um VENV.
