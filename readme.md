# Discord bot to take attendance for meetings and sprints

## How to use
1. Create a virtual environment and install the packages.  
`pip3 install -r requirements.txt`
2. Create an application and a bot [here](https://discord.com/developers/applications). Under the 'Bot' tab,
    - Copy the Token into a `.env` file:  
    `DISCORD_TOKEN={TokenHere}` 
    - Activate 'SERVER MEMBERS INTENT'.
3. Invite the bot to join a server  
    - Under the 'OAuth2' tab, select 'bot' and make sure you have View Channels and Send Messages permissions.
    - Go to the generated URL and choose a server, click Authorize. Note that you will only see the server where you have "Manage Server" permissions. You should now see the Bot in the server.
4. In your discord server, right click the text channel for the Bot to post to and copy the ID. Replace this in `main.py` TEXT_CHANNEL_ID. Do the same for for the voice channel for the Bot to take attendance in.  
5. Run the bot with `python3 main.py`. To see a list of the available commands, type `!help` in the discord channel.  
