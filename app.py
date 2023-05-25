import mysql.connector
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Configurações do banco de dados
db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'calculadora_db'
}

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

def obter_conexao():
    return mysql.connector.connect(**db_config)

@app.route('/calculadora', methods=['GET'])
def obter_calculos():
    numero = request.args.get('numero')
    if numero:
        numero = int(numero)

        # Verifica se o resultado já está armazenado no banco de dados
        conn = obter_conexao()
        cursor = conn.cursor()
        query = "SELECT * FROM resultados WHERE numero = %s"
        cursor.execute(query, (numero,))
        resultado_db = cursor.fetchone()

        if resultado_db:
            # Se o resultado já existe no banco de dados, retorne-o diretamente
            resultado = {
                'numero': resultado_db[0],
                'fatorial': resultado_db[1],
                'super_fatorial': resultado_db[2]
            }
        else:
            # Caso contrário, faça os cálculos e armazene o resultado no banco de dados
            fatorial = calcular_fatorial(numero)
            super_fatorial = calcular_super_fatorial(numero)
            resultado = {'numero': numero, 'fatorial': fatorial, 'super_fatorial': super_fatorial}

            # Insere o resultado no banco de dados
            insert_query = "INSERT INTO resultados (numero, fatorial, super_fatorial) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (numero, fatorial, super_fatorial))
            conn.commit()

        cursor.close()
        conn.close()
    else:
        resultado = None

    return render_template('calculadora.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
