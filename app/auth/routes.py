from app.auth import bp
from flask import render_template, request
from app.models.user import User

@bp.route('/')
def index():
    users = User.query.all()
    return render_template('auth/index.html', users=users)

@bp.route('/register', methods =('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password= request.form['password']

        if not title:
            flash('El titulo es obligatorio')
        elif not content:
            flash('El contenido es obligatorio')
        else:
            message = Message(title = title, content = content, picture = picture)
            db.session.add(message)
            db.session.commit()
            return redirect(url_for('messages.index'))

    return render_template('auth/register.html')







