from tkinter import *
import tkinter as tk
final = ('veuiller remplir les champs')

def polybe(texte):

    #https://fr.wikipedia.org/wiki/Carr%C3%A9_de_Polybe#/media/Fichier:Carr%C3%A9_de_Polybe_avec_chiffres_et_symboles.png
    #carré utiliser pour simplifier l'histoire des i/j ou des nombre greque
    alphaber=('abcdefghijklmnopqrstuvwxyz0123456789 !"#$%&\'()*+,-./:;<=>?@[\]^_') # l'anti slache pour les guillemer 
    alphaber2=(list(alphaber.strip()))
    entre=[]
    result=[]
    espace=dict()
    for i in range (8):
        entre.append(alphaber2[i*8:8+i*8]) #séparer en groupe de 8 comme sur le tableau donné au dessus
    vattexte = (list(texte.strip())) #convevrtire en liste
    l=0
    for i in vattexte:
        if i not in alphaber2:
            espace[l]=i # et enregistré leur positoin pour plus tard
        l+=1
    l=0

    for i in espace.keys():
        del vattexte[i-l]#supprimer les valeur
        l+=1
    l=0
    for i in vattexte:
        for sous_liste in entre:
            if i in sous_liste:
                y = entre.index(sous_liste)#trouver la position de la liste contenant la lettre
                t = entre[y].index(i)#trouver la position de la lettre dans la liste de la liste ou elle se trouve
                result.append(str(t+1)+str(y+1))#les additioner comme des str
                break #stopper la boucle pour eviter des calcule plus inutile qui obligerais a diviser les resultat
    for i,t in espace.items(): #rajoute les espace précédement enlever
            result.insert(i, t)

    fin= "".join(result) # la convertire en str
    return(fin)


def polydechiffre(texte):
    alphaber=('abcdefghijklmnopqrstuvwxyz0123456789 !"#$%&\'()*+,-./:;<=>?@[\]^_') # l'anti slache pour les guillemer 
    alphaber2=(list(alphaber.strip()))
    entre=[]
    result=[]
    espace=dict()
    for i in range (8):
        entre.append(alphaber2[i*8:8+i*8]) #séparer en groupe de 8 comme sur le tableau donné au dessus
    vattexte = (list(texte.strip())) #convevrtire en liste
    l=0
    for i in vattexte:
        if i not in alphaber2:
            espace[l]=i # et enregistré leur positoin pour plus tard

        l+=1
    l=0

    for i in espace.keys():
        del vattexte[i-l]#supprimer les valeur
        l+=1
    l=0
    fin= "".join(vattexte) # la convertire en str
    liste = [fin[i:i+2] for i in range(0, len(fin), 2)]#séparer tout les 2 éléments

    for i in liste:
        p1=str(i[:1])
        p2=str(i[1:])
        result.append(entre[int(p2)-1][int(p1)-1])

    for i,t in espace.items(): #rajoute les espace précédement enlever
            result.insert(int((i+l)/2), t)

            l+=1

    fin= "".join(result) # la convertire en str
    return (fin)

def cesar(texte): #pour le chiffrement cesar j'utilise une methode différente que pour le rot13 car ce n'est qu'une chiffrement en rot3
    alphaber=('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    alphaber2=(list(alphaber.strip()))
    lalphaber2 = len(alphaber2)
    entre=[]
    espace=dict()
    list_texte=(list(texte.strip()))
    l=0
    for i in list_texte:
        if i not in alphaber2:
            espace[l]=i # et enregistré leur positoin pour plus tard
        l+=1
    l=0
    for i in espace.keys():
        del list_texte[i-l]#supprimer les valeur
        l+=1
    l=0
    for i in list_texte:
        t = alphaber.index(i)
        t +=3 # on ajout 3 a la position de maniers a faire un chiffrement cesar
        if t >= lalphaber2: # on n'a 52 element dans notre alpahber donc avec le +3 si c'est au dessus il ne trouvera pas donc on verifi et on soustrait pour faire le tour le la variable
            t-= lalphaber2
        entre.append(alphaber[t])

    for i,t in espace.items(): #rajoute les espace précédement enlever
        entre.insert(i, t)
    resulte= "".join(entre) # la convertire en str
    return(resulte)


def cesardechiffre(texte): #pour le chiffrement cesar j'utilise une methode différente que pour le rot13 car ce n'est qu'une chiffrement en rot3
    alphaber=('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    alphaber2=(list(alphaber.strip()))
    lalphaber2 = len(alphaber2)
    entre=[]
    espace=dict()
    list_texte=(list(texte.strip()))
    print(len(alphaber2))
    l=0
    for i in list_texte:
        if i not in alphaber2:
            espace[l]=i # et enregistré leur positoin pour plus tard
        l+=1
    l=0
    for i in espace.keys():
        del list_texte[i-l]#supprimer les valeur
        l+=1
    l=0
    for i in list_texte:
        t = alphaber.index(i)
        t -=3 # on enleve 3 a la position de maniers a trouver la position originel
        if t < 0: # on n'a 52 element dans notre alpahber donc avec le -3 si c'est au dessus il ne trouvera pas donc on verifi et on soustrait pour faire le tour le la variable
            t+= lalphaber2
        entre.append(alphaber[t])
    for i,t in espace.items(): #rajoute les espace précédement enlever
        entre.insert(i, t)
    resulte= "".join(entre) # la convertire en str
    return(resulte)


def rot13(texte): # si on passe un message déchifré il nous renvoie du rot13 et inversement si on lui donne du rot13 il nous renvoie le message déchifrer se qui resemble plus a de la substitution
    alphaber=('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    alphaber2=(list(alphaber.strip()))
    alphaber13 =('NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')
    entre=[]
    espace= dict()
    list_texte=(list(texte.strip())) #transformer en liste
    l=0
    for i in list_texte:
        if i not in alphaber2:
            espace[l]=i # et enregistré leur positoin pour plus tard
        l+=1
    l=0
    for i in espace.keys():
        del list_texte[i-l]#supprimer les valeur
        l+=1
    l=0
    print(espace)


    for i in list_texte:
        t = alphaber.index(i) #trouver la position de i dans alpahber
        entre.append(alphaber13[t]) # et mettre le nombre corerspondant a la position dans la variable entre

    for i,t in espace.items(): #rajoute les espace précédement enlever
        entre.insert(i, t)


    
    resulte= "".join(entre) # la convertire en str
    return(resulte)


def vingénére(texte,cle):
    alphaber=('abcdefghijklmnopqrstuvwxyz')
    alphaber2=(list(alphaber.strip()))
    valcle=[] #valeur cle
    valtexte=[]  # valeur texte
    list_cle=(list(cle.strip()))
    list_texte=(list(texte.strip()))
    espace = dict()
    entre=[]
    fin=[]
    l=0

    for i in list_texte:
        if i not in alphaber2:
            espace[l]=i # et enregistré leur positoin pour plus tard
        l+=1
    l=0

    for i in espace.keys():
        del list_texte[i-l]#supprimer les valeur
        l+=1
    l=0
    for i in list_cle:
        valcle.append(alphaber.index(i))#recupérer les valeur dans alphaber

    for i in list_texte:
        valtexte.append(alphaber.index(i))#recupérer les valeur dans alphaber
    y=len(valcle)
    s=(int(len(valtexte)/y+1))

    for i in range (s):
        entre.append(valtexte[i*y:y+i*y]) #séparer chaque éléments par groupe du nombre qui il a dlélements dans la clé

    for i in range(y):
        for k in range(y):
            try: #test si les valeur exicte d'ajouter la valeur avec sont homonime de la cle 
                t = entre[i][k]+valcle[k]
            except:
                continue
            #print(entre[i][k],"+",valcle[k],"=",t)
            if t >= 26: #dans l'a)haber il y a 26 lettre donc on les soustré pour faire le tour de la variable
                t-=26
            fin.append(alphaber[t])


    for i,t in espace.items(): #rajoute les espace précédement enlever
        fin.insert(i, t)

    resulte= "".join(fin)
    return(resulte)



def vingénéredéchiffre(texte,cle):
    alphaber=('abcdefghijklmnopqrstuvwxyz')
    alphaber2=(list(alphaber.strip()))
    valcle=[] #valeur cle
    valtexte=[]  # valeur texte
    list_cle=(list(cle.strip()))
    list_texte=(list(texte.strip()))
    espace = dict()
    entre=[]
    fin=[]
    l=0

    for i in list_texte:
        if i not in alphaber2:
            espace[l]=i # et enregistré leur positoin pour plus tard
        l+=1
    l=0

    for i in espace.keys():
        del list_texte[i-l]#supprimer les valeur
        l+=1
    l=0
    for i in list_cle:
        valcle.append(alphaber.index(i))#recupérer les valeur dans alphaber

    for i in list_texte:
        valtexte.append(alphaber.index(i))#recupérer les valeur dans alphaber
    y=len(valcle)
    s=(int(len(valtexte)/y+1))

    for i in range (s):
        entre.append(valtexte[i*y:y+i*y]) #séparer chaque éléments par groupe du nombre qui il a dlélements dans la clé

    for i in range(y):
        for k in range(y):
            try: #test si les valeur exicte d'ajouter la valeur avec sont homonime de la cle 
                t = entre[i][k]-valcle[k]
            except:
                continue
            #print(entre[i][k],"+",valcle[k],"=",t)
            if t < 0: #dans l'a)haber il y a 26 lettre donc on les soustré pour faire le tour de la variable
                t+=26
            fin.append(alphaber[t])

    print(espace)
    for i,t in espace.items(): #rajoute les espace précédement enlever
        fin.insert(i, t)

    resulte= "".join(fin)
    return(resulte)


def afficher(): 
    p = 0 
    t = value.get() #recupere les valeur pour savoir quelles sont les choix de l'utilisateur
    h = value2.get()
    message=entry.get()
    cle=entry2.get()
    if t == '' or h == '' or message == '':
        final.set('veuiller remplir les champs')
    if t == "1":
        if h == "1":
            final.set(polybe(message))
        elif h == "2":
            if cle =='':
                final.set("remplir la case")
            final.set(vingénére(message,cle))
        elif h == "3":
            p = rot13(message)
            final.set(str(p))
        elif h == "4":
            final.set(cesar(message))
        else:
            final.set("donner un nombre correcte")
    if t == "2":
        if h == "1":
            final.set(polydechiffre(message))
        elif h == "2":
            if cle == '':
                final.Set("remplire le champs")
            final.set(vingénéredéchiffre(message,cle))
        elif h == "3":
            final.set(rot13(message))
        elif h == "4":
            final.set(cesardechiffre(message))
        else:
            final.set("donner un nombre correcte")
        


 
fenetre = tk.Tk() # crée une fenêtre avec tkinter pour faciliter l'interaction, le designe n'est pas ouf mais sa fait l'affaire
entry = tk.Entry(fenetre)
entry2 = tk.Entry(fenetre)

label = tk.Label(fenetre, text="notre programe utilise des dictionnaire spécifique pour certain algo vous pouvez les modifier depuis le code source ou ils sont mis en évidence")
label.pack()
value = tk.StringVar() 
bouton1 = tk.Radiobutton(fenetre, text="chiffré", variable=value, value=1)
bouton2 = tk.Radiobutton(fenetre, text="déchiffré", variable=value, value=2)
bouton1.pack(side=LEFT)
bouton2.pack(side=LEFT)
value2=tk.StringVar()
choix1 = tk.Radiobutton(fenetre, text="polybe", variable=value2, value=1, command=afficher)
choix2 = tk.Radiobutton(fenetre, text="vingénére", variable=value2, value=2, command=afficher)
choix3 = tk.Radiobutton(fenetre, text="rot13", variable=value2, value=3, command=afficher)
choix4 = tk.Radiobutton(fenetre, text="cesare", variable=value2, value=4, command=afficher)
choix1.pack()
choix2.pack()
choix3.pack()
choix4.pack()

entry.pack() 
label = tk.Label(fenetre, text="cle pour vingénére")
label.pack()
entry2.pack()
bouton=tk.Button(fenetre, text="calculer", command=afficher)
bouton.pack()
final=tk.StringVar()
afficher()
final.set("veuiller remplir les champs")

entree = tk.Entry(fenetre, textvariable=final, width=30)
entree.pack()

fenetre.mainloop()


