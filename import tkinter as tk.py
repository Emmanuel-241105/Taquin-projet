import tkinter as tk
from tkinter import messagebox
from random import shuffle, randint

# ---------- LOGIQUE JEU ----------
def cartes_deck():
    couleurs = ['carreau', 'coeur', 'pique', 'trefle']
    valeurs = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'valet', 'dame', 'roi']
    deck = [v + ' de ' + c for c in couleurs for v in valeurs]
    shuffle(deck)
    return deck

def score(main):
    total = 0
    aces = 0
    for carte in main:
        val = carte.split(' ')[0]
        if val in ['valet', 'dame', 'roi']:
            total += 10
        elif val == 'as':
            aces += 1
            total += 11
        else:
            total += int(val)
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

def distrib_cartes(deck, nb_cartes):
    return [deck.pop() for _ in range(nb_cartes)]

def abandon():
    messagebox.showinfo("Abandon", "Vous avez abandonné la partie.")
    reset_jeu()

# ---------- INTERFACE ----------
class BlackjackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack")
        self.root.geometry("800x600")
        self.root.configure(bg="#006400")  # Vert foncé

        self.deck = []
        self.main_j = []
        self.main_c = []

        self.page_accueil()

    def page_accueil(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        titre = tk.Label(self.root, text="Blackjack", font=("Helvetica", 48, "bold"), bg="#006400", fg="white")
        titre.pack(pady=100)

        jouer_btn = tk.Button(self.root, text="Jouer", font=("Helvetica", 24), bg="gold", fg="black",
                              command=self.page_jeu, width=15, height=2)
        jouer_btn.pack(pady=20)

    def page_jeu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.deck = cartes_deck()
        self.main_j = distrib_cartes(self.deck, 2)
        self.main_c = distrib_cartes(self.deck, 2)

        # Affichage joueur et croupier
        self.label_joueur = tk.Label(self.root, text="", font=("Helvetica", 16), bg="#006400", fg="white")
        self.label_joueur.pack(pady=10)

        self.label_croupier = tk.Label(self.root, text="", font=("Helvetica", 16), bg="#006400", fg="white")
        self.label_croupier.pack(pady=10)

        # Boutons de jeu
        btn_frame = tk.Frame(self.root, bg="#006400")
        btn_frame.pack(pady=30)

        tk.Button(btn_frame, text="Hit", command=self.hit, font=("Helvetica", 16), bg="white", width=10).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Stand", command=self.stand, font=("Helvetica", 16), bg="white", width=10).grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="Abandon", command=abandon, font=("Helvetica", 16), bg="white", width=10).grid(row=0, column=2, padx=10)
        tk.Button(btn_frame, text="Accueil", command=self.page_accueil, font=("Helvetica", 16), bg="gray", width=10).grid(row=0, column=3, padx=10)

        self.update_affichage()

    def update_affichage(self):
        self.label_joueur.config(text=f"Main Joueur: {self.main_j} (Score: {score(self.main_j)})")
        self.label_croupier.config(text=f"Main Croupier: {self.main_c[0]}, ??")

    def hit(self):
        self.main_j.append(self.deck.pop())
        self.update_affichage()
        if score(self.main_j) > 21:
            messagebox.showinfo("Défaite", "Vous avez dépassé 21, vous avez perdu.")
            reset_jeu()

    def stand(self):
        while score(self.main_c) < 17:
            self.main_c.append(self.deck.pop())

        joueur = score(self.main_j)
        croupier = score(self.main_c)
        resultat = ""

        if croupier > 21 or joueur > croupier:
            resultat = "Vous avez gagné !"
        elif joueur < croupier:
            resultat = "Vous avez perdu..."
        else:
            resultat = "Égalité !"

        messagebox.showinfo("Résultat", f"{resultat}\nVotre main: {self.main_j} ({joueur})\nMain croupier: {self.main_c} ({croupier})")
        reset_jeu()

def reset_jeu():
    root.destroy()
    root_new = tk.Tk()
    app = BlackjackApp(root_new)
    root_new.mainloop()

# Lancer l'app
root = tk.Tk()
app = BlackjackApp(root)
root.mainloop()