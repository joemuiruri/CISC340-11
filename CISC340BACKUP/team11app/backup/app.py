from flask import Flask, render_template, request, session, abort

app = Flask(__name__)

@app.route('/')
def index():
    return 'Home Page!'

@app.route('/indexs')
def cakes():
    return render_template('/projgit/CISC340-11/index.html')

if __name__ == '__main__':
    app.run(host='192.168.0.133',port=5000,debug=True)
