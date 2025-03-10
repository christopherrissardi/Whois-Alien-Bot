##=====================================================>>> BIBLIOTECAS IMPORTADAS <<<=======================================================##
from discord.ext import commands, tasks
from dotenv import load_dotenv 
from datetime import datetime
import discord   
import requests
import os 
import string
import random
import io
import nest_asyncio
import time
import aiohttp 
import re
import secrets
from faker import Faker
from leakcheck import LeakCheckAPI_Public
import hashlib
import base64
from io import BytesIO

fake = Faker("pt_BR")

load_dotenv()
API_KEY = os.getenv("API_KEY")

nest_asyncio.apply()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot(command_prefix='./', intents=intents)

@client.event
async def on_ready():
    activity = discord.Game(name='Created By Alien', type=3) # Mensagem do bot quando Online
    await client.change_presence(status=discord.Status.dnd, activity=activity)
    print("Conectado")

@client.event
async def on_message(message):
    if isinstance(message.channel, discord.DMChannel):
        return
    await client.process_commands(message)

@client.event
async def on_member_join(member):
    welcome = member.guild.get_channel(913133936610246656) # Canal de boas vindas do servidor House´s Alien
    user_id = member.id

    if welcome:

        embed = discord.Embed(title=f'Olá {member} Seja muito bem vindo ao nosso servidor!', description=f'A partir de agora <@{user_id}>, você terá alguns requisitos a serem cumpridos para que você possa ser um membro em nosso servidor. Segue abaixo os requisitos')

        embed.add_field(name="\n\n", value="\n\n", inline=False)        
        embed.add_field(name="Requisitos Importântes:", value="", inline=False) 
        embed.add_field(name="\n\n", value="\n\n", inline=False)        
        embed.add_field(name="Requisito 1", value=f"Leia atentamente canal de <#{913138175520673812}>. É de extrema importância que você leia atentamente as regras e os termos!", inline=False)
        embed.add_field(name="Requisito 2", value=f"A opinião do <@{589502565243289612}> sempre prevalecerá! se ele dizer não, é não!", inline=False)
        embed.add_field(name="\n\n", value="\n\n", inline=False)        

        embed.add_field(name="Outros requisitos:", value="", inline=False)        
        embed.add_field(name="\n\n", value="\n\n", inline=False)        

        embed.add_field(name="Requisito 3", value="2 (duas) cópias do comprovante de residência", inline=False)
        embed.add_field(name="Requisito 4", value="1 (uma) cópia da escritura do terreno ou do imóvel reconhecida em cartórioㅤㅤ", inline=False)
        embed.add_field(name="Requisito 5", value="1 (uma) copia do RGㅤㅤ", inline=False)
        embed.add_field(name="Requisito 6", value="1 (uma) foto 3x4 recenteㅤㅤ", inline=False)
        embed.add_field(name="Requisito 7", value="Ter CPF com situação regular na Receita Federal", inline=False)
        embed.add_field(name="Requisito 8", value="Ter conta no Serasa com mais de 30 dias de criaçãoㅤㅤ", inline=False)        
        embed.add_field(name="", value="Lembrando, antes de tudo sempre tenha senso de humor e senso de dissernimento! Nada acima é verdadeiro a não ser os 2 primeiros requisitos!", inline=False)        
        embed.set_image(url='https://i.imgur.com/yInAO6g.gif')
        embed.set_footer(text='Whois Alien © All Rights Reserved', icon_url='')
        
        role = member.guild.get_role(913150428907184149) # Cargo de "Membro" para novos usuários
        if role:
            await member.add_roles(role)

        await welcome.send(embed=embed)

def convert_info(value):
    if value == True: 
        return "Sim"
    elif value == False:  
        return "Não"
    return value

@client.command()
async def codigo(ctx):
    # Defina o código que será enviado dentro do bloco de código
    codigo = """```python
def ola_mundo():
    print("Olá, mundo!")
ola_mundo()
```"""
    
    # Envia o bloco de código para o canal
    await ctx.send(codigo)


@client.command()
async def userinfo(ctx, member: discord.Member):
    # Obtém informações do usuário
    user_id = member.id
    joined_at = member.joined_at
    created_at = member.created_at
    avatar_url = member.avatar.url
    permissions = member.roles

    
    # Formatando as informações
    embed = discord.Embed(title=f'Informações de {member}')
    embed.add_field(name="Nome de usuário", value=f"`{member}`", inline=True)
    embed.add_field(name="ID de usuário", value=f"`{user_id}`", inline=True)
    embed.add_field(name="Entrou no Discord em", value=created_at.strftime("%d/%m/%Y %H:%M:%S"), inline=False)
    embed.add_field(name="Entrou no servidor em", value=joined_at.strftime("%d/%m/%Y %H:%M:%S"), inline=False)
    embed.set_image(url=avatar_url)
    # Envia o embed no canal onde o comando foi chamado
    await ctx.send(embed=embed)



@client.command()
async def avatar(ctx, member: discord.Member):

    avatar_url = member.avatar.url

    embed = discord.Embed(title=f"Avatar de {member.display_name}")
    embed.set_image(url=avatar_url)
    embed.set_footer(text=f"Solicitado por @{ctx.author.display_name}", icon_url="")
    await ctx.send(embed=embed)






@client.command() 
async def clear(ctx, amount: int): 
    if ctx.author.guild_permissions.manage_messages:
        if amount <= 0 or amount > 100:

            embed = discord.Embed(title='Não foi possível excluir as mensagens!', description='Por favor, forneça um número entre 1 e 100 para limpar mensagens.')
            await ctx.send(embed=embed)
        else:
            await ctx.channel.purge(limit=amount + 1)
            embed = discord.Embed(title='Limpeza de Mensagens feita!', description=f'{amount} mensagens foram excluídas.')
            await ctx.send(embed=embed, delete_after=5)
    else:
        embed = discord.Embed(title='',description='Sai dai bostinha, você não tem permissão para limpar as mensagens.',)
        await ctx.send(embed=embed)

@clear.error 
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArguments):
        await ctx.send('...')

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

    embed = discord.Embed(title=f'Usuário Expulso: {member.name}', description=f'O usuário {member.mention} foi expulso do servidor por ser babaca!')
    await ctx.send(embed=embed)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

    embed = discord.Embed(title=f'Usuário Banido: {member.name}', description=f'O usuário {member.mention} foi bnido do servidor por ser otário e babaca!')
    await ctx.send(embed=embed)

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

    if (user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user)
      await ctx.send(f'Desbanido {user.mention}')
      return

@client.command()
async def mute(ctx, member: discord.Member):
    if ctx.author.guild_permissions.mute_members:
        mute_role = discord.utils.get(ctx.guild.roles, name='Muted') 
        if mute_role:
            await member.add_roles(mute_role)
            await ctx.send(f'{member.mention} foi mutado por {ctx.author.mention}.')
        else:
            await ctx.send('O cargo de silenciamento (Muted) não foi encontrado. Crie um cargo com esse nome e configure as permissões corretamente.')
    else:
        await ctx.send('Você não tem permissão para mutar membros.')

@client.command()
async def unmute(ctx, member: discord.Member): 

    if ctx.author.guild_permissions.mute_members:
        mute_role = discord.utils.get(ctx.guild.roles, name='Muted') #Nome do cargo silenciado ----> Muted
        if mute_role:
            await member.remove_roles(mute_role)
            await ctx.send(f'{member.mention} foi desmutado por {ctx.author.mention}.')
        else:
            await ctx.send('O cargo de silenciamento (Muted) não foi encontrado. Crie um cargo com esse nome e configure as permissões corretamente.')
    else:
        await ctx.send('Você não tem permissão para desmutar membros.')

@client.command()
async def ping(ctx, ping_host=None):
    bot_latency = round(client.latency * 1000) 
    start_time = time.time()

    if ping_host is None:
        await ctx.send("Calculando o ping...")
        time.sleep(0.5)
        server_ping = round((time.time() - start_time) * 1000)

        embed = discord.Embed(title='')
        embed.add_field(name='• Ping do usuário', value=f"{round(client.latency * 500)} ms", inline=False)
        embed.add_field(name='• Ping do Bot', value=f"{bot_latency} ms", inline=False)
        embed.add_field(name='• Ping do Discord', value=f"{server_ping} ms", inline=False)
        embed.set_author(name='ㅤㅤㅤCONSULTA DE PINGㅤㅤㅤㅤ', icon_url='')
        embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved', icon_url='')

        await ctx.send(embed=embed)

    else:
        view_dns_key = os.getenv("VIEWDNS_TOKEN")
        url = f"https://api.viewdns.info/ping/?host={ping_host}&apikey={view_dns_key}&output=json"

        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

                replies = data.get('response', {}).get('replys', [])
                
                embed = discord.Embed(title=f"", description="")
                
                if not replies:
                    embed.set_author(name="NENHUMA RESPOSTA DE PING FOI ENCONTRADA.", icon_url='')
                    await ctx.send(embed=embed)
                    return

                for ping_info in replies:
                    rtt_info = ping_info.get('rtt', 'Desconhecido')
                    embed.add_field(name="Tempo de resposta", value=f"{rtt_info}", inline=False)

                embed.set_author(name=f'ㅤㅤㅤPING EFETUADO COM SUCESSOㅤㅤㅤㅤ', icon_url='')
                embed.add_field(name="Host:", value=f"{ping_host}", inline=False)

                embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved', icon_url='')

                await ctx.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="")
            embed.add_field(name="", value=f"Ocorreu um erro ao consultar o servidor: {str(e)}", inline=False)
            embed.set_author(name='Erro na Resposta da API', icon_url='')

            await ctx.send(embed=embed)

@client.command() 
async def termos(ctx):

    embed = discord.Embed(title='ㅤㅤㅤRegras/Termos e Responsabilidades - Houses Alienㅤㅤㅤ', description='\n\n Tempo de Leitura: **3 minutos**\n\n')

    embed.add_field(name="\n", value="\n", inline=False)
    embed.add_field(name="Termos de uso e Responsabilidades", value="", inline=False)
    embed.add_field(name="\n", value="\n", inline=False)
    embed.add_field(name="1. Comunidade Inclusivaㅤ", value='O Bot de Discord Whois Alien se esforça para criar um ambiente inclusivo onde todos os usuários são bem-vindos e respeitados. Não toleramos qualquer forma de discriminação com base em raça, cor, religião, identidade de gênero, orientação sexual, deficiência ou qualquer outra característica protegida por lei. \n\n', inline=False)
    embed.add_field(name="2. LGPD - Lei Geral de Proteção de Dados", value='As consultas de dados realizadas pelo Bot de Discord Whois Alien estão em estrita conformidade com a Lei Geral de Proteção de Dados (LGPD). Isso significa que:\n\n             - Os dados coletados são utilizados apenas para os fins específicos para os quais foram autorizados.\n\n             - Os usuários têm o direito de acessar, corrigir ou excluir seus dados pessoais contatando o criador/compilador do mesmo, conforme previsto pela LGPD.', inline=False)
    embed.add_field(name="3. Uso Indevido das Consultas", value='O criador do Bot de Discord Whois Alien não é responsável pelo uso indevido das consultas realizadas pela ferramenta. Os participantes do servidor também são orientados a usar as informações obtidas de maneira ética e legal. Qualquer uso indevido é estritamente proibido e não reflete a intenção ou responsabilidade do criador ou dos participantes do servidor.', inline=False)
    embed.add_field(name="4. Dados Gerados e Coincidências", value='Dados gerados pelo Bot de Discord Whois Alien que possam coincidir com informações reais são puramente coincidência. O bot é projetado para fornecer informações gerais baseadas em dados disponíveis publicamente e não garante a precisão ou exatidão das informações fornecidas.', inline=False)
    embed.add_field(name="5. Uso Consciente e Ético da Ferramenta", value='Os usuários são incentivados a usar o Bot de Discord Whois Alien de maneira consciente e ética. Isso inclui:\n\n             - Não utilizar a ferramenta para atividades ilegais ou ilícitas.\n\n             - Respeitar os direitos de privacidade de terceiros.\n\n             - Não realizar consultas em larga escala que possam sobrecarregar os sistemas ou violar os termos de serviço de terceiros.', inline=False)
    embed.add_field(name="6. Consequências do Uso Indevido", value='Qualquer uso indevido do Bot de Discord Whois Alien resultará em medidas disciplinares, incluindo, mas não limitado a, banimento permanente do servidor e revogação do acesso à ferramenta. A equipe de moderação se reserva o direito de tomar ações apropriadas para manter a integridade e a segurança do ambiente do servidor.', inline=False)
    embed.add_field(name="", value='', inline=False)
    embed.add_field(name="Outros Detalhes e Informações Importantes", value='', inline=False)    
    embed.add_field(name="", value='\n\n- **Atualizações e Mudanças**: O Bot de Discord Whois Alien pode ser atualizado periodicamente para melhorar funcionalidades e segurança. Os usuários serão informados sobre quaisquer mudanças significativas que possam afetar o uso da ferramenta.\n\n             - **Suporte e Contato**: Para dúvidas, suporte ou relatar problemas, os usuários podem entrar em contato com o dono do servidor, conforme as instruções fornecidas.', inline=False)    
    embed.add_field(name="", value='Estes termos e responsabilidades visam garantir um ambiente seguro, ético e responsável para todos os usuários que interagem com o Bot de Discord Whois Alien.', inline=False)
    embed.add_field(name="", value=f'Caso verifique que seus dados estão presentes na ferramenta e você tenha interesse em remove-los, entre em contato diretamente com o <@{589502565243289612}>.', inline=False)
    embed.add_field(name="\n", value="\n", inline=False)    
    embed.set_footer(text='Termos e políticas elaboradas por offalien\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

    await ctx.send(embed=embed)

@client.command() 
async def regras(ctx):

    embed = discord.Embed(title='ㅤㅤㅤRegras/Termos e Responsabilidades - Houses Alienㅤㅤㅤ', description='Olá usuários! Gostaria de deixar as boas-vindas a você, membro ou amigo que está presente em nosso servidor! Esta aba é dedicada a deixar as regras e termos que seguimos para que fique o mais transparente possível as coisas que rolam por aqui. Como uma comunidade organizada, temos diretrizes a serem seguidas e termos a serem respeitados, então esperamos que você **dedique o seu tempo para que você possa ler as diretrizes e políticas**!\n\n Tempo de Leitura: **10 minutos**')
    embed.add_field(name="", value="", inline=False)
    embed.add_field(name="Regras do servidor:", value="", inline=False)
    embed.add_field(name="\n", value="\n", inline=False)
    embed.add_field(name="🌁 1. O que acontece aqui, fica aqui", value="Aqui em nosso servidor é igual Las Vegas! **Tudo o que ocorre aqui, fica por aqui!** não saiam espalhando informações/desinformações, senso comum ou outros itens que possam vir ocorrer por aqui!", inline=False)
    embed.add_field(name="🗣️ 2. Xingamentos", value="Nossa comunidade foi criada especialmente com o intuito de poder juntar os amigos e colegas para jogarem... Como todos sabem, em jogos online sempre houve e sempre haverá xingamentos e brigas internas em relação aos membros, então não há nenhuma restrição de xingamentos e outros insultos com o intuito de difamar, menosprezar e/ou insultar quaisquer dos membros. Sempre conseguimos distinguir o que é brincadeira ou não, então a regra é clara, xingamentos e outros insultos que sejam apenas por brincadeiras entre amigos é permitido! O que não será permitido são brigas e desavenças entre membros que não se conhecem! Se você não conhece o outro membro, por gentileza, não insulte-o até possuir um certo nível de intimidade! ", inline=False)
    embed.add_field(name="❌ 3. Preconceito", value="Não será tolerada a discriminação por raça, cor, religião, identidade de gênero, orientação sexual, deficiência ou qualquer outro fator extra-racial aqui dentro do servidor! Se houver difamação e brincadeirinhas toscas que possa prejudicar algum outro membro, será notificado ou expulso e não quero nem saber de justificativa!", inline=False)
    embed.add_field(name="👾 4. Vírus/Malwares", value="Totalmente proibido disseminar Malwares, Trojans, Ransonwares, phishing e qualquer outro tipo de conteúdo que possa trazer malefícios à comunidade.", inline=False)
    embed.add_field(name="⚽ 5. Futebol", value="Liberado debater sobre futebol desde que seja algo ético e sensato. Brincadeiras são liberadas desde que outros membros se sintam confortáveis.", inline=False)
    embed.add_field(name="💼 6. Política", value="Assuntos sobre Política também são liberados, desde que você tenha mínimo conhecimento prévio e conteúdo para debater. Nossa comunidade não possui nenhuma filiação partidária, muito menos posições políticas. A opinião dos membros, é, apenas, opinião dos membros. Assuntos políticos aqui dentro do servidor, podem não estar relacionados à opinião direta dos membros! Se você quiser debater sobre política, debata! porém tenha a total ciência do que está falando e não saia espalhando desinformação, muito menos ignorância.", inline=False)
    embed.add_field(name="⛪ 7. Religião", value="Pode ser debatido desde que não exista ignorância.", inline=False)
    embed.add_field(name="😀 8. Membros", value=f"Nunca confie 100% em ninguém do servidor, muito menos nos membros! Aqui raramente alguém vai te chamar no privado para querer saber algo sobre você ou algo relacionado! Confie apenas nos membros com cargos de <@&{913150421063835659}> ou <@&{913150435651629106}> já que são de confiança do dono do servidor.", inline=False)
    embed.add_field(name="🤖 9. Comandos de Bot", value=f"Os comandos dos bots disponíveis no servidor devem ser usados apenas no canal <#{1179508687556051074}>. Comandos de música devem ser usados apenas no canal <#{913225365072257046}>.", inline=False)
    embed.add_field(name="📯 10. Divulgações", value=f"Caso queira fazer alguma divulgação no servidor, use o canal <#{913225542059315240}>. OBS: Só será aceito divulgações coerentes como redes sociais, campanhas beneficentes, vakinhas e outros! Links para outros servidores, pedir permissão para mim (<@{589502565243289612}>).", inline=False)
    embed.add_field(name="📧 11. Convites", value=f"Para manter algo mais organizado, nenhum usuário tem a permissão de criar link de convites a não ser os membros com privilégios, como o <@&{913150421063835659}> ou <@&{913150435651629106}>. Peço a gentileza de outros membros que usem apenas o convite fixado no canal <#{1065675289163726848}>!", inline=False)
    embed.add_field(name="⚙️ 12. Atualizações", value=f"Sempre que houver atualizações significativas no servidor será notificado em <#{913137314845306900}>, então é de extrema importância que seja lido as mensagens do canal quando houver atualização!", inline=False)
    embed.add_field(name="🎰 13. Jogos de Azar", value=f"É totalmente proibídio a divulgação e/ou disseminação de links, publicidades, campanhas e outros meios que venham existir sobre jogos de azar, apostas esportivas, bets, slots e quaiquer outros serviços relacionados! Nossa comunidade é totalmente contra esse tipo de ato e o criador <@{589502565243289612}> repugna qualquer coisa relacionada a essa área! Se você, você que faz parte desse esquema de pirâmide financeira vir divulgar aqui no meu servidor, você será banido e não vai ter justificativa!", inline=False)
    embed.add_field(name="🧠 14. Conhecimento", value="O conhecimento te liberta! discuta e propague o quanto quiser! Hoje em dia com o aumento de pessoas nas redes sociais e a quantidade de desinformação que é propagada diariamente, é raro achar alguém que fale coisas boas e propague conteúdo de qualidade. Grande parte das pessoas na atualidade fazem vídeos e espalham conteúdos extremamente ruins e/ou sem valor a agregar para a comunidade como um todo. Aqui valorizamos conteúdos bons e conhecimentos! Então fique a vontade para discutir/debater/conversar sobre quaisquer assuntos!", inline=False)
    embed.add_field(name="🗃️ 15. Termos e Políticas", value=f"Será destinado em um comando separado os termos e políticas do servidor em relação ao Bot <@{927981778419998750}> e em relação a outros itens, então a regra número 12 é estar ciente de TODOS OS TERMOS E POLÍTICAS do mesmo em relação ao servidor. LEIAM! Seu orgão genital não vai cair por perder alguns minutos da sua vida lendo ao importante! - Comando para visualizar os termos: `./termos`", inline=False)
    embed.add_field(name="🏷️ 16. Regra importante", value=f"A regra 16 é importantissima! A regra 16 é somente a regra 16! Obrigado!", inline=False)
   
    embed.add_field(name="\n", value="\n", inline=False)
    embed.set_footer(text='Regras elaboradas por offalien\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

    await ctx.send(embed=embed)

@client.command()
async def consultas(ctx):

    embed = discord.Embed(title='',)

    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE DADOSㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

    embed.add_field(name="*Consulta de dados*", value="", inline=False)
    embed.add_field(name="🕵🏻‍♂️ Consulta por Nome", value="Use o comando `./nome` {NOME COMPLETO} para realizar a consulta de dados através do nome completo do indivíduo.", inline=False)
    embed.add_field(name="👽 Consulta por CPF básico", value="Use o comando `./cpf0` {CPF DA PESSOA} para a consultar os dados básicos.", inline=False)
    embed.add_field(name="🔍 Consulta por CPF completo", value="Use o comando `./cpf` {CPF DA PESSOA} para a consultar os dados completa.", inline=False)
    embed.add_field(name="📳 Consulta por Telefone", value="Use o comando `./telefone` {TELEFONE} para realizar a consulta dos dados do proprietário da linha telefonica.", inline=False)
    embed.add_field(name="💎 Consulta por Telefone fixo", value="Use o comando `./fixo` {TELEFONE} para realizar a consulta dos dados do proprietário da linha telefonica fixa (RESIDÊNCIAL).", inline=False)
    embed.add_field(name="📮 Consulta por E-mail", value="Use o comando `./email` {EMAIL} para realizar a consulta dos dados do proprietário do email (SE DISPONÍVEL).", inline=False)
    embed.add_field(name="📑 Consulta por CEP para pessoas", value="Use o comando `./cep_pessoas` {CEP DA RUA} para realizar a consulta de todos os indivíduos que moram na respectiva rua.", inline=False)
    embed.add_field(name="👩‍👦 Consulta de filhos pelo Nome da mãe", value="Use o comando `./mae` {NOME DA MÃE} para realizar a consulta dos dados dos filhos pelo nome da mãe.", inline=False)
    embed.add_field(name="👨‍👦 Consulta de filhos pelo Nome do pai", value="Use o comando `./pai` {NOME DO PAI} para realizar a consulta dos dados dos filhos pelo nome do pai.", inline=False)
    embed.add_field(name="🚘 Consulta de Placa", value="Use o comando `./placa` {PLACA DO VEÍCULO} para realizar a consulta de veículo.", inline=False)
    embed.add_field(name="🏨 Consulta por CNPJ", value="Use o comando `./cnpj` {CNPJ} para consultar de CNPJ completa.", inline=False)

    embed.add_field(name="Consulta de dados/ferramentas", value="", inline=False)
    embed.add_field(name="📌 Consulta de IP", value="Use o comando `./ip` {IP} para realizar a consulta do IP.", inline=False)
    embed.add_field(name="💳 Consulta de BIN", value="Use o comando `./bin` {NÚMERO DA BIN} para realizar a consulta.", inline=False)
    embed.add_field(name="📫 Consulta por CEP", value="Use o comando `./cep` {CEP DA RUA} para realizar a consulta.", inline=False)
    embed.add_field(name="🦠 Consulta de Covid19", value="Use o comando `./covid` {SIGLA DO ESTADO} para realizar a consulta.", inline=False)
    embed.add_field(name="🏦 Consulta de Banco", value="Use o comando `./banco` {CÓDIGO DO BANCO} para realizar a consulta.", inline=False)
    embed.add_field(name="💾 Consulta de Site", value="Use o comando `./site` {URL DO SITE} para realizar a consulta.", inline=False)
    embed.add_field(name="📴 Consulta de Operadora", value="Use o comando `./operadora` {NÚMERO DE CELULAR} para realizar a consulta.", inline=False)    
    embed.add_field(name="🤖 Consulta de Info-email", value="Use o comando `./emailinfo` {EMAIL} para realizar a consulta.", inline=False)
    embed.add_field(name="💰 Consulta de cotação de moedas", value="Use o comando `./cotacao` {PAR DE MOEDA} para realizar a consulta.", inline=False)
    embed.add_field(name="🏙️ Consulta de cidades por DDD", value="Use o comando `./ddd` {DDD} para realizar a consulta do DDD por cidades.", inline=False)
    embed.add_field(name="🌐 Consulta Whois básica", value="Use o comando `./whois` {NOME DO DOMÍNIO} para realizar a consulta de Whois.", inline=False)

    embed.set_image(url='https://i.gifer.com/Cewn.gif')
    embed.set_footer(text='Whois Alien © All Rights Reserved', icon_url='')

    await ctx.send(embed=embed)

@client.command()
async def ajuda(ctx):

    embed = discord.Embed(title='ㅤㅤㅤㅤㅤㅤㅤㅤㅤWhois Alienㅤㅤㅤㅤㅤㅤㅤㅤ')
    embed.add_field(name="ㅤ", value='Olá, estou aqui para te ajudar! Aqui está algum dos comandos que o `Whois Alien` possui. Ficou com alguma dúvida em relação aos comandos abaixo? Digite `/[NOME DO COMANDO]`. Exemplo: `./admin`\n\nOBS: Grande parte das consultas de dados como: nome, cpf, cpf2, telefone, mãe, pai e email estão sendo hospedados em meu computador pessoal, no entanto, os comandos só irão funcionar quando o ALIEN estiver online. Parte da madrugada não irá funcionar as consultas, infelizmente! Desde já peço mil desculpas pelo transtorno e tudo será resolvido, ou melhor, normalizado. \n\n', inline=False)
    embed.add_field(name="🔐 Moderação", value='Use o comando `./admin` para ver os comandos administrativos. Comando de moderação existentes: `./kick`, `./ban`, `./unban`, `./unmute`, `./role`, `./mute`, `./clear` `\n\n (OS COMANDOS ADMINISTRATIVOS SÓ FUNCIONARÃO PARA PESSOAS COM CARGOS AUTORIZADOS)`', inline=False)
    embed.add_field(name="🛠️ Ferramentas Avançadas", value='Use o comando `./ferramentas` para obter mais informações. Ferramentas disponíveis: `./portscan`, `./traceroute`, `./whois`', inline=False)
    embed.add_field(name="🧭 Consulta de Dados", value='Use o comando `./consultas` para obter mais informações sobre a aba de consulta de dados. Consultas disponíveis: `./nome`, `./cpf`, `./cpf0`, `./telefone`, `./fixo`, `./cep_pessoas`, `./email`, `./mae`, `./pai`, `./cnpj`, `./placa [NÃO ESTÁ FUNCIONANDO NO MOMENTO]`, `./ip`, `./bin`, `./cep`, `./covid`, `./banco`, `./site`, `./operadora`, `./emailinfo` e possivelmente outros entrem nessa lista futuramente. ', inline=False)
    embed.add_field(name="⚙️ Geradores", value='Use o comando `./gerador` para obter mais informações. Ferramentas disponíveis: `./gerarpessoa`, `./gerarcartao`, `./geraremail`, `./gerarcpf`, `./gerarusr`, `./gerarsenha`, `./gerarveiculo`, `./gerartel`, `./gerarimei`', inline=False)
    embed.add_field(name="🎵 Músicas", value='Use o comando `./musica` para vizualizar os comandos. Comandos acessíveis a classe: `./play`, `./stop`, `./pause`, `./resume`, `./back`, `./skip`, `./disconnect` `\n\n (OS MENUS DE MÚSICAS AINDA NÃO FORAM IMPLEMENTADOS)`', inline=False)
    embed.add_field(name="🪐 Informações", value='Use o comando `./info` para ver os comandos disponíveis. Comandos existentes: `./ajuda`, `./ping`, `./serverinfo`, `./userinfo`', inline=False)
    embed.add_field(name="OBS:", value='`O BOT AINDA ESTÁ EM DESENVOLVIMENTO!, POR ESSE MOTIVO ALGUNS COMANDOS AINDA NÃO FORAM CORRIGIDOS OU IMPLEMENTADOS.`', inline=False)
    embed.set_image(url="https://i.imgur.com/GAw2sJ4.jpg")
    embed.set_footer(text='Whois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

    await ctx.author.send(embed=embed)


@client.command()
async def admin(ctx):

    embed = discord.Embed(title='')

    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤWhois Alienㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

    embed.add_field(name="", value="Aqui fica os comandos administrativos, no entanto, somente pessoas com cargos superiores conseguiram usar essa função.", inline=False)
    embed.add_field(name="Os comandos administrativos são:", value="\n`./kick`, `./ban`, `./unban`, `./mute`, `./unmute`, `./role`, `./clear`", inline=False)
    embed.add_field(name="", value="Cada comando tem um objetivo diferente. Abaixo estará uma ***explicação breve*** de como usa-los.", inline=False)
    embed.add_field(name="❌ Comando de Expulsar", value="Use o comando `./kick` e o @ usuário da pessoa. *Exemplo ./kick @ALIEN*", inline=False)
    embed.add_field(name="⛔ Comando de Banir", value="Use o comando `./ban` e o @ usuário de quem deseja banir. *Exemplo ./ban @ALIEN*", inline=False)
    embed.add_field(name="🟢 Comando de Desbanir", value="Use o comando `./unban` precedido do @ usuário de quem deseja desbanir. *Exemplo ./unban @ALIEN*", inline=False)
    embed.add_field(name="🔇 Comando de Mutar", value="Use o comando  `./mute` e em seguida o @ usuário de quem deseja mutar. *Exemplo ./mute @ALIEN*", inline=False)
    embed.add_field(name="🔊 Comando de Desmutar", value="Use o comando `./unmute` e o @ usuário de quem deseja desmutar. *Exemplo ./unmute @ALIEN*", inline=False)
    embed.add_field(name="➕ Comando de Adicionar Cargos", value="Esse comando ainda está em fase de criação.", inline=False)
    embed.add_field(name="✔️ Comando de Limpar mensagens", value="Use o comando `./clear` e em seguida a quantidade de mensagens que deseja limpar. *Exemplo ./clear 10*", inline=False)
    embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

    await ctx.send(embed=embed); 




@client.command()
async def nome(ctx, *, nome=None):

    if not nome: 
        embed = discord.Embed(title="")
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE NOME', icon_url='')
        embed.add_field(name="Use o comando: `./nome` e o {NOME} que deseja.", value='*Exemplo: `./nome` Fulano dos Santos*', inline=False)
        await ctx.send(embed=embed)
        return  

    nome_formatado = nome.strip().replace(' ', '%20')
    data = f"http://127.0.0.1:44340/alienlabs/api/database/serasa/basic/search?nome={nome_formatado}"

    headers = {"apikey": API_KEY}

    response = requests.get(data, headers=headers)

    try:
        if response.status_code == 200:
            data_json = response.json()

            if isinstance(data_json, list) and len(data_json) > 1:
                file_contents = ""
                for index, result in enumerate(data_json, 1):
                    file_contents += f"RESULTADO {index}:\n\n• NOME: {result['nome']}\n• CPF: {result['cpf']}\n• SEXO: {result['sexo']}\n• DATA DE NASCIMENTO: {result['data_nascimento']}\n\n"

                file_contents += "Whois Alien © All Rights Reserved\n"

                file = io.StringIO(file_contents)
                file.seek(0)

                await ctx.send(file=discord.File(file, filename="resultados.txt"))
            elif isinstance(data_json, dict) or (isinstance(data_json, list) and len(data_json) == 1):
                result = data_json[0] if isinstance(data_json, list) else data_json

                embed = discord.Embed(title='')
                embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE NOMEㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

                embed.add_field(name='• NOME', value=result.get('nome').upper() or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• CPF', value=result.get('cpf') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• SEXO', value=result.get('sexo') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• DATA DE NASCIMENTO', value=result.get('data_nascimento') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• IDADE', value=result.get('idade') or 'SEM INFORMAÇÃO', inline=False)

                embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)
                embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="")
            embed.set_author(name=f'ㅤㅤㅤNOME NÃO ENCONTRADO!ㅤㅤㅤ', icon_url='')
            await ctx.send(embed=embed)

    except Exception as e:       
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE NOME', icon_url='')
        embed.add_field(name="Use o comando: `./nome` e o {NOME} que deseja consultar.", value='*Exemplo: `./nome` Fulano dos Santos*', inline=False)

        await ctx.send(embed=embed)


@client.command()
async def cpf1(ctx, *, cpf1=None):

    if not cpf1:
        embed = discord.Embed(title="")
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE CPF', icon_url='')
        embed.add_field(name="Use o comando: `./cpf1` e o {CPF} que deseja.", value='*Exemplo: `./cpf1` 123.456.789-12*', inline=False)
        await ctx.send(embed=embed)
        return

    cpf_formatado = cpf1.strip()
    data = f"http://127.0.0.1:44340/alienlabs/api/database/serasa/basic/search?cpf={cpf_formatado}"

    headers = {"apikey": API_KEY}

    response = requests.get(data, headers=headers)

    try:
        if response.status_code == 200:
            data = response.json()

            if len(data) > 0:
                cpf_info = data[0] 

                embed = discord.Embed(title='')

                embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE CPFㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

                embed.add_field(name='• CPF', value=cpf_info.get('cpf') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name="• NOME", value=cpf_info.get('nome').upper() or 'SEM INFORMAÇÃO'.upper(), inline=False)
                embed.add_field(name='• SEXO', value=cpf_info.get('sexo') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• DATA DE NASCIMENTO', value=cpf_info.get('data_nascimento') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• IDADE', value=cpf_info.get('idade') or 'SEM INFORMAÇÃO', inline=False)

                embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)
                embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="")
            embed.set_author(name=f'ㅤㅤㅤCPF NÃO ENCONTRADO!ㅤㅤㅤ', icon_url='')

            await ctx.send(embed=embed)

    except Exception as e:

        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE CPF', icon_url='')
        embed.add_field(name="Use o comando: `./cpf2` e o {CPF} que deseja.", value='*Exemplo: `/cpf2` 123.456.789-12*', inline=False)

        await ctx.send(embed=embed)


@client.command()
async def cpf2(ctx, *, cpf2=None):

    if not cpf2:
        embed = discord.Embed(title="")
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE CPF', icon_url='')
        embed.add_field(name="Use o comando: `./cpf2` e o {CPF} que deseja.", value='*Exemplo: `./cpf2` 123.456.789-12*', inline=False)
        await ctx.send(embed=embed)
        return


    cpf_formatado = cpf2.strip()
    data = f"http://127.0.0.1:44340/alienlabs/api/database/datasus/search?cpf={cpf_formatado}"

    headers = {"apikey": API_KEY}

    response = requests.get(data, headers=headers)
    try:
        if response.status_code == 200:
            data = response.json()

            if len(data) > 0:
                cpf2_info = data[0]

                embed = discord.Embed(title='')

                embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE CPFㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

                embed.add_field(name='• CPF', value=cpf2_info.get('cpf') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name="• CNS", value=cpf2_info.get('cns') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name="• RG", value=cpf2_info.get('rgNumero') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name="• ORGÃO EMISSOR", value=cpf2_info.get('rgOrgaoEmisor') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name="• RG UF", value=cpf2_info.get('rgUf') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name="• NOME", value=(cpf2_info.get('nome') or 'SEM INFORMAÇÃO').upper(), inline=False)
                embed.add_field(name="• DATA DE NASCIMENTO", value=cpf2_info.get('nascimento') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name="• NOME DA MÃE", value=cpf2_info.get('mae') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name="• NOME DO PAI", value=cpf2_info.get('pai') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name="• CIDADE DE NASCIMENTO", value=cpf2_info.get('municipioNascimento') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name="• LOGRADOURO", value=cpf2_info.get('logradouro') + (',') + (' ') + cpf2_info.get('numero') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name="• BAIRRO", value=cpf2_info.get('bairro') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name="• CIDADE", value=cpf2_info.get('municipio') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name="• CEP", value=cpf2_info.get('cep') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name="• TELEFONE", value=cpf2_info.get('telefone') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name="• TELEFONE SECUNDÁRIO", value=cpf2_info.get('telefoneSecundario') or 'SEM INFORMAÇÃO', inline=False)


                embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)
                embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="")
                embed.set_author(name=f'CPF NÃO ENCONTRADO!', icon_url='')

                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="")
            embed.set_author(name=f'CPF NÃO ENCONTRADO! {response.status_code}', icon_url='')

            await ctx.send(embed=embed)

    except Exception as e:
        embed = discord.Embed(title='')
        embed.set_author(name=f'CPF NÃO ENCONTRADO! {response.status_code}', icon_url='')

        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE CPF', icon_url='')
        embed.add_field(name="Use o comando: `./cpf2` e o {CPF} que deseja.", value='*Exemplo: `./cpf2` 123.456.789-12*', inline=False)

        await ctx.send(embed=embed)



@client.command()
async def cpf(ctx, *, cpf=None):

    if not cpf:
        embed = discord.Embed(title="")
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE CPF', icon_url='')
        embed.add_field(name="Use o comando: `./cpf` e o {CPF} que deseja.", value='*Exemplo: `./cpf` 123.456.789-12*', inline=False)
        await ctx.send(embed=embed)
        return


    cpf_formatado = cpf.strip()
    data = f"http://127.0.0.1:44340/alienlabs/api/database/serasa/full/search?CPF={cpf_formatado}"

    headers = {"apikey": API_KEY}

    response = requests.get(data, headers=headers)
    try:
        if response.status_code == 200:
            data = response.json()

            if len(data) > 0:
                cpf_info = data[0]

                idade = cpf_info.get('IDADE')

                enderecos_str = ""

                # Recupera os endereços do JSON (supondo que seja uma lista)
                enderecos = cpf_info.get('ENDEREÇOS', [])

                # Itera sobre cada endereço
                for endereco in enderecos:
                    rua = endereco.get('rua')
                    numero = endereco.get('numero')
                    bairro = endereco.get('bairro')
                    cidade = endereco.get('cidade')
                    uf = endereco.get('uf')

                    # Verifica se o campo "rua" está vazio ou não
                    if not rua:  # Se "rua" estiver vazio ou None
                        continue  # Pula esse endereço e vai para o próximo

                    # Se a rua não for vazia, monta o endereço
                    enderecos_str += f"{rua}, {numero} - {bairro} - {cidade}, {uf}\n"


                telefone_str = ""

                telefone_principal = cpf_info.get('TELEFONE', '')
                telefone_secundario = cpf_info.get('TELEFONE_SECUNDARIO', '')

                if telefone_principal != 'SEM INFORMAÇÃO':
                    telefone_str += f"{telefone_principal}\n"

                if telefone_secundario != 'SEM INFORMAÇÃO':
                    telefone_str += f"{telefone_secundario}"

                telefones_normais = []
                telefones_fixos = []

                telefones = cpf_info.get('TELEFONES', [])
                for telefone_info in telefones:
                    telefone = telefone_info.get('telefone')
                    telefone_fixo = telefone_info.get('telefone_fixo')

                    if telefone_fixo:
                        telefones_fixos.append(f"{telefone}")
                    else:
                        telefones_normais.append(f"{telefone}")

                for telefone in telefones_normais:
                    telefone_str += f"{telefone}\n"

                for telefone in telefones_fixos:
                    telefone_str += f"{telefone}\n"

                if not telefone_str.strip():
                    telefone_str = "SEM INFORMAÇÃO"


                renda_info = cpf_info.get("FAIXA_RENDA", {})

                if renda_info:
                    faixa_poder_aquisitivo = renda_info.get("FX_PODER_AQUISITIVO", "Sem Informação")
                    renda_poder_aquisitivo = renda_info.get("PODER_AQUISITIVO", "Sem Informação")
                    renda_bruta = renda_info.get("RENDA_PODER_AQUISITIVO", "Sem Informação")

                    renda_str = (
                        f"➤ Renda: {renda_bruta}\n"
                        f"➤ Poder Aquisitivo: {renda_poder_aquisitivo}\n"
                        f"➤ Faixa: {faixa_poder_aquisitivo}")
                else:
                    renda_str = "SEM INFORMAÇÃO"


                score_info = cpf_info.get("SCORE_ORGAOS", {})

                if score_info:
                    csb8_score_str = score_info.get("CSB8", "Sem Informação")
                    csb8_faixa_str = score_info.get("CSB8_FAIXA", "Sem Informação")
                    csba_score_str = score_info.get("CSBA", "SSem Informação")
                    csba_faixa_str = score_info.get("CSBA_FAIXA", "Sem Informação")
                    score_str = (
                        f"➤ CSB8: {csb8_score_str}\n"
                        f"➤ CSB8 FAIXA: {csb8_faixa_str}\n"
                        f"➤ CSBA: {csba_score_str}\n"
                        f"➤ CSBA FAIXA: {csba_faixa_str}")
                else:
                    score_str = "Sem Informação"


                mosaic_info = cpf_info.get("MOSAIC", {})
                if mosaic_info:
                    desc_mosaic = mosaic_info.get("CD_MOSAIC_NOVO", "Sem Informação")
                    desc_mosaic_secund = mosaic_info.get("DESC_MOSAIC_NOV", "Sem Informação")
                    desc_mosaic_novo = mosaic_info.get("INFOR_MOSAIC_NOV", "Sem Informação")
                    mosaic_str = (
                        f"➤ Mosaic: {desc_mosaic}\n"
                        f"➤ Descrição: {desc_mosaic_secund}\n"
                        f"➤ Informação: {desc_mosaic_novo}")
                else:
                    mosaic_str = "SEM INFORMAÇÃO"


                parentes_info = cpf_info.get("PARENTES", {})
                if parentes_info:
                    cpf_vinculo = parentes_info.get("CPF_VINCULO", "Sem Informação")
                    nome_vinculo = parentes_info.get("NOME_VINCULO", "Sem Informação")
                    vinculo = parentes_info.get("VINCULO", "Sem Informação")
                    parente_str = (
                        f"➤ Nome: {nome_vinculo}\n"
                        f"➤ CPF: {cpf_vinculo}\n"
                        f"➤ Vínculo: {vinculo}")
                else:
                    parente_str = "SEM INFORMAÇÃO"


                conjuge_info = cpf_info.get("CONJUGE", {})
                if conjuge_info:
                    cpf_conjuge = conjuge_info.get("CPF", "Sem Informação")
                    nome_conjuge = conjuge_info.get("NOME", "Sem Informação")
                    nascimento_conjuge = conjuge_info.get("NASC", "Sem Informação")
                    conjuge_str = (
                        f"➤ Nome: {nome_conjuge}\n"
                        f"➤ CPF: {cpf_conjuge}\n"
                        f"➤ Nascimento: {nascimento_conjuge}")
                else:
                    conjuge_str = "SEM INFORMAÇÃO"


                ensino_info = cpf_info.get("ENSINO_SUPERIOR", {})

                # Verifica se a API retornou a mensagem de falta de informações
                if ensino_info.get("message") == "SEM INFORMAÇÕES ATÉ O MOMENTO":
                    superior_str = "SEM INFORMAÇÃO"
                else:
                    # Verifica se há pelo menos um valor válido preenchido
                    if ensino_info and any(value not in ["", None] for value in ensino_info.values()):
                        ano_conclusao = ensino_info.get("ANO_CONCLUSAO", "")
                        ano_vestibular = ensino_info.get("ANO_VESTIBULAR", "")
                        campus_cursado = ensino_info.get("CAMPUS", "")
                        cota = ensino_info.get("COTA", "")
                        curso_efetuado = ensino_info.get("CURSO", "")
                        data_inclusao = ensino_info.get("DATA_INCLUSAO", "")
                        faculdade = ensino_info.get("FACULDADE", "")
                        inscricao_vestibular = ensino_info.get("INSCRICAO_VESTIBULAR", "")
                        periodo_cursado = ensino_info.get("PERIODO_CURSADO", "")
                        uf_cursado = ensino_info.get("UF", "")

                        superior_str = (
                            f"➤ Curso: {curso_efetuado}\n"
                            f"➤ Ano Conclusão: {ano_conclusao}\n"
                            f"➤ Faculdade: {faculdade}\n"
                            f"➤ Campus: {campus_cursado}\n"
                            f"➤ Período: {periodo_cursado}\n"
                            f"➤ Inscrição Vestibular: {inscricao_vestibular}\n"
                            f"➤ Ano Vestibular: {ano_vestibular}\n"
                            f"➤ UF: {uf_cursado}\n"
                            f"➤ Cotas: {cota}\n"
                            f"➤ Data de inclusão: {data_inclusao}"
                        ).strip()  # Remove espaços extras no final
                    else:
                        superior_str = "SEM INFORMAÇÃO"


                irpf_info = cpf_info.get("INFORMACOES_IRPF", {})

                # Verifica se a API retornou a mensagem de falta de informações
                if irpf_info.get("message") == "SEM INFORMAÇÕES NO MOMENTO":
                    rfb_str = "SEM INFORMAÇÃO"
                else:
                    # Verifica se há pelo menos um valor válido preenchido
                    if irpf_info and any(value not in ["", None] for value in irpf_info.values()):
                        ano_referencia = irpf_info.get("ANO_REFERENCIA", "")
                        cod_agencia = irpf_info.get("COD_AGENCIA", "")
                        data_info = irpf_info.get("DATA_INFORMACAO", "")
                        banco_responsavel = irpf_info.get("INSTITUICAO_BANCARIA", "")
                        lote = irpf_info.get("NUMERO_LOTE", "")
                        status_rfb = irpf_info.get("STATUS_RECEITA_FEDERAL", "")

                        rfb_str = (
                            f"➤ Código Agência: {cod_agencia}\n"
                            f"➤ Banco Responsável: {banco_responsavel}\n"
                            f"➤ Lote: {lote}\n"
                            f"➤ Status: {status_rfb}\n"
                            f"➤ Ano de Referência: {ano_referencia}\n"
                            f"➤ Data da Informação: {data_info}"
                        ).strip()  # Remove espaços extras no final
                    else:
                        rfb_str = "SEM INFORMAÇÃO"


                fgts_info = cpf_info.get("INFORMACOES_IRPF", {})

                if fgts_info.get("message") == "SEM INFORMAÇÕES NO MOMENTO":
                    fgts_str = "SEM INFORMAÇÃO"
                else:

                    if fgts_info and any(value not in ["", None] for value in irpf_info.values()):
                        cpf_beneficiado = fgts_info.get("CPF", "")
                        id_cadastro = fgts_info.get("CADASTRO_ID", "")
                        data_fgts = fgts_info.get("DT_INCLUSAO", "")
                        flag_2017 = fgts_info.get("FLAG_2017", "")
                        flag_2018 = fgts_info.get("FLAG_2018", "")

                        fgts_str = (
                            f"➤ CPF: {cpf_beneficiado}\n"
                            f"➤ Cadastro: {id_cadastro}\n"
                            f"➤ Data Inclusão: {data_fgts}\n"
                            f"➤ 2017: {flag_2017}\n"
                            f"➤ 2018: {flag_2018}\n"
                        ).strip() 
                    else:
                        fgts_str = "SEM INFORMAÇÃO"


                embed = discord.Embed(title='')

                embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE CPFㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

                embed.add_field(name='Nome', value=cpf_info.get('NOME') or 'Sem Informação', inline=False)
                embed.add_field(name='CPF', value=cpf_info.get('CPF') or 'Sem Informação', inline=True)
                embed.add_field(name='Nascimento', value=cpf_info.get('NASC') or 'Sem Informação', inline=True)
                embed.add_field(name='Idade', value=cpf_info.get('IDADE') or 'Sem Informação', inline=True)
                embed.add_field(name='Estado Civil', value=cpf_info.get('ESTCIV') or 'Sem Informação', inline=True)
                embed.add_field(name='Sexo', value=cpf_info.get('SEXO') or 'Sem Informação', inline=True)
                embed.add_field(name='Nacionalidade', value=cpf_info.get('NACIONALID') or 'Sem Informação', inline=True)
                embed.add_field(name='Naturalidade', value=cpf_info.get('MUNICIPIO_NASCIMENTO') or 'Sem Informação', inline=True)                
                embed.add_field(name='Escolaridade', value=cpf_info.get('ESCOLARIDADE') or 'Sem Informação', inline=True)                
                embed.add_field(name='Profissão', value=cpf_info.get('OCUPACAO').upper() or 'Sem Informação', inline=True)
                embed.add_field(name='Data de Ocupação', value=cpf_info.get('OCUPACAO_DATA').upper() or 'Sem Informação', inline=True)
                embed.add_field(name='Informação de CBO', value=cpf_info.get('CBO').upper() or 'Sem Informação', inline=True)
                embed.add_field(name='E-mail', value=cpf_info.get('INFORMACOES_EMAIL', {}).get('EMAIL', 'Sem Informação'), inline=True)              
                embed.add_field(name='Nome da Mãe', value=cpf_info.get('NOME_MAE') or 'Sem Informação', inline=True)
                embed.add_field(name='Nome do Pai', value=cpf_info.get('NOME_PAI') or 'Sem Informação', inline=True)
                embed.add_field(name='Situação CPF', value=cpf_info.get('CD_SIT_CAD') or 'Sem Informação', inline=True)
                embed.add_field(name='Data de Situação', value=cpf_info.get('DT_SIT_CAD') or 'Sem Informação', inline=True)
                embed.add_field(name='Óbito', value=cpf_info.get('OBITO') or 'Sem Informação', inline=True)
                embed.add_field(name='Data de Óbito', value=cpf_info.get('DT_OB') or 'Sem Informação', inline=True)
                embed.add_field(name='CNS', value=cpf_info.get('CNS') or 'Sem Informação', inline=True)
                embed.add_field(name='PIS', value=cpf_info.get('PIS') or 'Sem Informação', inline=True)
                embed.add_field(name='NIS', value=cpf_info.get('NIS') or 'Sem Informação', inline=True)  
                embed.add_field(name='RG', value=cpf_info.get('INFORMACOES_RG', {}).get('RG', 'Sem Informação'), inline=True)
                embed.add_field(name='Órgão Emissor RG', value=cpf_info.get('INFORMACOES_RG', {}).get('ORGAO_EMISSOR', 'Sem Informação'), inline=True)
                embed.add_field(name='UF Emissão RG', value=cpf_info.get('INFORMACOES_RG', {}).get('UF_EMISSAO', 'Sem Informação'), inline=True)

                await ctx.send(embed=embed)

                embed = discord.Embed(title='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ')
                embed.add_field(name='Título Eleitoral', value=cpf_info.get('INFORMACOES_TSE', {}).get('TITULO_ELEITOR', 'Sem Informação'), inline=True)
                embed.add_field(name='Zona Eleitoral', value=cpf_info.get('INFORMACOES_TSE', {}).get('ZONA', 'Sem Informação'), inline=True)
                embed.add_field(name='Seção Eleitoral', value=cpf_info.get('INFORMACOES_TSE', {}).get('SECAO', 'Sem Informação'), inline=True)
                embed.add_field(name='Poder Aquisitivo', value=renda_str, inline=True)
                embed.add_field(name='Scores', value=score_str, inline=True)
                embed.add_field(name='Mosaic', value=mosaic_str, inline=True)
                embed.add_field(name='Parente', value=parente_str, inline=True)
                embed.add_field(name='Conjugê', value=conjuge_str, inline=True)
                embed.add_field(name='Informação FGTS', value=fgts_str, inline=True)
                embed.add_field(name='Imposto de Renda', value=rfb_str, inline=True)
                embed.add_field(name="Ensino Superior", value=superior_str, inline=True) 
                embed.add_field(name='Telefones', value=telefone_str, inline=True)
                embed.add_field(name='Endereços', value=enderecos_str, inline=False)

                embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="")
                embed.set_author(name=f'CPF NÃO ENCONTRADO!', icon_url='')

                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="")
            embed.set_author(name=f'CPF NÃO ENCONTRADO! {response.status_code}', icon_url='')

            await ctx.send(embed=embed)

    except Exception as e:
        embed = discord.Embed(title='')
        embed.set_author(name=f'CPF NÃO ENCONTRADO! {response.status_code}', icon_url='')

        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE CPF', icon_url='')
        embed.add_field(name="Use o comando: `./cpf` e o {CPF} que deseja.", value='*Exemplo: `./cpf` 123.456.789-12*', inline=False)

        await ctx.send(embed=embed)


@client.command()
async def mae(ctx, *, mae=None):

    if not mae:

        embed = discord.Embed(title="")
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE NOME', icon_url='')
        embed.add_field(name="Use o comando: `./mae` e o nome da {MÃE} que deseja.", value='*Exemplo: `./mae` Fulana Santos*', inline=False)
        await ctx.send(embed=embed)
        return

    mae_formatado = mae.strip().replace(' ', '%20')
    data = f"http://127.0.0.1:44340/alienlabs/api/database/serasa/full/search?NOME_MAE={mae_formatado}"

    headers = {"apikey": API_KEY}

    response = requests.get(data, headers=headers)

    try:
        if response.status_code == 200:
            data_json = response.json()

            if isinstance(data_json, list) and len(data_json) > 1:
                file_contents = ""
                for index, result in enumerate(data_json, 1):
                    file_contents += f"RESULTADO {index}:\n\n• NOME: {result['NOME']}\n• CPF: {result['CPF']}\n• DATA DE NASCIMENTO: {result['NASC']}\n• NOME DA MÃE: {result['NOME_MAE']}\n\n"

                file_contents += "Whois Alien © All Rights Reserved\n"

                file = io.StringIO(file_contents)
                file.seek(0)

                await ctx.send(file=discord.File(file, filename="resultados.txt"))
            elif isinstance(data_json, dict) or (isinstance(data_json, list) and len(data_json) == 1):
                result = data_json[0] if isinstance(data_json, list) else data_json

                embed = discord.Embed(title='')
                embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤCONSULTA DE NOME DA MÃEㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

                embed.add_field(name='• NOME', value=result.get('NOME').upper() or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• CPF', value=result.get('CPF') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• DATA DE NASCIMENTO', value=result.get('NASC') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• NOME DA MÃE', value=result.get('NOME_MAE') or 'SEM INFORMAÇÃO', inline=False)

                embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)
                embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="")
            embed.set_author(name=f'ㅤㅤㅤNOME DA MÃE NÃO ENCONTRADO!ㅤㅤㅤ', icon_url='')
            await ctx.send(embed=embed)

    except Exception as e:       
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE NOME', icon_url='')
        embed.add_field(name="Use o comando: `./mae` e o nome da {MÃE} que deseja.", value='*Exemplo: `./mae` Fulana da Silva Santos*', inline=False)

        await ctx.send(embed=embed)

@client.command()
async def pai(ctx, *, pai=None):

    if not pai:

        embed = discord.Embed(title="")
        embed.set_author(name='ㅤㅤㅤㅤ👽 CONSULTA PELO NOME DO PAI', icon_url='')
        embed.add_field(name="Use o comando: `./pai` e o nome do {PAI} que deseja.", value='*Exemplo: `./pai` Fulano De Jesus Matos*', inline=False)
        await ctx.send(embed=embed)
        return


    pai_formatado = pai.strip().replace(' ', '%20')
    data = f"http://127.0.0.1:44340/alienlabs/api/database/datasus/search?pai={pai_formatado}"

    headers = {"apikey": API_KEY}

    response = requests.get(data, headers=headers)

    try:
        if response.status_code == 200:
            data_json = response.json()

            if isinstance(data_json, list) and len(data_json) > 1:
                file_contents = ""
                for index, result in enumerate(data_json, 1):
                    file_contents += f"RESULTADO {index}:\n\n• NOME: {result['nome'].upper()}\n• CPF: {result['cpf']}\n• DATA DE NASCIMENTO: {result['nascimento']}\n• NOME DO PAI: {result['pai']}\n\n"

                file_contents += "Whois Alien © All Rights Reserved\n"

                file = io.StringIO(file_contents)
                file.seek(0)

                await ctx.send(file=discord.File(file, filename="resultados.txt"))
            elif isinstance(data_json, dict) or (isinstance(data_json, list) and len(data_json) == 1):
                result = data_json[0] if isinstance(data_json, list) else data_json

                embed = discord.Embed(title='')
                embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤCONSULTA DE NOME DO PAIㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

                embed.add_field(name='• NOME', value=result.get('nome').upper() or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• CPF', value=result.get('cpf') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• DATA DE NASCIMENTO', value=result.get('nascimento') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• NOME DO PAI', value=result.get('pai') or 'SEM INFORMAÇÃO', inline=False)

                embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)
                embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="")
            embed.set_author(name=f'ㅤㅤㅤNOME DO PAI NÃO ENCONTRADO!ㅤㅤㅤ', icon_url='')
            await ctx.send(embed=embed)

    except Exception as e:       
        embed.set_author(name='ㅤㅤㅤㅤ👽 CONSULTA PELO NOME DO PAI', icon_url='')
        embed.add_field(name="Use o comando: `./pai` e o nome do {PAI} que deseja.", value='*Exemplo: `./pai` Fulano De Jesus Matos*', inline=False)

        await ctx.send(embed=embed)

@client.command()
async def telefone(ctx, *, telefone=None):

    if not telefone:
        embed = discord.Embed(title="")
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE TELEFONE', icon_url='')
        embed.add_field(name="Use o comando: `./telefone` e o {TELEFONE} que deseja.", value='Exemplo: `./telefone` 11987654321', inline=False)
        await ctx.send(embed=embed)
        return

    telefone_formatado = telefone.strip().replace(' ', '%20')
    data = f"http://127.0.0.1:44340/alienlabs/api/database/phone/search?telefone={telefone_formatado}"

    headers = {"apikey": API_KEY}

    response = requests.get(data, headers=headers)

    try:
        if response.status_code == 200:
            data_json = response.json()

            if isinstance(data_json, list) and len(data_json) > 1:
                file_contents = ""
                for index, result in enumerate(data_json, 1):
                    file_contents += f"RESULTADO {index}:\n\n• TELEFONE: {result['telefone']}\n• NOME: {result['nome'].upper()}\n• CPF/CNPJ: {result['cpf']}\n• LOGRADOURO: {result['rua']}\n• NÚMERO: {result['numero']}\n• COMPLEMENTO: {result['complemento']}\n• BAIRRO: {result['bairro']}\n• CIDADE: {result['cidade']}\n• ESTADO: {result['uf']}\n• CEP: {result['cep']}\n • OPERADORA: {result['operadora']}\n\n"

                file_contents += "Whois Alien © All Rights Reserved\n"

                file = io.StringIO(file_contents)
                file.seek(0)

                await ctx.send(file=discord.File(file, filename="resultados.txt"))
            elif isinstance(data_json, dict) or (isinstance(data_json, list) and len(data_json) == 1):
                result = data_json[0] if isinstance(data_json, list) else data_json

                embed = discord.Embed(title='')
                embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤCONSULTA DE TELEFONEㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

                embed.add_field(name='• TELEFONE', value=result.get('telefone') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• NOME', value=result.get('nome').upper() or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• CPF/CNPJ', value=result.get('cpf') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• LOGRADOURO', value=result.get('rua') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• NÚMERO', value=result.get('numero') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• COMPLEMENTO', value=result.get('complemento') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• BAIRRO', value=result.get('bairro') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• CIDADE', value=result.get('cidade') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• ESTADO', value=result.get('uf') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• CEP', value=result.get('cep') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• OPERADORA', value=result.get('operadora') or 'SEM INFORMAÇÃO', inline=False)

                embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)
                embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"TELEFONE NÃO ENCONTRADO! {response.status_code}")
            await ctx.send(embed=embed)

    except Exception as e:       
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE TELEFONE', icon_url='')
        embed.add_field(name="Use o comando: `./telefone` e o {TELEFONE} que deseja.", value='Exemplo: `./telefone` 11987654321', inline=False)

        await ctx.send(embed=embed)

@client.command()
async def fixo(ctx, *, fixo=None):

    if not fixo:
        embed = discord.Embed(title="")
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE TELEFONE', icon_url='')
        embed.add_field(name="Use o comando: `./fixo` e o {TELEFONE} que deseja.", value='Exemplo: `./fixo` 1833621583', inline=False)

        await ctx.send(embed=embed)
        return


    fixo_formatado = fixo.strip().replace(' ', '%20')
    data = f"http://127.0.0.1:44340/alienlabs/api/database/phone/search?fixo={fixo_formatado}"

    headers = {"apikey": API_KEY}

    response = requests.get(data, headers=headers)

    try:
        if response.status_code == 200:
            data_json = response.json()

            if isinstance(data_json, list) and len(data_json) > 1:
                file_contents = ""
                for index, result in enumerate(data_json, 1):
                    file_contents += f"RESULTADO {index}:\n\n• TELEFONE: {result['telefone']}\n• NOME: {result['nome'].upper()}\n• CPF/CNPJ: {result['cpf']}\n• LOGRADOURO: {result['rua']}\n• NÚMERO: {result['numero']}\n• COMPLEMENTO: {result['complemento']}\n• BAIRRO: {result['bairro']}\n• CIDADE: {result['cidade']}\n• ESTADO: {result['uf']}\n• CEP: {result['cep']}\n • OPERADORA: {result['operadora']}\n\n"

                file_contents += "Whois Alien © All Rights Reserved\n"

                file = io.StringIO(file_contents)
                file.seek(0)

                await ctx.send(file=discord.File(file, filename="resultados.txt"))
            elif isinstance(data_json, dict) or (isinstance(data_json, list) and len(data_json) == 1):
                result = data_json[0] if isinstance(data_json, list) else data_json

                embed = discord.Embed(title='')
                embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤCONSULTA DE TELEFONEㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

                embed.add_field(name='• TELEFONE FIXO', value=result.get('fixo') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• NOME', value=result.get('nome').upper() or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• CPF/CNPJ', value=result.get('cpf') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• LOGRADOURO', value=result.get('rua') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• NÚMERO', value=result.get('numero') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• COMPLEMENTO', value=result.get('complemento') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• BAIRRO', value=result.get('bairro') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• CIDADE', value=result.get('cidade') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• ESTADO', value=result.get('uf') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• CEP', value=result.get('cep') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• OPERADORA', value=result.get('operadora') or 'SEM INFORMAÇÃO', inline=False)

                embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)
                embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"TELEFONE NÃO ENCONTRADO! {response.status_code}")
            await ctx.send(embed=embed)

    except Exception as e:       
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE TELEFONE', icon_url='')
        embed.add_field(name="Use o comando:", value='`./fixo` e o {TELEFONE} que deseja.', inline=False)
        embed.add_field(value='Exemplo: `./fixo` 1833621583', inline=False)

        await ctx.send(embed=embed)


@client.command()
async def email(ctx, *, email=None):

    if not email:

        embed = discord.Embed(title="")
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE E-MAIL', icon_url='')
        embed.add_field(name="Use o comando: `./email` e o {EMAIL} que deseja.", value='*Exemplo: `./email` fulanodetal@gmail.com*', inline=False)
        await ctx.send(embed=embed)
        return


    email_formatado = email.strip().replace(' ', '%20')
    data = f"http://127.0.0.1:44340/alienlabs/api/database/email/search?e-mail={email_formatado}"

    headers = {"apikey": API_KEY}

    response = requests.get(data, headers=headers)

    try:
        if response.status_code == 200:
            data_json = response.json()

            if isinstance(data_json, list) and len(data_json) > 1:
                file_contents = ""
                for index, result in enumerate(data_json, 1):
                    file_contents += f"RESULTADO {index}:\n\n• NOME: {result['nome'].upper()}\n• CPF: {result['cpf']}\n• E-MAIL: {result['e-mail']}\n\n"

                file_contents += "Whois Alien © All Rights Reserved\n"

                file = io.StringIO(file_contents)
                file.seek(0)

                await ctx.send(file=discord.File(file, filename="resultados.txt"))
            elif isinstance(data_json, dict) or (isinstance(data_json, list) and len(data_json) == 1):
                result = data_json[0] if isinstance(data_json, list) else data_json

                embed = discord.Embed(title='')
                embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤCONSULTA DE DADOS POR EMAILㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

                embed.add_field(name='• NOME', value=result.get('nome') or 'SEM INFORMAÇÃO'.upper(), inline=False)
                embed.add_field(name='• CPF', value=result.get('cpf') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• E-MAIL', value=result.get('e-mail') or 'SEM INFORMAÇÃO', inline=False)

                embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)
                embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="")
            embed.set_author(name=f'ㅤㅤㅤE-MAIL NÃO ENCONTRADO!ㅤㅤㅤ', icon_url='')
            await ctx.send(embed=embed)

    except Exception as e:       
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE E-MAIL', icon_url='')
        embed.add_field(name="Use o comando: `./email` e o {EMAIL} que deseja.", value='*Exemplo: `./email` fulanodetal@gmail.com*', inline=False)

        await ctx.send(embed=embed)


@client.command()
async def cep_pessoas(ctx, *, cep_pessoas=None):

    if not cep_pessoas:
        embed = discord.Embed(title="")
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE CEP', icon_url='')
        embed.add_field(name="Use o comando: `./cep` e o {CEP} que deseja.", value='Exemplo: `./cep` 01153000', inline=False)
        await ctx.send(embed=embed)
        return

    cep_pessoas_formatado = cep_pessoas.strip().replace(' ', '%20')
    data = f"http://127.0.0.1:44340/alienlabs/api/database/datasus/search?cep={cep_pessoas_formatado}"

    headers = {"apikey": API_KEY}

    response = requests.get(data, headers=headers)

    try:
        if response.status_code == 200:
            data_json = response.json()

            if isinstance(data_json, list) and len(data_json) > 1:
                file_contents = ""
                for index, result in enumerate(data_json, 1):
                    file_contents += f"RESULTADO {index}:\n\n• NOME: {result['nome'].upper()}\n• CPF: {result['cpf']}\n• DATA DE NASCIMENTO: {result['nascimento']}\n• LOGRADOURO: {result['logradouro']}\n• NUMERO: {result['numero']}\n• CEP: {result['cep']}\n• MUNICIPIO: {result['municipio']}\n\n"

                file_contents += "\nWhois Alien © All Rights Reserved\n"

                file = io.StringIO(file_contents)
                file.seek(0)

                await ctx.send(file=discord.File(file, filename="resultados.txt"))
            elif isinstance(data_json, dict) or (isinstance(data_json, list) and len(data_json) == 1):
                result = data_json[0] if isinstance(data_json, list) else data_json

                embed = discord.Embed(title='')
                embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤCONSULTA DE DADOS POR CEPㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

                embed.add_field(name='• NOME', value=result.get('nome').upper() or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• CPF', value=result.get('cpf') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• DATA DE NASCIMENTO', value=result.get('nascimento') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• LOGRADOURO', value=result.get('logradouro') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• NÚMERO', value=result.get('numero') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• CEP', value=result.get('cep') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• MUNICIPIO', value=result.get('municipio') or 'SEM INFORMAÇÃO', inline=False)

                embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)
                embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"CEP NÃO ENCONTRADO! {response.status_code}")
            await ctx.send(embed=embed)

    except Exception as e:       
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE CEP', icon_url='')
        embed.add_field(name="Use o comando: `./cep` e o {CEP} que deseja.", value='Exemplo: `./cep` 01153000', inline=False)

        await ctx.send(embed=embed)

@client.command()
async def placa(ctx, *, placa=None):

    if not placa:

        embed = discord.Embed(title="")
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE PLACA', icon_url='')
        embed.add_field(name="Use o comando: `./placa` e a {PLACA} que deseja.", value='Exemplo: `./placa` ABC1234', inline=False)
        await ctx.send(embed=embed)
        return

    placa_formatada = placa.strip().upper().replace('-', '')
    url = f"http://127.0.0.1:44340/alienlabs/api/database/vehicle/search?placa={placa_formatada}"

    headers = {"apikey": API_KEY}

    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            data = response.json()

            if len(data) > 0:
                placa_veiculo = data[0] 
                modelo_veiculo = placa_veiculo.get('modelo_veiculo', {})

                embed = discord.Embed(title="")
                embed.set_author(
                    name=f'ㅤㅤㅤㅤㅤㅤㅤCONSULTA DE PLACA - INFORMAÇÕES GERAISㅤㅤㅤㅤㅤㅤㅤㅤ',icon_url='')
                embed.set_thumbnail(url=placa_veiculo.get('logo_marca', ''))

                embed.add_field(name="Placa do veículo", value=placa_veiculo.get('placa', 'Desconhecido'), inline=True)
                embed.add_field(name="Marca", value=modelo_veiculo.get('marca', 'Desconhecido'), inline=True)
                embed.add_field(name="Modelo", value=modelo_veiculo.get('modelo', 'Desconhecido'), inline=True)
                embed.add_field(name="Cor do Veículo", value=placa_veiculo.get('cor_veiculo', 'Desconhecido'), inline=True)
                embed.add_field(name="Grupo do Modelo", value=modelo_veiculo.get('grupo_modelo_veiculo', 'Desconhecido'), inline=True)
                embed.add_field(name="Segmento", value=modelo_veiculo.get('segmento', 'Desconhecido'), inline=True)
                embed.add_field(name="Sub-Segmento", value=modelo_veiculo.get('sub_segmento', 'Desconhecido'), inline=True)
                embed.add_field(name="Tipo de Veículo", value=placa_veiculo.get('tipo_veiculo', 'Desconhecido'), inline=True)
                embed.add_field(name="Espécie do Veículo", value=placa_veiculo.get('especie_veiculo', 'Desconhecido'), inline=True)
                embed.add_field(name="Tipo de Montagem", value=placa_veiculo.get('tipo_montagem', 'Desconhecido'), inline=True)
                embed.add_field(name="Situação do Chassi", value=placa_veiculo.get('situacao_chassi', 'Desconhecido'), inline=True)
                embed.add_field(name="Chassi", value=placa_veiculo.get('chassi', 'Desconhecido'), inline=True)
                embed.add_field(name="Renavam", value=placa_veiculo.get('renavam', 'Desconhecido'), inline=True)
                embed.add_field(name="Número do motor", value=placa_veiculo.get('motor', 'Desconhecido'), inline=True)
                embed.add_field(name="Combustível", value=placa_veiculo.get('combustivel', 'Desconhecido'), inline=True)
                embed.add_field(name="Linha", value=placa_veiculo.get('linha', 'Desconhecido'), inline=True)
                embed.add_field(name="Situação do veículo", value=placa_veiculo.get('situacao_veiculo', 'Desconhecido'), inline=True)
                embed.add_field(name="Tipo DOC. Proprietário", value=placa_veiculo.get('tipo_doc_prop', 'Desconhecido'), inline=True)
                embed.add_field(name="Município", value=placa_veiculo.get('municipio', 'Desconhecido'), inline=True)
                embed.add_field(name="UF da Placa", value=placa_veiculo.get('uf_placa', 'Desconhecido'), inline=True)
                embed.add_field(name="Ano de Fabricação", value=placa_veiculo.get('ano_fabricacao', 'Desconhecido'), inline=True)
                embed.add_field(name="Ano do Modelo", value=placa_veiculo.get('ano_modelo', 'Desconhecido'), inline=True)
                embed.add_field(name="Nacionalidade", value=placa_veiculo.get('nacionalidade', 'Desconhecido'), inline=True)
                embed.add_field(name="Data de atualização", value=placa_veiculo.get('data_atualizacao', 'Desconhecido'), inline=True)
                embed.add_field(name="Última atualização", value=placa_veiculo.get('ultima_atualizacao', 'Desconhecido'), inline=True)

                embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved')
                await ctx.send(embed=embed)

                embed = discord.Embed(title="")
                embed.set_author(
                    name=f'ㅤㅤㅤㅤㅤㅤㅤCONSULTA DE PLACA - INFORMAÇÕES GERAISㅤㅤㅤㅤㅤㅤㅤㅤ',icon_url='')
                embed.set_thumbnail(url=placa_veiculo.get('placa_png', ''))

                embed.add_field(name="Cilindradas", value=placa_veiculo.get('cilindradas', 'Desconhecido'), inline=True)
                embed.add_field(name="Potência", value=placa_veiculo.get('potencia', 'Desconhecido'), inline=True)
                embed.add_field(name="Carroceria", value=placa_veiculo.get('carroceria', 'Desconhecido'), inline=True)
                embed.add_field(name="Tipo de Carroceria", value=placa_veiculo.get('tipo_carroceria', 'Desconhecido'), inline=True)
                embed.add_field(name="Peso Bruto Total", value=placa_veiculo.get('peso_bruto_total', 'Desconhecido'), inline=True)
                embed.add_field(name="Capacidade de Carga", value=placa_veiculo.get('capacidade_carga', 'Desconhecido'), inline=True)
                embed.add_field(name="Capacidade Máxima de Tração", value=placa_veiculo.get('cap_maxima_tracao', 'Desconhecido'), inline=True)
                embed.add_field(name="Eixo traseiro", value=placa_veiculo.get('eixo_traseiro_dif', 'Desconhecido'), inline=True)
                embed.add_field(name="Terceiro eixo", value=placa_veiculo.get('terceiro_eixo', 'Desconhecido'), inline=True)
                embed.add_field(name="Quantidade de eixos", value=placa_veiculo.get('eixos', 'Desconhecido'), inline=True)
                embed.add_field(name="Quantidade de passageiros", value=placa_veiculo.get('quantidade_passageiro', 'Desconhecido'), inline=True)
                embed.add_field(name="Caixa de cambio", value=placa_veiculo.get('caixa_cambio', 'Desconhecido'), inline=True)

                embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved')
                await ctx.send(embed=embed)

                embed = discord.Embed(title="")
                embed.set_author(
                    name=f'ㅤㅤㅤㅤCONSULTA DE PLACA - INFORMAÇÕES TRIBUTÁRIASㅤㅤㅤㅤㅤㅤㅤㅤ',icon_url='')
                embed.set_thumbnail(url="https://i.imgur.com/TKLsWNT.png")

                embed.add_field(name="ID do Veículo", value=placa_veiculo.get('id_veiculo', 'Desconhecido'), inline=True)
                embed.add_field(name="Tipo de Documento Importadora", value=placa_veiculo.get('tipo_doc_importadora', 'Desconhecido'), inline=True)
                embed.add_field(name="CNPJ Importadora", value=placa_veiculo.get('ident_importadora', 'Desconhecido'), inline=True)
                embed.add_field(name="Declaração de Imposto", value=placa_veiculo.get('di', 'Desconhecido'), inline=True)
                embed.add_field(name="Reg. Declaração de Imposto", value=placa_veiculo.get('registro_di', 'Desconhecido'), inline=True)
                embed.add_field(name="Unidade da Secr. da RFB", value=placa_veiculo.get('uf_faturado', 'Desconhecido'), inline=True)
                embed.add_field(name="Limite Restrição Tributária", value=placa_veiculo.get('limite_restricao_trib', 'Desconhecido'), inline=True)
                embed.add_field(name="Comprado em", value=placa_veiculo.get('faturado', 'Desconhecido'), inline=True)
                embed.add_field(name="Tipo de Documento Faturado", value=placa_veiculo.get('tipo_doc_faturado', 'Desconhecido'), inline=True)
                embed.add_field(name="UF de faturamento", value=placa_veiculo.get('uf_faturado', 'Desconhecido'), inline=True)
                embed.add_field(name="Placa modelo antigo", value=placa_veiculo.get('placa_modelo_antigo', 'Desconhecido'), inline=True)
                embed.add_field(name="Placa modelo novo", value=placa_veiculo.get('placa_modelo_novo', 'Desconhecido'), inline=True)
                embed.add_field(name="Restrição 1", value=placa_veiculo.get('restricao_1', 'Desconhecido'), inline=True)
                embed.add_field(name="Restrição 2", value=placa_veiculo.get('restricao_2', 'Desconhecido'), inline=True)
                embed.add_field(name="Restrição 3", value=placa_veiculo.get('restricao_3', 'Desconhecido'), inline=True)
                embed.add_field(name="Restrição 4", value=placa_veiculo.get('restricao_4', 'Desconhecido'), inline=True)
                embed.add_field(name="Proprietário", value=placa_veiculo.get('proprietario_info', {}).get('proprietario', 'Desconhecido'), inline=True)
                embed.add_field(name="CPF/CNPJ", value=placa_veiculo.get('proprietario_info', {}).get('cpf', 'Desconhecido'), inline=True)

                embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved')
                await ctx.send(embed=embed)

            else:
                embed = discord.Embed(title="")
                embed.set_author(name='PLACA NÃO ENCONTRADAㅤㅤㅤ', icon_url='')
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="")
            embed.set_author(name='ㅤㅤㅤPLACA NÃO ENCONTRADAㅤㅤㅤ', icon_url='')
            await ctx.send(embed=embed)

    except Exception as e:

        embed = discord.Embed(title="")
        embed.set_author(name=f'ㅤㅤㅤErro inesperado: {e}ㅤㅤㅤ', icon_url='')
        await ctx.send(embed=embed)

@client.command()
async def foto(ctx, *, foto=None):
    if not foto:
        embed = discord.Embed(title="")
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE FOTO', icon_url='')
        embed.add_field(name="Use o comando: `./foto` e o {CPF} que deseja.", value='*Exemplo: `./foto` 123.456.789-12*', inline=False)
        await ctx.send(embed=embed)
        return

    cpf_formatado = foto.strip()
    data = f"http://127.0.0.1:44340//alienlabs/api/database/fotos/rj/search?CPF={cpf_formatado}"

    headers = {"apikey": API_KEY}
    response = requests.get(data, headers=headers)

    try:
        if response.status_code == 200:
            data = response.json()

            if len(data) > 0:
                cpf_info = data[0]
                foto_base64 = cpf_info.get("FOTO")

                embed = discord.Embed(title='')
                embed.set_author(name='ㅤㅤㅤCONSULTA DE FOTO RJㅤㅤㅤ', icon_url='')
                embed.add_field(name="• NOME", value=cpf_info.get('NOME_COMPLETO') or 'SEM INFORMAÇÃO'.upper(), inline=False)
                embed.add_field(name='• CPF', value=cpf_info.get('CPF') or 'SEM INFORMAÇÃO', inline=False)
                embed.add_field(name='• NASCIMENTO', value=cpf_info.get('DT_NASCIMENTO') or 'SEM INFORMAÇÃO', inline=False)

                file = None
                if foto_base64:
                    # Decodifica a imagem
                    image_bytes = base64.b64decode(foto_base64)
                    image_file = BytesIO(image_bytes)
                    image_file.seek(0)

                    # Cria o arquivo para enviar
                    file = discord.File(image_file, filename="foto.png")
                    embed.set_image(url="attachment://foto.png")  # Define a imagem do embed usando o anexo

                embed.add_field(name='', value='', inline=False)
                embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
                await ctx.send(embed=embed, file=file if file else None)

        else:
            embed = discord.Embed(title="")
            embed.set_author(name=f'ㅤㅤㅤPESSOA NÃO ENCONTRADA!ㅤㅤㅤ', icon_url='')
            await ctx.send(embed=embed)

    except Exception as e:
        embed = discord.Embed(title="")
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE FOTO', icon_url='')
        embed.add_field(name="Use o comando: `./foto` e o {CPF} que deseja.", value='*Exemplo: `/foto` 123.456.789-12*', inline=False)
        await ctx.send(embed=embed)

@client.command()
async def cnpj(ctx, cnpj=None):

    if not cnpj:

        embed = discord.Embed(title="")
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DE CNPJ', icon_url='')
        embed.add_field(name="Use o comando: `./cnpj` e a {CNPJ} que deseja.", value='Exemplo: `./cnpj` 00000000000191', inline=False)
        await ctx.send(embed=embed)
        return


    cnpj = re.sub(r"[.\-\/]", "", cnpj)

    url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
    response = requests.get(url)
    data = response.json()


    def verificar_erro_api(data):
        if data.get("status") == "ERROR":
            return data.get("message", "Erro desconhecido.")
        return None

    erro = verificar_erro_api(data)
    if erro:
        embed = discord.Embed(title='')

        embed.set_author(name=f'ㅤㅤㅤCNPJ NÃO ENCONTRADOㅤㅤㅤ', icon_url='')
        return await ctx.send(embed=embed)

    def formatar_qualificacao(qualificacao):

        return re.sub(r"^\d+-", "", qualificacao).strip()


    def verificar_campo(campo, padrao="Sem informação"):
        return campo if campo else padrao

    def buscar_informacoes_socio(nome, qualificacao):
        try:
            api_url = f"http://127.0.0.1:44340/alienlabs/api/database/serasa/basic/search?nome={nome}"
            headers = {"apikey": API_KEY}
            resposta = requests.get(api_url, headers=headers).json()

            if len(resposta) == 1:
                socio = resposta[0]
                return f"- **Nome**: {socio['nome'].upper()}\n- **CPF**: {socio['cpf']}\n- **Qualificação**: {qualificacao}"
            elif len(resposta) > 1:
                return f"- **Nome**: {nome}\n- **Qualificação**: {qualificacao}"
            else:
                return f"- **Nome**: {nome}\n- **Qualificação**: {qualificacao}"
        except Exception as e:

            return f"- **Nome**: {nome}\n- **Qualificação**: {qualificacao}"


    try:
        atividade_principal = data.get("atividade_principal", [])
        if atividade_principal:
            atividade = f"{verificar_campo(atividade_principal[0]['code'])} - {verificar_campo(atividade_principal[0]['text'])}"

        endereco = f"{verificar_campo(data.get('logradouro'))}, {verificar_campo(data.get('numero'))}, {verificar_campo(data.get('bairro'))}, {verificar_campo(data.get('municipio'))} - {verificar_campo(data.get('uf'))}, - {verificar_campo(data.get('cep'))}"
        contato = f"Email: {verificar_campo(data.get('email'))}\nTelefone: {verificar_campo(data.get('telefone'))}"

        embed = discord.Embed(title='')
        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE CNPJㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

        embed.add_field(name="• CNPJ", value=verificar_campo(data.get("cnpj")), inline=False)
        embed.add_field(name="• NOME DA EMPRESA", value=verificar_campo(data.get("nome")), inline=False)
        embed.add_field(name="• NOME FANTASIA", value=verificar_campo(data.get("fantasia")), inline=False)
        embed.add_field(name="• DATA DE ABERTURA", value=verificar_campo(data.get("abertura")), inline=False)
        embed.add_field(name="• SITUAÇÃO DA EMPRESA", value=verificar_campo(data.get("situacao")), inline=False)
        embed.add_field(name="• CAPITAL SOCIAL", value=f"R$ {verificar_campo(data.get('capital_social'))}", inline=False)
        embed.add_field(name="• TIPO", value=verificar_campo(data.get("tipo")), inline=False)
        embed.add_field(name="• PORTE", value=verificar_campo(data.get("porte")), inline=False)
        embed.add_field(name="• NATUREZA JURÍDICA", value=verificar_campo(data.get("natureza_juridica")), inline=False)
        embed.add_field(name="• ATIVIDADE PRINCIPAL", value=atividade, inline=False)
        embed.add_field(name="• ENDEREÇO", value=endereco, inline=False)    
        embed.add_field(name="• COMPLEMENTO DO ENDEREÇO", value=verificar_campo(data.get("complemento")), inline=False)
        embed.add_field(name="• CONTATOS DA EMPRESA", value=contato, inline=False)
        embed.add_field(name="• ÚLTIMA ATUALIZAÇÃO", value=verificar_campo(data.get("ultima_atualizacao")), inline=False)
        embed.add_field(name="• STATUS DA EMPRESA", value=verificar_campo(data.get("status")), inline=False)
        embed.add_field(name="• ENTES FEDERAIS", value=verificar_campo(data.get("efr")), inline=False)
        embed.add_field(name="• MOTIVO SITUAÇÃO", value=verificar_campo(data.get("motivo_situacao")), inline=False)
        embed.add_field(name="• SITUAÇÃO ESPECIAL", value=verificar_campo(data.get("situacao_especial")), inline=False)
        embed.add_field(name="• DATA SITUAÇÃO ESPECIAL", value=verificar_campo(data.get("data_situacao_especial")), inline=False)
        embed.add_field(name="• SÓCIOS/ADMINISTRADORES", value="", inline=False)

        qsa = data.get("qsa", [])

        if qsa:

            qsa_limited = qsa[:15]

            if len(qsa) > 15:
                socios_nomes = "\n".join([f"{verificar_campo(s['nome'])}" for s in qsa_limited])
                embed.add_field(name="", value=socios_nomes, inline=False)
                embed.add_field(name="• Aviso", value=f"Exibindo os primeiros 15 de {len(qsa)} sócios.", inline=False)
            else:
                socios_info = []
                for socio in qsa_limited:
                    nome_socio = verificar_campo(socio.get('nome'))
                    qualificacao_socio = formatar_qualificacao(verificar_campo(socio.get('qual')))
                    info_socio = buscar_informacoes_socio(nome_socio, qualificacao_socio)
                    if info_socio:
                        socios_info.append(info_socio)

                if socios_info:
                    socios_texto = "\n\n".join(socios_info)
                    embed.add_field(name="", value=socios_texto, inline=False)
                else:
                    socios_nomes = "\n".join([f"- **Nome**: {verificar_campo(s['nome'])}\n- **Qualificação**: {verificar_campo(s['qual'])}" for s in qsa_limited])
                    embed.add_field(name="", value=socios_nomes, inline=False)
        else:
            embed.add_field(name="", value="Nenhum sócio proprietário encontrado.", inline=False)


        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

        await ctx.send(embed=embed)
        return

    except Exception as e:
        embed = discord.Embed(title='Erro na consulta')
        embed.add_field(name="Detalhes", value=str(e), inline=False)
        return await ctx.send(embed=embed)


@client.command()
async def ip(ctx, ip=None):

    if not ip:
        embed = discord.Embed(title='')
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO IPㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `./ip` e o {IP} que deseja.", value='*Exemplo: `./ip` 127.0.0.1*', inline=False)
        await ctx.send(embed=embed)
        return

    data = requests.get(f"https://ipwhois.app/json/{ip}").json()

    MAPS_API = os.getenv("GOOGLE_MAPS_API_KEY")

    latitude = data.get('latitude')
    longitude = data.get('longitude')

    maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"
    mapa_url = f"https://maps.googleapis.com/maps/api/staticmap?center={latitude},{longitude}&zoom=15&size=700x250&markers=color:red%7C{latitude},{longitude}&key={MAPS_API}"


    country_code_icon = data.get('country_code').lower()

    try:
        embed = discord.Embed(title='')

        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE IPㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
        embed.add_field(name="\n\n", value="\n\n", inline=False)
        embed.add_field(name="IP", value=data.get('ip', 'Sem informação'), inline=True)
        embed.add_field(name="TIPO", value=data.get('type', 'Sem informação'), inline=True)
        embed.add_field(name="STATUS", value=data.get('success', 'Sem informação'), inline=True)
        embed.add_field(name="CIDADE", value=data.get('city', 'Sem informação'), inline=True)
        embed.add_field(name="ESTADO", value=data.get('region', 'Sem informação'), inline=True)
        embed.add_field(name="PAÍS", value=data.get('country', 'Sem informação'), inline=True)
        embed.add_field(name="CONTINENTE", value=data.get('continent_code', 'Sem informação'), inline=True)
        embed.add_field(name="CÓD. DO PAIS", value=data.get('country_code', 'Sem informação'), inline=True)
        embed.add_field(name="LOCALIZAÇÃO", value=f"[{latitude},{longitude}]({maps_link})", inline=True)
        embed.add_field(name="PROVEDOR", value=data.get('isp', 'Sem informação'), inline=True)
        embed.add_field(name="ORG", value=data.get('org', 'Sem informação'), inline=True)
        embed.add_field(name="ASN", value=data.get('asn', 'Sem informação'), inline=True)
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="INFORMAÇÕES EXTRAS", value="", inline=False)
        embed.add_field(name="CÓD. DO CONTINENTE", value=data.get('continent_code', 'Sem informação'), inline=True)
        embed.add_field(name="CAPITAL DO PAÍS", value=data.get('country_capital', 'Sem informação'), inline=True)
        embed.add_field(name="DDI", value=data.get('country_phone', 'Sem informação'), inline=True)
        embed.add_field(name="MOEDA", value=data.get('currency', 'Sem informação'), inline=True)
        embed.add_field(name="VALOR DA MOEDA", value=data.get('currency_rates', 'Sem informação'), inline=True)
        embed.add_field(name="COD. DA MOEDA", value=data.get('currency_code', 'Sem informação'), inline=True)
        embed.add_field(name="FUSO HORÁRIO", value=data.get('timezone', 'Sem informação'), inline=True)
        embed.add_field(name="OFFSET", value=data.get('timezone_name', 'Sem informação'), inline=True)
        embed.add_field(name="GMT", value=data.get('timezone_gmt', 'Sem informação'), inline=True)

        embed.set_thumbnail(url=f"https://flagcdn.com/w640/{country_code_icon}.png")
        embed.set_image(url=mapa_url)

        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

        await ctx.send(embed=embed)

        return
    except Exception:
        pass

@client.command()
async def covid(ctx, covid = None):

    data = requests.get(f"https://covid19-brazil-api.vercel.app/api/report/v1/brazil/uf/{covid}").json()

    try:
        embed = discord.Embed(title='')

        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE COVID19ㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

        embed.add_field(name="• ESTADO", value=data.get('state', 'Sem informação'), inline=False)
        embed.add_field(name="• CASOS", value=data.get('cases', 'Sem informação'), inline=False)
        embed.add_field(name="• MORTES", value=data.get('deaths', 'Sem informação'), inline=False)
        embed.add_field(name="• SUSPEITOS", value=data.get ('suspects', 'Sem informação'), inline=False)
        embed.add_field(name="• DESCARTADOS", value=data.get('refuses', 'Sem informação'), inline=False)
        embed.add_field(name="• ÚLTIMA ATUALIZAÇÃO", value=data.get('datetime', 'Sem informação'), inline=False)

        embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

        await ctx.send(embed=embed)
        
        return
    except Exception:
        pass

        embed = discord.Embed(title='')

    if (covid == None):
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO COVIDㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `./covid` e o {ESTADO} que deseja.", value='*Exemplo*: `./covid SP`', inline=False)
        embed.add_field(name="Observação:", value='*Utilize apenas a sigla do estado correspondente!*', inline=False)
        embed.add_field(name="Estados Brasileiros com suas respectivas siglas:", value='Acre - `AC`\nAlagoas - `AL`\nAmazonas - `AM`\nBahia - `BA`\nCeará - `CE`\nDistrito Federal - `DF`\nEspírito Santo - `ES`\nGoiás - `GO`\nMaranhão - `MA`\nMato Grosso - `MT`\nMato Grosso do Sul - `MS`\nMinas Gerais - `MG`\nPará - `PA`\nParaíba - `PB`\nParaná - `PR`\nPernambuco - `PE`\nPiauí - `PI`\nRio de Janeiro - `RJ`\nRio Grande do Norte - `RN`\nRio Grande do Sul - `RS`\nRondônia - `RO`\nRoraima	- `RR`\nSanta Catarina - `SC`\nSão Paulo - `SP`\nSergipe - `SE`\nTocantins - `TO`\n', inline=False)
        return await ctx.send(embed=embed)
    else:
       embed.set_author(name='ㅤㅤㅤㅤㅤㅤESTADO INVÁLIDOㅤㅤㅤ', icon_url='')
       return await ctx.send(embed=embed)


@client.command()
async def cep(ctx, cep=None):

    MAPS_API = os.getenv("GOOGLE_MAPS_API_KEY")

    if not cep:
        embed = discord.Embed(title='')
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO CEP', icon_url='')
        embed.add_field(name="Use o comando: `/cep` e o {CEP} que deseja.", value='*Exemplo*: `/cep 70150904`', inline=False)
        embed.add_field(name="Observação:", value='*Não utilize pontos, hifens e caracteres especiais*', inline=False)      
        await ctx.send(embed=embed)
        return

    # Requisição para a API de CEP
    data = requests.get(f"https://cep.awesomeapi.com.br/json/{cep}").json()

    if 'erro' in data:
        embed = discord.Embed(title='')
        embed.set_author(name='CEP NÃO ENCONTRADO', icon_url='')
        await ctx.send(embed=embed)
        return

    latitude = data.get('lat')
    longitude = data.get('lng')

    maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"
    mapa_url = f"https://maps.googleapis.com/maps/api/staticmap?center={latitude},{longitude}&zoom=15&size=600x300&markers=color:red%7C{latitude},{longitude}&key={MAPS_API}"

    embed = discord.Embed(title='')

    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE CEPㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='') #----->> TÍTULO DO CÓDIGO

    embed.add_field(name="• CEP", value=data.get('cep', 'Sem Informação'), inline=False)
    embed.add_field(name="• NOME DA RUA", value=data.get('address', 'Sem Informação'), inline=False)
    embed.add_field(name="• BAIRRO", value=data.get('district', 'Sem Informação'), inline=False)
    embed.add_field(name="• CIDADE", value=data.get('city', 'Sem Informação'), inline=False)
    embed.add_field(name="• ESTADO", value=data.get('state', 'Sem Informação'), inline=False)
    embed.add_field(name="• IBGE", value=data.get('city_ibge', 'Sem Informação'), inline=False)
    embed.add_field(name="• DDD", value=data.get('ddd', 'Sem Informação'), inline=False)
    embed.add_field(name="• LOCALIZAÇÃO", value=f"[{latitude},{longitude}]({maps_link})", inline=False)
    embed.set_image(url=mapa_url)  # Adiciona a imagem do mapa

    embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved', icon_url='')

    await ctx.send(embed=embed)

@client.command()
async def banco(ctx, banco=None):

    if banco is None:

        embed = discord.Embed(title='')
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO BANCOㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `./banco` e o {CÓDIGO DO BANCO}", value='*Exemplo*: `./banco 237`', inline=False)
        embed.add_field(name="Observação:", value='*Utilize apenas o código bancário correspondente!*', inline=False)
        return await ctx.send(embed=embed)

    try:
        data = requests.get(f"https://brasilapi.com.br/api/banks/v1/{banco}").json()

        embed = discord.Embed(title='')

        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE BANCOㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

        embed.add_field(name="• ISPB", value=data['ispb'], inline=False)
        embed.add_field(name="• NOME DO BANCO", value=data['name'], inline=False)
        embed.add_field(name="• CÓDIGO DO BANCO", value=data['code'], inline=False)
        embed.add_field(name="• INFORMAÇÕES ADICIONAIS", value=data['fullName'], inline=False)
        embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)

        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
        await ctx.send(embed=embed)

    except Exception:
        embed = discord.Embed(title='')
        embed.set_author(name='ㅤㅤCÓDIGO BANCÁRIO NÃO ENCONTRADOㅤㅤ', icon_url='')
        return await ctx.send(embed=embed)

@client.command()
async def bin(ctx, bin):

    try:
        data = f"https://lookup.binlist.net/{bin}"

        response = requests.get(data)

        if response.status_code == 200:
            data = response.json()

            embed = discord.Embed(title='')

            embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE BINㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

            embed.add_field(name="• BIN", value=data.get("{bin}"), inline=False)
            embed.add_field(name="• MODELO", value=data.get("type", "Desconhecido"), inline=False)
            embed.add_field(name="• BANDEIRA", value=data.get("scheme", "Desconhecido"), inline=False)
            embed.add_field(name="• NÍVEL", value=data.get("brand", "Desconhecido"), inline=False)
            embed.add_field(name="• PAÍS", value=data.get("country", {}).get("name", "Desconhecido"), inline=False)
            embed.add_field(name="• SIGLA DO PAÍS", value=data.get("country", {}).get("alpha2", "Desconhecido"), inline=False)
            embed.add_field(name="• BANCO", value=data.get("bank", {}).get("name", "Desconhecido"), inline=False)
            embed.add_field(name="• SITE DO BANCO", value=data.get("bank", {}).get("url", "Desconhecido"), inline=False)
            embed.add_field(name="• TELEFONE", value=data.get("bank", {}).get("phone", "Desconhecido"), inline=False)
            embed.add_field(name="• CIDADE", value=data.get("bank", {}).get("city", "Desconhecido"), inline=False)

            embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)                 
            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

            await ctx.send(embed=embed)
 
        else:
            embed = discord.Embed(title='') 
            embed.set_author(name='ㅤㅤㅤBIN NÃO ENCONTRADAㅤㅤㅤ', icon_url='')
            await ctx.send(embed=embed)

    except Exception as e: 

        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO BINㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `./bin` e a {BIN} que deseja.", value='*Exemplo*: `./bin 522840`', inline=False)
        embed.add_field(name="Observação:", value='*Não utilize pontos, hifens e caracteres especiais*', inline=False)     

        await ctx.send(embed=embed)

@client.command()
async def site(ctx, ip=None):

    if not ip:
        embed = discord.Embed(title='')
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO IPㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `./ip` e o {IP} que deseja.", value='*Exemplo: `./ip` 127.0.0.1*', inline=False)
        await ctx.send(embed=embed)
        return

    data = requests.get(f"https://ipwhois.app/json/{site}").json()

    MAPS_API = os.getenv("GOOGLE_MAPS_API_KEY")

    latitude = data.get('latitude')
    longitude = data.get('longitude')

    maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"
    mapa_url = f"https://maps.googleapis.com/maps/api/staticmap?center={latitude},{longitude}&zoom=15&size=700x250&markers=color:red%7C{latitude},{longitude}&key={MAPS_API}"

    country_code_icon = data.get('country_code').lower()

    try:
        embed = discord.Embed(title='')

        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE SITEㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
        embed.add_field(name="\n\n", value="\n\n", inline=False)
        embed.add_field(name="IP", value=data.get('ip', 'Sem informação'), inline=True)
        embed.add_field(name="TIPO", value=data.get('type', 'Sem informação'), inline=True)
        embed.add_field(name="STATUS", value=data.get('success', 'Sem informação'), inline=True)
        embed.add_field(name="CIDADE", value=data.get('city', 'Sem informação'), inline=True)
        embed.add_field(name="ESTADO", value=data.get('region', 'Sem informação'), inline=True)
        embed.add_field(name="PAÍS", value=data.get('country', 'Sem informação'), inline=True)
        embed.add_field(name="CONTINENTE", value=data.get('continent_code', 'Sem informação'), inline=True)
        embed.add_field(name="CÓD. DO PAIS", value=data.get('country_code', 'Sem informação'), inline=True)
        embed.add_field(name="LOCALIZAÇÃO", value=f"[{latitude},{longitude}]({maps_link})", inline=True)
        embed.add_field(name="PROVEDOR", value=data.get('isp', 'Sem informação'), inline=True)
        embed.add_field(name="ORG", value=data.get('org', 'Sem informação'), inline=True)
        embed.add_field(name="ASN", value=data.get('asn', 'Sem informação'), inline=True)
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="INFORMAÇÕES EXTRAS", value="", inline=False)
        embed.add_field(name="CÓD. DO CONTINENTE", value=data.get('continent_code', 'Sem informação'), inline=True)
        embed.add_field(name="CAPITAL DO PAÍS", value=data.get('country_capital', 'Sem informação'), inline=True)
        embed.add_field(name="DDI", value=data.get('country_phone', 'Sem informação'), inline=True)
        embed.add_field(name="MOEDA", value=data.get('currency', 'Sem informação'), inline=True)
        embed.add_field(name="VALOR DA MOEDA", value=data.get('currency_rates', 'Sem informação'), inline=True)
        embed.add_field(name="COD. DA MOEDA", value=data.get('currency_code', 'Sem informação'), inline=True)
        embed.add_field(name="FUSO HORÁRIO", value=data.get('timezone', 'Sem informação'), inline=True)
        embed.add_field(name="OFFSET", value=data.get('timezone_name', 'Sem informação'), inline=True)
        embed.add_field(name="GMT", value=data.get('timezone_gmt', 'Sem informação'), inline=True)

        embed.set_thumbnail(url=f"https://flagcdn.com/w640/{country_code_icon}.png")
        embed.set_image(url=mapa_url)

        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

        await ctx.send(embed=embed)

        return
    except Exception:
        pass


@client.command()
async def cotacao(ctx, cotacao = None):

    if cotacao is None:
        
        embed = discord.Embed(title='')

        embed.set_author(name='ㅤㅤㅤㅤ   👽 COMANDO COTAÇÃOㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `/cotacao` e o {PAR DE MOEDA} que deseja", value='*Exemplo*: `/cotacao BRL-USD`', inline=False)
        embed.add_field(name="Observação:", value='*O par precisa ser separado com hifen*', inline=False)   
        return await ctx.send(embed=embed)

    data = requests.get(f"https://economia.awesomeapi.com.br/last/{cotacao}").json()
    coin_name = cotacao.replace("-", "")

    if coin_name in data:
        
        embed = discord.Embed(title='')

        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCOTAÇÃO DE MOEDASㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

        embed.add_field(name="• MOEDA A COMPARAR", value=data[coin_name]["code"], inline=False)
        embed.add_field(name="• MOEDA A SER COMPARADA", value=data[coin_name]["codein"], inline=False)
        embed.add_field(name="• NOME DAS PARIEDADES", value=data[coin_name]["name"], inline=False)
        embed.add_field(name="• MÁXIMA DO DIA", value=data[coin_name]["high"], inline=False)
        embed.add_field(name="• MÍNIMA DO DIA", value=data[coin_name]["low"], inline=False)
        embed.add_field(name="• VARIAÇÃO", value=data[coin_name]["varBid"], inline=False)
        embed.add_field(name="• PORCENTAGEM DE VARIAÇÃO", value=data[coin_name]["pctChange"], inline=False)
        embed.add_field(name="• COMPRA", value=data[coin_name]["bid"], inline=False)
        embed.add_field(name="• VENDA", value=data[coin_name]["ask"], inline=False)
        embed.add_field(name="• ATUALIZAÇÃO", value=data[coin_name]["create_date"], inline=False)
        embed.add_field(name="Observação", value=f"Pode haver alguma pequena diferença na cotação das moedas!!! Grande parte dos sites que fornecem essa informação informa margem de erros, então vale sempre conferir a informação mais precisa possível no TradingView, O site está disponível abaixo:\nhttps://br.tradingview.com/", inline=False)

        embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)             
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
    else:
        embed = discord.Embed(title='')
        embed.set_author(name='ㅤㅤCOTAÇÃO DE MOEDAS INVÁLIDAㅤㅤㅤ', icon_url='')

    embed.set_author(name='ㅤㅤCOTAÇÃO DE MOEDAS INVÁLIDAㅤㅤㅤ', icon_url='')

    await ctx.send(embed=embed)

@client.command() 
async def ddd(ctx, ddd = None):

    if ddd is None:
        
        embed = discord.Embed(title='') 
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO DDDㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `./ddd` e o {DDD} que deseja", value='*Exemplo*: `./ddd 11`', inline=False)
        await ctx.send(embed=embed)
        return

    data = requests.get(f"https://brasilapi.com.br/api/ddd/v1/{ddd}").json() 

    try:
        if 'type' in data and data['type'] == 'ddd_error':
            embed = discord.Embed(title='')
            embed.set_author(name='ㅤㅤDDD INVÁLIDO, CIDADE NÃO ENCONTRADAㅤㅤ', icon_url='')
            await ctx.send(embed=embed)
            return

        else: 
            embed = discord.Embed(title='')

            embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCONSULTA DE CIDADES POR DDDㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='') #----->> TÍTULO DO CÓDIGO

            embed.add_field(name="Estado", value=data.get('state', 'Sem Informação'), inline=False)
            embed.add_field(name="Cidades", value=','.join([f"`{city}`" for city in data.get("cities")]), inline=False)

            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

            await ctx.send(embed=embed)

    except Exception:
        pass   

@client.command()
async def whois(ctx, domain: str):

    api_key_whois = os.getenv("IP2WHOIS_KEY")
    api_url = f"https://api.ip2whois.com/v2?key={api_key_whois}&domain={domain}"
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(api_url) as response:
                if response.status != 200:
                    embed = discord.Embed(title="")
                    embed.set_author(name=f'ERRO AO OBTER OS DADOS WHOIS PARA! ERRO: {response.status}', icon_url='')
                    await ctx.send(embed=embed)
                    return
                
                data = await response.json()

        def get_value(key, default="Não encontrado"):
            return str(data.get(key, default)) if data.get(key) else default

        def get_nested_value(parent_key, child_key, default="Não encontrado"):
            return str(data.get(parent_key, {}).get(child_key, default)) if data.get(parent_key) else default

        def format_section(section_data):

            formatted = ""
            for key, value in section_data.items():
                formatted += f"- **{key.capitalize().replace('_', ' ')}:** {value if value else 'Não encontrado'}\n"
            return formatted.strip()

        embed = discord.Embed(title=f"")
        
        embed.set_author(name='ㅤㅤㅤㅤㅤㅤCONSULTA WHOIS REALIZADA COM SUCESSOㅤㅤㅤㅤㅤㅤ', icon_url='')

        embed.add_field(name="Domínio", value=get_value("domain"), inline=False)
        embed.add_field(name="ID do Domínio", value=get_value("domain_id"), inline=False)
        embed.add_field(name="Status", value=get_value("status"), inline=False)
        embed.add_field(name="Criado em", value=get_value("create_date"), inline=False)
        embed.add_field(name="Atualizado em", value=get_value("update_date"), inline=False)
        embed.add_field(name="Expira em", value=get_value("expire_date"), inline=False)
        embed.add_field(name="Idade do Domínio (dias)", value=get_value("domain_age") + " dias", inline=False)
        embed.add_field(name="Servidor WHOIS", value=get_value("whois_server"), inline=False)

        sections = {
            "Informações do Registrador": data.get("registrar", {}),
            "Informações do Registrante": data.get("registrant", {}),
            "Informações do Administrador": data.get("admin", {}),
            "Informações Técnicas": data.get("tech", {}),
            "Informações de Cobrança": data.get("billing", {}),
        }

        for title, section_data in sections.items():
            if section_data:  
                embed.add_field(name=title, value=format_section(section_data), inline=False)

        nameservers = data.get("nameservers", [])
        if nameservers:
            embed.add_field(
                name="Servidores de Nome (DNS)",
                value="\n".join(nameservers) if nameservers else "Não encontrado",
                inline=False
            )

        embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)             
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

        await ctx.send(embed=embed)

    except Exception as e:
        await ctx.send(f"❌ Ocorreu um erro ao consultar o domínio **{domain}**:\n{str(e)}")


@client.command()
async def maclookup(ctx, maclookup):

    mac_key = os.getenv("WHOISXML_TOKEN")
    url = f"https://mac-address.whoisxmlapi.com/api/v1?apiKey={mac_key}&macAddress={maclookup}&outputFormat=json"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            date_created_iso = data.get("blockDetails", {}).get("dateCreated", "SEM INFORMAÇÃO")
            date_updated_iso = data.get("blockDetails", {}).get("dateUpdated", "SEM INFORMAÇÃO")

            date_created_br = datetime.strptime(date_created_iso, "%Y-%m-%d").strftime("%d/%m/%Y") 
            date_updated_br = datetime.strptime(date_updated_iso, "%Y-%m-%d").strftime("%d/%m/%Y")

            embed = discord.Embed(title="")

            embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤBUSCA DE ENDEREÇO MACㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='') 

            embed.add_field(name="• INICIAL DO MAC ADRESS", value=data.get("vendorDetails", {}).get("oui", "SEM INFORMAÇÃO"), inline=False)
            embed.add_field(name="• ENDEREÇO PRIVADO", value=data.get("vendorDetails", {}).get("isPrivate", "SEM INFORMAÇÃO"), inline=False)
            embed.add_field(name="• FABRICANTE", value=data.get("vendorDetails", {}).get("companyName", "SEM INFORMAÇÃO"), inline=False)
            embed.add_field(name="• ENDEREÇO DO FABRICANTE", value=data.get("vendorDetails", {}).get("companyAddress", "SEM INFORMAÇÃO"), inline=False)
            embed.add_field(name="• PAÍS", value=data.get("vendorDetails", {}).get("countryCode", "SEM INFORMAÇÃO"), inline=False)
            embed.add_field(name="• BLOCO ENCONTRADO", value=data.get("blockDetails", {}).get("blockFound", "SEM INFORMAÇÃO"), inline=False)
            embed.add_field(name="• DATA DE CRIAÇÃO", value=date_created_br, inline=False)
            embed.add_field(name="• DATA DE ATUALIZAÇÃO", value=date_updated_br, inline=False)
            embed.add_field(name="• ENDEREÇO MAC COMPLETO", value=data.get("macAddressDetails", {}).get("searchTerm", "SEM INFORMAÇÃO"), inline=False)
            embed.add_field(name="• VALIDO", value=data.get("macAddressDetails", {}).get("isValid", "SEM INFORMAÇÃO"), inline=False)
            embed.add_field(name="• MAQUINA VIRTUAL ATIVA", value=data.get("virtualMachine", {}).get("virtualMachine", "SEM INFORMAÇÃO"), inline=False)
            embed.add_field(name="• TRANSMISSÃO", value=data.get("macAddressDetails", {}).get("transmissionType", "SEM INFORMAÇÃO"), inline=False)
            embed.add_field(name="• ADMINISTRADOR", value=data.get("macAddressDetails", {}).get("administrationType", "SEM INFORMAÇÃO"), inline=False)
            embed.add_field(name="• NOTAS WIRESHARK", value=data.get("macAddressDetails", {}).get("wiresharkNotes", "SEM INFORMAÇÃO"), inline=False)

            embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)             
            embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
            
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(title="")
            embed.set_author(name=f'ERRO AO CONSULTAR O ENDEREÇO MAC {maclookup}', icon_url='')

            await ctx.send(embed=embed)

    except Exception as e: 
        
        embed = discord.Embed(title="")

        embed.set_author(name="ㅤㅤCOMANDO DE CONSULTA DE ENDEREÇO MACㅤㅤ") 
        embed.add_field(name="Use o comando: `./maclookup` e a endereço {MAC} que deseja.", value='*Exemplo*: `./maclookup 00:00:5E:00:53:AF`', inline=False)
        embed.add_field(name="Observação:", value='*Pode ser utilizado somente letras maiúscilas e minúsculas*', inline=False)  
        await ctx.send(embed=embed)

# @client.command()
# async def reverseip(ctx, reverseip):

#     view_dns_key = os.getenv("VIEWDNS_TOKEN")

#     url = f"https://api.viewdns.info/reverseip/?host={reverseip}&apikey={view_dns_key}&output=json"

#     try:
#         response = requests.get(url)

#         if response.status_code == 200:
#             data = response.json()
#             reverse_ip = data.get('response', {}).get('domains', [])

#             embed = discord.Embed(title="", description="")

#             for reverse in reverse_ip:

#                 nome_site = reverse.get('name', 'Desconhecida')
#                 ultimo_resolve = reverse.get('last_resolved', 'Desconhecido')


#                 embed.add_field(name=f"NOME DO SITE: {nome_site}", value=f"ÚLTIMO RESOLVER: {ultimo_resolve}", inline=False)

#                 embed.set_author(name='ㅤㅤㅤㅤREVERSE IP LOOKUP EFETUADO COM SUCESSOㅤㅤㅤ', icon_url='')
#                 embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

#             await ctx.send(embed=embed)

#         else:

#             embed = discord.Embed(title="",)
#             embed.add_field(name="", value=f"Ocorreu um erro durante consultar o IP Reverso. Status code: {response.status_code}", inline=False)
#             embed.set_author(name='Erro na Resposta da API - ReverseIP Lookup', icon_url='')

#             await ctx.send(embed=embed)

#     except Exception as e:
#         embed = discord.Embed(title="")
#         embed.add_field(name="", value=f"Ocorreu um erro ao consultar o IP Reverso: {str(e)}", inline=False)
#         embed.set_author(name='Erro na Resposta da API - ReverseIP Lookup', icon_url='')

#         await ctx.send(embed=embed)

# @client.command()
# async def traceroute(ctx, traceroute):

#     view_dns_key = os.getenv("VIEWDNS_TOKEN")
#     url = f"https://api.viewdns.info/traceroute/?domain={traceroute}&apikey={view_dns_key}&output=json"

#     try:
#         response = requests.get(url)

#         if response.status_code == 200:
#             data = response.json()
#             route = data.get('response', {}).get('hops', [])

#             embed = discord.Embed(title="", description="")

#             for route_info in route:

#                 numero_id = route_info.get('number', 'Desconhecida')
#                 hostname = route_info.get('hostname', 'Desconhecido')
#                 ip_addrs = route_info.get('ip', 'Desconhecido')
#                 rtt_info = route_info.get('rtt', 'Desconhecido')
                
#                 embed.add_field(name=f"SERVIDOR N°: {numero_id}", value=f"ENDEREÇO IP: {ip_addrs}\nSERVIDOR: {hostname}\nTEMPO DE IDA E VOLTA (ms): {rtt_info}", inline=False)

#                 embed.set_author(name='ㅤㅤㅤㅤㅤTRACEROUTE EFETUADO COM SUCESSOㅤㅤㅤㅤ', icon_url='')
#                 embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

#             await ctx.send(embed=embed)

#         else:

#             embed = discord.Embed(title="",)
#             embed.add_field(name="", value=f"Ocorreu um erro durante traçar a rota do servidor. Status code: {response.status_code}", inline=False)
#             embed.set_author(name='Erro na Resposta da API - Traceroute', icon_url='')

#             await ctx.send(embed=embed)

#     except Exception as e:
#         embed = discord.Embed(title="")
#         embed.add_field(name="", value=f"Ocorreu um erro ao traçar a rota do servidor: {str(e)}", inline=False)
#         embed.set_author(name='Erro na Resposta da API - Traceroute', icon_url='')

#         await ctx.send(embed=embed)

@client.command()
async def portscan(ctx, portscan):
    
    view_dns_key = os.getenv("VIEWDNS_TOKEN")
    url = f"https://api.viewdns.info/portscan/?host={portscan}&apikey={view_dns_key}&output=json"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            portas = data.get('response', {}).get('port', [])

            embed = discord.Embed(title="", description="Nosso scan de portas são totalmente baseados nos bancos de dados do Nmap.")
            
            for porta_info in portas:

                numero_porta = porta_info.get('number', 'Desconhecida')
                servico = porta_info.get('service', 'Desconhecido')
                status = porta_info.get('status', 'Desconhecido')
                
                embed.add_field(name=f"Porta {numero_porta}", value=f"Serviço: {servico}\nStatus: {status}", inline=True)
                embed.set_author(name='ㅤㅤㅤㅤㅤㅤSCAN DE PORTAS EFETUADO COM SUCESSOㅤㅤㅤㅤ', icon_url='')
                embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

            await ctx.send(embed=embed)

        else:

            embed = discord.Embed(title="",)
            embed.add_field(name="", value=f"ERRO: {response.status_code}", inline=False)
            embed.set_author(name='ERRO NA RESPOSTA DA API - PORTSCAN', icon_url='')

            await ctx.send(embed=embed)

    except Exception as e:
        embed = discord.Embed(title="")
        embed.add_field(name="", value=f"ERRO: {str(e)}", inline=False)
        embed.set_author(name='ERRO NA RESPOSTA DA API - PORTSCAN', icon_url='')
        await ctx.send(embed=embed)


# @client.command() 
# async def operadora(ctx, operadora = None):

#     operadora_token = os.getenv("APILAYER_TOKEN")
#     data = requests.get(f"http://apilayer.net/api/validate?access_key={operadora_token}&number={operadora}&country_code=&format=1").json()
    
#     try:
#         embed = discord.Embed(title='')

#         embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤCHECKER DE OPERADORAㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='') #----->> TÍTULO DO CÓDIGO

#         embed.add_field(name="• VÁLIDO", value=data['valid'], inline=False)
#         embed.add_field(name="• NÚMERO", value=data['number'], inline=False)
#         embed.add_field(name="• FORMATO INTERNACIONAL", value=data['international_format'], inline=False)
#         embed.add_field(name="• DDI DO PAÍS", value=data['country_prefix'], inline=False)
#         embed.add_field(name="• CÓDIGO DO PAÍS", value=data['country_code'], inline=False)
#         embed.add_field(name="• NOME DO PAÍS", value=data['country_name'], inline=False)
#         embed.add_field(name="• LOCALIZAÇÃO", value=data['location'], inline=False)
#         embed.add_field(name="• OPERADORA/PROVEDOR", value=data['carrier'], inline=False)
#         embed.add_field(name="• LINHA DE DISPOSITÍVO", value=data['line_type'], inline=False)

#         embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)                
#         embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

#         await ctx.send(embed=embed)

#         return
#     except Exception:
#         pass

#         embed = discord.Embed(title='')

#     if (operadora == None):
#         embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO OPERADORAㅤㅤㅤ', icon_url='')
#         embed.add_field(name="Use o comando: `/operadora` e a {NÚMERO}", value='*Exemplo*: `/operadora +5511987654321`', inline=False)
#         embed.add_field(name="Observação:", value='*utilize o padrão universal.*', inline=False)        
#         return await ctx.send(embed=embed)
#     else: 
#        embed.set_author(name='ㅤㅤㅤOPERADORA NÃO ENCONTRADAㅤㅤㅤ', icon_url='')
#        return await ctx.send(embed=embed)



@client.command()
async def emailinfo(ctx, emailinfo=None):

    email_token = os.getenv("APILAYER_TOKEN")
    data = requests.get(
        f"https://api.apilayer.com/email_verification/check?email={emailinfo}&apikey={email_token}"
    ).json()
    
    try:
        embed = discord.Embed(title='')

        embed.set_author(
            name='ㅤㅤㅤㅤㅤㅤㅤㅤCHECKER DE E-MAILㅤㅤㅤㅤㅤㅤㅤㅤ', 
            icon_url=''
        )  # ----->> TÍTULO DO CÓDIGO

        # Preenche o embed com os dados, convertendo os valores booleanos
        embed.add_field(name="• E-MAIL", value=data['email'], inline=False)
        embed.add_field(name="• USUÁRIO", value=data['user'], inline=False)
        embed.add_field(name="• DOMÍNIO", value=data['domain'], inline=False)
        embed.add_field(name="• FORMATO VÁLIDO", value=convert_info(data['format_valid']), inline=False)
        embed.add_field(name="• CORREIO VÁLIDO", value=convert_info(data['mx_found']), inline=False)
        embed.add_field(name="• SMTP DISPONÍVEL", value=convert_info(data['smtp_check']), inline=False)
        embed.add_field(name="• FUNÇÕES ATIVAS", value=convert_info(data['role']), inline=False)
        embed.add_field(name="• E-MAIL DISPONÍVEL", value=convert_info(data['disposable']), inline=False)
        embed.add_field(name="• E-MAIL GRATUITO", value=convert_info(data['free']), inline=False)
        embed.add_field(name="• PONTUAÇÃO DE E-MAIL", value=data['score'], inline=False)

        embed.add_field(name="ㅤ", value='👽ﾠ**By Whois Alien**', inline=False)             
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')

        await ctx.send(embed=embed)

        return
    except Exception:
        pass

        embed = discord.Embed(title='')

    if (emailinfo == None): #--------->> SE ENCONTRAR BRANCO OU NULO, RETORNA O COMANDO DO BOT DE "TUTORIAL"
        embed.set_author(name='ㅤㅤㅤㅤ👽 COMANDO EMAILㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `/emailinfo` e a {E-MAIL}", value='*Exemplo*: `/emailinfo google@gmail.com`', inline=False)
        return await ctx.send(embed=embed)
    else: #--------->> SE NÃO ENCONTRAR, RETORNA NÃO ENCONTRADO
       embed.set_author(name='E-MAIL NÃO ENCONTRADO', icon_url='')
       return await ctx.send(embed=embed)
   

#<---------------------------------------------------------------------------
# Abas interativas - informações e geradores

@client.command()
async def gerador(ctx):

    embed = discord.Embed(title='')

    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤGERADORESㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
    embed.add_field(name="👥 Gerador de Pessoas", value="Use o comando `./gerar_pessoa` para gerar uma pessoa fictícia.",inline=False)
    embed.add_field(name="💳 Gerador de Cartão", value="Use o comando `./gerar_cartao` para gerar um cartão Debito/Crédito fictício.", inline=False)
    embed.add_field(name="🔆 Gerador de CPF", value="Use o comando `./gerar_cpf` para gerar e validar um CPF fictício.", inline=False)
    embed.add_field(name="🎮 Gerador de Username", value="Use o comando `./gerar_usr` para gerar um username.", inline=False)
    embed.add_field(name="🔐 Gerador de senhas", value="Use o comando `./gerar_senha` para gerar uma senha.", inline=False)
    embed.add_field(name="📞 Gerador de número de telefone", value="Use o comando `./gerar_tel` para gerar um telefone fictício.", inline=False)
    embed.add_field(name="🪪 Gerador de RG", value="Use o comando `./gerar_rg` para gerar um RG.", inline=False)
    embed.add_field(name="📱 Gerador de User Agent", value="Use o comando `./gerar_agent` para gerar um User Agent de um navegador.", inline=False)
    embed.add_field(name="📫 Gerador de E-mail", value="Use o comando `./gerar_email` para gerar um e-mail.", inline=False)
    embed.add_field(name="📲 Gerador de Passaporte", value="Use o comando `./gerar_passaporte` para gerar um passaporte fictício.", inline=False)
    embed.add_field(name="📜 Gerador de Texto", value="Use o comando `./gerar_texto` para gerar um Texto convencional.", inline=False)
    embed.add_field(name="💾 Gerador de IP", value="Use o comando `./gerar_ip` para gerar um IP.", inline=False)
    embed.add_field(name="💻 Gerador de MAC Address", value="Use o comando `./gerar_mac para gerar um endereço MAC", inline=False)
    embed.add_field(name="🌐 Gerador de URL", value="Use o comando `./gerarg` para gerar um RG.", inline=False)
    embed.add_field(name="📍 Gerador de Coordenadas", value="Use o comando `./gerar_coordenadas` para gerar um Coordenada Geogŕaficas aleatória.", inline=False)
    embed.add_field(name="📆 Gerador de Data", value="Use o comando `./gerar_data` para gerar uma Data Aleatória.", inline=False)
    embed.add_field(name="🏬 Gerador de CNPJ", value="Use o comando `./gerar_cnpj` para gerar um CNPJ.", inline=False)
    embed.add_field(name="🔮 Gerador de Cor", value="Use o comando `./gerar_cor` para gerar uma cor Aleatória.", inline=False)
    embed.add_field(name="🚗 Gerador de Placa", value="Use o comando `./gerar_placa` para gerar uma Placa.", inline=False)
   
    embed.set_footer(text='Whois Alien © All Rights Reserved', icon_url='')

    await ctx.send(embed=embed)

def remover_titulos(nome):

    return re.sub(r'\b(Dr\.|Dra\.|Sr\.|Srta\.)\b', '', nome).strip()

@client.command()
async def gerar_pessoa(ctx):

    try:
        embed = discord.Embed(title='')
        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤGERADOR DE PESSOAㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')

        embed.add_field(name="Nome", value=remover_titulos(fake.name()), inline=True)
        embed.add_field(name="CPF", value=fake.cpf(), inline=True)
        embed.add_field(name="Data de Nascimento", value=fake.date_of_birth(minimum_age=18, maximum_age=85), inline=True)
        embed.add_field(name="Nacionalidade", value="Brasil", inline=True)
        embed.add_field(name="Naturalidade", value=fake.estado_nome(), inline=True)
        embed.add_field(name="Profissão", value=fake.job(), inline=True)
        embed.add_field(name="E-mail", value=fake.free_email(), inline=True)
        embed.add_field(name="Nome da Mãe", value=remover_titulos(fake.name_female()), inline=True)
        embed.add_field(name="Nome do Pai", value=remover_titulos(fake.name_male()), inline=True)
        embed.add_field(name="Nome do Irmão(a)", value=remover_titulos(fake.name()), inline=True)
        embed.add_field(name="Nome da Avó", value=remover_titulos(fake.name_female()), inline=True)
        embed.add_field(name="Nome do Avô", value=remover_titulos(fake.name_male()), inline=True)
        embed.add_field(name="RG", value=fake.random_number(9, fix_len=True), inline=True)
        embed.add_field(name="Telefone", value=fake.cellphone_number(), inline=True)
        embed.add_field(name="Endereço", value=fake.address().replace("\n", ", "), inline=True)
        embed.add_field(name="Placa do Carro", value=fake.license_plate(), inline=True)
        embed.add_field(name="Chassi do Carro", value=fake.vin(), inline=True)
        embed.add_field(name="Cartão de crédito", value=fake.credit_card_number(), inline=True)
        embed.add_field(name="Validade do Cartão", value=fake.credit_card_expire(), inline=True)
        embed.add_field(name="Cod. Segurança Cartão", value=fake.credit_card_security_code(), inline=True)
        embed.add_field(name="Cor preferida", value=fake.safe_color_name(), inline=True)
        embed.add_field(name="CNPJ do Trabalho", value=fake.cnpj(), inline=True)
        embed.add_field(name="Endereço IP", value=fake.ipv4(), inline=True)
        embed.add_field(name="MAC do celular", value=fake.mac_address(), inline=True)
        embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved', icon_url='')
        await ctx.send(embed=embed)

    except Exception as e:
        embed = discord.Embed(title='')
        embed.set_author(name='NÃO FOI POSSÍVEL GERAR UMA PESSOA NO MOMENTO', icon_url='')
        await ctx.send(embed=embed)
        
@client.command()
async def gerar_usr(ctx):

    try:
        embed = discord.Embed(title='')

        embed.set_author(name='USERNAME GERADO COM SUCESSO', icon_url='')
        embed.add_field(name="", value=fake.user_name(), inline=False)
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
        await ctx.send(embed=embed)

        return
    except Exception:
        pass

        embed = discord.Embed(title='')

        embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UM USER NO MOMENTOㅤㅤㅤ', icon_url='')
        await ctx.send(embed=embed)

@client.command()
async def gerar_email(ctx):

    try:
        embed = discord.Embed(title='')
        embed.set_author(name='EMAIL GERADO COM SUCESSO', icon_url='')
        embed.add_field(name="", value=fake.ascii_free_email(), inline=False)
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
        await ctx.send(embed=embed)

        return
    except Exception:
       
        embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UM E-MAIL NO MOMENTOㅤㅤㅤ', icon_url='')
        return await ctx.send(embed=embed)


@client.command()
async def gerar_tel(ctx):

    try:
        embed = discord.Embed(title='')
        embed.set_author(name='TELEFONE GERADO COM SUCESSO', icon_url='')
        embed.add_field(name="", value=fake.cellphone_number(), inline=False)
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
        await ctx.send(embed=embed)

        return
    except Exception:
       
        embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UM TELEFONE NO MOMENTOㅤㅤㅤ', icon_url='')
        return await ctx.send(embed=embed)

@client.command()
async def gerar_cpf(ctx):

    try:
        embed = discord.Embed(title='')
        embed.set_author(name='CPF GERADO COM SUCESSO', icon_url='')
        embed.add_field(name="", value=fake.cpf(), inline=False)
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
        await ctx.send(embed=embed)

        return
    except Exception:
        pass

        embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UM CPF NO MOMENTOㅤㅤㅤ', icon_url='')
        return await ctx.send(embed=embed)

@client.command()
async def gerar_cartao(ctx):

    try:
        embed = discord.Embed(title='')
        embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤGERADOR DE CARTÃOㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
        embed.add_field(name="• Número do Cartão", value=fake.credit_card_number(), inline=False)
        embed.add_field(name="• Data de expiração", value=fake.credit_card_expire(), inline=False)
        embed.add_field(name="• Código de segurança", value=fake.credit_card_security_code(), inline=False)
        embed.add_field(name="• Banco", value=fake.credit_card_provider(), inline=False)
        embed.add_field(name="• Nome do Proprietário", value=fake.name(), inline=False)
        embed.add_field(name="• CPF", value=fake.cpf(), inline=False)
        embed.add_field(name="• Data de Nascimento", value=fake.date_of_birth(minimum_age=18, maximum_age=85), inline=False)
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
        await ctx.send(embed=embed)

        return
    except Exception:

        embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UM CARTÃOㅤㅤㅤ', icon_url='')
        await ctx.send(embed=embed)

@client.command()
async def gerar_rg(ctx):

    try:
        embed = discord.Embed(title='')
        embed.set_author(name='RG GERADO COM SUCESSO', icon_url='')
        embed.add_field(name="", value=fake.rg(), inline=False)
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
        await ctx.send(embed=embed)

        return
    except Exception:
       
        embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UM RG NO MOMENTOㅤㅤㅤ', icon_url='')
        return await ctx.send(embed=embed)


@client.command()
async def gerar_agent(ctx):

    try:
        embed = discord.Embed(title='')
        embed.set_author(name='USER AGENT GERADO COM SUCESSO', icon_url='')
        embed.add_field(name="", value=fake.user_agent(), inline=False)
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
        await ctx.send(embed=embed)

        return
    except Exception:
       
        embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UM USER AGENT NO MOMENTOㅤㅤㅤ', icon_url='')
        return await ctx.send(embed=embed)


@client.command()
async def gerar_passaporte(ctx):

    try:
        embed = discord.Embed(title='')
        embed.set_author(name='PASSAPORTE GERADO COM SUCESSO', icon_url='')
        embed.add_field(name="", value=fake.passport_full(), inline=False)
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
        await ctx.send(embed=embed)

        return
    except Exception:
       
        embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UM PASSAPORTE NO MOMENTOㅤㅤㅤ', icon_url='')
        return await ctx.send(embed=embed)


@client.command()
async def gerar_texto(ctx):

    try:
        embed = discord.Embed(title='')
        embed.set_author(name='TEXTO GERADO COM SUCESSO', icon_url='')
        embed.add_field(name="", value=fake.text(max_nb_chars=200, ext_word_list=None), inline=False)
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
        await ctx.send(embed=embed)

        return
    except Exception:
       
        embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UM TEXTO NO MOMENTOㅤㅤㅤ', icon_url='')
        return await ctx.send(embed=embed)



@client.command()
async def gerar_ip(ctx):

    try:
        embed = discord.Embed(title='')
        embed.set_author(name='IP GERADO COM SUCESSO', icon_url='')
        embed.add_field(name="", value=fake.ipv4(), inline=False)
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
        await ctx.send(embed=embed)

        return
    except Exception:
       
        embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UM IP NO MOMENTOㅤㅤㅤ', icon_url='')
        return await ctx.send(embed=embed)


@client.command()
async def gerar_mac(ctx):

    try:
        embed = discord.Embed(title='')
        embed.set_author(name='MAC GERADO COM SUCESSO', icon_url='')
        embed.add_field(name="", value=fake.mac_address(), inline=False)
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
        await ctx.send(embed=embed)

        return
    except Exception:
       
        embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UM MAC NO MOMENTOㅤㅤㅤ', icon_url='')
        return await ctx.send(embed=embed)

@client.command()
async def gerar_url(ctx):

    try:
        embed = discord.Embed(title='')
        embed.set_author(name='URL GERADA COM SUCESSO', icon_url='')
        embed.add_field(name="", value=fake.url(), inline=False)
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
        await ctx.send(embed=embed)

        return
    except Exception:
       
        embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UMA URL NO MOMENTOㅤㅤㅤ', icon_url='')
        return await ctx.send(embed=embed)

@client.command()
async def gerar_coordenadas(ctx):

    try:
        embed = discord.Embed(title='')
        embed.set_author(name='COORDENADA GERADA COM SUCESSO', icon_url='')
        embed.add_field(name="", value=fake.latitude() + ',' + fake.longitude(), inline=False)
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
        await ctx.send(embed=embed)

        return
    except Exception:
       
        embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UMA COORDENADA NO MOMENTOㅤㅤㅤ', icon_url='')
        return await ctx.send(embed=embed)

@client.command()
async def gerar_data(ctx):

    try:
        embed = discord.Embed(title='')
        embed.set_author(name='DATA GERADA COM SUCESSO', icon_url='')
        embed.add_field(name="", value=fake.date(), inline=False)
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
        await ctx.send(embed=embed)

        return
    except Exception:
       
        embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UMA DATA NO MOMENTOㅤㅤㅤ', icon_url='')
        return await ctx.send(embed=embed)

@client.command()
async def gerar_cnpj(ctx):

    global embed
    try:
        embed = discord.Embed(title='')
        embed.set_author(name='CNPJ GERADO COM SUCESSO', icon_url='')
        embed.add_field(name="", value=fake.cnpj(), inline=False)
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
        await ctx.send(embed=embed)

        return
    except Exception:
       
        embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UM CNPJ NO MOMENTOㅤㅤㅤ', icon_url='')
        return await ctx.send(embed=embed)

@client.command()
async def gerar_cor(ctx):

    global embed
    cor = fake.color()

    try:
        cor_hex = int(cor.replace("#", "0x"), 16)  # Converte "#RRGGBB" para 0xRRGGBB

        embed = discord.Embed(title='', colour=discord.Colour(cor_hex), description='')
        embed.set_author(name='COR GERADA COM SUCESSO', icon_url='')
        embed.add_field(name="", value=cor, inline=False)
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
        await ctx.send(embed=embed)

        return
    except Exception:
       
        embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UM CNPJ NO MOMENTOㅤㅤㅤ', icon_url='')
        return await ctx.send(embed=embed)

@client.command()
async def gerar_placa(ctx):

    try:
        embed = discord.Embed(title='')
        embed.set_author(name='PLACA GERADA COM SUCESSO', icon_url='')
        embed.add_field(name="", value=fake.license_plate(), inline=False)
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
        await ctx.send(embed=embed)

        return
    except Exception:
       
        embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UMA PLACA NO MOMENTOㅤㅤㅤ', icon_url='')
        return await ctx.send(embed=embed)

@client.command()
async def gerar_endereco(ctx):

    try:
        embed = discord.Embed(title='')
        embed.set_author(name='ENDEREÇO GERADA COM SUCESSO', icon_url='')
        embed.add_field(name="", value=fake.address(), inline=False)
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
        await ctx.send(embed=embed)

        return
    except Exception:
       
        embed.set_author(name='ㅤㅤㅤNÃO FOI POSSÍVEL GERAR UM ENDEREÇO NO MOMENTOㅤㅤㅤ', icon_url='')
        return await ctx.send(embed=embed)

@client.command()
async def gerar_senha(ctx, length=36):

    if 10 <= length <= 64:

        password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    
        embed = discord.Embed(title="Senha gerada com Sucesso!")
        embed.add_field(name="", value='Sua senha foi enviada em seu privado!', inline=False)             
        await ctx.send(embed=embed)
        embed = discord.Embed(title="")

        embed.set_author(name='SENHA GERADA COM SUCESSO', icon_url='')
        embed.add_field(name="", value=password, inline=False)
        embed.add_field(name="Dicas para criar senhas fortes:", value="Matéria do site [Kaspersky](https://www.kaspersky.com.br/resource-center/threats/how-to-create-a-strong-password)", inline=False)
        embed.add_field(name="Recomendação pessoal de gerenciador de senhas:", value="[Bitwarden](https://bitwarden.com/) - Sistema Open Source.", inline=False)
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
        await ctx.author.send(embed=embed)

    else:
        embed = discord.Embed(title="")
        embed.set_author(name='O comprimento da senha deve estar entre 10 e 64 caracteres.', icon_url='')
        await ctx.send(embed=embed)





#------------------ Generation Developer Tools 

@client.command()
async def genpassword(ctx, length=36):

    if 10 <= length <= 64:

        password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    
        embed = discord.Embed(title="Senha gerada com Sucesso!")
        embed.add_field(name="", value='Sua senha foi enviada em seu privado!', inline=False)             
        await ctx.send(embed=embed)
        embed = discord.Embed(title="")

        embed.set_author(name='SENHA GERADA COM SUCESSO', icon_url='')
        embed.add_field(name="", value=password, inline=False)
        embed.add_field(name="Dicas para criar senhas fortes:", value="Matéria do site [Kaspersky](https://www.kaspersky.com.br/resource-center/threats/how-to-create-a-strong-password)", inline=False)
        embed.add_field(name="Recomendação pessoal de gerenciador de senhas:", value="[Bitwarden](https://bitwarden.com/) - Sistema Open Source.", inline=False)
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')
        await ctx.author.send(embed=embed)

    else:
        embed = discord.Embed(title="")
        embed.set_author(name='O comprimento da senha deve estar entre 10 e 64 caracteres.', icon_url='')
        await ctx.send(embed=embed)

@client.command()
async def genkey(ctx):
    timestamp = datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
    
    embed = discord.Embed(title="Chave gerada com Sucesso!")
    embed.add_field(name="", value='Sua chave foi enviada em seu privado!', inline=False)             
    await ctx.send(embed=embed)
    
    key = f"{secrets.token_hex(4)}-{secrets.token_hex(2)}-{secrets.token_hex(2)}-{secrets.token_hex(2)}-{secrets.token_hex(6)}"
    
    embed = discord.Embed(title="")
    embed.set_author(name=f'', icon_url='')
    embed.add_field(name="", value=key, inline=False)
    embed.set_footer(text=f'Generated By {ctx.author} in {timestamp}', icon_url='')
    

    await ctx.author.send(embed=embed)

@client.command()
async def pwned(ctx, email_pwned=None):

    if not email_pwned:
        
        embed = discord.Embed(title='')

        embed.set_author(name='ㅤㅤㅤㅤ   👽 COMANDO VERIFICAÇÃO DE VAZAMENTOSㅤㅤㅤ', icon_url='')
        embed.add_field(name="Use o comando: `./pwned` e o e-mail ou usuário que deseja verificar.", value='*Exemplo*: `./pwned joao@gmail.com`', inline=False)
        return await ctx.send(embed=embed)

    try:
        api = LeakCheckAPI_Public()
        data = api.lookup(query=email_pwned)  # Chama a API corretamente

        leaks = data.get("sources", [])
        leak_info = "\n".join(f"- {leak['name']} ({leak['date']})" for leak in leaks) if leaks else "Nenhum vazamento encontrado."

        embed = discord.Embed(title="")
        embed.set_author(name="ㅤㅤㅤㅤ   VERIFICAÇÃO DE VAZAMENTO DE E-MAILSㅤㅤㅤㅤ   ")
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="E-mail", value=email_pwned, inline=True)
        embed.add_field(name="Total de Vazamentos", value=str(data.get("found", 0)), inline=True)
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="", value="", inline=False)

        embed.add_field(name="Locais de vazamento", value=leak_info, inline=False)
        embed.set_footer(text='Requested By {}\nWhois Alien © All Rights Reserved'.format(ctx.author), icon_url='')        
        await ctx.send(embed=embed)

    except ValueError as e:
        if "Not found" in str(e):  # Trata o erro corretamente
            await ctx.send(f"O e-mail `{email_pwned}` não foi encontrado em nenhum vazamento.")
        else:
            await ctx.send(f"Ocorreu um erro ao processar a solicitação: {e}")













#--------------------- GEN HASH ENCRYPT


@client.command()
async def gen_md5(ctx, *, text: str = ""):

    md5_hash = hashlib.md5(text.encode()).hexdigest()
    
    embed = discord.Embed(title='')
    embed.set_author(name="ㅤㅤㅤㅤㅤㅤㅤHASH MD5ㅤㅤㅤㅤㅤㅤㅤ   ")
    embed.add_field(name="Input", value=text if text else "[Empty String]", inline=False)
    embed.add_field(name="Hash MD5", value=md5_hash, inline=False)
    embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved')
    
    await ctx.send(embed=embed)

@client.command()
async def gen_sha1(ctx, *, text: str = ""):

    sha1_hash = hashlib.sha1(text.encode()).hexdigest()
    
    embed = discord.Embed(title='')
    embed.set_author(name="ㅤㅤㅤㅤㅤㅤㅤHASH SHA1ㅤㅤㅤㅤㅤㅤㅤ   ")
    embed.add_field(name="Input", value=text if text else "[Empty String]", inline=False)
    embed.add_field(name="Hash SHA1", value=sha1_hash, inline=False)
    embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved')
    
    await ctx.send(embed=embed)

@client.command()
async def gen_sha256(ctx, *, text: str = ""):

    sha256_hash = hashlib.sha256(text.encode()).hexdigest()
    
    embed = discord.Embed(title='')
    embed.set_author(name="ㅤㅤㅤㅤㅤㅤㅤHASH SHA256ㅤㅤㅤㅤㅤㅤㅤ   ")
    embed.add_field(name="Input", value=text if text else "[Empty String]", inline=False)
    embed.add_field(name="Hash SHA256", value=sha256_hash, inline=False)
    embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved')
    
    await ctx.send(embed=embed)

@client.command()
async def gen_sha512(ctx, *, text: str = ""):

    sha512_hash = hashlib.sha512(text.encode()).hexdigest()
    
    embed = discord.Embed(title='')
    embed.set_author(name="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤHASH SHA512ㅤㅤㅤㅤㅤㅤㅤ   ")
    embed.add_field(name="Input", value=text if text else "[Empty String]", inline=False)
    embed.add_field(name="Hash SHA512", value=sha512_hash, inline=False)
    embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved')
    
    await ctx.send(embed=embed)

@client.command()
async def gen_blake2b(ctx, *, text: str = ""):

    blake2b_hash = hashlib.blake2b(text.encode()).hexdigest()
    
    embed = discord.Embed(title='')
    embed.set_author(name="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤHASH BLAKE2Bㅤㅤㅤㅤㅤㅤㅤ   ")
    embed.add_field(name="Input", value=text if text else "[Empty String]", inline=False)
    embed.add_field(name="Hash BLAKE2B", value=blake2b_hash, inline=False)
    embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved')
    
    await ctx.send(embed=embed)

@client.command()
async def gen_blake2s(ctx, *, text: str = ""):

    blake2s_hash = hashlib.blake2s(text.encode()).hexdigest()
    
    embed = discord.Embed(title='')
    embed.set_author(name="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤHASH BLAKE2Bㅤㅤㅤㅤㅤㅤㅤ   ")
    embed.add_field(name="Input", value=text if text else "[Empty String]", inline=False)
    embed.add_field(name="Hash BLAKE2S", value=blake2s_hash, inline=False)
    embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved')
    
    await ctx.send(embed=embed)

@client.command()
async def gen_sha224(ctx, *, text: str = ""):

    sha224_hash = hashlib.sha224(text.encode()).hexdigest()
    
    embed = discord.Embed(title='')
    embed.set_author(name="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤHASH SHA224ㅤㅤㅤㅤㅤㅤㅤ   ")
    embed.add_field(name="Input", value=text if text else "[Empty String]", inline=False)
    embed.add_field(name="Hash SHA224", value=sha224_hash, inline=False)
    embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved')
    
    await ctx.send(embed=embed)

@client.command()
async def gen_sha384(ctx, *, text: str = ""):

    sha384_hash = hashlib.sha384(text.encode()).hexdigest()
    
    embed = discord.Embed(title='')
    embed.set_author(name="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤHASH SHA384ㅤㅤㅤㅤㅤㅤㅤ   ")
    embed.add_field(name="Input", value=text if text else "[Empty String]", inline=False)
    embed.add_field(name="Hash SHA384", value=sha384_hash, inline=False)
    embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved')
    
    await ctx.send(embed=embed)

@client.command()
async def gen_shake128(ctx, *, text: str = ""):

    shake128_hash = hashlib.shake_128(text.encode()).hexdigest()
    
    embed = discord.Embed(title='')
    embed.set_author(name="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤHASH SHAKE128ㅤㅤㅤㅤㅤㅤㅤ   ")
    embed.add_field(name="Input", value=text if text else "[Empty String]", inline=False)
    embed.add_field(name="Hash SHAKE128", value=shake128_hash, inline=False)
    embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved')
    
    await ctx.send(embed=embed)

@client.command()
async def gen_shake256(ctx, *, text: str = ""):

    shake256_hash = hashlib.shake_256(text.encode()).hexdigest()
    
    embed = discord.Embed(title='')
    embed.set_author(name="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤHASH SHAKE256ㅤㅤㅤㅤㅤㅤㅤ   ")
    embed.add_field(name="Input", value=text if text else "[Empty String]", inline=False)
    embed.add_field(name="Hash SHAKE256", value=shake256_hash, inline=False)
    embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved')
    
    await ctx.send(embed=embed)

@client.command()
async def gen_scrypt(ctx, *, text: str = ""):

    scrypt_hash = hashlib.scrypt(text.encode()).hexdigest()
    
    embed = discord.Embed(title='')
    embed.set_author(name="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤHASH SCRYPTㅤㅤㅤㅤㅤㅤㅤ   ")
    embed.add_field(name="Input", value=text if text else "[Empty String]", inline=False)
    embed.add_field(name="Hash SCRYPT", value=scrypt_hash, inline=False)
    embed.set_footer(text=f'Requested By {ctx.author}\nWhois Alien © All Rights Reserved')
    
    await ctx.send(embed=embed)




















































@client.command()
async def repositorio(ctx):
    await ctx.send("https://github.com/christopherrissardi/Whois-Alien-Bot")



 
bot_token = os.getenv("BOT_TOKEN")
client.run(bot_token)
