# **TwoFactor**

About: Twofactor.py is a program that generates an 8 factor code that is sent to a cell phone and can be used for 
authentication

Functionality: Generate a secure two factor authentication code every 60 seconds.

How to use:

1. Clone TwoFactor into a directory of your choosing
2. Open a Windows Powershell, Windows Command Prompt, or *NIX Terminal in the directory of EZConfig.py
3. Enter `python TwoFactorRun.py` in the command line
   1. Note: If program does not run properly, use `sudo python TwoFactorRun.py`
4. Example: `C:\Users\Admin\Documents\Python\TwoFactor' python TwoFactorRun.py`
5. Your two factor code will be printed to the command line
	1. `CTRL + C` will stop the program

In Progress:
1. Sending code via SMS to a cell phone number
2. Proper code authentication, invalidation of old code after 60 seconds
3. Encryption
