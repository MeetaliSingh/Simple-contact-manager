from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contacts_list import *
app = Flask(__name__)

@app.route('/')
def home():
    users = User.objects.all()
    return render_template('users.html', u=users)

@app.route('/view')
def view():
    error = None
    return render_template('view.html', error=error)

@app.route('/view', methods=['POST'])
def view_rest():
    name = request.form['name']
    try:
        this_user = User.objects.get(name=name)
        return render_template('single_user.html', uu=this_user)
    except:
        error = 'Name not in list'
        return redirect(url_for('home'))

@app.route('/add')
def add():
    error = None
    return render_template('add.html', error=error)

@app.route('/add', methods=['POST'])
def add_rest():
    new_user = User(email=request.form['email'], name=request.form['name'], phone=request.form['phone']).save()
    new_user = User.objects.get(name=new_user.name)
    return render_template('single_user.html', uu=new_user)

@app.route('/delete')
def delete():
    error = None
    return render_template('delete.html', error=error)

@app.route('/delete', methods=['POST'])
def delete_rest():
    name = request.form['name']
    try:
        this_user = User.objects.get(name=name)
        this_user.delete()
        return redirect(url_for('home'))
    except:
        error = 'Name not in list'
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.debug = True
    app.run(port=3000)