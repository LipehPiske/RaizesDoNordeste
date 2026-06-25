# RaizesDoNordeste
# Sobre o Projeto

Este projeto foi desenvolvido para a disciplina Projeto: Engenharia de Software, com foco em Qualidade de Software(QA), do Centro Universitário Internacional Uninter.

O sistema simula o funcionamento de uma rede de restaurantes chamada Raízes do Nordeste, permitindo realizar pedidos, consultar o cardápio, simular pagamentos, acompanhar o andamento dos pedidos e gerenciar informações de estoque e funcionários. O principal objetivo é avaliar a qualidade do sistema, verificando seu funcionamento, desempenho, segurança e capacidade de atender diversos usuários simultaneamente.

# Funcionalidades do Sistema

O sistema oferece as seguintes funcionalidades:

* Realização de pedidos;
* Consulta ao cardápio;
* Cancelamento de pedidos;
* Simulação de pagamentos;
* Controle básico de estoque;
* Login para clientes e administradores;
* Geração de relatórios de estoque e funcionários.

# Tecnologias Utilizadas

As principais ferramentas utilizadas no desenvolvimento e nos testes foram:

* Python: linguagem principal do projeto;
* Flask: utilizado para desenvolver a aplicação e suas APIs;
* Locust: empregado nos testes de carga, simulando múltiplos usuários acessando o sistema simultaneamente;
* OWASPZAP: utilizado para testes de segurança;
* GitHub: plataforma para armazenamento e controle de versão do código-fonte.

# Estrutura do Projeto

Os principais arquivos do sistema são:

* main.py: arquivo responsável por iniciar a aplicação;
* app_flask.py: implementação das APIs do sistema;
* telas.py: organização das telas e menus;
* dados_sistema.py: armazenamento dos dados utilizados pela aplicação;
* locustfile.py: configuração dos testes de carga e estresse.

# Testes Realizados

Durante o desenvolvimento foram executados diversos testes, incluindo:

* Validação do login com credenciais válidas e inválidas;
* Testes de pedidos com estoque disponível e indisponível;
* Testes de geração de relatórios;
* Testes completos do fluxo de pedidos;
* Simulação de até 500 usuários acessando o sistema ao mesmo tempo;
* Testes de segurança;
* Testes de desempenho, carga e tempo de resposta.

# Critérios Avaliados

Os testes verificaram se o sistema atende aos seguintes requisitos:

* Tempo de resposta entre 1 e 2 segundos;
* Disponibilidade mínima de 99,5%;
* Taxa de falhas inferior a 2%;
* Capacidade de suportar grande quantidade de usuários simultâneos;
* Conformidade com os princípios da Lei Geral de Proteção de Dados (LGPD).

# Segurança

Em relação à segurança, o sistema foi projetado seguindo boas práticas para proteção das informações dos usuários. Entre os principais aspectos avaliados estão:

* Proteção dos dados pessoais;
* Tratamento adequado de informações sensíveis;
* Testes de vulnerabilidade utilizando ferramentas específicas;
* Medidas para reduzir riscos de vazamento de dados;
* Adequação aos princípios estabelecidos pela LGPD.

# Como Executar o Projeto

Para executar o sistema, siga os passos abaixo:

1. Instale o Python em seu computador;
2. Instale as bibliotecas necessárias, como Flask e Locust;
3. Abra o terminal na pasta onde o projeto está armazenado;
4. Execute o comando:

python main.py
