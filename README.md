
# ⬛👽 Whois Alien Discord Bot

![0625](https://github.com/cristopherrissardi/Whois-Alien-Bot/assets/93612872/878cc6c7-64ae-4b98-9552-62ecfe4f68d0)


O Bot Whois Alien foi desenvolvido para suceder outros bots já criados, como o [Alien.py](https://github.com/cristopherrissardi/Alien.py) e o [Al Capone](https://github.com/cristopherrissardi/Al-Capone-Bot). Atualmente, o projeto está ativo exclusivamente no servidor [House's Alien](https://discord.gg/nHgHJtg3re).

O principal objetivo deste projeto é semelhante aos anteriores: permitir a consulta de dados através de comandos enviados ao Bot. Em novembro de 2023, o projeto já suportava consultas de nome, CPF e outros dados pessoais. Até onde se sabe, o Whois Alien foi o primeiro bot no Discord dedicado à consulta de dados.

Além das funcionalidades mencionadas, o Bot Whois Alien se destaca por sua capacidade de realizar análises detalhadas de segurança, como varreduras de portas e traceroute, que são úteis para identificar vulnerabilidades em sistemas. Essas ferramentas não apenas ampliam o escopo de utilidade do bot, mas também o posicionam como uma ferramenta versátil para administradores de sistemas e entusiastas de segurança cibernética dentro do Discord.


# Termos de uso e responsabilidades

Dentro do nosso bot temos uma opção dedicada dos termos de uso e responsabilidades dos usuários para com o nosso servidor, nosso objetivo desde o início é possuir um bot próprio/único e totalmente autônomo dentro de nosso ambiente. Com a criação do parâmetro citado, é possível observar que nos importamos com a nossa comunidade e visamos obter um local limpo, integro e com regras passiva/ativa a serem seguidas. 

Usando o comando `./termos`, é possível visualizar os termos propagados por nós, para que tenhamos um controle mais absoluto em relação as nossas informações. 

Vale ressaltar que constantemente estamos pensando em novos termos e responsabilidades para serem atualizados. Futuramente será implementado novas políticas de uso, de tal forma que não prejudique os usuários, muito menos vise prejudicar entidades públicas/privadas a qual parte interessarem. 


---

# Direitos reservados


É fundamental ressaltar que nosso projeto foi construído totalmente do zero, sendo em ideias, funcionalidades, ferramentas e outras objeções. Dedicamos tempo, esforço e inúmeros testes, tivemos que lidar com vários erros, bugs, problemas de código, problemas de API, falhas em consumir dados externos e outros vários fatores que quase impossibilitaram a criação do mesmo, mas com muita dedicação chegamos em um resultado extremamente positivo.

Ficamos genuinamente satisfeitos em saber que nosso projeto pode servir como fonte de inspiração para outros desenvolvedores que desejam explorar e expandir o universo dos bots. No entanto, é de extrema importância para nós que qualquer uso do nosso projeto como base seja conduzido com integridade e respeito. Pedimos gentilmente que os interessados evitem copiar, plagiar ou depreciar de qualquer forma o trabalho que dedicamos com tanto empenho e dedicação.

Acreditamos firmemente na importância de um desenvolvimento ético e responsável. Encorajamos que novos projetos sejam construídos com originalidade, respeitando os direitos de propriedade intelectual e reconhecendo a fonte de inspiração quando apropriado. 


---

# Comandos e Funcionalidades do Bot

Abaixo será disponibilizado a lista de todos os comandos e suas funcionalidades. Para visualizar a opção mais resumida do código, basta digitar dentro do servidor `./ajuda` e o bot irá retornar todas as opções disponíveis.

---
### 🔐 Moderação: 

O Bot possui comandos administrativos, com a opção `./admin` é possível visualizar todos os comandos de moderação. Vale ressaltar que apenas pessoas autorizadas tem a permissão de usar os comandos de moderação. 

Comandos de moderação:

- ⭕ `./kick` - Comando para expulsar algum usuário do servidor.
- ⛔ `./ban` - Comando para banir pessoas do servidor.
- 🟢 `./unban` - Desbane pessoas do servidor.
- 🔇 `./mute` - Muta (desabilita o microfone) do usuário em questão.
- 🔊 `./unmute` - Desmuta (reativa o microfone) do usuário.
- ⚜️ `./role` - Atribui cargo a um usuário. [BUGADO]
- ❌ `./clear` - Limpa as mensagens do canal em específico.

#### 📜 Manual dos comandos de moderação

- ⭕ `./kick` - Deve ser precedido do @user da pessoa que deseja expulsar
	Exemplo: `./kick` @joaozinho#1234

- ⛔ `./ban` - Deve ser precedido do @user da pessoa que deseja expulsar.
	Exemplo: `./ban` @joaozinho#1234

- 🟢 `./unban` - Deve ser precedido do @user da pessoa que deseja mutar.
	Exemplo:  `./unban` @joaozinho#1234

- 🔇 `./mute` - Deve conter o @user da pessoa que deseja desmutar.
	Exemplo: `./mute` @joaozinho#1234

- 🔊 `./unmute` - Deve ser inserido junto ao @user da pessoa que deseja desmutar.
	Exemplo: `./unmute` @joaozinho#1234

- ⚜️ `./role` - Deve preceder o @user da pessoa + Menção do cargo ou ID do cargo
	Exemplo: `./role` @joaozinho#1234 @admin
	OBS: Esse parâmetro ainda tá um pouco bugado, seja corrigido em breve

- ❌ `./clear` - Deve ser inserido o parâmetro + número de mensagens a excluir.
	Exemplo: `./clear` 30


---
### 🛠️ Ferramentas Avançadas

As ferramentas avançadas são ferramentas voltadas para pessoas um pouco mais experientes. No momento, possui apenas 3 ferramentas avançadas. É possível visualizar passando o parâmetro `./ferramentas` dentro do servidor e será retornado as opções disponíveis.

Comando das ferramentas avançadas:

- 🚀 `./portscan` - Comando para escanear portas em um determinado host. 
- 🛰️ `./traceroute` - Comando para traçar a rota do host em questão.
- 🛩️ `./maclookup` - Comando para resolver endereços MAC, localizando fabricante e outras informações adicionais.

#### 📜 Manual dos comandos das ferramentas avançadas

- 🚀 `./portscan` - Deve ser precedido do endereço IP/host do alvo.
	Exemplo: `./portscan` www.google.com

- 🛰️ `./traceroute` - Deve ser precedido do endereço IP/host do alvo.
	Exemplo: `./traceroute` www.google.com

- 🛩️ `./maclookup` - Deve ser precedido do MAC Address do alvo.
	Exemplo: `./maclookup` E1:48:3A:6E:11:36

OBS: As opções de `./portscan` e `./traceroute` podem ser utilizadas passando o endereço IP ou o domínio/URL, não tem problema!


---
### 🧭 Consulta de Dados

As consultas de dados consistem em retornar dados pessoais de grande parte da população Brasileira. Usando o parâmetro ./consultas será retornado todas as consultas disponíveis no bot. 


Consultas de dados pessoais disponíveis:

- 🕵️ `./nome` - Consulta dados pessoais através do nome.
- 👽 `./cpf` - Consulta dados pessoais através do cpf. (Retorna todos os dados possíveis)
- 📞 `./telefone` - Consulta de dados por telefone. (Retorna dados do titular da linha)
- ☎️ `./fixo` - Consulta de dados por telefone fixo. 
- 🙋‍♀️ `./mae` - Consulta de filhos através do nome da mãe. 
- 🙋‍♂️ `./pai` - Consulta de filhos através do nome da pai. 
- 📭 `./email` - Consulta de dados através do e-mail. (Retorna os dados pessoais pelo e-mail)
- 📌 `./cep_pessoas` - Consulta de dados pessoais de todos os moradores da rua.
- 🚘 **`./placa` - NÃO IMPLEMENTADA! (Por falta de API, não foi implementada essa consulta)**

Outras consultas:

- 🏗️ `./cnpj` - Busca de informações através do número do CNPJ. 
- 🧩 `./ip` - Comando para realizar consulta de IP. 
- 💳 `./bin` - Comando para consultar as informações de cartão de crédito pela BIN. 
- 📮 `./cep` - Comando para a consulta de um determinado CEP de rua.
- 🔬 `./covid` - Mostra os casos de covid19 e mortes de cada estado.
- 🏛️ `./banco` - Retorna qual é o banco através do dígito bancário
- 📐 `./site` -  Igual ao comando de IP, porém para sites.
- 🏟️ `./operadora` - Verifica qual operadora e qual região é um determinado número de telefone.
- 🌐 `./emailinfo` - Faz a verificação de qual provedor de e-mail está sendo usado e outras informações.


#### 📜 Manual dos comandos das consultas

Consultas de dados pessoais:

- 🕵️ `./nome` -  Deve ser precedido junto ao nome completo da pessoa que deseja consultar.
	Exemplo: `./nome` Jair Messias Bolsonaro
	OBS: Se atente para colocar sempre o nome completo da pessoa!

- 👽 `./cpf` -  Deve ser incluído junto ao CPF da pessoa.
	Exemplo: `./cpf` 45317828791
	OBS: Não estranhe caso o CPF não seja retornado, nem todo mundo teve dados vazados!

- 📞 `./telefone` - Precisa ser incluído parâmetro junto ao número de telefone.
	Exemplo: `./telefone` 11987654321
	OBS: Lembre-se sempre de colocar nesse formato acima (DDD + 9 + número). Nunca utilize +DDI e sim somente o DDD, digito verificador (9) e o número de telefone. 

- ☎️ `./fixo` - Precisa ser incluído parâmetro junto ao número de telefone fixo.
	Exemplo: `./fixo` 1133355555
	OBS: Lembre-se sempre de colocar nesse formato acima (DDD + número). Nunca utilize +DDI e sim somente o DDD e o número de telefone fixo. 

- 🙋‍♀️ `./mae` - Digite o parâmetro e insira o nome completo da mãe que deseja procurar.
	Exemplo: `./mae` Olinda Bonturi Bolsonaro
	OBS: Atente-se em colocar o nome completo da mãe para que seja mais fácil encontrar os filhos.
	OBS 2: Evite procurar com nomes "comuns" pois irá retornar milhares de filhos. 

- 🙋‍♂️ `./pai` - Digite o parâmetro e insira o nome completo do pai que deseja procurar.
	Exemplo: `./pai` Jair Messias Bolsonaro
	OBS: Atente-se em colocar o nome completo do pai para que seja mais fácil encontrar os filhos.
	OBS 2: Evite procurar com nomes "comuns" pois irá retornar milhares de filhos. 

📭 `./email` - Insira o comando precedido do endereço de e-mail que deseja consultar.
	 Exemplo: `./email` lula@gmail.com
	 OBS: A consulta de dados por e-mail é extremamente difícil, porém não é impossível! Raramente irá retornar algo.

📌 `./cep_pessoas` - Insira o comando junto com o CEP que deseja ver os moradores.
	 Exemplo: `./cep_pessoas` 01153000
	 OBS: Evite esse tipo de consulta para CEPs com milhares de habitantes. Irá demorar muito para retornar todos os moradores.


Outras consultas:

- 🏗️ `./cnpj` - Insira o comando precedido do número do CNPJ desejado.
	Exemplo: `./cnpj` 00.000.000/0001-91

- 🧩 `./ip` - Digite o comando precedido do número de IP desejado.
	Exemplo: `./ip` 8.8.8.8

- 💳 `./bin` - Digite o comando precedido do número da BIN desejada. (BIN = 6 primeiros dígitos do cartão)
	Exemplo: `./bin` 512372

- 📮 `./cep` - Insira o comando + CEP da rua.
	Exemplo: `./cep` 01153000

- 🔬 `./covid` - Digite o comando e a sigla do estado que deseja verificar os casos de covid19
	Exemplo: `./covid` SP
	OBS: Caso tenha alguma dúvida, digite o comando `./covid` e irá retornar as siglas dos estados.

- 🏛️ `./banco` - Digite o número do banco para verificar a qual instituição pertence.
	Exemplo: `./banco` 01

- 📐 `./site` -  Digite o comando precedido do número de IP do site ou a URL.
	Exemplo: `./site` www.google.com

- 🏟️ `./operadora` - Digite o comando precedido com o número de telefone no formato internacional
	Exemplo: `./operadora` +5511987654321
	OBS: Nesse caso deve ser usado no formato que está acima, formato internacional. Essa opção verifica todas as operadoras do mundo e não limita-se apenas ao brasil.

- 🌐 `./emailinfo` - Digite o comando precedido do endereço de e-mail
	Exemplo: `./emailinfo` your_email@exemple.com


---

### ⚙️ Geradores

A opção de geradores tem como objetivo ajudar os usuários do Bot a gerarem dados, basta digitar `./gerador` e o bot irá retornar todas as opções de geradores disponíveis. 

⚠️ **Disclaimer**: Vale ressaltar que todos os dados gerados pela nossa ferramenta são fictícios e não tem nenhuma objeção de prejudicar quaisquer órgãos que assim forem, muito menos beneficiar com atos ilícitos usuários do Projeto Whois Alien. Existe a possibilidade de algum dado gerado ser verdadeiro porém qualquer dado gerado pela nossa ferramenta que tenha teor verídico, será mera e total coincidência. 


Geradores disponíveis:

- 👥 `./gerarpessoa` - Gera dados de uma pessoa
- 💳 `./gerarcartao` - Gera cartão, seja ele débito ou crédito
- 🗂️ `./geraremail` - Gera um e-mail aleatório [OFFLINE]
- 🔅 `./gerarcpf` - Gera um CPF aleatório (Possível chance de ser verdadeiro)
- 🎮 `./gerarusr` - Gera um username aleatório [OFFLINE]
- 🔐 `./gerarsenha` - Gera uma senha forte e aleatória.
- 🚗 `./gerarveiculo` - Gera os dados de um veículo aleatório. [OFFLINE]
- 📞 `./gerartel` - Gera um número de telefone aleatório [OFFLINE]
- 📡 `./gerarimei` - Gera um número de IMEI aleatório [OFFLINE]

Observação: Alguns dos geradores estão offline para que possam ser feitos as devidas manutenções nas APIs.


#### 📜 Manual dos comandos de geradores


- 👥 `./gerarpessoa` - Insira apenas o comando
	Exemplo: `./gerarpessoa`

- 💳 `./gerarcartao` - Insira apenas o comando
	Exemplo: `./gerarcartao`

- 🗂️ `./geraremail` - Insira apenas o comando
	Exemplo: `./geraremail`

- 🔅 `./gerarcpf` - Insira apenas o comando
	Exemplo: `./gerarcpf`

- 🎮 `./gerarusr` - Insira apenas o comando
	Exemplo: `./gerarusr`

- 🔐 `./gerarsenha` -  Insira apenas o comando
	Exemplo: `./gerarsenha`

- 🚗 `./gerarveiculo` - Insira apenas o comando
	Exemplo: `./gerarveiculo

- 📞 `./gerartel` - Insira apenas o comando
	Exemplo: `./gerartel`

- 📡 `./gerarimei` - Insira apenas o comando
	Exemplo: `./gerarimei`

Para todos os comandos de geração de informações será a mesma coisa. Digite apenas o parâmetro!
Futuramente será implementado corrigido e implementado mais opções de geradores! 


---

### 🎵 Músicas [Ainda não implementado]

Os comandos de música ainda não foram implementados, atualmente se encontra em versão de testes! 

Preview dos comando implementados em breve:

- ⏩ `./play` - Comando para reproduzir a música
- ⏺️ `./stop` - Comando para parar a música
- ⏸️ `./pause` - Comando para pausar a música no minuto em que ela estava
- 🔁 `./resume` - Comando para reproduzir a música no minuto que ela estava
- ⏪ `./back` - Comando para voltar a música
- ⏭️ `./skip` - Comando para pular música
- ❌`./disconnect` - Comando para desconectar o bot de música

---

### 🪐 Informações

Está aba é dedicada a mostrar os comandos de informações dentro do bot. Digite `./info` para ver as informações adicionais.

Comandos disponíveis:

- 🚀 `./ajuda` - Retorna uma página de ajuda mostrando todos os comandos do bot.
- 🛰️ `./ping` - Mostra o ping do usuário e o ping do usuário em relação ao servidor do discord.
- ⚓ `./serverinfo` - Mostra as opções do servidor. (Ainda em implementação).
- 🎠 `./userinfo` - Mostra informações do usuário. (Ainda em implementação).

Os critérios de uso são apenas os comandos isolados, não é necessário nenhum complemento, então é somente digitar os comandos acima.


---

### 🎓 Diversos

A aba diversos mostra os comandos diversos do Bot, sem alguma classificação especial. Digitando a opção ``./diversos``, é possível ver a lista de comandos diversos.

Lista de comandos:

- 💰 `./cotacao` - Mostra a cotação das moedas desejadas em relação uma entre outra.
- 🏟️ `./ddd` - Mostra todas as cidades em relação ao DDD desejado.
- 💼 `./feriados` - Mostra os feriados de cada ano.


#### 📜 Manual dos comandos diversos

- 💰 `./cotacao` - Insira o comando + par de moedas que deseja converter
	Exemplo: `./cotacao` EUR-BRL
	Lembre-se de colocar nesse formato igual está acima MOEDA1-MOEDA2

- 🏟️ `./ddd` - Insira o comando e o DDD que desejar.
	Exemplo: `./cotacao` 47

- 💼 `./feriados` - Insira o comando e o ano que deseja verificar os feriados.
	Exemplo: `./feriados` 2025



---

### 🉐 Tradutor 

Dedicado a explicar como funciona o tradutor do bot. Use o comando `./tradutor` e será exibido a forma que traduz o texto. 

Comando para traduzir:

- 🉐 `./traduzir` - Insira o comando + sigla do idioma que deseja traduzir + texto
	Exemplo: `./traduzir` pt Hello friend, you are very beautiful! I'm Alien!


---

### 🌐 Inteligência artificial [BETA]


O bot ainda esta em sua primeira versão, por isso a opção de inteligência artificial está sendo desenvolvida, porém já é possível ter uma ideia das funções que estarão por vir. Digite o comando `./ia` e será retornado as opções disponíveis. 

O comando `./projectovnia` será exibido a opção da inteligência artificial própria do Whois Alien. 

Já foram implementados as APIs das outras IA, como GPT4 e Gemini-Pro, porém ainda necessita de alguns ajustes para corrigir bugs e arrumar algumas funcionalidades.


---

# 📊 Fontes de dados

Abaixo, estou disponibilizando todos os locais e fontes de onde estão sendo retiradas as informações.

| APIS                        | Local                                                             |
| --------------------------- | ----------------------------------------------------------------- |
|                             |                                                                   |
| Todas as consultas de dados | Minhas próprias APIs                                              |
| IP Lookup                   | [IPWHOIS](https://ipwhois.io/)                                    |
| Card BIN API                | [Lookup Bin List](https://lookup.binlist.net/)                    |
| CEP by viacep               | [Viacep](https://viacep.com.br/)                                  |
| covid19 API                 | [Covid19 Brazil API](https://covid19-brazil-api-docs.vercel.app/) |
| Bank API                    | [BrasilAPI](https://brasilapi.com.br/docs#tag/BANKS)              |
| Website lookup API          | [IPWHOIS](https://ipwhois.io/)                                    |
| API consulta de operadora   | [APILayer](https://apilayer.com/)                                 |
| API consulta de e-mail      | [APILayer](https://apilayer.com/)                                 |
| API consulta de CNPJ        | [HYB](https://hyb.com.br/)                                        |
| Maclookup                   | [WhoisXMLapi](https://mac-address.whoisxmlapi.com/)               |
| ReverseIP                   | [ViewDNS.info](https://viewdns.info/api/)                         |
| Traceroute                  | [ViewDNS.info](https://viewdns.info/api/)                         |
| Portscan                    | [ViewDNS.info](https://viewdns.info/api/)                         |
| Cotação entre moedas        | [AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas)        |
| Cidades por DDD             | [BrasilAPI](https://brasilapi.com.br/docs#tag/DDD)                |
| Feriados                    | [Invertexto](https://api.invertexto.com/)                         |
| Gerador de pessoas          | [Invertexto](https://api.invertexto.com/)                         |
| Gerador de cartão           | [Invertexto](https://api.invertexto.com/)                         |
| Gerador de CPF              | [Invertexto](https://api.invertexto.com/)                         |
| Tradutor                    | [Python Library](https://pypi.org/project/googletrans/)           |
| Inteligência artificial     | [gpt4free](https://github.com/xtekky/gpt4free)                    |


---

