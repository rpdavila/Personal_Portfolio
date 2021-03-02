from website import app, mail
from flask import render_template, request, redirect, url_for
from website.forms import ContactForm, TwitterForm
from website.dbqueries import (insert_from_contact_form, grab_country_data, get_data_to_html_table,
                               delete_records_in_twitter_trends)
from twitter_api import trends_available, retrieve_data
from flask_mail import Message


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/contact', methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if request.method == "POST":
        if form.validate_on_submit():
            insert_from_contact_form(form)
            send_email(form)
            return redirect(url_for('home'))
    return render_template('contact.html', form=form, title='Contact')


def send_email(form):
    msg = Message(subject=f'{form.subject.data}',
                  sender=f'{form.email.data}',
                  recipients=['rafael.pietri@gmail.com'])
    msg.body = f'Hello my name is {form.name.data},\n{form.body.data}'
    mail.send(msg)


@app.route('/projects')
def projects():
    return render_template('projects.html', title='Projects')


@app.route('/twitter-api', methods=["GET", "POST"])
def twitter():
    form = TwitterForm()
    fetch_data = get_data_to_html_table()
    trends_available()
    for country in grab_country_data():
        data = str(country[0])
        form.country.choices += [(data, data)]
    if request.method == "POST":
        if form.submit1:
            form.validate_on_submit()
            delete_records_in_twitter_trends()
            field_data = form.country.data
            retrieve_data(field_data)
        elif form.submit2:
            form.validate_on_submit()
            fetch_data = fetch_data
    return render_template("twitter-api.html", form=form, fetch_data=fetch_data, title="Twitter-API")
