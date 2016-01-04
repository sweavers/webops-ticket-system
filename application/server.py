from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from application import app, db
from application.models import Tickets
from application.forms import TicketForm
import re
import os
import requests

app.config['SECRET_KEY'] = 'somethingsomethingdarkside'

@app.before_first_request
def init_request():
    db.create_all()

@app.route('/view_tickets', methods=['GET', 'POST'])
def index():
    db.create_all()
    form = TicketForm(request.form)
    ticket_data = {}

    if request.method == 'POST':
        project_data = form.project.data
        title_data = form.title.data
        description_data = form.description.data
        contact_data = form.contact.data
        priority_data = form.priority.data

        ticket_row = Tickets(project=project_data, title=title_data, description=description_data, contact=contact_data, priority=priority_data)
        db.session.add(ticket_row)
        db.session.commit()

    tickets = Tickets.query.all()

    for ticket_row in tickets:
        print('-__-__-__-__-__-__--__-_-_-_-_')
        print(ticket_row.project,ticket_row.title,ticket_row.contact)
        ticket_data.update({"project": ticket_row.project, "title": ticket_row.title, "description": ticket_row.description, "contact": ticket_row.contact, "priority": ticket_row.priority})

    return render_template('view_tickets.html', ticket_data=ticket_data)

@app.route('/create_ticket', methods=['GET', 'POST'])
def new():
    db.create_all()
    form = TicketForm(request.form)
    return render_template('ticket_form.html', form=form)
