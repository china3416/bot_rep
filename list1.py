import discord
from discord.ext import commands
from discord.utils import get
discord.Intents.all()
import os


bot = commands.Bot(intents = discord.Intents.all(), command_prefix="/", description="Test Bot for the discord.py")

count1 = 0
count2 = 0
i = 3
y = 0
z = 0
team_id = 0

# список зарегестрированных команд
team_name = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
black_list = []




# снять роль
@bot.command()
@commands.has_role(817170720941015050)
async def clear_role(ctx, *, name_role: str):
    global y
    y = 0
    role = discord.utils.get(ctx.guild.roles, name=name_role)
    cap = role.members
    x = len(cap)
    while y <= x - 1:
        await cap[y].remove_roles(role)
        y = y + 1




# черный список
@bot.command()
@commands.has_role(817170720941015050)
async def b_list(ctx, member: discord.Member):
    black_list.append(member)




# "белый" список
@bot.command()
@commands.has_role(817170720941015050)
async def w_list(ctx, member: discord.Member):
    for item in black_list:
        if item == member:
            black_list.remove(member)





#Открытие регистрации
@bot.command()
@commands.has_role(817170720941015050)
async def open_reg(ctx):
    global team_id
    global count1
    global count2
    channel = bot.get_channel(819000355613835304)
    team_list_ch = bot.get_channel(816827996681666650)
    Manager = discord.utils.get(ctx.guild.roles, name="Manager")

    team_name = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
    
    count1 = 0
    count2 = 0
    i = 3
    msg_teamList = await team_list_ch.send('**Team List\n1. '+team_name[1]+' \n2. '+team_name[2]+' \n3. '+team_name[3]+' \n4. '+team_name[4]+' \n5. '+team_name[5]+' \n6. '+team_name[6]+' '
                                             '\n7. '+team_name[7]+'\n8. '+team_name[8]+'\n9. '+team_name[9]+'\n10. '+team_name[10]+''
                                             '\n11. '+team_name[11]+'\n12. '+team_name[12]+'\n13. '+team_name[13]+'\n14. '+team_name[14]+''
                                             '\n15. '+team_name[15]+'\n16. '+team_name[16]+'\n17. '+team_name[17]+'\n18. '+team_name[18]+''
                                             '\n19. '+team_name[19]+'\n20. '+team_name[20]+'\nReserve\n1. '+team_name[21]+''
                                             '\n2. '+team_name[22]+'\n3. '+team_name[23]+'\n4. '+team_name[24]+'\n5. '+team_name[25]+'**')

    team_id = msg_teamList.id


    await channel.send("**Регистрация открыта! @everyone**")
    await channel.set_permissions(Manager, read_messages=True, send_messages=True)






#Сообщение с данными от матча
@bot.command()
@commands.has_role(817170720941015050)
async def lobby(ctx, map: str, time_m: str, id_m: str, passw: str):


    embed_obj = discord.Embed(colour = discord.Color.from_rgb(199, 0, 0))
    embed_obj.set_thumbnail(url="https://images-ext-2.discordapp.net/external/9dR6id4q62Sl2jHvwAHf0b7C0sMdZX9FoU-WOjTJWAA/https/media.discordapp.net/attachments/636308078697906179/819003527711817748/Black_Clover_logo.png")
    embed_obj.add_field(name="**MAP:** ", value=map, inline=False)
    embed_obj.add_field(name="**Start:**", value=time_m, inline=False)
    embed_obj.add_field(name="**ID:**", value=id_m, inline=False)
    embed_obj.add_field(name="**Password:**", value=passw, inline=False)
    lobby_ch = bot.get_channel(818907684207853568)

    await lobby_ch.send("@everyone", embed=embed_obj)





# embed сообщение

@bot.command()
@commands.has_role(817170720941015050)
async def send(ctx, *, text: str):

    embedVar = discord.Embed(description=text, color = discord.Color.from_rgb(199, 0, 0))

    await ctx.send(embed=embedVar)





# Редактирование списка участников
@bot.command()
@commands.has_role(817170720941015050)
async def team(ctx, i: int, *, name: str):

    if name == 'none':
        name = '-'

    team_name[i] = name

    team_list_ch = bot.get_channel(816827996681666650)
    team_list_edit = await team_list_ch.fetch_message(team_id)
    await team_list_edit.edit(content='**Team List \n1. '+team_name[1]+' \n2. '+team_name[2]+' \n3. '+team_name[3]+' \n4. '+team_name[4]+' \n5. '+team_name[5]+' \n6. '+team_name[6]+' '
                                      '\n7. '+team_name[7]+'\n8. '+team_name[8]+'\n9. '+team_name[9]+'\n10. '+team_name[10]+''
                                      '\n11. '+team_name[11]+'\n12. '+team_name[12]+'\n13. '+team_name[13]+'\n14. '+team_name[14]+''
                                      '\n15. '+team_name[15]+'\n16. '+team_name[16]+'\n17. '+team_name[17]+'\n18. '+team_name[18]+''
                                      '\n19. '+team_name[19]+'\n20. '+team_name[20]+'\nReserve\n1. '+team_name[21]+''
                                      '\n2. '+team_name[22]+'\n3. '+team_name[23]+'\n4. '+team_name[24]+'\n5. '+team_name[25]+'**')






# Процесс регистрации
@bot.event
async def on_message(message):

    await bot.process_commands(message)
    #данные: сообщение рользователя, получение роли, данные пользователя
    msg = message.content


    role = discord.utils.get(message.guild.roles, name="Cap-chat")
    Manager = discord.utils.get(message.guild.roles, name="Manager")
    user = message.author
    reg_ch = bot.get_channel(819000355613835304)
    team_list_ch = bot.get_channel(816827996681666650)


    global count1
    global count2
    global i



    if message.channel.id == 819000355613835304:

        for item in black_list:

            if item == message.author:
                await message.add_reaction("<:No:818987499766546432>")
                return
        if message.author == bot.user or count2 > 4:
            return

        if count1 <= 17:
            await user.add_roles(role)
            await message.add_reaction("<:Yes:818988469891629087>")
            count1 = count1 + 1
            team_name[i] = msg
            i = i + 1
            if count1 >= 1:
                team_list_edit = await team_list_ch.fetch_message(team_id)
                await team_list_edit.edit(content='**Team List\n1. '+team_name[1]+' \n2. '+team_name[2]+' \n3. '+team_name[3]+' \n4. '+team_name[4]+' \n5. '+team_name[5]+' \n6. '+team_name[6]+' '
                                                         '\n7. '+team_name[7]+'\n8. '+team_name[8]+'\n9. '+team_name[9]+'\n10. '+team_name[10]+''
                                                         '\n11. '+team_name[11]+'\n12. '+team_name[12]+'\n13. '+team_name[13]+'\n14. '+team_name[14]+''
                                                         '\n15. '+team_name[15]+'\n16. '+team_name[16]+'\n17. '+team_name[17]+'\n18. '+team_name[18]+''
                                                         '\n19. '+team_name[19]+'\n20. '+team_name[20]+'\nReserve\n1. '+team_name[21]+''
                                                         '\n2. '+team_name[22]+'\n3. '+team_name[23]+'\n4. '+team_name[24]+'\n5. '+team_name[25]+'**')


        else:
            await message.add_reaction("<:Res:818992166906888233>")
            count2 = count2 + 1
            team_name[i] = msg
            i = i + 1
            reserve_edit = await team_list_ch.fetch_message(team_id)
            await reserve_edit.edit(content='**Team List\n1. '+team_name[1]+' \n2. '+team_name[2]+' \n3. '+team_name[3]+' \n4. '+team_name[4]+' \n5. '+team_name[5]+' \n6. '+team_name[6]+' '
                                      '\n7. '+team_name[7]+'\n8. '+team_name[8]+'\n9. '+team_name[9]+'\n10. '+team_name[10]+''
                                      '\n11. '+team_name[11]+'\n12. '+team_name[12]+'\n13. '+team_name[13]+'\n14. '+team_name[14]+''
                                      '\n15. '+team_name[15]+'\n16. '+team_name[16]+'\n17. '+team_name[17]+'\n18. '+team_name[18]+''
                                      '\n19. '+team_name[19]+'\n20. '+team_name[20]+'\nReserve\n1. '+team_name[21]+''
                                      '\n2. '+team_name[22]+'\n3. '+team_name[23]+'\n4. '+team_name[24]+'\n5. '+team_name[25]+'**')



        if count2 > 4:

            embed_obj = discord.Embed(description='**Регистрация закрыта! @everyone**', colour = discord.Color.from_rgb(199, 0, 0))

            await reg_ch.send(embed=embed_obj)
            await message.channel.set_permissions(message.guild.default_role, read_messages=True, send_messages=False)
            await message.channel.set_permissions(Manager, read_messages=True, send_messages=False)





token = os.environ.get('BOT_TOKEN')
bot.run(token)


