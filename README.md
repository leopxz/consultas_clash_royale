# Clash Royale Battle Analysis 

## Descrição
Esta aplicação web permite aos usuários realizar consultas sobre o desempenho de cartas e decks no jogo Clash Royale. Utilizando o Flask e MongoDB, a aplicação fornece informações sobre a porcentagem de vitórias e derrotas, decks vitoriosos e muito mais.

## Funcionalidades
- **Porcentagem de Vitórias/Derrotas de uma Carta**: Permite consultar a taxa de vitórias e derrotas de uma carta específica dentro de um intervalo de datas.
- **Decks com Mais de X% de Vitórias**: Lista os decks que obtiveram uma taxa de vitórias superior a um percentual definido pelo usuário.
- **Consultas sobre Combos de Cartas**: Oferece a possibilidade de consultar a quantidade de derrotas ao utilizar um conjunto de cartas.

## Tecnologias Utilizadas
- **Flask**: Framework web em Python para construção da aplicação.
- **MongoDB**: Banco de dados NoSQL utilizado para armazenar os dados de partidas.
- **HTML/CSS**: Tecnologias para criação da interface do usuário.

## Instalação
Clone o repositório:
```
git clone https://github.com/leopxz/consultas_clash_royale
```
Navegue até o diretório do projeto:
```
cd consultas_clash_royale
```
Instale as dependências:
```
pip install -r requirements.txt
pip install Flask pymongo
```
Configure a conexão com o MongoDB: Substitua a string de conexão no código pela sua própria string de conexão.

## Execução
Inicie o servidor Flask:
```
python app.py
```
Acesse a API no navegador:
```
http://127.0.0.1:5000
```

## Endpoints

GET /porcentagem_vitorias_derrotas: Retorna a porcentagem de vitórias e derrotas de uma carta.

### Parâmetros:
carta: ID da carta.
inicio: Data de início (formato YYYY-MM-DD).
fim: Data de fim (formato YYYY-MM-DD).
GET /decks_vitoriosos: Lista os decks que obtiveram mais de X% de vitórias.

### Parâmetros:
porcentagem: Porcentagem mínima de vitórias.
inicio: Data de início (formato YYYY-MM-DD).
fim: Data de fim (formato YYYY-MM-DD).

## Estrutura do Projeto
<br>
/projeto_flask_clash<br>
│<br>
├── app.py                # Código principal da aplicação<br>
├── templates/            # Diretório contendo os templates HTML<br>
│   ├── index.html        # Página inicial com formulários de consulta<br>
│   └── porcentagem_vitorias_derrotas.html # Página de resultados de vitórias<br>
└── static/               # Diretório para arquivos estáticos (CSS, imagens, etc.)<br>
    └──css/<br>
│   ├── style.css         # Diretório contendo a estética da aplicação. <br>
