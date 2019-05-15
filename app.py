#!flask/bin/python
#a very simple webapp implemented using flask


from flask import Flask   #loading the Flask framework 

app = Flask(__name__)      # creates a flask application to run my code

@app.route('/')        #defines what happens when a person wants to go to locate "/" of the site


def index():
    return "Hello, dudes!"
    

if __name__ == '__main__':
    app.run(debug=True)