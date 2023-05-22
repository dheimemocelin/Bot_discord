import hikari
import lightbulb

bot = lightbulb.BotApp(
    token=open('token.txt', 'r').read(), 
    default_enabled_guilds=(int(open('ds_channel_id.txt', 'r').read())))


@bot.command
@lightbulb.command('msg_dheime', 'Saldação Bot Mocelin')
@lightbulb.implements(lightbulb.SlashCommand)
async def hello(ctx):
    await ctx.respond('*Ola tudo bem?*')


#Piadas
import random

p1 = "O que o pato disse para a pata \nR.: Vem Quá!"
p2 = "Porque o menino estava falando ao telefone deitado? \nR.: Para não cair a ligação."
p3 = "Qual é a fórmula da água benta? \nR.: H Deus O!"
p4 = "Qual é a cidade brasileira que não tem táxi? \nR.: Uberlândia"
p5 = "Qual é a fruta que anda de trem? \nR.: O kiwiiiii."
p6 = "O que é um pontinho preto no avião? \nR.: Uma aeromosca."
p7 = "Como o Batman faz para entrar na Bat-caverna? \nR.: Ele bat-palma."
p8 = "Por que o pão não entende a batata? \nR.: Porque o pão é francês e a batata é inglesa"
p9 = "O que o zero disse para o oito? \nR.: Belo cinto!"
p10 = "Por que os elétrons nunca são convidados para festas? \nR.: Porque eles são muito negativos."

piadas=[p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

@bot.command
@lightbulb.command('piada', 'Receba uma piada')
@lightbulb.implements(lightbulb.SlashCommand)

async def joke(ctx):
    n = random.randint(1,10)
    await ctx.respond(f"*{piadas[n]}*")


#Calculadora
@bot.command
@lightbulb.command('calculadora', 'Calculadora')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_calculator(ctx):
    pass

@my_calculator.child
@lightbulb.option('n2', 'Segundo número', type=float)
@lightbulb.option('n1', 'Primeiro número', type=float)
@lightbulb.command('soma', 'Operação de Adição')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def soma(ctx):
    r = ctx.options.n1 + ctx.options.n2
    await ctx.respond(f"*O resultado é  **{r}***")

@my_calculator.child
@lightbulb.option('n2', 'Segundo número', type=float)
@lightbulb.option('n1', 'Primeiro número', type=float)
@lightbulb.command('subtracao', 'Operação de Subtração')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subtracao(ctx):
    r = ctx.options.n1 - ctx.options.n2
    await ctx.respond(f"*O resultado é  **{r}***")

@my_calculator.child
@lightbulb.option('n2', 'Segundo número', type=float)
@lightbulb.option('n1', 'Primeiro número', type=float)
@lightbulb.command('multiplicacao', 'Operação de Multiplicação')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def multiplicacao(ctx):
    r = ctx.options.n1 * ctx.options.n2
    await ctx.respond(f"*O resultado é  **{round(r, 1)}***")

@my_calculator.child
@lightbulb.option('n2', 'Segundo número', type=float)
@lightbulb.option('n1', 'Primeiro número', type=float)
@lightbulb.command('divisao', 'Operação de Divisão')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def divisao(ctx):
    r = ctx.options.n1 / ctx.options.n2
    await ctx.respond(f"*O resultado é  **{round(r, 1)}***")



#Temperatura
import requests
import string

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
APY_KEY = open('api_weather_key.txt', 'r').read()

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

@bot.command
@lightbulb.option('pais', 'País', type=str)
@lightbulb.option('cidade', 'Cidade', type=str)
@lightbulb.command('temperatura', 'Informe uma cidade e seu país para saber a temperatura atual')
@lightbulb.implements(lightbulb.SlashCommand)

async def temperatura(ctx):
    country = ctx.options.pais
    CITY = string.capwords(ctx.options.cidade) + "," + country[0:2].lower()
    
    url = BASE_URL + "q=" + CITY + "&APPID=" + API_KEY 
    response = requests.get(url).json()
    
    temp_kelvin = response['main']['temp']
    umidade = response['main']['humidity']
    vento = response['wind']['speed']

    temp_celsius = str(round(kelvin_to_celsius(temp_kelvin)))

    await ctx.respond(f"```A temperatura atual em {string.capwords(ctx.options.cidade)} é de {temp_celsius} ºC \numidade do ar: {umidade}% \nvento: {vento} m/s```")


bot.run()
