
# Discord.py Workshop 

## Introduction to creating Bots in Python 

Discord is one of the world's most popular messaging apps currently, allowing millions to communicate each day over their platform. To increase how interactive messaging over Discord can be, Users can create Discord Bots, which can do a multitude of things such as:

<ul> 
	<li> Built-In text based games </li>
	<li> Displaying information from other websites using APIs and Webhooks </li>
	<li> Manage the security and permissions of your server and its members </li>
	<li> And many more!  </li>
</ul> 

To achieve this, we will be utilizing a Python based API Wrapper made for Discord called <a href='https://discordpy.readthedocs.io/en/stable/'> <u> Discord.py </u> </a> 
To get started first join this discord to add your bot in: https://discord.gg/JXggbVHFwB

## Beforehand Knowledge

In this particular workshop, our main goal is to create a useful Discord Bot that can display information for a multitude of public APIs at our disposal. In this instance, we will be using an API that outputs a random cat image.  This workshop will teach our students the idea of Asynchronous programming and how Python can be used to built something useful at the Intermediate level. 

### 1. Understanding the Module 

```Discord.py``` is a fairly complex module to understand as it comes bundled with the use of multiple libraries to function correctly in addition to the use of class based programming. Because of this, we want our students to understand that referring back to the documentation of this module is highly encouraged. Its simply impossible to understand and know everything when first going into intermediate level programming via Python. 

### 2. Asynchronous Programming

Asynchronous Programming is an essential part to developing Discord bots within Python and even on other platforms. In order for code to understand when to return a particular response, we need to ensure that the code is constantly running and 'listening out' for an input to return said output. This is where Asynchronous programming comes in, it allows us to complete multiple tasks without necessarily being done with a separate one. 

### 3. Discord Developer Portal 

In order to actually run our bot on Discord we'll have to use the Discord Developer Portal. The Discord Developer Portal is the place where we can create applications and generate a specific key that coincides with said application. We need this special key to verify our bot and ensures no one can alter it...as depending on our bot's permissions, it could damage the discord server its in. To do this we need a discord account, and on the <a href='https://discord.com/developers/applications'>Discord Developer Portal Website</a>, click new application to create your first application!

<p align="center">		
 <img src="https://i.ibb.co/q5fkSJ8/download.png"> 
</p>

<br>

<p align="center">
 After creating your application, scroll down to the Bot Tab 
</p>

<br>

<p align="center">
 <img src="https://i.ibb.co/M8QywsS/image.png"> 
</p>

<p align="center">
 Here we're going to do two things: Reset our bot token and save this somewhere safe, whether it be in our browser, notepad or otherwise, 
 </p>
 
<br>

<p align="center">
<img src="https://i.ibb.co/9rzwZHH/image.png"> 
</p> 

<br>

<p align="center">
 Then, under "Privileged Gateway Intents", check each of these boxes and don't forget to save the changes ! 
  </p> 

<br>

<p align="center">
<img src="https://i.ibb.co/NyjWGyN/image.png"> 
</p> 

<br>

<p align="center">
 That's all we need to do to prepare for our discord bot!  
</p>

<br>

Now in order to add our newly created bot to a server, we have to navigate to the Oauth2 Tab, from there we click URL Generator. From there we will select only the **'Bot'** scope and the  **'Send Messages'** permission. After scrolling to the bottom where it says Generated URL, we can copy this link, open it in a separate tab, and invite our bot to our server !

<p align="center">
	<img src="https://i.ibb.co/RybGT4c/image.png"> 
</p>



## Creating the Image-Downloader 

### 1. The Boilerplate



The Boilerplate will consist of the code needed to run a discord bot. 

```python
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

```
Our code consists of the necessities needed to start a Discord Bot. We import the discord module to actually connect to discord and the requests module, which we'll use what we learned in our Python API workshop to make a request to a cat image API. We created a class named MyClient and passed the discord.Client argument to establish the link between discord and our machine. We can use MyClient methods (Functions) to perform specific tasks as these are pre-defined and outlined on the documentation. 

The 'async' keyword turns our pre-defined on_ready function into an asynchronous function which waits for the parameters needed to send the code within the block. We will send our bot's username and user ID once the link to discord is established. 

If we were to run this code ( With your specific bot token added ), the output will be similar to this: 
<p align="center">
	  <img src="https://i.ibb.co/XFYHY6H/image.png"> 
</p>



### 2. On_Message Method 

The on_message method allowed our bot to listen out for a particular message sent by a user, and send a response based on it. We can ensure that the bot only responds to a message not sent by itself by comparing the IDs sent by the user and the ID of the Bot! 

```python

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
			await  message.channel.send('I love cats')


```
As an example, we can set the bot to send the message " I love cats! " if a user says the word cat. 
<br> 

<p align="center">
The output should look like this: 
</p> 
<p align="center">
	 <img src="https://i.ibb.co/1GyR0qK/image.png"> 
</p>




### 3. Adding an API to our bot 

We can utilize the on_message method and a separate function in order to send information retrieved from an API request through our discord bot. For this we'll be using a request library. First, lets create a new function named 'kitty'
 
```python
def kitty():
	# 
```

Using the request library, lets make a request to the cataas API, and save the JSON data we retrieve from it as JSON data

```python


def kitty():
	response = requests.get('https://cataas.com/cat?json=true')
	json_data = response.json()


```
Then we can do some string editing in order to get the cat image as an actual image that can be sent by the bot. 

```python


def kitty():
	response = requests.get('https://cataas.com/cat?json=true')
	json_data = response.json()
	cat_image_url = json_data['url']
	cat_image = 'https://cataas.com/' + cat_image_url
	return cat_image 



```

We can now pass this function through our original on_message method in order to allow our bot to send a cat image anytime we say the word cat.

```python
import  discord
import  requests

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
			await  message.channel.send(kitty())


```

<p align="center">
The Output should look like this: 
<p> 
<p align="center">
 <img src='https://i.ibb.co/68xyHDZ/image.png'> 
 </p>


### 4. Additonal Learning

Now that we've completed the workshop, there are so many possibilities with Discord.py that you can try out for yourself. We implore our students to look for more content centered around creating a useful discord bot, especially the documentation. You can even try to utilize your own API request in your bot to find the information you desire ! 


| Additional Learning  | Description |
| ------------- |:-------------:|
| [Discord​​​​.py Docs](https://discordpy.readthedocs.io/en/stable/)     |```Discord.py``` is a Python library that exhaustively implements Discord's APIs in an efficient and Pythonic way.|
| [Code a Discord Bot with Python - FreeCodeCamp](https://www.youtube.com/watch?v=SPTfmiYiuok&ab_channel=freeCodeCamp.org)    | Constructive course on how to make a Discord Bot in Python3 created by FreeCodeCamp|
| [Python Requests Module - W3Schools](https://www.w3schools.com/python/module_requests.asp)| Learn how to Create API requests in Python  |
 [Introduction To JSON - W3Schools](https://github.com/public-apis/public-apis) | An intro to utilizing and understanding JSON data and why it's crucial in programming.
| [Public APIS - Github](https://github.com/public-apis/public-apis) | A list of free to use APIs that you can include within your projects ! | 
 [Classes In Python - W3Schools](https://github.com/public-apis/public-apis) | A brief look at how classes/objects are initialized and used within Python3 




