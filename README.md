# YayaBot

hi, this is a moderation type bot for IBXToycat's discord server!

Requirements:
[Python 3.8+](https://www.python.org/downloads/), 
[Git](https://git-scm.com/downloads), 
Pip (for module install)

Quickstart Debian/Ubuntu:
`sudo apt install python3 git python3-pip`

### How Do I Run The Bot?
- download/clone it
`git clone https://github.com/SushiInYourFace/YayaBot`
- in the directory run
`python -m pip install -r requirements.txt -U`
- get your bot's token from the [discord applications page](https://discord.com/developers/applications/) and put it in a new file named `token.txt`
- run the bot!!
`python start.py`

("python" may be "py" (on windows) or "python3" (on linux if other versions are installed)) (sudo/admin may be required for downloading requirements or use `--user` to install for your user)


### What Is This Bot For?

This bot is designed to be specifically tailored to the needs of the IBXToyChat server, as the server's needs are not fully satisfied by a generic discord bot.

### Will It Work In My Server?

Because the bot is designed for ToyChat specifically, in order to use it you will need your server to be set up in a way similar to the Toychat server. In order to use all the bot's features, your server should have
- a mute role that lets users see channels they normally would, but removes their permission to send messages there
- a "gravel" role that prevents users from seeing normal channels, and optionally grants them permission to another channel only seen by moderators and those with the role
- A moderator role with limited powers, as well as an administrator role with greater permissions
- A modlog channel, where the bot can store edited and deleted messages.

**PLEASE NOTE:** This bot is still very much a work in progress, so it is not recommended to use it in its current state.
