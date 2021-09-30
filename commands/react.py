#local imports
from deff import *

@leChauffeur.command()
async def ajoute_reaction(ctx,toReact,*reaction):

    commands=[]
    exist=0
    i=6


    #opening the file and stock it
    f=open("assets/commands.csv",'r',encoding="UTF-8")
    while 1:
        line = f.readline()
        if line == "":
            break
        else:
            commands += [line.split(",")]
    f.close()

    #verifying if the first expression already exists or not
    for i in range(len(commands)):
        if (toReact.lower() == str(commands[i][0]).lower()):
            exist=1
            nline=i
            break

    #if the first expression doesn't exits we just write all the message
    if (exist == 0):
        f=open("assets/commands.csv",'a',encoding="UTF-8")
        f.write(toReact)
        for i in reaction :
            f.write(","+i)
        f.write("\n")

    #else, we take only last part and add it to the already existing line
    else :

        f=open("assets/commands.csv",'r',encoding="UTF-8")
        commands = f.readlines()
        f.close()

        tmp=""
        for i in range(len(commands[nline])-1):
            tmp+=commands[nline][i]
        commands[nline]=tmp
        for i in reaction :
            commands[nline]+=","+i
        commands[nline]+="\n"


        f=open("assets/commands.csv",'w',encoding="UTF-8")
        f.writelines(commands)


    f.close()
    await ctx.message.delete()

@leChauffeur.command()
async def rm(ctx,toReact):

    commands = []
    exists = 0

    f=open("assets/commands.csv","r",encoding="UTF-8")
    while 1:
        line = f.readline()
        if line == "":
            break
        else:
            commands += [line.split(",")]
    f.close()

    for i in range(len(commands)):
        if toReact == commands[i][0]:
            nLine=i
            exists=1
            break

    if exists == 1:
        f=open("assets/commands.csv","r",encoding="UTF-8")
        text=f.readlines()
        f.close()
        text.pop(nLine)
        f=open("assets/commands.csv","w",encoding="UTF-8")
        f.writelines(text)
        await ctx.message.delete()
    else :
        await ctx.send("Cette expression n'a pas été trouvé")
