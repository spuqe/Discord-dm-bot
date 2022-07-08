import discum, random, time
from rich import console, print
bot = discum.Client(token=input('Token: '), log=False)
memberz = []
guildz = input("Please input guild ID: ")
channel = input("Please input a channel ID in that guild: ")
messag = ("{Capitan's signals} \n We are a crypto trading community that educates people about trading, gives profitable signals, and looks forward to making a profit! We discuss about crypto and its opportunitie \n \n ● Free crypto singals \n ● Crypto help \n ● Crypto tricks and tips\n ● Free learning material\n\n https://cdn.discordapp.com/attachments/913434621578973184/939879699360919632/desing.jpg\n \n \n https://capttrade.vip/\n https://discord.gg/4mY8356svm\n https://t.me/Captains_Signals\n")
timez = ("1")
@bot.gateway.command
def memberTest(resp):
    if resp.event.ready_supplemental:
        bot.gateway.fetchMembers(guildz, channel)
    if bot.gateway.finishedMemberFetching(guildz):
        bot.gateway.removeCommand(memberTest)
        bot.gateway.close()
bot.gateway.run()
print("Starting add members.")
for memberID in bot.gateway.session.guild(guildz).members:
    memberz.append(memberID)
print("Starting to DM.")
for x in memberz:
    try:
        rand = random.randint(0,20)
        if rand == 20:
            print(f'Sleeping - 45s')
            time.sleep(45)
            print(f'Waking up!')
        print(f"Ready to send some dms {x}.")
        time.sleep(int(timez))
        newDM = bot.createDM([f"{x}"]).json()["id"]
        bot.sendMessage(newDM, f"{messag}")
        print(f'DMed {x}.')
    except Exception as E:
        print(E)
        print(f'Couldn\'t DM {x}.')
