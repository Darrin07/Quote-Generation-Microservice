from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

# Dictionary to store quotes based on hydration progress levels
quotes = {
    "0%": "Getting started is the hardest part. You got this!",
    "50%": "You're halfway there! Keep up the great work!",
    "100%": "Congratulations on reaching your goal! Stay hydrated!"
}

@app.route('/')
def home():
    return "Welcome to the Quote Generation Microservice! Use /api/quote to get a quote or /get_quote to use the HTML interface."

@app.route('/get_quote', methods=['GET'])
def get_quote_html():
    user_id = request.args.get('user_id')
    progress_level = request.args.get('progress_level')

    quote = None
    if progress_level in quotes:
        quote = quotes[progress_level]

    return render_template('quote_form.html', user_id=user_id, quote=quote)

@app.route('/api/quote', methods=['GET'])
def get_quote_api():
    # Get user_id and progress_level from request parameters
    user_id = request.args.get('user_id')
    progress_level = request.args.get('progress_level')

    # Check if progress_level is in quotes dictionary
    if progress_level in quotes:
        quote = quotes[progress_level]
        return jsonify({"user_id": user_id, "quote": quote})
    else:
        return jsonify({"error": "Invalid progress level."}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
