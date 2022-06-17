# django_basico

Este é um projeto básico para testar meus conhecimentos no framework django. Usei os seguintes conceitos: 
- Utilização do modelo MTV
- Criação de models (sqlite3)
- Visualização das models nos templates
- Uso de laços de repetição e estruturas condicionais nos templates
- Uso de arquivos estáticos e a sintaxe django-html

Fiz deploy da aplicação na heroku, porém, ocorre um erro de servidor (500) ao tentar acessar o link da página inicial. Tentarei resolver esse tipo de problema no próximo projeto.

- Link da aplicação: https://project-gbrmns.herokuapp.com (

Em localhost, este erro não ocorre.

1. Página de mangás

![2022-06-17 (1)](https://user-images.githubusercontent.com/82483656/174400707-3d6c6cf8-76a6-4d74-aaf7-d14e5956f15a.png)

Os nomes de mangás e autores são puxados do db (através da sintaxe django-html). Isso pode ser visto no arquivo "mangas.html" do repositório.

2. Página do mangá

![2022-06-17 (2)](https://user-images.githubusercontent.com/82483656/174401604-4839abb7-2893-41a1-883c-e563b3666aa6.png)

As informações desta página também são puxadas automaticamente do db, pode ser visto no arquivo "manga.html".

- Com isso, o django cria a estrutura para todas as informações, sem a necessidade de vários arquivos html!
