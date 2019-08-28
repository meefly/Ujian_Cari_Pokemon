import requests
from flask import Flask, render_template, jsonify, request, redirect

app = Flask(__name__)
       
@app.route('/',methods = ['GET'])
def home():
    return render_template('home.html')

@app.route('/hasil', methods=['POST'])
def post():
    name = request.form['nama']
    url = 'https://pokeapi.co/api/v2/pokemon/'+name
    datapoke = requests.get(url)
    
    if str(datapoke) == '<Response [404]>':
        return redirect('/NotFound')
    
    filenama = datapoke.json()['name']
    besar = filenama[0].upper()
    nama = besar + filenama[1:]
    
    id_pokemon = datapoke.json()['id']
    tinggi_pokemon = datapoke.json()['height']
    berat_pokemon = datapoke.json()['weight']
    
    gambar = datapoke.json()['sprites']
    gambar1 = gambar['front_default']
    
    biodata=[nama,gambar1,id_pokemon,berat_pokemon,tinggi_pokemon]
    return render_template('hasil.html',x=biodata)   
    
@app.route('/NotFound')
def notFound():
    return render_template('error.html')

if __name__ == "__main__":
    app.run(debug = True)

