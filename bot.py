import discord

client = discord.Client()

import csv
l = dict()
with open('listname.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0

    for row in csv_reader:
        l[row['name']]= 0

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    id = client.get_guild(766551335982071848)

    Kaguya = "Kaguya-sama wa Kokurasetai?: Tensai-tachi no Renai Zunousen"
    for i in l.keys():
        if i.find(message.content) != -1:
            l[i] = l[i] +1

    if message.content.find("top5") != -1:
        top=sorted(l.items(), reverse=True, key=lambda x: x[1])[:5]
        for x in top:
            await message.channel.send(f'{x}')


client.run("NzY2NTUxNzcyOTE0NTE1OTk5.X4lA-A.p3344ezCD3Mg2dR0NZlLPV1zOQA")
