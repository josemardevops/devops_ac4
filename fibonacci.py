import os
from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/')

def sequencia_fibonacci():
    c = 100
    s = 2
    number_1 = 0
    number_2 = 1
    fibonacci = "0,1,"
    while s < c:
        add_fibo = number_1 + number_2
        if s < c - 1:
            fibonacci = fibonacci + str(add_fibo) + ", "
        else:
            fibonacci = fibonacci + str(add_fibo) + "."
        number_1 = number_2
        number_2 = add_fibo
        s += 1
    return fibonacci

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
