INSTRUCTIONS ON WHAT THE CODE DOES BELOW



LINES 1-5: States flask to create loop, render_template to serve HTML, jsonify to return JSON files, request to handle incoming data

LINES 6-12: Sets the speed of the ball, creates the ball itself and the properties, height , etc; creates the dimensions of the paddles for both players, sets the scoreboard format for both players, @app.route('/'), this is a route decorator, whenever a user runs the function this should appear: def index():
    return render_template('index.html')
    
LINES 13-18: def index(): defines the python function named index, This function will be triggered when someone visits the root route / of the web app (like http://localhost:5000/), thanks to the decorator @app.route('/') above it. return render_template('index.html')Tells Flask to return an HTML page called index.html to the user. Flask will look for this file inside a folder named templates/. @app.route('/update', methods=['GET', 'POST']) Sets up another route in Flask, this time at /update. It accepts both GET (default) and POST (when the frontend sends data). The function update() will run when the browser makes a request to /update. def update(): Defines the update() function to handle logic every time /update is requested. This function handles the movement of the paddles, moves the ball, updates positioning and scoring and returns the new games state as JSON. global ball, paddle_a, paddle_b, scores: This tells python that inside the function you want to modify the global game state variables and not create new local variables.


LINES 20-24: if request.method == 'POST': Checks if the request is a POST request, POST is used when the front end sends data. data = request.json: Gets the JSON data sent from the frontend and stores it in the variable data. paddle_a['y'] = data.get('paddle_a_y', paddle_a['y']): Tries to get paddle_a_y from the incoming data. If it’s found, it updates paddle_a['y'] to that new value. If it’s not found, it keeps the current value (paddle_a['y']). This prevents errors if the key is missing. paddle_b['y'] = data.get('paddle_b_y', paddle_b['y']), the same logic above but for the other paddle.


LINES 26-36: ball['x'] += ball['dx']: Moves the ball horizontally depending on the velocity. ball['y'] += ball['dy']: Moves the ball vertically depending the velocity. if ball['y'] <= 0 or ball['y'] >= 600: ball['dy'] *= -1: Checks if the ball hits the bottom or top of the screen. If it does, it reverses the vertical direction by multiplying dy by -1 making the ball bounce off the wall and go the other way. BALL COLLISION WITH PADDLES: if (
    ball['x'] <= 30 and paddle_a['y'] <= ball['y'] <= paddle_a['y'] + paddle_a['height']
) or (
    ball['x'] >= 770 and paddle_b['y'] <= ball['y'] <= paddle_b['y'] + paddle_b['height']
):
    ball['dx'] *= -1: Checks if the ball hits paddle A (on the left) or paddle B (on the right): For paddle A: ball’s x-position is at or before 30, and it's vertically inside the paddle’s range. For paddle B: ball’s x-position is at or after 770, and it’s vertically inside paddle B’s range. If it hits either paddle, it reverses horizontal direction (dx *= -1), so it bounces back.


LINES 39-49: if ball['x'] <= 0: Checks if the ball has gone past the left edge of the screen (i.e., player A missed the ball). scores['b'] += 1: Increases Player B's score by 1 because A missed. ball = {"x": 400, "y": 300, "dx": 5, "dy": 5}: Resets the ball to the center of the screen (x = 400, y = 300) after a score. Sets its direction to move right and slightly down (positive dx, positive dy). elif ball['x'] >= 800: Checks if the ball has gone past the right edge of the screen (i.e., player B missed the ball). scores['a'] += 1: Increases Player A's score by 1. ball = {"x": 400, "y": 300, "dx": -5, "dy": 5} Resets the ball again, this time with dx = -5 to move leftward toward player B. return jsonify(ball=ball, paddle_a=paddle_a, paddle_b=paddle_b, scores=scores) Sends back the entire updated game state to the client (browser) as a JSON object: Ball position and direction, Paddle positions, updated scores. if __name__ == '__main__': This line means: only run the next line if this script is being run directly (not imported as a module). app.run(port=5000) tarts the Flask web server on http://localhost:5000. That’s where your game will run. 












    











