#To keep on checking in into the performance of your neural net
#Start up a flask server that that pipes everything from stdout to
#a webpage

import html
import sys
from subprocess import Popen, PIPE, STDOUT, DEVNULL
from textwrap import dedent

from flask import Flask, Response # $ pip install flask

app = Flask(__name__)

@app.route('/')
def index():
    def g():
        yield "<!doctype html><title>Neural network on Driver Telemetry logs </title>"

        command = ["python","convnet.py"]
        with subprocess.Popen(command, shell=True, stdin=DEVNULL, stdout=subprocess.PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True) as p:
            for line in p.stdout:
                yield "<code>{}</code>".format(html.escape(line.rstrip("\n")))
                yield "<br>\n"
    return Response(g(), mimetype='text/html')

if __name__ == "__main__":
    import webbrowser
    webbrowser.open('http://localhost:23423') # show the page in browser
    app.run(host='localhost', port=23423, debug=True) # run the server

