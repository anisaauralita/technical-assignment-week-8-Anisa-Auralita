# mengimpor modul pymongo
import pymongo

# Konfigurasi mongodb
client = pymongo.MongoClient("mongodb+srv://masipnupro:Bismillah@cluster0.iubqgry.mongodb.net/?retryWrites=true&w=majority")

# Konfigurasi database
db = client['location']

# Konfigurasi koleksi
my_collections = db['track']
import json
from flask import Flask
from flask import render_template
from flask import request, jsonify

from datetime import datetime

from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def welcome():
   return render_template('welcome.html')

@app.route('/tambah')
def tambah():
   return render_template('tambah.html')

@app.route('/lihat')
def lihat():
   # details = list(my_collections.find({}, {'latitude', 'longitude'}))
   # return render_template('lihat.html', details=details)
   for x in my_collections.find():
      val = [x["id_transaksi"],x["kecepatan"],x["longitude"],x["latitude"],x["timestamp"]]
      return (val)

@app.route('/sukses')
def sukses():
   return render_template('sukses.html')


@app.route('/proses',methods = ['POST', 'GET'])
def proses():
   id_transaksi = request.form['id_transaksi']
   kecepatan = request.form['kecepatan']
   latitude = request.form['latitude']
   longitude = request.form['longitude']
   timestamp = datetime.now()

   # Data yang ingin dimasukkan
   data = {'id_transaksi':id_transaksi, 'kecepatan': kecepatan,'latitude':latitude,'longitude':longitude, 'timestamp':timestamp}
   results = my_collections.insert_one(data)
   return redirect("http://127.0.0.1:5000/sukses")

if __name__ == '__main__':
   app.run(debug = True)