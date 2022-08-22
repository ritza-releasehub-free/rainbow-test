from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///count-database.sqlite3'

db = SQLAlchemy(app)

class counts(db.Model):
    id = db.Column('count_id', db.Integer, primary_key=True)
    value = db.Column(db.Integer)

try:
    db.create_all()
except:
    print("couldn't create db")
    pass


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
