from app import app

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
