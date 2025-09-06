from flask import Flask, request, url_for, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route("/")
def main():
    return render_template('home.html', current_time=datetime.utcnow())

@app.route("/user/<user_name>/<pt>/<institution>")
def user(user_name, pt, institution):
    return render_template('user.html', user_name=user_name, pt=pt, institution=institution)

@app.route("/user/<user_name>")
def contexto(user_name):
    user_agent = request.headers.get("User-Agent", "desconhecido")
    remote_ip = request.remote_addr or "desconhecido"
    host = request.host or "desconhecido"
    return render_template(
        "contexto.html",
        user_name=user_name,
        user_agent=user_agent,
        remote_ip=remote_ip,
        host=host,
    )

@app.errorhandler(404)
def not_found(e):
    return render_template('not_found.html'), 404

if __name__ == "__main__":
    app.run(debug=True)