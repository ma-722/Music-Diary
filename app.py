from flask import Flask,render_template

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
  return render_template('index.html')

# spotify branch test
@app.route('/', methods = ['GET'])
def spotify():
  return render_template('index.html')

if __name__ == '__main__':
  app()