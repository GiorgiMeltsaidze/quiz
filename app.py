from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = ["iyide manqana", "gaakete samushao", "daureke mziurs"]

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form['task']
    tasks.append(task)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

@app.route('add.html')
def home():
    return render_template('add.html')