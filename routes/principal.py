from flask import Blueprint, render_template
from models.contactus import messages
from forms.registerform import contactusform
from utils.db import db

principal = Blueprint("principal", __name__, url_prefix="/")



@principal.route("/", methods=["GET", "POST"])
def mensajenuevo():
    form = contactusform()
    if form.validate_on_submit():
            firstname = form.firstname.data
            lastname = form.lastname.data
            email = form.email.data
            message = form.message.data
            newmessage = messages(firstname, lastname, email, message)
            db.session.add(newmessage)
            db.session.commit()
    return render_template("principal.html", form=form)

@principal.route("/messages")
def messagess():
    messagesList = messages.query.all()
    return render_template("mensajes.html", messagesList=messagesList)