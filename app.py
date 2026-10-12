from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"mensagem": "Bem-vindo a API FastOrder!"})

@app.route('/api/status')
def status():
    return jsonify({"status": "operacional", "servico": "Fastorder-Web"})

# Missão 5.1: Rota /api/soma
@app.route('/api/soma')
def soma():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    
    if a is None or b is None:
        return jsonify({"erro": "Parâmetros 'a' e 'b' são obrigatórios"}), 400
        
    resultado = a - b
    return jsonify({"resultado": resultado})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)