import discord
import requests


def kitty():
	response = requests.get('https://cataas.com/cat?json=true')
	json_data = response.json()
	cat_image_url = json_data['url']
	cat_image = 'https://cataas.com/' + cat_image_url
	return cat_image 

class  MyClient(discord.Client):

	async  def  on_ready(self):
		print(self.user)
		print(self.user.id)
		
	async  def  on_message(self, message):
		
		# Ensures that discord bot does not reply to itself 
		if message.author == self.user:
			return 
		# Bot sends 'I love cats' if a server member sends the word cat 
		if  message.content.startswith('cat'):
			await message.channel.send(kitty())



intents = discord.Intents.default()
intents.message_content = True


client = MyClient(intents=intents)
client.run('INSERT BOT TOKEN HERE ')
