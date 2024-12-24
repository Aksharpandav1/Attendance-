from flask import Flask, render_template, send_file, request, redirect, flash, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_paginate import Pagination, get_page_args
from flask_migrate import Migrate
from datetime import datetime
import pandas as pd
from io import BytesIO
from reportlab.pdfgen import canvas

# Initialize the Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'  # Replace with your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'securekey'

# Initialize SQLAlchemy
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route("/")
def home():
    return "Home Page"

@app.route("/home")
def another_home():
    return "Another Home Page"

@app.route('/devotees')
def view_devotees():
    # Your code to view devotees
    return render_template('devotees.html')

@app.route('/attendance-log')
def attendance_log():
    # Your code to view attendance log
    return render_template('attendance_log.html')

@app.route('/mark-attendance', methods=['GET', 'POST'])
def mark_attendance():
    search_query = request.args.get('search', '').strip()
    devotees = []
    if search_query:
        devotees = Devotee.query.filter(
            (Devotee.name.ilike(f"%{search_query}%")) |
            (Devotee.serial_number.like(f"%{search_query}%"))
        ).all()
    else:
        devotees = Devotee.query.all()

    if request.method == 'POST':
        attendance_ids = request.form.getlist('attendance')
        if not attendance_ids:
            flash('No devotees selected for attendance.', 'warning')
        else:
            for devotee_id in attendance_ids:
                attendance = Attendance(devotee_id=devotee_id, date=datetime.date.today())
                db.session.add(attendance)
            db.session.commit()
            flash('Attendance marked successfully!', 'success')
        return redirect('/mark-attendance')

    return render_template('mark_attendance.html', devotees=devotees, search_query=search_query)

# Define your models
class Devotee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serial_number = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200))
    position = db.Column(db.String(50))
    contact = db.Column(db.String(15))

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serial_number = db.Column(db.String(10), nullable=False)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(10), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Route: Export Devotees to Excel
@app.route('/export/devotees/excel')
def export_devotees_excel():
    devotees = Devotee.query.all()
    data = [{'Serial Number': d.serial_number, 'Name': d.name, 'Address': d.address, 
             'Position': d.position, 'Contact': d.contact} for d in devotees]
    df = pd.DataFrame(data)
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Devotees')
    writer.save()
    output.seek(0)
    return send_file(output, download_name='devotees.xlsx', as_attachment=True)

# Route: Export Attendance to PDF
@app.route('/export/attendance/pdf')
def export_attendance_pdf():
    attendance_records = db.session.query(
        Attendance.date, Devotee.serial_number, Devotee.name, Attendance.status
    ).join(Devotee).all()
    output = BytesIO()
    pdf = canvas.Canvas(output)
    pdf.drawString(100, 800, "Attendance Records")
    y = 750
    for record in attendance_records:
        pdf.drawString(100, y, f"{record.date} - {record.serial_number} - {record.name} - {record.status}")
        y -= 20
    pdf.save()
    output.seek(0)
    return send_file(output, download_name='attendance.pdf', as_attachment=True)

# Create database tables
if __name__ == '__main__':
    with app.app_context():  # Ensures we're in the app context
        db.create_all()      # Creates the tables in the database
        print("Database tables created successfully!")
    app.run(debug=True)       # Runs the Flask application
