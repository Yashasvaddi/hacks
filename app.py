from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__=='__main_':
    app.run(debug=True)
zcxzcxz

   # hiihihihifdfsfdf