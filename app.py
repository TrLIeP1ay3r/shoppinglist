from flask import Flask, request,render_template, redirect,session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Items.db'
db = SQLAlchemy(app)
app.secret_key = 'secret_key'

class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean)

    def __init__(self,name, done ):
        self.name = name
        self.done = done

with app.app_context():
    db.create_all()


@app.route('/', methods=['GET','POST'])
def index():
    items = Items.query.all()
    if request.method == 'POST':
        # handle request
        name = request.form['name']
        # done = request.form['done']

        new_item = Items(name=name, done=False)
        db.session.add(new_item)
        db.session.commit()
        
        return redirect('/')
    return render_template('base.html', items=items)

@app.route('/update/<int:item_id>')
def update(item_id):
    item = Items.query.filter_by(id=item_id).first()
    item.done = not item.done
    db.session.commit()
    return redirect('/')

@app.route('/delete/<int:item_id>')
def delete(item_id):
    item = Items.query.filter_by(id=item_id).first()
    db.session.delete(item)
    db.session.commit()
    return redirect('/')
   

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')