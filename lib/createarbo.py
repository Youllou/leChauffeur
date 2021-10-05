import os



def build(self,guild):
    f = open("../assets/Id2Name.csv", 'a', encoding='UTF-8')
    f.write(f"{str(guild.id)} : {guild.name}\n")
    os.mkdir(f"./assets/{str(guild.id)}")
    os.mkdir(f"./assets/{str(guild.id)}/music")
    f = open(f"./assets/{str(guild.id)}/role_react.csv",'w',encoding='UTF-8')
    f = open(f"./assets/{str(guild.id)}/emote_only_channel.csv",'w',encoding='UTF-8')
    f = open(f"./assets/{str(guild.id)}/reactions.csv",'w',encoding='UTF-8')
    f = open(f"./assets/{str(guild.id)}/commandChan.csv",'w',encoding='UTF-8')
    f = open(f"./assets/{str(guild.id)}/active_react.csv",'w',encoding='UTF-8')