from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Sample in-memory storage for todos
todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    new_todo = request.form.get('todo')
    if new_todo:
        todos.append(new_todo)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>', methods=['POST'])
def delete_todo(index):
    if 0 <= index < len(todos):
        todos.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
ls