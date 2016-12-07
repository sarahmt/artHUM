import os
from flask import Blueprint, Flask, render_template


app = Flask(__name__, static_url_path='')


#do not inculed in finished app
app.config["DEBUG"] = True


#error message
@app.errorhandler(404)
def page_not_found(error):
    return "Sorry, this page was not found."


#contact page
@app.route("/3")
def contact():
	return render_template("3.html")

#support page
@app.route("/1")
def support():
    return render_template("1.html")

#events page
@app.route("/4")
def community():
    return render_template("4.html")

#dossier page
@app.route("/dossier")
def dossier():
    return render_template("dossier.html")


#about page
@app.route("/2")
def about():
    return render_template("2.html")


#home page
@app.route("/")
def homegrid():
    return render_template("home.html")

@app.route("/<filename>")
def song(filename):
    return render_template('play.html',
                           title = filename,
                           music_file = filename)


if __name__ == "__main__":
	app.run(host="0.0.0.0")
