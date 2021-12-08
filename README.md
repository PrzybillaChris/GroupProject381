# GroupProject381
## Welcome to out project!
A group project for the class 381 - Programmability and Automation by Chris Przybilla, Ben Strangler, and Jacob Mahoney

## Environment setup
In this tutorial we will go over the basic how-to's of how this program works.
The current set up is intended for two routers connected over the internet with BGP as their routing protocol. They will be managed through this program.
![image](https://user-images.githubusercontent.com/94020133/145106170-3dc82eba-3585-4536-99fd-ab2207d99697.png)

We will be using a Webex chatbot to accomplish tasks.
# What you will need for this bot.
•	Oracle VM VirtualBox Manager software
•	2 CSR1kv VMs for the routers
•	Webex developer/teams & an account affiliated with them
•	An Ngrok server hosted on a linux based client
•	Visual Studio code for running the program(or other programs that can run code)

To start out with this project load the files into your coding program and open up the 381Bot.py file.
From here scoll down until you see the bot details section:

![image](https://user-images.githubusercontent.com/94020133/145107177-fbeab37f-8bbe-4e82-b48f-439adfa5474d.png)

Enter in the information needed by the code to access your chatbot. Which includs the bots address, your teams token, and finally your ngrok session link.
The ngrok session link can be found after creating a session in a terminal window. Open a terminal window and enter the command 'ngok http 5000'
This will open an ngrok session for you to use. Copy and paste the https link from here and paste it into the 381Bot.py code.

![image](https://user-images.githubusercontent.com/94020133/145107537-92f103eb-1fd1-4112-82c7-032cc3275fb9.png)

Once you have these in there, go to the uselessskills.py file and enter your webex teams token again into the teams_token variable quotes.

![image](https://user-images.githubusercontent.com/94020133/145107730-d024e698-552f-443d-a9fb-adfb640d4448.png)

If you do not already have one already, make a webex for developers account. Got to start making apps and create a new application.

![image](https://user-images.githubusercontent.com/94020133/145109003-1ee3f1a4-157d-40b8-95bd-65121e71ec9a.png)
![image](https://user-images.githubusercontent.com/94020133/145109044-b9bf4ec1-ec5c-46c6-89c5-3b0a20518052.png)

Select Create a bot

![image](https://user-images.githubusercontent.com/94020133/145109119-80305e33-c656-47ba-aa22-bc9fc9caf92d.png)

Upon finishing the completion of making the bot you will be presented with your bots access token. Enter this is in the bots address line in the 381Bot.py file.

Using the same login as the webex developer account sign into Webex Teams and set up a chat session with the chatbot. Just enter the bot access token in as the person to add in the conversation.

Now that we have this all set up, we can almost use out chatbot with the commands in the 381Bot.py file.
Below are tutorials on how to set up each of the functions with your own devices. Note the devices used for making this program were hosted in Oracle VM Virtualbox, so you will have to change the ip address settings for the devices for them to work properly.

## Starting the chatbot Tutorial
To start the chatbot to work with any of the program files you will first need to start the chatbot. To do this first start your ngrok session and copy the session id into the 381Bot.py file.
Then go into visual studio code or its equivilent and open a ternial(by hitting terminal -> New terminal) if one isnt already open and enter the command python3 381Bot.py. This will start the python program and connect it to the chatbot for response.
It will look something similar to this and once it goes to the connected page you can begin sending commands to the chatbot.

![image](https://user-images.githubusercontent.com/94020133/145112430-cc51d9ac-c100-4773-be21-7bfb8f11f5a1.png)



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



## Ansible Program Tutorial

In this tutorial I will go over how to get the anisble program working.
The ansible function is for backing up a device's running configuration.
In the chatbot type either backup or router2 to bakup either device.
To donfigure these devices in the settings go the their correspondent hosts and playbook files detailed in their function catagories

![image](https://user-images.githubusercontent.com/94020133/145112774-27fe3488-ddb1-4baf-a19c-6289b38d663a.png)
Enter in the ip address of the device along with the username and password for ssh to connect to it in the hosts file.

![image](https://user-images.githubusercontent.com/94020133/145113053-c15e3ca7-1c33-43fd-9116-66cebee2150c.png)
Then in the backup_cisco_router_playbook.yaml files just change the hosts variable to the hostname on the device itself.

![image](https://user-images.githubusercontent.com/94020133/145113270-befec283-afd6-481f-8a8b-eb68d23b7cc1.png)

From here the program will run and save the running config of the devices to the backups folder with the command that was run and on the device specified.

![image](https://user-images.githubusercontent.com/94020133/145113386-0c2a1558-861e-4b23-8fce-2616b04bd519.png)


## Genie Robot Tutorial
This function titled monitor_int is used to continually monitor the status of interfaces on the two routers. Checking their status if they are up or down and reporting it back to the chatbot.
With this program it is goof to note that you only need to modify the routers/yml file in the testbed folder.
Edit the ip, password, and username fields to make this operational. Note: make the password field appear in the encrpyted form it does in the devices show run section, not in plaintext.
Once this is done you can run the 'monitor interfaces' command. This will use the monitor_int function. From here it will monitor the interfaces every 20 seconds and send updates to the bots interface. On all interfaces being up it will display:

![image](https://user-images.githubusercontent.com/94020133/145114487-ac6f4381-885d-4762-a7c5-8584aac33a28.png)

On an interace going down it will display:

![image](https://user-images.githubusercontent.com/94020133/145114574-9334c1ac-c462-41f3-b6ed-85b7d57597b6.png)

This allows for network admins to distinguish problems with their interfaces and fix them accordingly.
You can use the 'stop monitoring' command at any time to stop the monitor.
This program utilizes the testbed to connect to the routers and set up to connection for future use in the monitoring session.

## Genie Monitoring for diaster Tutorial
Much like the previous monitoring function, this will monitor interfaces and their states. This one however is meant to be used on one interface in the event that it would change or whatever reason it may be. The purpose is to restore a site-to-site vpn connection that would go down as a result of an ip address changing.
So as with the previous tutorial examine the routers/yml file ad change the ip, password, and username fields.
Once here we need to modify a couple of files to the specifications of your devices.
Since this setup is meant to change the ip address of a changing interface, we need to adjust the ip of the device that doesn't change. Go to the intial_ip.py file and change the 2nd if statements ip address to the ip of the device that is not changing.

![image](https://user-images.githubusercontent.com/94020133/145125422-4eaa3c0b-b58a-4bed-a602-b0c5be488dfb.png)

In the monitor_VPN_int.py file, so the same thing as the previous step and change the ip address to the address of the device that will not be changing.

![image](https://user-images.githubusercontent.com/94020133/145125595-481c3268-1845-43d9-8471-ae6ab8666560.png)

From here the code is ready to run
Enter monitor-vpn into the chatbot to start the code.
What this function will do is: 
•	Check the intial ip on start of the command and store it into a variable
•	Check the current ip address of the interface
•	Compare the old ip address to the new ip address.
•	If they are the same then the code will do nothing and wait for the duration of the timer to test it again. The timer can be changed to a different value in the monitor_vpn_job function at any time.
•	If the addresses are different, then the program reconfigure the vpn addressing int he running config to reflect the new topology.
•	The new address will be saved into the old_ip variable to then be tested on future values by the program.

As a note the bot gives no indication that it is running, this part is intentional so that any addressing changes can be easily found and recorded if need be. That being said any changes in ip addressing found by this program will be directly sent to the chatbot.

![image](https://user-images.githubusercontent.com/94020133/145127949-829dd63a-e5d0-4a5b-88b2-69c44c8038fb.png)

That is all for this project. There are some other functions in this chatbot that can be used for other networking purposes not mentioned in this guide.






