from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'admin'


notes=[]
@app.route('/', methods=["POST",'GET'])
def index():
     if 'username' in session:
            username = session['username']

            return ('Welcome '+ username+"</br> <a href= '/add_note'>Click here to add notes</a> </br> <b><a href = '/logout'>click here to log out</a></b>")


     return "<b>LOG IN</b> <br><a href = '/login'> click here to log in</a>"


@app.route("/add_note",methods=['POST','GET'])
def add_note():

    if 'username' in session:
        print("session call")
        if request.method == 'POST':

            p = request.form.get("note")
            notes.extend([p])
            print(notes)


    else:
        print("not call")
        return redirect(url_for('index'))
    return render_template('home.html' ,notes=notes, p=session['username'])

@app.route('/login', methods=['GET', 'POST'])
def login():
     if 'username' not in session:

         if request.method == 'POST':
             session['username'] = request.form.get('username')
             return redirect("/")
         return render_template("login.html")

     else:
        return redirect(url_for('index'))


@app.route("/logout")
def logout():
    session.pop('username',None)

    return redirect("/")






if __name__ == '__main__':
    app.run(debug=True)
