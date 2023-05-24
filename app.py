from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

def calcular_fatorial(numero):
    if numero < 0:
        return "Número deve ser não-negativo."
    elif numero == 0 or numero == 1:
        return 1
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial

def calcular_super_fatorial(numero):
    if numero < 0:
        return "Número deve ser não-negativo."
    elif numero == 0 or numero == 1:
        return 1
    else:
        super_fatorial = 1
        for i in range(1, numero + 1):
            super_fatorial *= calcular_fatorial(i)
        return super_fatorial

@app.route('/calculadora', methods=['GET'])
def obter_calculos():
    numero = request.args.get('numero')
    if numero:
        numero = int(numero)
        fatorial = calcular_fatorial(numero)
        super_fatorial = calcular_super_fatorial(numero)
        resultado = {'numero': numero, 'fatorial': fatorial, 'super_fatorial': super_fatorial}
    else:
        resultado = None

    return render_template('calculadora.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
