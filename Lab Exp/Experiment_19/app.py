from flask import Flask, jsonify
app=Flask(__name__)
@app.get('/')
def home(): return jsonify(message='CI/CD Flask application')
@app.get('/health')
def health(): return jsonify(status='ok')
