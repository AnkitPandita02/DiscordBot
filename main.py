import os

import discord
import openai

# with open("chat.txt", "r") as f:  code to train the bot 
#   chat = f.read()
chat = ""

openai.api_key = os.getenv(" your_OPENAI_API_KEY")

token = os.environ['YOUR_SECRET_KEY\TOKEN FROM DISCORD']


class MyClient(discord.Client):

  async def on_ready(self):
    print(f'Logged on as {self.user}!')

  async def on_message(self, message):
    global chat
    chat += f"{message.author}: {message.content}\n"
    print(f'Message from {message.author}: {message.content}')
    if self.user!= message.author:
      if self.user in message.mentions:
        channel = message.channel
        response = openai.completions.create(
          model="text-davinci-003",
          prompt = f"{chat}\n",
          temperature=1,
          max_tokens=256,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0
        )
        messageToSend = response.choices[0].text
        await channel.send(messageToSend)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
