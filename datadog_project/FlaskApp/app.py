from flask import Flask
from flask import render_template
import os
from datadog import initialize, statsd

options = {
    'api_key':'THIS_IS_API_KEY',
    'app_key':'THIS_IS_APP_KEY'
}

initialize(**options)
template_dir = os.path.abspath('/vagrant/FlaskApp')
app = Flask(__name__, template_folder=template_dir)

@app.route("/")
@app.route("/Home.html")
def home():
    statsd.increment("datadog_demo.home")
    return render_template('Home.html')

@app.route("/Career.html")
def career():
    statsd.increment("datadog_demo.career")
    return render_template('Career.html')

@app.route("/Contact.html")
def contact():
    statsd.increment("datadog_demo.contact")
    return render_template('Contact.html')

if __name__ == "__main__":
    app.run(host='192.168.33.10', port=5000, debug=True)
