
from app.models.kuotaModel import db, Quota
from app import app
from flask import render_template,request,redirect


@app.route('/kuotadata', methods=['GET','POST'])
def choose():
    if request.method == 'POST':
        nama = request.form['nama']
        sekolah = request.form['sekolah']
        email = request.form['email']
        nomor = request.form['nomor']
        perdana = request.form['perdana']
        try:
            newsData = Quota(nama=nama, sekolah=sekolah, email=email,nomor=nomor, perdana=perdana)

            db.session.add(newsData)
            db.session.commit()
        except Exception as e:
            print("Failed to add data.")
            print(e)
    listkuota = Quota.query.all()
    return render_template('kuota.html',data=enumerate(listkuota, 1))

@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    data = Quota.query.filter_by(id=id).first()
    return render_template("update.html", data=data)


@app.route('/updatekuota', methods=['POST'])
def updatekuota():
    if request.method == 'POST':
        id = request.form['id']
        nama = request.form['nama']
        sekolah = request.form['sekolah']
        email = request.form['email']
        nomor = request.form['nomor']
        perdana = request.form['perdana']
        print(nama)
        try:
            kuota = Quota.query.filter_by(id=id).first()
            kuota.nama = nama
            kuota.sekolah = sekolah
            kuota.email = email
            kuota.nomor = nomor
            kuota.perdana = perdana
            db.session.commit()
        except Exception as e:
            print("Failed to update data")
            print(e)
        return redirect("/kuotadata")

@app.route('/delete/<int:id>')
def delete(id):
    try:
        data = Quota.query.filter_by(id=id).first()
        db.session.delete(data)
        db.session.commit()
    except Exception as e:
        print("Failed delete mahasiswa")
        print(e)
    return redirect("/kuotadata")



