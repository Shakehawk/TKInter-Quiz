
import random
from tkinter import *


window = Tk()
window.title("Quiz")
window.geometry("600x450")

questions = [
    # =========================
    # SCHWER (1–30)
    # =========================
    ["Wie viele Bits hat ein IPv6-Adresse?", "64", "128", "256", "32"],
    ["Wer entwickelte die Relativitätstheorie?", "Isaac Newton", "Nikola Tesla", "Albert Einstein", "Galileo Galilei"],
    ["Was beschreibt die Heisenbergsche Unschärferelation?", "Gravitation", "Quantenmechanik", "Thermodynamik", "Relativität"],
    ["Welche Programmiersprache ist funktional?", "Java", "Python", "Haskell", "C"],
    ["Was ist die chemische Formel von Ozon?", "O2", "CO2", "O3", "H2O"],
    ["Welches Land hatte nie eine Kolonie?", "Deutschland", "Japan", "Thailand", "Spanien"],
    ["Was ist der größte Mond im Sonnensystem?", "Titan", "Europa", "Ganymed", "Io"],
    ["Was bedeutet HTTP Statuscode 418?", "Serverfehler", "Nicht gefunden", "I'm a teapot", "Zeitüberschreitung"],
    ["Welches Element hat die Ordnungszahl 79?", "Silber", "Gold", "Platin", "Quecksilber"],
    ["Welche Datenstruktur arbeitet nach LIFO?", "Queue", "Stack", "Tree", "Graph"],
    ["Was ist die Zeitkomplexität von Binary Search?", "O(n)", "O(n²)", "O(log n)", "O(1)"],
    ["Wer schrieb 'Also sprach Zarathustra'?", "Goethe", "Nietzsche", "Kafka", "Schopenhauer"],
    ["Was ist kein SQL-Befehl?", "SELECT", "INSERT", "UPDATE", "FETCHALL"],
    ["Welches Land hat die längste Küstenlinie?", "Australien", "USA", "Kanada", "Russland"],
    ["Was ist die Einheit von elektrischer Spannung?", "Ampere", "Watt", "Volt", "Ohm"],
    ["Was ist ein Boolean?", "Zahl", "Text", "Wahrheitswert", "Liste"],
    ["Welches Planetensystem ist am nächsten zur Erde?", "Alpha Centauri", "Proxima Centauri", "TRAPPIST-1", "Sirius"],
    ["Was bedeutet DNS?", "Data Network System", "Domain Name System", "Digital Network Server", "Dynamic Name Service"],
    ["Welche Sprache wird für Android-Apps bevorzugt?", "Swift", "Kotlin", "C#", "Ruby"],
    ["Was ist kein Betriebssystem?", "Linux", "Windows", "Python", "macOS"],
    ["Was ist der pH-Wert von reinem Wasser?", "5", "6", "7", "8"],
    ["Welcher Ozean ist der größte?", "Atlantik", "Indischer Ozean", "Pazifik", "Arktischer Ozean"],
    ["Was ist die Hauptaufgabe der CPU?", "Speichern", "Rechnen", "Darstellen", "Kühlen"],
    ["Welche Einheit misst Frequenz?", "Volt", "Hertz", "Joule", "Ohm"],
    ["Was ist ein Algorithmus?", "Hardware", "Programm", "Schrittfolge", "Variable"],
    ["Welche Farbe hat Chlor?", "Rot", "Gelbgrün", "Blau", "Farblos"],
    ["Was ist kein Cloud-Dienst?", "AWS", "Azure", "Google Drive", "Windows XP"],
    ["Welche Zahl ist binär korrekt?", "102", "111", "89", "128"],
    ["Was bedeutet API?", "Application Programming Interface", "Advanced Program Index", "Automatic Process Input", "Applied Protocol Interface"],
    ["Welches Protokoll ist verschlüsselt?", "HTTP", "FTP", "HTTPS", "SMTP"],

    # =========================
    # MITTEL (31–70)
    # =========================
    ["Was ist die Hauptstadt von Kanada?", "Toronto", "Vancouver", "Ottawa", "Montreal"],
    ["Wie viele Kontinente gibt es?", "5", "6", "7", "8"],
    ["Welche Sprache spricht man in Brasilien?", "Spanisch", "Englisch", "Portugiesisch", "Französisch"],
    ["Welches Tier ist das größte an Land?", "Nashorn", "Elefant", "Giraffe", "Nilpferd"],
    ["Was ist 9 × 8?", "64", "72", "81", "69"],
    ["Welche Farbe entsteht aus Blau und Gelb?", "Grün", "Orange", "Lila", "Braun"],
    ["Wie viele Sekunden hat eine Minute?", "30", "45", "60", "90"],
    ["Was ist der vierte Planet?", "Erde", "Mars", "Jupiter", "Venus"],
    ["Welches Metall ist flüssig?", "Eisen", "Gold", "Quecksilber", "Kupfer"],
    ["Wie viele Tage hat ein Schaltjahr?", "364", "365", "366", "367"],
    ["Welche Einheit misst Strom?", "Volt", "Watt", "Ampere", "Ohm"],
    ["Was ist HTML?", "Programmiersprache", "Auszeichnungssprache", "Datenbank", "Betriebssystem"],
    ["Welche Stadt ist die Hauptstadt von Italien?", "Mailand", "Rom", "Neapel", "Turin"],
    ["Was ist die Wurzel aus 81?", "7", "8", "9", "10"],
    ["Welche Jahreszeit folgt auf den Sommer?", "Frühling", "Herbst", "Winter", "Sommer"],
    ["Welches Gas atmen wir ein?", "CO2", "Sauerstoff", "Stickstoff", "Helium"],
    ["Wie viele Spieler hat ein Fußballteam?", "9", "10", "11", "12"],
    ["Welche Farbe hat eine Banane?", "Grün", "Gelb", "Rot", "Blau"],
    ["Was ist größer?", "MB", "GB", "KB", "Byte"],
    ["Wie viele Monate hat ein Jahr?", "10", "11", "12", "13"],
    ["Welche Zahl ist gerade?", "3", "5", "8", "9"],
    ["Was ist Eis?", "Gas", "Flüssigkeit", "Feststoff", "Plasma"],
    ["Wie viele Stunden hat ein Tag?", "12", "18", "24", "36"],
    ["Welche Sprache wird in Spanien gesprochen?", "Italienisch", "Portugiesisch", "Spanisch", "Französisch"],
    ["Welche Farbe hat der Himmel?", "Grün", "Blau", "Rot", "Schwarz"],
    ["Was ist ein Dreieck?", "Viereck", "Fünfeck", "Dreieck", "Kreis"],
    ["Wie viele Beine hat ein Hund?", "2", "3", "4", "5"],
    ["Was ist 100 / 10?", "5", "10", "20", "50"],
    ["Welches Tier sagt 'Miau'?", "Hund", "Kuh", "Katze", "Schaf"],
    ["Welche Farbe hat Schnee?", "Schwarz", "Weiß", "Grau", "Blau"],

    # =========================
    # LEICHT (71–100)
    # =========================
    ["Was ist die Hauptstadt von Frankreich?", "Berlin", "Rom", "Paris", "Madrid"],
    ["2 + 2 = ?", "3", "4", "5", "6"],
    ["Welche Farbe hat Gras?", "Blau", "Gelb", "Grün", "Rot"],
    ["Wie viele Augen hat ein Mensch?", "1", "2", "3", "4"],
    ["Was trinkt eine Kuh?", "Milch", "Wasser", "Saft", "Cola"],
    ["Welche Form hat ein Ball?", "Eckig", "Rund", "Dreieckig", "Flach"],
    ["Was scheint am Tag?", "Mond", "Sterne", "Sonne", "Lampe"],
    ["Welche Zahl kommt nach 9?", "8", "9", "10", "11"],
    ["Welche Farbe hat Blut?", "Blau", "Grün", "Rot", "Gelb"],
    ["Was ist Feuer?", "Kalt", "Warm", "Heiß", "Nass"],
    ["Wie viele Finger hat eine Hand?", "3", "4", "5", "6"],
    ["Was sagt der Hund?", "Miau", "Muh", "Wuff", "Mäh"],
    ["Welche Farbe hat eine Erdbeere?", "Blau", "Gelb", "Rot", "Grün"],
    ["Was benutzt man zum Schreiben?", "Löffel", "Stift", "Schuh", "Teller"],
    ["Was ist größer?", "Maus", "Elefant", "Ameise", "Fliege"],
    ["Welche Jahreszeit ist kalt?", "Sommer", "Frühling", "Winter", "Herbst"],
    ["Was fährt auf Schienen?", "Auto", "Fahrrad", "Zug", "Boot"],
    ["Was ist Zucker?", "Salzig", "Bitter", "Süß", "Sauer"],
    ["Welche Farbe hat die Sonne?", "Blau", "Gelb", "Grün", "Schwarz"],
    ["Wie viele Räder hat ein Fahrrad?", "1", "2", "3", "4"]
]

def clear(): 
    List = window.grid_slaves()
    for n in List:
        n.destroy()


class Quiz:
    def __init__(self, questions):
        clear()
        self.Fragen = []
        for n in questions:
            self.Fragen.append(n)
        self.a1=""
        self.a2=""
        self.a3=""
        self.a4=""
        self.Ra=""
        self.richtigButton = Button(window, text="",font=("Arial", 14))
        self.antwort1 = Button(window, text="",font=("Arial", 14))
        self.antwort2 = Button(window, text="",font=("Arial", 14))
        self.antwort3 = Button(window, text="",font=("Arial", 14))
        self.antwort4 = Button(window, text="",font=("Arial", 14))
        self.lock=False
        self.right=0
        self.naechste=Button(window,text="nächste",font=("Arial",14),command=self.Frage)
        self.nummer=0
        self.Max=3
        self.Frage()
    
    def Frage(self):
        self.naechste.grid(column=0,row=5,pady=5)
        if len(self.Fragen) > 0 and self.nummer < self.Max:
            self.nummer += 1
            self.lock=False
            randomNum = random.randint(0,len(self.Fragen)-1)
            fragenText = self.Fragen[randomNum][0]
            self.Ra = self.Fragen[randomNum][2]
            antworten = []
            for i in range(1,5):
                antworten.append(self.Fragen[randomNum][i])
            random.shuffle(antworten)

            self.a1 = antworten[0]
            self.a2 = antworten[1]
            self.a3 = antworten[2]
            self.a4 = antworten[3]

            frage = Text(window,font=("Arial",14), width=40, height=2)
            frage.insert(END,fragenText)
            frage.grid(column=0,row=0,padx=80,pady=(75,0))

            self.antwort1 = Button(window, text=self.a1, font=("Arial",14),width=39, command=self.control1)
            self.antwort2 = Button(window, text=self.a2, font=("Arial",14),width=39, command=self.control2)
            self.antwort3 = Button(window, text=self.a3, font=("Arial",14),width=39, command=self.control3)
            self.antwort4 = Button(window, text=self.a4, font=("Arial",14),width=39, command=self.control4)

            self.antwort1.grid(column=0,row=1,pady=(8,5))
            self.antwort2.grid(column=0,row=2,pady=5)
            self.antwort3.grid(column=0,row=3,pady=5)
            self.antwort4.grid(column=0,row=4,pady=5)

            if self.a1 == self.Ra:
                self.richtigButton = self.antwort1
            elif self.a2 == self.Ra:
                self.richtigButton = self.antwort2
            elif self.a3 == self.Ra:
                self.richtigButton = self.antwort3
            elif self.a4 == self.Ra:
                self.richtigButton = self.antwort4
            self.Fragen.pop(randomNum)
        else:
            clear()
            lb=Label(window,text="Du hast " + str(self.right) + " von " + str(self.Max) + " Fragen richtig beantwortet!", font=("Arial",14))
            lb.grid(column=0,row=0,padx=120,pady=(170,15))
            zumMenu = Button(window, text="Menu", font=("Arial",14), command=menuCreator)
            zumMenu.grid(column=0,row=1)

    def control1(self):
        if self.lock==False:
            if self.Ra != self.a1:
                self.antwort1.configure(bg="red")
            else:
                self.antwort1.configure(bg="green")
                self.right += 1
            self.richtigButton.configure(bg="green")
            self.lock = True

    def control2(self):
        if self.lock==False:
            if self.Ra != self.a2:
                self.antwort2.configure(bg="red")
            else:
                self.antwort2.configure(bg="green")
                self.right += 1
            self.richtigButton.configure(bg="green")
            self.lock = True

    def control3(self):
        if self.lock==False:
            if self.Ra != self.a3:
                self.antwort3.configure(bg="red")
            else:
                self.antwort3.configure(bg="green")
                self.right += 1
            self.richtigButton.configure(bg="green")
            self.lock = True

    def control4(self):
        if self.lock==False:
            if self.Ra != self.a4:
                self.antwort4.configure(bg="red")
            else:
                self.antwort4.configure(bg="green")
                self.right += 1
            self.richtigButton.configure(bg="green")
            self.lock = True


class Menu:
    def __init__(self):
        clear()
        self.Quiz = Button(window, text="Quiz", font=("Arial", 14), command=quizCreator, width=15, height=3)
        self.Quiz.grid(column=0,row=0,padx=218,pady=170)


def menuCreator():
    m = Menu()

def quizCreator():
    q = Quiz(questions)

menuCreator()
window.mainloop()