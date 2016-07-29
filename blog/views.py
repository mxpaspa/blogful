from flask import render_template

from . import app
from .database import session, Entry

@app.route("/")
def entries():
    allEntries = session.query(Entry)
    allEntries = allEntries.order_by(Entry.datetime.desc())
    allEntries = allEntries.all()
    return render_template("entries.html",
        entries=allEntries
    )