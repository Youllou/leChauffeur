# leChauffeur
A french discord Bot<br>
link to add to server : https://discord.com/api/oauth2/authorize?client_id=779346176599130152&permissions=8&scope=bot
## Here come the HELP
between {} : optionals argument , between [] : required arguments<br>
stp is a shortcut for s'il te plait meaning please.<br>
I thought it was funny to ask politly to the bot to do things<br>
<br>
### reactions
 stp add `[word/expression to react to]` `[reactions]` (if one single `expression` contain spaces you've got to suround it by quotes, you can add more than a `reaction` by seperating each by a space)<br>
 adds a `word/expression` which the bot will react to with one of the give `reactions`<br>
<br>
stp rm `[word/expression to remove]`<br>
removes a `word/expression` from the reaction list<br>
<br>
stp reaction<br>
gives the reaction list (only `word/expression` which the bot will react to)<br>
<br>
### random bullshit GO
stp rand `{lettre number}` `{digit number}`<br>
generate a random lightshot link (lightshot is a web screenshot storage)<br>
<br>
### Be a `insert thing`
stp bzzbzz `{@somoeone}`<br>
be a bee (was part of an electoral campaign for a school association)<br>
<br>
stp titan `{@someone}`<br>
be a titan form attack on titan<br>
<br>
those two function will download your profile picture only during the file processing, then, all file containing your profile picture will be deleted from the local sever<br>
Though, you should be aware that the picture sent on discord will kept by discord's servers<br>
<br>
### Let's play a little Game
stp shifumi `[@someone]`<br>
play a game of shifumi against someone<br>
<br>
stp shifu_class<br>
have the leaderboard printed<br>
<br>
### admin only
stp active_react `[partout,#ici,nulpart]`<br>
will give the permission to the bot to react to `word/expression` added by users everywhere, on a specific channel or nowhere,<br>
with the specific channel beeing identified by it's mention `#channels-name`<br>
<br>
stp regarde `#ici`<br>
translated to look.<br>
It will tell the bot where to look for commands with `#ici` being the channel mention.<br>
Elsewhere it will not read commands<br>
<br>
stp goulag_config `[@gouag_role]`<br>
with this command you can setup a "goulag" role<br>
usualy this role doesnt have access to any channel or only one<br>
it is given as a punishment<br>
<br>
stp goulag `[@someone]`<br>
this command will remove all user mentioned roles and give him the role configured with goulag_config<br>
<br>
stp ajoute_roleReaction `[emoji]` `[@role]` <br>
translate to add_roleReaction<br>
this command should be done in a reply of a message<br>
with this command the bot will add an `emoji` reaction to the replied message<br>
whenever someone will click on that reaction, he will get the `role` assigned<br>
<br>
stp send [message]<br>
will send a message for you<br>
very usefull for the command just above<br>
