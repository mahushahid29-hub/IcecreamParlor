from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3, os

app = Flask(__name__)
CORS(app)

DB = os.environ.get("DB_PATH", "/data/orders.db")

def init_db():
    os.makedirs(os.path.dirname(DB), exist_ok=True)
    conn = sqlite3.connect(DB)
    conn.execute("""CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        base TEXT, size TEXT, flavors TEXT, total REAL
    )""")
    conn.commit()
    conn.close()

PRICES = {
    "Cone":    {"Small": 2.50, "Medium": 4.00, "Large": 5.50},
    "Cup":     {"Small": 2.00, "Medium": 3.50, "Large": 5.00},
    "Brownie": {"Small": 1.50, "Medium": 1.50, "Large": 1.50},
}
FLAVOR_PRICES = {
    "Chocolate": 2.00, "Strawberry": 2.00, "Vanilla": 1.50,
    "Cookies and Cream": 2.50, "Caramel": 1.50, "Pistachio": 2.50
}

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

@app.route('/order', methods=['POST'])
def order():
    d = request.json
    base, size, flavors = d['base'], d['size'], d.get('flavors', [])
    total = PRICES.get(base, {}).get(size, 0) + sum(FLAVOR_PRICES.get(f, 0) for f in flavors)
    conn = sqlite3.connect(DB)
    conn.execute("INSERT INTO orders(base,size,flavors,total) VALUES(?,?,?,?)",
                 (base, size, ', '.join(flavors), total))
    conn.commit()
    conn.close()
    return jsonify({"total": total})

@app.route('/orders')
def orders():
    conn = sqlite3.connect(DB)
    rows = conn.execute("SELECT id,base,size,flavors,total FROM orders ORDER BY id DESC LIMIT 20").fetchall()
    conn.close()
    return jsonify([{"id": r[0], "base": r[1], "size": r[2], "flavors": r[3], "total": r[4]} for r in rows])

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=False)
