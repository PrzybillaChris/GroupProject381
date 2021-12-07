# GroupProject381
A group project for the class Programmability and Automation 381 by Chris Przybilla, Ben Strangler, and Jacob Mahoney



## Paramiko Tutorial
For you to get the code you would need to download Oracle VM VirtualBox Manager and need 3 VMs. 2 that would act like a router and the VM that can act like the desktop. You would first need to create a bot that can chat with you on Webex developer. Do not have an account then create one. With a bot made then you write some code that will give the bot something to do for you. Sometimes you would want to see the output of all your coding for a router. With the code that is written down will show you the running-config of the router that you want. That being either router1 or router2. With that you would need to have something that will show the running-configuration or the configuration that you made for the router. It can help troubleshoot if there is a problem and just to see the finished product of your hard work coding for the router. The code that I wrote will go through the router with the use of Paramiko that will put the entries of enable, config terminal, username and password then show running-configuration command (show run). 
### Requirements:
•	Oracle VM VirtualBox Manager software
•	2 CSR1kv VMs for the routers
•	Webex developer/teams & an account affiliated with them
•	Knowledge of the Paramiko coding language and some python coding language

The Final product:
 ![image](https://user-images.githubusercontent.com/94020133/145105031-8c61ad41-c8f5-464b-ad6e-fe4441ddc080.png)


To start off you would need to create an account with Webex if not done so before. Then you would create a bot with the create an app function when you create the account and login. Then with that you need the tokens for the bot. Would need the import commands of:
 ![image](https://user-images.githubusercontent.com/94020133/145105042-7c3dbb0a-96cf-483b-9ab3-89aaf72fc619.png)

 
You would need to create a function/def command. With that it will then allow you to put in the code and be able to just call the function to run through the code within the function. That makes it easier.
![image](https://user-images.githubusercontent.com/94020133/145105053-086e34e5-2ab9-4ee6-b1e1-243a4bf4b509.png)

 
You would need to add the different routers, by doing router (1 or 2), give what the hostname is which is the IP address of the routers/CSR1kvs, the port that you are using, which is port 22, give the username and password to get into the router/CSR1kvs. 
![image](https://user-images.githubusercontent.com/94020133/145105077-1ebcf7b3-3540-495d-9f7c-ae83b04da265.png)


Then you would need to put the if/elif statements so it can differentiate between which routers you would be connecting to. With the if statement you would be putting the code that calls a response variable to make into the message you are trying to convey. Then, would connect you to the routers by using SSH. Then you will add which router you would like to connect to by using the ssh.client commands. With the connection then you would need to use the shell = ssh_client.invoke _shell() to make a shell object to implement into the router. 
![image](https://user-images.githubusercontent.com/94020133/145105093-f1e20277-ff3f-40be-b5f3-c95b4831bb57.png)
![image](https://user-images.githubusercontent.com/94020133/145105116-fa3daf75-7d9e-498b-bae6-f0960457f853.png)

 
With the start of the if/elif statement good, you would then have the shell object get called and send the code you would want to implement for the shell to send to the router. Which is the shell.send command with the input of terminal length 0, enable, password of the router which is cisco123!, and then the show run code. After implanting the shell.send commands you have time.sleep (#) for however long you would want the code to halt to make sure everything is peachy. Then you have the output = shell.recv(#) for reading the buffer for the ouput. Then you have the response.text = ouput.decode(‘utf-8’) to decode the encoded message.  
![image](https://user-images.githubusercontent.com/94020133/145105140-c0eed541-8932-40af-942c-af03d78bc10b.png)
![image](https://user-images.githubusercontent.com/94020133/145105150-fc067987-c456-4cd8-9e61-535b52ceec12.png)


Then you must close the ssh connection and print out the message that you are closing the connection by using an if statement to see if it is to close or not. Then you would need to return the response. To send the message to your bot that you created.
![image](https://user-images.githubusercontent.com/94020133/145105171-ef33fbd8-e514-4368-8aa9-74b3e954c317.png)
![image](https://user-images.githubusercontent.com/94020133/145105184-bc68f771-72da-47ba-b41e-1bfdd5944d13.png)

  
Then you would need to add a bot.add command to make sure that you can add the code/def that you just made can be used. Which is bot.add (what you want the things that are to be displayed on the /help page that you have. Then you would add a description of what it is and then the function that you made.
 ![image](https://user-images.githubusercontent.com/94020133/145105192-fced85dc-2b82-41a8-bac1-e1a6f40bb7f4.png)
![image](https://user-images.githubusercontent.com/94020133/145105206-63c71125-ddd6-406d-a484-5eb02457b42c.png)
 
That should be the end and you should be able to finish the code then.




























## Netconf Tutorial

Sometimes, certain events will require an interface to be shut down or turned on and its connection terminated or restored. For this reason, it can be beneficial to have an easy way to turn these interfaces off with one simply line of code rather than having to enter the device’s console, enter the exec password, enter global configuration mode, select the interface, and then turn it off or on. With the help of a Webex bot and Netconf, we can turn this long hassle into a simple, one-line, command that does all the work for you.

### Required Resources:
•	Visual Studio Software
•	2 virtual CSR1000 machines
•	A Webex Teams account
•	The following import commands in visual studio:
 
 ![image](https://user-images.githubusercontent.com/94020133/145104409-9c759335-4cd3-4d0b-ac29-1e7daae31001.png)


First off, a connection was created between the two routers using the G2 interface on both routers. After this, a management connection was created within Visual Studios for both routers (M being router 1 and R being router 2). This connection would include the host ip, port, username, password, and hostkey_verify functions of interface G2 on both routers.
![image](https://user-images.githubusercontent.com/94020133/145104433-56e3f501-76a3-46c4-a15b-01f024b894a6.png)

 
After creating these commands, we can create the “add.command” command that creates the actual framework for changing the state of the desired interface. This was done by using the command bot.add_command("Name of command", "Description for command”, “Name for command function”).  For our command, we used the name changeint and a command function of change_interface. The user would input changeint within the bot and when the bot identifies the command, it will run the change_interface function.  This change interface function is described below.
 ![image](https://user-images.githubusercontent.com/94020133/145104455-573d8d0b-fab1-4104-a2e0-d2a0b5c6276f.png)

From here, a config command using XML is created. The interface that will be turned on or off will be GigabitEthernet2. The XML configuration will automatically be set to true for enabled, meaning it will be turned on by default. After this, an if statement is utilized to determine if the connection on either router 1 or 2 needs to be enabled or disabled.
![image](https://user-images.githubusercontent.com/94020133/145104464-f221a828-eb87-4cf5-aedd-87fe8b4c79c3.png)

 
If the user types in “changeint enable 1”, router 1’s GigabitEthernet 2 interface will be set to up, and a response of “Int G2 was successfully enabled.” will display on the bot. The same thing will happen to router 2 if the user changes the 1 in “changeint enable 1” to a 2. If the user wishes to shut down the interface in question, they can change the enable portion of the command to disable (changeint disable 2). This will, in turn, send a response through the Webex bot that says “Int G2 was successfully disabled”. If the user, by chance, misspells any part of the command or enters any invalid variables, the bot will respond with “Wrong command, please try again.” instructing the user that they messed up somewhere in the command. 
