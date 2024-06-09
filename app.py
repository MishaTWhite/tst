from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    api_url = f"https://sf-ecom-api.silpo.ua/v1/uk/branches/00000000-0000-0000-0000-000000000000/search-meal?query={query}"
    response = requests.get(api_url)
    data = response.json()
    
    return render_template('results.html', items=data['items'])

if __name__ == '__main__':
    app.run(debug=True)
