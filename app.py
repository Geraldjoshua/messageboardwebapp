#!flask/bin/python
#a very simple webapp implemented using flask


from flask import Flask, redirect, render_template, request,url_for    #loading the Flask framework 

app = Flask(__name__)      # creates a flask application to run my code

#handle view and send data
@app.route('/',methods=["GET","POST"])        #defines what happens when a person wants to go to locate "/" of the site



def index():
	if request.method =="GET":
		return render_template("main_page.html", comments=comments)
    
	comments.append(request.form["contents"])
	return redirect(url_for('index'))
	
@app.route("/login/")
def login():
	return render_template("login_page.html")
    
comments= []
if __name__ == '__main__':
    app.run(debug=True)