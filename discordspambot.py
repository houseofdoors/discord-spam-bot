import pyautogui, sys, time

# Discord spam bot program. I was too busy asking whether or not I could, I forgot to ask whether I should.

def sendspam():
    # Warning
    print('''This bot spams a message of your choice on Discord.
    It sends the message to whatever page you are on in Discord.
    It does not stop until you press CTRL+C while in the command window.
    It only posts 1 message per second due to Discord's 5/5 rule. Any faster and you will get IP banned for API abuse.
    This may get you banned, and your friends now hate you.''')
    message = input('Enter your message here: ')
    try:
        while True:
            # Spams the user's desired message, with a short gap to prevent getting stopped for spam.
            pyautogui.click(400, 990)
            pyautogui.typewrite(f'{message}')
            pyautogui.typewrite('\n')
            time.sleep(1)
    except KeyboardInterrupt:
        # Exits the program if the users clicks CTRL+C
        sys.exit()

sendspam()