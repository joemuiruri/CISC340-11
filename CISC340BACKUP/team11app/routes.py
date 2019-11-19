from team11app import team11app

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/password')
def index():
    return "Please Enter your Password"
