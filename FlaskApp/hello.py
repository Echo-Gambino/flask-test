from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route("/")
def index():
    return "Flask App!"

@app.route("/hello/<string:Sname>/")
def hello(Sname):
    return render_template('test.html', name=Sname)

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

