from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import os

from database import get_connection, init_db

app = Flask(__name__)
CORS(app)

init_db()

# ==========================================
# ROTA INICIAL
# ==========================================

@app.route("/")
def home():
    return jsonify({
        "mensagem": "API funcionando",
        "status": "ok"
    })


# ==========================================
# LISTAR LANÇAMENTOS
# ==========================================

@app.route("/lancamentos", methods=["GET"])
def listar_lancamentos():

    conn = get_connection()

    lancamentos = conn.execute("""
        SELECT *
        FROM lancamentos
        ORDER BY id ASC
    """).fetchall()

    conn.close()

    return jsonify([dict(l) for l in lancamentos])


# ==========================================
# ADICIONAR LANÇAMENTO
# ==========================================

@app.route("/lancamentos", methods=["POST"])
def adicionar_lancamento():

    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Nenhum dado enviado"}), 400

    descricao = dados.get("descricao", "").strip()
    valor = dados.get("valor")
    tipo = dados.get("tipo")
    categoria = dados.get("categoria", "Outros")

    if not descricao:
        return jsonify({"erro": "Descrição obrigatória"}), 400

    if valor is None:
        return jsonify({"erro": "Valor obrigatório"}), 400

    if tipo not in ["receita", "gasto"]:
        return jsonify({"erro": "Tipo inválido"}), 400

    agora = datetime.now()

    data = agora.strftime("%d/%m/%Y")
    mes = agora.strftime("%Y-%m")

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO lancamentos
        (descricao, valor, tipo, categoria, data, mes)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        descricao,
        float(valor),
        tipo,
        categoria,
        data,
        mes
    ))

    conn.commit()

    novo_id = cursor.lastrowid

    conn.close()

    return jsonify({
        "id": novo_id,
        "descricao": descricao,
        "valor": valor,
        "tipo": tipo,
        "categoria": categoria,
        "data": data,
        "mes": mes
    }), 201


# ==========================================
# EXCLUIR UM LANÇAMENTO
# ==========================================

@app.route("/lancamentos/<int:id>", methods=["DELETE"])
def excluir_lancamento(id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM lancamentos
        WHERE id = ?
    """, (id,))

    conn.commit()

    removidos = cursor.rowcount

    conn.close()

    if removidos == 0:
        return jsonify({
            "erro": "Lançamento não encontrado"
        }), 404

    return jsonify({
        "mensagem": "Lançamento excluído"
    })


# ==========================================
# EXCLUIR TODOS
# ==========================================

@app.route("/lancamentos", methods=["DELETE"])
def excluir_todos():

    conn = get_connection()

    conn.execute("""
        DELETE FROM lancamentos
    """)

    conn.commit()
    conn.close()

    return jsonify({
        "mensagem": "Todos os lançamentos foram removidos"
    })