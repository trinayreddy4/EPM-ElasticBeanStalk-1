from flask import Flask

application = Flask(__name__)

@application.route("/")
def index():
    return "Hello from meqw5pg3 Elastic Beanstalk CI-CD verification-2026102014102224610"