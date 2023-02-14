import csv
from tkinter import *
from tkinter import messagebox
import hashlib

#CSV-Datei öffnen und Speichern von Daten ermöglichen
def open_csv():
    with open("users.csv", 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        users = list(reader)
    return users

#Speichern und verschlüsseln von Passwort und Benutzernamen
def save_credentials():
    username = username_entry.get()
    password = password_entry.get()
    hash_object = hashlib.sha256()
    password1 = password.encode()
    hash_object.update(password1)
    hex_dig = hash_object.hexdigest()

    with open("users.csv" , mode="a", newline="") as csv_file:
        fieldnames = ["username", "password", "highscore1", "score1", "highscore2", "score2"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({"username": username, "password": hex_dig, "highscore1" : 0, "score1" : 0, "highscore2" : 0, "score2" : 0})




#Erstellen vom UI für Login/Registrierung
root = Tk()
root.geometry("300x200")
root.title("Super cooles Spiel")
LR_label = Label(root, text="Login/Registrierung", font=("Arial Rounded", 18))
username_label = Label(root, text="Benutzername")
username_entry = Entry(root)
password_label = Label(root, text="Passwort")
password_entry = Entry(root, show="*")


#Login- und Registrierungsfunktionen
def register():
    username = username_entry.get()
    if not username:
        messagebox.showerror("Error", "Bitte geben Sie einen Benutzernamen ein")
        return
    password = password_entry.get()
    if not password:
        messagebox.showerror("Error", "Bitte geben Sie ein Passwort ein")
    else:
        messagebox.showinfo("Registrierung", "Registrierung erfolgreich abgeschlossen")
        save_credentials()

def login():
    users = open_csv()
    username = username_entry.get()
    password = password_entry.get()

    # Entschlüsseln des Passworts
    hash_object = hashlib.sha256()
    password = password.encode()
    hash_object.update(password)
    hex_dig = hash_object.hexdigest()

    for user in users:
        if user["username"] == username and user["password"] == hex_dig:
            messagebox.showinfo("Login erfolgreich", "Sie haben sich erfolgreich eingeloggt")
            highscore1 = user["highscore1"]
            highscore2 = user["highscore2"]
            root.destroy()

            def start_game1():
                print("Game 1 wird gestartet.")
                game.destroy()
                import game1
                game1.start_game()

            def start_game2():
                print("Game 2 wird gestartet.")
                game.destroy()
                import game2
                game2.start_game()

            game = Tk()
            game.geometry("300x300")
            game.title("Spieleauswahl")

            spiel_label = Label(game, text="Spieleauswahl", font=("Arial Rounded", 18))

            user_label = Label(game, text="Angemeldet als: {}".format(username), font=("Arial Rounded", 10))
            highscore1_label = Label(game, text="Highscore Game1: {}".format(highscore1), font=("Arial Rounded", 10))
            highscore2_label = Label(game, text="Highscore Game2: {}".format(highscore2), font=("Arial Rounded", 10))

            # Button erstellen mit Bild
            image1 = PhotoImage(file="pong.png")
            image2 = PhotoImage(file="snake.png")
            Spielebtn = Frame(game)
            Spielebtn.columnconfigure(0, weight=1)
            Spielebtn.columnconfigure(1, weight=1)

            game1_button = Button(Spielebtn, image=image1, command=start_game1)
            game1_button.grid(row=0, column=0, sticky="news")

            game2_button = Button(Spielebtn, image=image2, command=start_game2)
            game2_button.grid(row=0, column=1, sticky="news", padx=10)

            user_label.pack(side="top", anchor="w")
            spiel_label.pack(padx=10, pady=10)
            Spielebtn.pack()
            highscore2_label.pack(side="bottom", anchor="s")
            highscore1_label.pack(side="bottom", anchor="s")


            game.mainloop()
            return
    messagebox.showerror("Login fehlgeschlagen", "Ungültiger Benutzername oder Passwort")
#Button und Button Grid erstellen
LogRegbtn = Frame(root)
LogRegbtn.columnconfigure(0, weight=1)
LogRegbtn.columnconfigure(1, weight=1)

register_button = Button(LogRegbtn, text="Registrieren", command=register, font=("arial", 9))
register_button.grid(row=0, column=0, sticky="news")
login_button = Button(LogRegbtn, text="Anmelden", command=login, font=("arial", 9))
login_button.grid(row=0, column=1, sticky="news")

#Implementieren der einzelnen Bausteine
LR_label.pack()
Button(root, text="Quit", command=root.destroy).pack(side= "right" and "bottom")
username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack(padx=10, pady=10)
LogRegbtn.pack()

root.mainloop()

