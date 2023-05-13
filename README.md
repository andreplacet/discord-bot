# Alpha-BOT

AlphaBot é uma iniciativa particular, no momento é um bot que recolhe informações de jogos e devolve baseada em comandos disponibilizados no discord

---

Jogos suportados

* League of Legends

---

Arquivo requirements para instalação da dependencias do projeto

> requirements.txt

**É aconselhavel o uso e virtual envoirements e executar comando**

`pip install -r requirements.txt`

---

É necessario criar um arquivo .env para configuração do bot com suas credencias do Discord, League of Legends API e OpenAPI para uso das integrações com esses serviços, caso opte por não utlizar algum, lembre-se de desabilitar esses comandos no bot.

variaveis necessarias no arquivo .env

```python
DISCORD_SECRET = '<suas credenciais aqui>'

OPEN_API_KEY = '<suas credenciais aqui>'
RIOT_API_KEY = '<suas credenciais aqui>'

SPOTIFY_CLIENT_ID = '<suas credenciais aqui>'
SPOTIFY_CLIENT_SECRET = '<suas credenciais aqui>'

```

a função do Spotify ainda não esta disponivel no momento.

---

Para rodar o bot de maneira local uso o comando `python main.py`

Lembrando que voce precisa criar sua conta [Discord Developer Portal](https://discord.com/developers)


##### **League of Legends**

* [X] Implementação de consulta do perfil de um invocador
* [ ] Resultado da ultima partida pelo nome de invocador
* [ ] Dados do ultimo patch notes
* [ ] Curiosidades sobre um campeão
* [ ] Dados resumidos dos status de um campeão
* [ ] Dados de nerf e buff do ultimo patch por campeao


##### Open API

* [ ] Implementação de perguntas para o ChatGPT
* [ ] Implementação de resposta por voz de uma resposta obtida do ChatGPT
