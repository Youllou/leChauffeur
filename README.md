# leChauffeur
A french discord Bot

## Here come the HELP
between {} : optionals argument , between [] : required arguments
stp is a shortcut for s'il te plait meaning please.
I thought it was funny to ask politly to the bot to do things

### reactions
 stp add `[word/expression to react to]` `[reactions]` (if one single `expression` contain spaces you've got to suround it by quotes, you can add more than a `reaction` by seperating each by a space)
 adds a `word/expression` which the bot will react to with one of the give `reactions`

stp rm `[word/expression to remove]`
removes a `word/expression` from the reaction list

stp reaction
gives the reaction list (only `word/expression` which the bot will react to)

### random bullshit GO
stp rand `{lettre number}` `{digit number}`
generate a random lightshot link (lightshot is a web screenshot storage)

### Be a `insert thing`
stp bzzbzz `{@somoeone}`
be a bee (was part of an electoral campaign for a school association)

stp titan `{@someone}`
be a titan form attack on titan

those two function will download your profile picture only during the file processing, then, all file containing your profile picture will be deleted from the local sever
Though, you should be aware that the picture sent on discord will kept by discord's servers

### Let's play a little Game
stp shifumi `[@someone]`
play a game of shifumi against someone

stp shifu_class
have the leaderboard printed

### admin only
stp active_react `[partout,#ici,nulpart]`
will give the permission to the bot to react to `word/expression` added by users everywhere, on a specific channel or nowhere,
with the specific channel beeing identified by it's mention `#channels-name`

stp regarde `#ici`
translated to look.
It will tell the bot where to look for commands with `#ici` being the channel mention.
Elsewhere it will not read commands

stp goulag_config `[@gouag_role]`
with this command you can setup a "goulag" role
usualy this role doesnt have access to any channel or only one
it is given as a punishment

stp goulag `[@someone]`
this command will remove all user mentioned roles and give him the role configured with goulag_config

stp ajoute_roleReaction `[emoji]` `[@role]` 
translate to add_roleReaction
this command should be done in a reply of a message
with this command the bot will add an `emoji` reaction to the replied message
whenever someone will click on that reaction, he will get the `role` assigned

stp send [message] (pas besoin de guillemets)
