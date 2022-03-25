from flask import Blueprint, render_template
from models.contactus import messages


mensajes = Blueprint("mensajes", __name__, url_prefix="/")

@mensajes.route("/messages",  methods=["GET", "POST"])
def messages():
    messagesList = messages.query.all()
    return render_template("mensajes.html", messagesList=messagesList)