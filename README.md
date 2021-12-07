# GroupProject381
A group project for the class Programmability and Automation 381 by Chris Przybilla, Ben Strangler, and Jacob Mahoney




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
