# damons_ping_graph
This is a tool used by DamonTheBot's developers to see network ping stats between the bot and discord.

# Use of the script.
This script is used to create a graph of the ping progression over time.

# IMPORTANT
This script DOES NOT get the ping of the application alone. You have to make an integration to your code writing the data in
the ping.data file inside the Ping_data folder in the format

tick:ping_number,\n

ie. 
1:1024,\n
2:679,\n
3:254,\n
4:233,\n
4:344,\n
5:445\n

# Installation
Have you got git; you can run '` git clone github.com/KlausVolkog/damons_ping_graph `' else, go to '` Code > Download zip `'
To run the script, you have to have python installed and then to install the module needed run '` pip install matplotlib `'
After the modules installation you can run the script freely.

# Program SceenShots
![image](https://user-images.githubusercontent.com/62770862/174667052-b138a90f-8056-432d-bfe8-f3ae58ddcd4b.png)
