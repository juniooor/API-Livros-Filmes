

# API de Filmes e Livros
Bem-vindo ao repositório da API de Filmes e Livros! Esta é uma API desenvolvida usando o Django Rest Framework para gerenciar informações sobre filmes e livros. A API permite a criação, listagem, atualização e exclusão de entradas de filmes e livros, além de oferecer recursos de busca e filtragem para ajudar os usuários a encontrar o conteúdo desejado.

## Recursos Principais
* **Modelos de Dados:** A API possui modelos bem definidos para representar filmes e livros, com campos detalhados para título, autor/diretor, gênero, ano de lançamento, avaliação e muito mais.

* **Operações de CRUD:** Através da API, você pode executar operações básicas de CRUD (Criar, Ler, Atualizar, Deletar) para adicionar novos filmes e livros, visualizar detalhes, atualizar informações e remover entradas.

* **Busca e Filtragem:** A API oferece recursos de busca e filtragem para ajudá-lo a encontrar rapidamente filmes ou livros específicos com base em critérios como título, gênero, autor/diretor e muito mais.

* **Autenticação e Autorização:** A segurança é uma prioridade. A API implementa autenticação de usuário, permitindo que apenas usuários autenticados executem operações de escrita (criação, atualização, exclusão).

## Como Usar
1. Clone este repositório para a sua máquina local.
2. Configure um ambiente virtual e instale as dependências usando pip install -r requirements.txt.
3. Execute as migrações do banco de dados com python manage.py migrate.
4. Crie um superusuário para acessar a interface administrativa com python manage.py createsuperuser.
5. Inicie o servidor de desenvolvimento com python manage.py runserver.
6. Acesse a interface administrativa em /admin/ para adicionar filmes e livros.
7. Use os endpoints da API em /api/filmes/ e /api/livros/ para interagir com a API.

## Tecnologias Utilizadas

* Django Rest Framework
* Django ORM
* SQLite (banco de dados de desenvolvimento)
## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues, propor melhorias ou enviar pull requests para tornar esta API ainda melhor.
