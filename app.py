
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Lawrence Armada's API!"

@app.route('/student')
def get_student():
    return jsonify({
        "student_id": "24-00118",
        "name": "LAWRENCE ARMADA",
        "program": "BSIT",
        "year": 3,
        "section": "A"
    })

@app.route('/hello')
def say_hello():
    name = request.args.get('name', 'Student')
    return jsonify({
        "message": f"Hello, {name}!"
    })

# New Endpoint 1
@app.route('/hobby')
def get_hobby():
    return jsonify({
        "hobby": "Playing online games",
        "description": "I enjoy playing games in my free time."
    })

# New Endpoint 2
@app.route('/total')
def calculate_total():
    try:
        price = float(request.args.get('price', 0))
        quantity = int(request.args.get('quantity', 0))

        if price < 0 or quantity < 0:
            return jsonify({
                "error": "Values cannot be negative"
            }), 400

        return jsonify({
            "price": price,
            "quantity": quantity,
            "total": round(price * quantity, 2)
        })

    except ValueError:
        return jsonify({
            "error": "Invalid input"
        }), 400

if __name__ == '__main__':
    app.run(debug=True)
