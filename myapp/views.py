from django.shortcuts import render

# Create your views here.
import tkinter as tk
import re

def verification2(liste):
    p = []
    index1 = []
    index2 = []

    # Supprimer les caractères indésirables
    liste = re.sub(r"[^()]", "", liste)

    if not liste or liste[0] == ")":
        return False

    for i in range(len(liste)):
        if liste[i] == "(":
            p.append(liste[i])
            index1.append(i)
        else:
            if p:
                p.pop()
                index2.append(index1.pop())
                index2.append(i)
            else:
                return False

    if len(p) == 0:
        n = 0
        result = ""
        for i in range(len(index2) // 2):
            result += f"La parenthèse ouvrante à l'indice {index2[n]} correspond à la parenthèse ouvrante de l'indice {index2[n + 1]}\n"
            n += 2
        return result
    else:
        return False

def verifier_parentheses():
    resultat.delete(1.0, tk.END)  # Efface le texte précédent
    chaine = entree.get()
    resultat_text = verification2(chaine)
    if resultat_text:
        resultat.insert(tk.END, "La chaîne est bien parenthésée.\n", "vert")
        resultat.insert(tk.END, resultat_text, "vert")
    else:
        resultat.insert(tk.END, "La chaîne n'est pas bien parenthésée.", "rouge")

fenetre = tk.Tk()
fenetre.title("Vérification de Parenthèses")

entree_label = tk.Label(fenetre, text="Entrez la chaîne de caractères :", font=("Helvetica", 14))
entree_label.pack(pady=5)

entree = tk.Entry(fenetre, font=("Helvetica", 12))
entree.pack(pady=10, padx=10, ipadx=5, ipady=5, fill=tk.X)

bouton = tk.Button(fenetre, text="Vérifier", command=verifier_parentheses, font=("Helvetica", 12))
bouton.pack(pady=10)

resultat = tk.Text(fenetre, height=6, width=40, font=("Helvetica", 12))
resultat.tag_config("vert", foreground="green")
resultat.tag_config("rouge", foreground="red")
resultat.pack(pady=10)

fenetre.geometry("400x400")  # Définir la taille de la fenêtre

fenetre.mainloop()


from django.shortcuts import render
from django.http import HttpResponse

def verifier_parentheses2(request):
    resultat_text = ""
    if request.method == 'POST':
        chaine = request.POST.get('chaine')
        resultat_text = verification2(chaine)
    return render(request, 'index.html', {'resultat_text': resultat_text})

def home(request):
    return render(request, 'index.html')