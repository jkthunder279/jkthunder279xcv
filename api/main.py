from flask import Flask, jsonify, request

app = Flask(__name__)

# Endpoint to get the current date and time
@app.route('/api/datetime', methods=['GET'])
def get_datetime():
    from datetime import datetime
    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    return jsonify({'current_datetime': now})

# Endpoint to evaluate a developer
@app.route('/api/evaluate', methods=['POST'])
def evaluate_developer():
    data = request.get_json()
    # Simulated evaluation logic
    evaluation = {
        'developer': data.get('name'),
        'score': 95,
        'comments': 'Excellent performance!'
    }
    return jsonify(evaluation)

if __name__ == '__main__':
    app.run(debug=True)