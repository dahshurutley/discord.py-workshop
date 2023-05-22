# ------- Starter Code Start -------- #
# Modules 
import  discord
import  requests

class  MyClient(discord.Client):

	async  def  on_ready(self):
		print(self.user)
		print(self.user.id)

# <---- Allows our bot to send messages ---->

intents  =  discord.Intents.default()
intents.message_content =  True

# <----------------------------------->

#  <------ Runs the 'Client' (Bot) ------>
client  =  MyClient(intents=intents)
client.run('Input you Private Key Here !!! ') 

# ------- Starter Code End -------- #
