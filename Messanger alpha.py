# Imports
from datetime import datetime

# Globale Variablen
posts = {}
user_current = None
user_pass = None
besuche = 0
access = False
guest_user = set()
name = None

# Defs
def login():
    user_current = None
    access = False
    while access != True:   
        user_log = input('Gib deinen Benutzernamen ein: ')
    
        match user_log:   
            case 'Arin':
                user_pass = input('Gib dein Passwort ein: ')
                if user_pass == 'a07':
                    print('Willkommen zurück!')
                    user_current = 'Arin'
                    access = True
                else:
                    print('Das Passwort ist falsch')
                    
            case 'Rieke':
                user_pass = input('Gib dein Passwort ein: ')
                if user_pass == 'r09':
                    print('Willkommen zurück!')
                    user_current = 'Rieke'
                    access = True
                else:
                    print('Das Passwort ist falsch')
        
            case 'Dagmar':
                user_pass = input('Gib dein Passwort ein: ')
                if user_pass == 'd72':
                    print('Willkommen zurück!')
                    user_current = 'Dagmar'
                    access = True
                else:
                    print('Das Passwort ist falsch')
        
            case 'Helmut':
                user_pass = input('Gib dein Passwort ein: ')
                if user_pass == 'h68':
                    print('Willkommen zurück!')
                    user_current = 'Helmut'
                    access = True
                else:
                    print('Das Passwort ist falsch')
                    
            case 'Lara':
                user_pass = input('Gib dein Passwort ein: ')
                if user_pass == 'l06':
                    print('Willkommen zurück!')
                    user_current = 'Lara'
                    access = True        
                else:
                    print('Das Passwort ist falsch')
                    
            case _:
                fehlerfrage = input('Dieser Benutzer existiert nicht \n War es ein Tippfehler? \n [ja/nein]: ')
                if fehlerfrage != 'nein' and fehlerfrage != 'Nein':
                    acces = False
                else:    
                    user_current = new_guest_user(name)
                    print('Du bist als Gast eingeloggt')
                    access = True

    return user_current


def start_mess():
    if __name__ == '__main__':
        # "None" bedeutet "Nicht gesetzt, aber bekannt"
        aktion = None
        besuche = 0  
        user_current = login()
        new_guest = set()
        
        while aktion != 'Q':
            aktion = input('Was möchtest Du tun? \n [P - Post erstellen, R - Posts lesen, Q - Beenden, L - Log Out] \n Eingabe: ')
            
            if aktion == 'P':
                post_text = input('Text: ')
                zeit = str(datetime.now())
                print(user_current + ' ' + zeit + ': ' +post_text)

                posts[user_current, zeit] = post_text

            elif aktion == "R":
                if posts == {}:
                    print('Keine Posts verfügbar, die du lesen könntest ;) \n')
                else:
                    print(posts)
                    besuche = besuche + 1
                    print ('Anzahl Besuche:', besuche)
                
            elif aktion == 'L':
                new_guest.clear()
                print('Du sind ausgeloggt. \n Gib deine Daten ein, um dich erneut einzuloggen. \n')
                user_current = login()
            
            elif aktion == "Q":
                print('Tschüss!')
                new_guest.clear()
                
            else:
                print('Aktion ist nicht erlaubt')
                

def new_guest_user(name):
    name = input('Gib deinen deinen Gastnamen ein: ')
    guest_user.add(name)
    return name

# Start
start_mess()
