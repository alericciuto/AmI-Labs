from flask import Flask, redirect, url_for, render_template, request
import db_interaction

app = Flask(__name__)


@app.route('/')
def index_redirect():
    db_interaction.import_tasks()
    return redirect(url_for("index"))


@app.route('/index')
def index():
    tasks = db_interaction.get_all_tasks()
    return render_template("index.html", tasks=tasks)


@app.route('/delete/<id_task>')
def delete(id_task):
    db_interaction.remove_task(id_task)
    return redirect(url_for("index"))


@app.route('/insert', methods=["POST"])
def insert():
    task = request.form["text_task"]
    db_interaction.add_task(task)
    return redirect("index")


if __name__ == '__main__':
    app.run()
