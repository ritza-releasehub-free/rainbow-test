from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import traceback

print("++++++++++++++")
print("")
print("RUNNING")
print("")
print("++++++++++++++")

user = 'postgres'
pw = '29626f9c15367aa6b'
url = 'example-app.cv6iiqxg5z3f.eu-west-2.rds.amazonaws.com'
db = 'postgres'
DB_URL = f'postgresql+psycopg2://{user}:{pw}@{url}/{db}'
print(DB_URL)

app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class counts(db.Model):
    id = db.Column('count_id', db.Integer, primary_key=True)
    value = db.Column(db.Integer)

try:
    db.create_all()
except Exception as e:
    print(e)
    print("couldn't craete db")
    traceback.print_exc()



@app.route("/", methods=['POST','GET'])
def hello():
    if request.method == 'POST':
        c = request.form['countbutton']
        count = counts(value=1)
        db.session.add(count)
        db.session.commit()

    total_counts = counts.query.count()
        
    return render_template('index.html', total=total_counts)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
