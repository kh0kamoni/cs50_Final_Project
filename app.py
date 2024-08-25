from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dining.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
# @login_required
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        room_number = request.form['room_number']
        floor_number = request.form['floor_number']
        password = generate_password_hash(request.form['password'], method='pbkdf2:sha256')
        
        new_user = User(name=name, phone=phone, room_number=room_number, floor_number=floor_number, password=password)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        phone = request.form['phone']
        password = request.form['password']
        user = User.query.filter_by(phone=phone).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid phone number or password!', 'danger')
    return render_template('login.html')

@app.route('/update_meal_status', methods=['POST'])
@login_required
def update_meal_status():
    if current_user.meal_status:
        current_user.meal_status = False
    else:
        current_user.meal_status = True

    if current_user.meal_status:
        current_user.total_meals += 1
        current_user.balance -= 65

    db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/admin/recharge', methods=['GET', 'POST'])
@login_required
def admin_recharge():
    if not (current_user.is_admin or current_user.is_dining_manager):
        return redirect(url_for('index'))

    if request.method == 'POST':
        user_id = request.form.get('user_id')
        amount = request.form.get('amount')
        user = User.query.get(user_id)
        if user:
            user.balance += float(amount)
            db.session.commit()
            flash(f"Recharged {user.name}'s balance by {amount}", 'success')
        else:
            flash('User not found', 'danger')

    room_number = request.args.get('room_number')
    floor_number = request.args.get('floor_number')
    
    query = User.query.order_by(User.phone)
    
    if room_number:
        query = query.filter(User.room_number == room_number)
    if floor_number:
        query = query.filter(User.floor_number == floor_number)
        
    users = query.all()

    return render_template('admin_recharge.html', users=users, room_number=room_number, floor_number=floor_number)



@app.route('/admin/select_dining_manager', methods=['GET', 'POST'])
@login_required
def select_dining_manager():
    if not current_user.is_admin:
        return redirect(url_for('index'))

    if request.method == 'POST':
        new_dining_manager_id = request.form.get('user_id')
        current_dining_manager = User.query.filter_by(is_dining_manager=True).first()
        if current_dining_manager:
            current_dining_manager.is_dining_manager = False
        new_dining_manager = User.query.get(new_dining_manager_id)
        if new_dining_manager:
            new_dining_manager.is_dining_manager = True
            db.session.commit()
            flash(f"New dining manager selected: {new_dining_manager.name}", 'success')
        else:
            flash('User not found', 'danger')

    # Handle search filters
    room_number = request.args.get('room_number', '')
    floor_number = request.args.get('floor_number', '')
    
    query = User.query.order_by(User.phone)
    
    if room_number:
        query = query.filter_by(room_number=room_number)
    if floor_number:
        query = query.filter_by(floor_number=floor_number)
        
    users = query.all()
    
    return render_template('select_dining_manager.html', users=users, room_number=room_number, floor_number=floor_number)


    # Handle search filters
    room_number = request.args.get('room_number')
    floor_number = request.args.get('floor_number')
    
    query = User.query.order_by(User.phone)
    
    if room_number:
        query = query.filter(User.room_number == room_number)
    if floor_number:
        query = query.filter(User.floor_number == floor_number)
        
    users = query.all()
    
    return render_template('select_dining_manager.html', users=users, room_number=room_number, floor_number=floor_number)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
