from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint

app = Flask(__name__)

@app.route("/")
def index():
    return "Flask App!"

"""
@app.route("/hello/<string:name>/")
def hello(name):
    return render_template('test.html', name=name)
"""

@app.route("/hello/<string:name>")
def hello(name):
    quotes = [ 
            "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
            "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
            "'To understand recursion you must first understand recursion..' -- Unknown",
            "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
            "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
            "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"
            ]

    randomNumber = randint(0, len(quotes)-1);
    quote = quotes[randomNumber] # </string:name></string:name>

    return render_template(
            'test.html', **locals())

if __name__ == "__main__":
    #app.run()

    # This allows this flaskapp to be viewed and interacted with on
    # http://127.x.x.x/...
    # port=80 is the default HTTP port
    # host='0.0.0.0' is a non-routable meta-address used to designate an invalid, unknown, or non-applicable target.
    # IMPORTANT: '0.0.0.0' means different things depending if the server or client is using it.
    # As a host address: Is a way to specify "any IPv4 address at all", 0.0.0.0 can mean all IPv4 addresses on the local machine.
    # Routing: Could represent the default route as a destination subnet... That the gateway to reach its destination is unspecified. Could mean that no additional routing is needed as the system is directly connected to the destination.
    #
    ##########
    #
    # Hypothesis:
    # I think that this may just mean that the app runs on "any IPv4 address at all" on port 80, the default HTTP port.

    app.run(host='0.0.0.0', port=80)
    pass

