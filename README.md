Backend do Gerenciador de Tarefas para Equipes
Visão Geral
Este projeto é a implementação backend de um sistema de gerenciamento de tarefas para equipes, ideal para gestores ou líderes técnicos que precisam enviar tarefas para integrantes das equipes. Ele inclui um quadro Kanban para uma organização eficiente das tarefas.

Funcionalidades
Gerenciamento de Tarefas: Permite criar, atualizar, deletar e visualizar tarefas, além de atribuí-las a membros específicos da equipe.
Quadro Kanban: Facilita a organização das tarefas em diferentes estágios de progresso.
Gerenciamento de Equipes: Gerencia equipes, incluindo a atribuição de líderes e membros.
Gerenciamento de Usuários: Cuida das contas de usuários e autenticação.
Detalhes Técnicos
Framework: Django 4.2.6
Banco de Dados: MySQL
Autenticação: JWT com rest_framework_simplejwt
CORS: Habilitado para todas as origens
Docker: Utiliza docker-compose.yml para configuração e implantação.
Instalação
Clone o repositório:
bash
Copy code
git clone https://github.com/lucasfrotabarroso14/Task-Manager-Rpg-Back.git
Navegue até o diretório do projeto:
bash
Copy code
cd Task-Manager-Rpg-Back
Use Docker para configurar o ambiente:
bash
Copy code
docker-compose up
Endpoints da API
Tarefas: /tasks/ (GET, POST, PUT, DELETE)
Usuários: /users/ (GET, POST, PUT, DELETE)
Equipes: /teams/ (GET, POST, PUT, DELETE)
Frontend
O frontend deste projeto pode ser encontrado em: Task Manager RPG Frontend.
