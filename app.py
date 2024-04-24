from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, redirect, render_template, flash, url_for, jsonify
from model import db, connect_db, Pet
from form import AddPet, EditPet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def Petlist():
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)

@app.route('/add', methods=["GET", "POST"])
def Addnewpet():
    form = AddPet()
    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added.")
        return redirect(url_for('Petlist'))
    else:
        return render_template("pet_form.html", form=form)
    
@app.route("/<int:pet_id>", methods=["GET", "POST"])
def Editpet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPet(obj=pet)
    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect(url_for('Petlist'))
    else:
        return render_template("edit.html", form=form, pet=pet)