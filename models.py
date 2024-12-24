class Devotee(db.Model):
    __tablename__ = 'devotees'  # Optional, sets a custom table name in the database
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each devotee
    serial_number = db.Column(db.String(10), unique=True, nullable=False)  # Serial Number
    name = db.Column(db.String(100), nullable=False)  # Name of the devotee
    address = db.Column(db.String(255), nullable=True)  # Address
    position = db.Column(db.String(50), nullable=False)  # Position (e.g., Devotee or Karyakar)
    contact_number = db.Column(db.String(15), nullable=False)  # Contact Number

class Attendance(db.Model):
    __tablename__ = 'attendance'  # Optional, sets a custom table name in the database
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each attendance record
    devotee_id = db.Column(db.Integer, db.ForeignKey('devotees.id'), nullable=False)  # Links to the devotee
    date = db.Column(db.Date, nullable=False)  # Date when attendance was marked

    # Relationship to the Devotee model
    devotee = db.relationship('Devotee', backref=db.backref('attendances', lazy=True))