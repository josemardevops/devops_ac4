import os
from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/')
def localiza_primos():
    c = 100
    s = 1
    number = 3
    primos = "2,"
    while s < c:
        qtd_divisores = 0
        for j in range(1, number+1):
            if number % j == 0:
                qtd_divisores += 1
        if qtd_divisores == 2:
            primos = primos + str(number) + ","
            s += 1
        number += 1

    return primos

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

