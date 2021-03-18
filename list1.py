import discord
from discord.ext import commands
from discord.utils import get
discord.Intents.all()
import os


bot = commands.Bot(intents = discord.Intents.all(), command_prefix="-", description="Test Bot for the discord.py")


teams = []
reserve = []
black_list = []

teams_count = 0
role_count = 0
i = 3
x = 0
l = 0
team_id = 0
reg_check = False

while x < 26:
    teams.append('-')
    x = x + 1


@bot.command()
@commands.has_role(817170720941015050)
async def open_reg(ctx):
    manager = discord.utils.get(ctx.guild.roles, name="Manager")
    team_list_ch = bot.get_channel(816827996681666650)
    reg_ch = bot.get_channel(819000355613835304)

    global reg_check
    global teams_count
    global i
    global x
    global team_id

    reg_check = True
    teams_count = 0
    i = 3
    x = 0


    while x < 26:
        teams[x] = '-'
        x = x + 1



    team_list_msg = await team_list_ch.send('**Team List\n1. '+teams[1]+' \n2. '+teams[2]+' \n3. '+teams[3]+' \n4. '+teams[4]+' \n5. '+teams[5]+' \n6. '+teams[6]+' '
                   '\n7. '+teams[7]+'\n8. '+teams[8]+'\n9. '+teams[9]+'\n10. '+teams[10]+''
                   '\n11. '+teams[11]+'\n12. '+teams[12]+'\n13. '+teams[13]+'\n14. '+teams[14]+''
                   '\n15. '+teams[15]+'\n16. '+teams[16]+'\n17. '+teams[17]+'\n18. '+teams[18]+''
                   '\n19. '+teams[19]+'\n20. '+teams[20]+'\nReserve\n1. '+teams[21]+''
                   '\n2. '+teams[22]+'\n3. '+teams[23]+'\n4. '+teams[24]+'\n5. '+teams[25]+'**')

    team_id = team_list_msg.id

    await reg_ch.send("**Регистрация открыта! @everyone**")
    await reg_ch.set_permissions(manager, read_messages=True, send_messages=False)
    await ctx.message.delete()



@bot.command()
async def reg(ctx, team_name: str, tag: str, member: discord.Member):
    team_list_ch = bot.get_channel(816827996681666650)
    reg_ch = bot.get_channel(819000355613835304)

    cap = discord.utils.get(ctx.guild.roles, name="Cap-chat")
    manager = discord.utils.get(ctx.guild.roles, name="Manager")

    global teams_count
    global i

    name = team_name + ' ' + tag + ' ' + member.mention

    if ctx.channel.id == 819000355613835304 and reg_check == True:
        if name in teams:
            await reg_ch.send('Ваша команда уже зарегистрирована!')
        else:
            for item in black_list:

                if item == ctx.author:
                    await ctx.message.add_reaction("<:No:818987499766546432>")
                    return

            if ctx.author == bot.user:
                return

            if teams_count < 18:
                await ctx.message.add_reaction("<:Yes:818988469891629087>")
                await member.add_roles(cap)

            if teams_count > 17 and teams_count < 23:
                await ctx.message.add_reaction("<:Res:818992166906888233>")
                reserve.append(member)

            if teams_count < 23:
                teams[i] = name
                i = i + 1



                teams_count = teams_count + 1
                team_list_edit = await team_list_ch.fetch_message(team_id)
                await team_list_edit.edit(content='**Team List\n1. '+teams[1]+' \n2. '+teams[2]+' \n3. '+teams[3]+' \n4. '+teams[4]+' \n5. '+teams[5]+' \n6. '+teams[6]+' '
                                                  '\n7. '+teams[7]+'\n8. '+teams[8]+'\n9. '+teams[9]+'\n10. '+teams[10]+''
                                                  '\n11. '+teams[11]+'\n12. '+teams[12]+'\n13. '+teams[13]+'\n14. '+teams[14]+''
                                                  '\n15. '+teams[15]+'\n16. '+teams[16]+'\n17. '+teams[17]+'\n18. '+teams[18]+''
                                                  '\n19. '+teams[19]+'\n20. '+teams[20]+'\nReserve\n1. '+teams[21]+''
                                                  '\n2. '+teams[22]+'\n3. '+teams[23]+'\n4. '+teams[24]+'\n5. '+teams[25]+'**')


            if teams_count > 22:
                embed_obj = discord.Embed(description='**Регистрация закрыта! @everyone**', colour = discord.Color.from_rgb(199, 0, 0))
                await ctx.send(embed=embed_obj)
                await reg_ch.set_permissions(manager, read_messages=True, send_messages=False)




@bot.command()
async def unreg(ctx, team_name: str, tag: str, member: discord.Member):
    team_list_ch = bot.get_channel(816827996681666650)
    cap = discord.utils.get(ctx.guild.roles, name="Cap-chat")

    global i
    global l

    if ctx.channel.id == 819000355613835304 and reg_check == True:
        teams.remove(team_name + ' ' + tag + ' ' + member.mention)
        await member.remove_roles(cap)
        teams.append('-')

        i = i - 1

        if teams_count > 17:
            await reserve[l].add_roles(cap)
            l += 1

        team_list_edit = await team_list_ch.fetch_message(team_id)
        await team_list_edit.edit(content='**Team List\n1. '+teams[1]+' \n2. '+teams[2]+' \n3. '+teams[3]+' \n4. '+teams[4]+' \n5. '+teams[5]+' \n6. '+teams[6]+' '
                                          '\n7. '+teams[7]+'\n8. '+teams[8]+'\n9. '+teams[9]+'\n10. '+teams[10]+''
                                          '\n11. '+teams[11]+'\n12. '+teams[12]+'\n13. '+teams[13]+'\n14. '+teams[14]+''
                                          '\n15. '+teams[15]+'\n16. '+teams[16]+'\n17. '+teams[17]+'\n18. '+teams[18]+''
                                          '\n19. '+teams[19]+'\n20. '+teams[20]+'\nReserve\n1. '+teams[21]+''
                                          '\n2. '+teams[22]+'\n3. '+teams[23]+'\n4. '+teams[24]+'\n5. '+teams[25]+'**')




# снять роль
@bot.command()
@commands.has_role(817170720941015050)
async def clear_role(ctx, *, name_role: str):
    global role_count
    role_count = 0
    role = discord.utils.get(ctx.guild.roles, name=name_role)
    cap = role.members
    member_length = len(cap)
    while role_count <= member_length - 1:
        await cap[role_count].remove_roles(role)
        role_count += 1
    await ctx.message.delete()

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




@bot.command()
@commands.has_role(817170720941015050)
async def close_reg(ctx):
    global reg_check

    reg_ch = bot.get_channel(819000355613835304)
    manager = discord.utils.get(ctx.guild.roles, name="Manager")
    reg_check = False
    embed_obj = discord.Embed(description='**Регистрация закрыта! @everyone**', colour = discord.Color.from_rgb(199, 0, 0))
    await reg_ch.set_permissions(manager, read_messages=True, send_messages=False)
    await reg_ch.send(embed=embed_obj)
    await ctx.message.delete()










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
    await ctx.message.delete()





# embed сообщение

@bot.command()
@commands.has_role(817170720941015050)
async def send(ctx, *, text: str):

    embedVar = discord.Embed(description=text, color = discord.Color.from_rgb(199, 0, 0))

    await ctx.send(embed=embedVar)
    await ctx.message.delete()





#Редактирование списка участников
@bot.command()
@commands.has_role(817170720941015050)
async def team(ctx, i: int, team_name: str, tag: str, member: discord.Member):

    name = team_name + ' ' + tag + ' ' + member.mention

    if team_name == 'none':
        teams.pop(i)
    else:
        teams[i] = name

    team_list_ch = bot.get_channel(816827996681666650)
    team_list_edit = await team_list_ch.fetch_message(team_id)
    await team_list_edit.edit(content='**Team List \n1. '+teams[1]+' \n2. '+teams[2]+' \n3. '+teams[3]+' \n4. '+teams[4]+' \n5. '+teams[5]+' \n6. '+teams[6]+' '
                                      '\n7. '+teams[7]+'\n8. '+teams[8]+'\n9. '+teams[9]+'\n10. '+teams[10]+''
                                      '\n11. '+teams[11]+'\n12. '+teams[12]+'\n13. '+teams[13]+'\n14. '+teams[14]+''
                                      '\n15. '+teams[15]+'\n16. '+teams[16]+'\n17. '+teams[17]+'\n18. '+teams[18]+''
                                      '\n19. '+teams[19]+'\n20. '+teams[20]+'\nReserve\n1. '+teams[21]+''
                                      '\n2. '+teams[22]+'\n3. '+teams[23]+'\n4. '+teams[24]+'\n5. '+teams[25]+'**')
    await ctx.message.delete()


token = os.environ.get('BOT_TOKEN')
bot.run(token)








