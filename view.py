from flask import Flask,render_template,request
import datetime



app = Flask(__name__)
liste=[]
@app.route("/")
def index():
    del liste[:]
    return render_template("principal.html")

@app.route("/regle.html",methods=["POST"])
def index1():

    return render_template("regle.html")


@app.route("/index.html",methods=["POST"])
def index1_2():

    return render_template("index.html")


@app.route("/resultat.html",methods=["POST"])
def index2():
    result=request.form
    choix = result["choix"]
    liste.append(choix)
    print(liste)
    return render_template("resultat.html",melo_principal=choix)

@app.route("/resultat2.html",methods=["POST"])
def index3():
    result=request.form
    choix2 = result["choix2"]
    liste.append(choix2)
    print(liste)
    return render_template("resultat2.html",melo_secondaire=choix2)

@app.route("/resultat3.html",methods=["POST"])
def index4():
    result=request.form
    choix3 = result["choix3"] 
    liste.append(choix3)
    print(liste)
    return render_template("resultat3.html",ambiance=choix3)


@app.route("/instruments.html",methods=["POST"])
def index5():

    return render_template("instruments.html")

@app.route("/contact.html",methods=["POST"])
def index6():

    return render_template("contact.html")


@app.route("/resultat4.html",methods=["POST"])
def index7():
    result=request.form
    choix4 = result["choix4"]
    liste.append(choix4)
    print(liste)
    #CHOIX DU SON
    #DRUM AFRO
    if liste==["G-P","G.E-MB","S.VIOLON","DRUMS.A"]:
        choix5 = "static/musiques/1.mp3"
    
    if liste==["G-P","G.E-MB","VIOLON","DRUMS.A"]:
        choix5 = "static/musiques/2.mp3"
    
    if liste==["G-P","G.E-MB","VIOLON.R","DRUMS.A"]:
        choix5 = "static/musiques/3.mp3"
    
    if liste==["G-P","G.E","S.VIOLON","DRUMS.A"]:
        choix5 = "static/musiques/4.mp3"
    
    if liste==["G-P","G.E","VIOLON","DRUMS.A"]:
        choix5 = "static/musiques/5.mp3"
    
    if liste==["G-P","G.E","VIOLON.R","DRUMS.A"]:
        choix5 = "static/musiques/6.mp3"
    
    if liste==["G-P","MB","S.VIOLON","DRUMS.A"]:
        choix5 = "static/musiques/7.mp3"
    
    if liste==["G-P","MB","VIOLON","DRUMS.A"]:
        choix5 = "static/musiques/8.mp3"

    if liste==["G-P","MB","VIOLON.R","DRUMS.A"]:
        choix5 = "static/musiques/9.mp3"
    
    if liste==["PIANO","G.E-MB","S.VIOLON","DRUMS.A"]:
        choix5 = "static/musiques/10.mp3"
    
    if liste==["PIANO","G.E-MB","VIOLON","DRUMS.A"]:
        choix5 = "static/musiques/11.mp3"
    
    if liste==["PIANO","G.E-MB","VIOLON.R","DRUMS.A"]:
        choix5 = "static/musiques/12.mp3"
    
    if liste==["PIANO","G.E","S.VIOLON","DRUMS.A"]:
        choix5 = "static/musiques/13.mp3"
    
    if liste==["PIANO","G.E","VIOLON","DRUMS.A"]:
        choix5 = "static/musiques/14.mp3"
    
    if liste==["PIANO","G.E","VIOLON.R","DRUMS.A"]:
        choix5 = "static/musiques/15.mp3"
    
    if liste==["PIANO","MB","S.VIOLON","DRUMS.A"]:
        choix5 = "static/musiques/16.mp3"
    
    if liste==["PIANO","MB","VIOLON","DRUMS.A"]:
        choix5 = "static/musiques/17.mp3"
    
    if liste==["PIANO","MB","VIOLON.R","DRUMS.A"]:
        choix5 = "static/musiques/18.mp3"
    
    if liste==["GUITARE","MB","VIOLON.R","DRUMS.A"]:
        choix5 = "static/musiques/61.mp3"
    
    if liste==["GUITARE","MB","S.VIOLON","DRUMS.A"]:
        choix5 = "static/musiques/55.mp3"
    
    if liste==["GUITARE","MB","VIOLON","DRUMS.A"]:
        choix5 = "static/musiques/58.mp3"

    if liste==["GUITARE","G.E-MB","VIOLON.R","DRUMS.A"]:
        choix5 = "static/musiques/61.mp3"
    
    if liste==["GUITARE","G.E-MB","S.VIOLON","DRUMS.A"]:
        choix5 = "static/musiques/55.mp3"
    
    if liste==["GUITARE","G.E-MB","VIOLON","DRUMS.A"]:
        choix5 = "static/musiques/58.mp3"

    if liste==["G-P","G.E-MB","S.VIOLON","DRUMS.T"]:
        choix5 = "static/musiques/19.mp3"
    
    if liste==["G-P","G.E-MB","VIOLON","DRUMS.T"]:
        choix5 = "static/musiques/20.mp3"
    
    if liste==["G-P","G.E-MB","VIOLON.R","DRUMS.T"]:
        choix5 = "static/musiques/21.mp3"
    
    if liste==["G-P","G.E","S.VIOLON","DRUMS.T"]:
        choix5 = "static/musiques/22.mp3"
    
    if liste==["G-P","G.E","VIOLON","DRUMS.T"]:
        choix5 = "static/musiques/23.mp3"
    
    if liste==["G-P","G.E","VIOLON.R","DRUMS.T"]:
        choix5 = "static/musiques/24.mp3"
    
    if liste==["G-P","MB","S.VIOLON","DRUMS.T"]:
        choix5 = "static/musiques/25.mp3"
    
    if liste==["G-P","MB","VIOLON","DRUMS.T"]:
        choix5 = "static/musiques/26.mp3"
    
    if liste==["G-P","MB","VIOLON.R","DRUMS.T"]:
        choix5 = "static/musiques/27.mp3"
    
    if liste==["PIANO","G.E-MB","S.VIOLON","DRUMS.T"]:
        choix5 = "static/musiques/28.mp3"
    
    if liste==["PIANO","G.E-MB","VIOLON","DRUMS.T"]:
        choix5 = "static/musiques/29.mp3"
    
    if liste==["PIANO","G.E-MB","VIOLON.R","DRUMS.T"]:
        choix5 = "static/musiques/30.mp3"
    
    if liste==["PIANO","G.E","S.VIOLON","DRUMS.T"]:
        choix5 = "static/musiques/31.mp3"
    
    if liste==["PIANO","G.E","VIOLON","DRUMS.T"]:
        choix5 = "static/musiques/32.mp3"
    
    if liste==["PIANO","G.E","VIOLON.R","DRUMS.T"]:
        choix5 = "static/musiques/33.mp3"
    
    if liste==["PIANO","MB","S.VIOLON","DRUMS.T"]:
        choix5 = "static/musiques/34.mp3"
    
    if liste==["PIANO","MB","VIOLON","DRUMS.T"]:
        choix5 = "static/musiques/35.mp3"
    
    if liste==["PIANO","MB","VIOLON.R","DRUMS.T"]:
        choix5 = "static/musiques/36.mp3"

    if liste==["GUITARE","MB","VIOLON.R","DRUMS.T"]:
        choix5 = "static/musiques/62.mp3"
    
    if liste==["GUITARE","MB","S.VIOLON","DRUMS.T"]:
        choix5 = "static/musiques/57.mp3"
    
    if liste==["GUITARE","MB","VIOLON","DRUMS.T"]:
        choix5 = "static/musiques/59.mp3"

    if liste==["GUITARE","G.E-MB","VIOLON.R","DRUMS.T"]:
        choix5 = "static/musiques/62.mp3"
    
    if liste==["GUITARE","G.E-MB","S.VIOLON","DRUMS.T"]:
        choix5 = "static/musiques/57.mp3"
    
    if liste==["GUITARE","G.E-MB","VIOLON","DRUMS.T"]:
        choix5 = "static/musiques/59.mp3"

    if liste==["G-P","G.E-MB","S.VIOLON","S.DRUMS"]:
        choix5 = "static/musiques/37.mp3"
    
    if liste==["G-P","G.E-MB","VIOLON","S.DRUMS"]:
        choix5 = "static/musiques/38.mp3"
    
    if liste==["G-P","G.E-MB","VIOLON.R","S.DRUMS"]:
        choix5 = "static/musiques/39.mp3"
    
    if liste==["G-P","G.E","S.VIOLON","S.DRUMS"]:
        choix5 = "static/musiques/40.mp3"
    
    if liste==["G-P","G.E","VIOLON","S.DRUMS"]:
        choix5 = "static/musiques/41.mp3"
    
    if liste==["G-P","G.E","VIOLON.R","S.DRUMS"]:
        choix5 = "static/musiques/42.mp3"
    
    if liste==["G-P","MB","S.VIOLON","S.DRUMS"]:
        choix5 = "static/musiques/43.mp3"
    
    if liste==["G-P","MB","VIOLON","S.DRUMS"]:
        choix5 = "static/musiques/44.mp3"
    
    if liste==["G-P","MB","VIOLON.R","S.DRUMS"]:
        choix5 = "static/musiques/45.mp3"
    
    if liste==["PIANO","G.E-MB","S.VIOLON","S.DRUMS"]:
        choix5 = "static/musiques/46.mp3"
    
    if liste==["PIANO","G.E-MB","VIOLON","S.DRUMS"]:
        choix5 = "static/musiques/47.mp3"
    
    if liste==["PIANO","G.E-MB","VIOLON.R","S.DRUMS"]:
        choix5 = "static/musiques/48.mp3"
    
    if liste==["PIANO","G.E","S.VIOLON","S.DRUMS"]:
        choix5 = "static/musiques/49.mp3"
    
    if liste==["PIANO","G.E","VIOLON","S.DRUMS"]:
        choix5 = "static/musiques/50.mp3"
    
    if liste==["PIANO","G.E","VIOLON.R","S.DRUMS"]:
        choix5 = "static/musiques/51.mp3"
    
    if liste==["PIANO","MB","S.VIOLON","S.DRUMS"]:
        choix5 = "static/musiques/52.mp3"
    
    if liste==["PIANO","MB","VIOLON","S.DRUMS"]:
        choix5 = "static/musiques/53.mp3"
    
    if liste==["PIANO","MB","VIOLON.R","S.DRUMS"]:
        choix5 = "static/musiques/54.mp3"

    if liste==["GUITARE","MB","VIOLON.R","S.DRUMS"]:
        choix5 = "static/musiques/63.mp3"
    
    if liste==["GUITARE","MB","S.VIOLON","S.DRUMS"]:
        choix5 = "static/musiques/56.mp3"
    
    if liste==["GUITARE","MB","VIOLON","S.DRUMS"]:
        choix5 = "static/musiques/60.mp3"
    
    if liste==["GUITARE","G.E-MB","VIOLON.R","S.DRUMS"]:
        choix5 = "static/musiques/63.mp3"
    
    if liste==["GUITARE","G.E-MB","S.VIOLON","S.DRUMS"]:
        choix5 = "static/musiques/56.mp3"
    
    if liste==["GUITARE","G.E-MB","VIOLON","S.DRUMS"]:
        choix5 = "static/musiques/60.mp3"

    if liste==["GUITARE","G.E","S.VIOLON","DRUMS.A"]:
        choix5 = "static/musiques/55.mp3"
    
    if liste==["GUITARE","G.E","S.VIOLON","S.DRUMS"]:
        choix5 = "static/musiques/56.mp3"
    
    if liste==["GUITARE","G.E","S.VIOLON","DRUMS.T"]:
        choix5 = "static/musiques/57.mp3"

    if liste==["GUITARE","G.E","VIOLON","DRUMS.A"]:
        choix5 = "static/musiques/58.mp3"

    if liste==["GUITARE","G.E","VIOLON","DRUMS.T"]:
        choix5 = "static/musiques/59.mp3"

    if liste==["GUITARE","G.E","VIOLON","S.DRUMS"]:
        choix5 = "static/musiques/60.mp3"

    if liste==["GUITARE","G.E","VIOLON.R","DRUMS.A"]:
        choix5 = "static/musiques/61.mp3"

    if liste==["GUITARE","G.E","VIOLON.R","DRUMS.T"]:
        choix5 = "static/musiques/62.mp3"

    if liste==["GUITARE","G.E","VIOLON.R","S.DRUMS"]:
        choix5 = "static/musiques/63.mp3"





    return render_template("resultat4.html",structure=choix4,choixson=choix5)










app.run(debug=False)
