from flask import Flask, request, redirect, render_template_string
app = Flask(__name__)
tasks = []
PAGE = '''<h1>To-Do List</h1><form method="post" action="/add"><input name="task" required><button>Add</button></form><ul>{% for t in tasks %}<li>{{t}}</li>{% endfor %}</ul>'''
@app.get('/')
def home(): return render_template_string(PAGE, tasks=tasks)
@app.post('/add')
def add(): tasks.append(request.form['task']); return redirect('/')
if __name__ == '__main__': app.run(host='0.0.0.0', port=5000)
