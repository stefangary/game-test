from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Game state
speed = 12
ball = {"x": 400, "y": 300, "dx": 10, "dy": 10}
paddle_a = {"y": 250, "height": 100}
paddle_b = {"y": 250, "height": 100}
scores = {"a": 0, "b": 0}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update', methods=['GET', 'POST'])
def update():
    global ball, paddle_a, paddle_b, scores
    
    if request.method == 'POST':
        data = request.json
        paddle_a['y'] = data.get('paddle_a_y', paddle_a['y'])
        paddle_b['y'] = data.get('paddle_b_y', paddle_b['y'])

    # Update ball position
    ball['x'] += ball['dx']
    ball['y'] += ball['dy']

    # Ball collision with top/bottom
    if ball['y'] <= 0 or ball['y'] >= 600:
        ball['dy'] *= -1

    # Ball collision with paddles
    if (ball['x'] <= 30 and paddle_a['y'] <= ball['y'] <= paddle_a['y'] + paddle_a['height']) or \
       (ball['x'] >= 770 and paddle_b['y'] <= ball['y'] <= paddle_b['y'] + paddle_b['height']):
        ball['dx'] *= -1

    # Ball out of bounds
    if ball['x'] <= 0:
        scores['b'] += 1
        ball = {"x": 400, "y": 300, "dx": 5, "dy": 5}
    elif ball['x'] >= 800:
        scores['a'] += 1
        ball = {"x": 400, "y": 300, "dx": -5, "dy": 5}

    return jsonify(ball=ball, paddle_a=paddle_a, paddle_b=paddle_b, scores=scores)

if __name__ == '__main__':
    app.run(port=5000)