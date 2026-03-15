from flask import Flask
import hashlib
import time

app = Flask(__name__)

blockchain = []

def vytvor_block(data):

    index = len(blockchain)

    cas = str(time.time())

    if len(blockchain) == 0:
        previous_hash = "0"
    else:
        previous_hash = blockchain[-1]["hash"]

    text = str(index) + data + cas + previous_hash

    hash = hashlib.sha256(text.encode()).hexdigest()

    block = {
        "index": index,
        "time": cas,
        "data": data,
        "hash": hash,
        "previous": previous_hash
    }

    blockchain.append(block)

@app.route("/")
def home():

    text = ""
    text += "Blockchain API funguje\n\n"

    text += "Jak pouzit:\n"
    text += "/add -> prida block\n"
    text += "/chain -> vypise blockchain\n\n"

    text += "Komandy:\n"
    text += "http://127.0.0.1:5000/add\n"
    text += "http://127.0.0.1:5000/chain\n"

    return text

@app.route("/chain")
def chain():

    vystup = ""

    for block in blockchain:
        vystup += str(block) + "\n"

    return vystup

@app.route("/add")
def add():

    data = "test data"

    vytvor_block(data)

    return "Block pridan"

vytvor_block("genesis")

app.run()