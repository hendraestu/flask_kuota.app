from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)


class Quota(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    nama = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    sekolah = db.Column(db.String(100), nullable=False)
    nomor = db.Column(db.String(100), nullable=False)
    perdana = db.Column(db.String(100), nullable=False)

    def init(self, nama, email, sekolah,nomor, perdana):
        self.nama = nama
        self.email = email
        self.sekolah = sekolah
        self.nomor = nomor
        self.perdana = perdana