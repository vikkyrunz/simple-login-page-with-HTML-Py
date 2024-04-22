from flask import Flask, render_template, redirect, request

app = Flask(__name__,template_folder='template')

@app.route('/')
def home():
   return render_template("index.html")

@app.route('/home')
def red_home():
   return redirect ('/') 

@app.route('/loggedin', methods=['POST'])
def loggedin():
   if request.method == 'POST':
       information = request.form

   return render_template("loggedin.html", data=information)

if __name__ == '__main__':
    app.run(debug = True)