from flask import Flask, jsonify
app=Flask(__name__)
@app.get('/')
def home(): return jsonify(service='backend', status='running')
app.run(host='0.0.0.0', port=5000)
