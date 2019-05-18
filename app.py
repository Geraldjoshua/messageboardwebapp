#!flask/bin/python
#a very simple webapp implemented using flask

import os
from flask import Flask, redirect, render_template, request,url_for ,session,flash   #loading the Flask framework 
from flask_sqlalchemy import SQLAlchemy 
from flask_login import current_user, login_user, LoginManager, UserMixin, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime


app = Flask(__name__)      # creates a flask application to run my code


project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "postdatabase.db"))
# SQLALCHEMY_DATABASE_URI = "mysql//{username}:{password}@{hostname}/{databasename}".format(
    # username="firstdb",
    # password="messageboard1",
    # hostname="localhost:5000",
    # databasename="firstdb$posts",
# )
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
app.secret_key = "butterchicken"
login_manager = LoginManager()
login_manager.init_app(app)







#handle view and send data
@app.route('/',methods=["GET","POST"])        #defines what happens when a person wants to go to locate "/" of the site

def index():
	
	if request.method =="GET":
		return render_template("main_page.html", error=False)
	if not current_user.is_authenticated:
		return redirect(url_for('index'))
	if request.form["password"]=="flask":
		return redirect (url_for('group1'))
	if request.form["password"]=="python":
		return redirect (url_for('group2'))
	if request.form["password"]=="angular":
		return redirect (url_for('group3'))
		
	return render_template("main_page.html",error=True) 
    
	#comments.append(request.form["contents"])
	return redirect(url_for('group1'))

@app.route("/group1/",methods=["GET","POST"])        #defines what happens when a person wants to go to locate "/" of the site
def group1():
	if request.method=="GET":
		return render_template("group1.html",comments=Comment.query.all())
	if request.method == 'POST':
		if "btn_success" in request.form:
			return redirect(url_for("index"))
		else:
			comment = Comment(content=request.form["contents"],commenter=current_user)
			db.session.add(comment)
			db.session.commit()
			return redirect(url_for("group1"))
	
	
	
@app.route("/group2/",methods=["GET","POST"])        #defines what happens when a person wants to go to locate "/" of the site
def group2():
	if request.method=="GET":
		return render_template("group2.html",comments=Comment2.query.all())
	if request.method == 'POST':
		if "btn_succes" in request.form:
			return redirect(url_for("index"))
		else:
			comment = Comment2(content=request.form["contents"],commenter=current_user)
			db.session.add(comment)
			db.session.commit()
			return redirect(url_for("group2"))
	
@app.route("/group3/",methods=["GET","POST"])        #defines what happens when a person wants to go to locate "/" of the site
def group3():
	if request.method=="GET":
		return render_template("group3.html",comments=Comment3.query.all())
	if request.method == 'POST':
		if "btn_succe" in request.form:
			return redirect(url_for("index"))
		else:
			comment = Comment3(content=request.form["contents"],commenter=current_user)
			db.session.add(comment)
			db.session.commit()
			return redirect(url_for("group3"))
	

		

	
@app.route("/login/", methods=["GET","POST"])
def login():
	if request.method =="GET":
		return render_template("login_page.html", error=False)
		
	user = load_user(request.form["username"])
	if user is None:
		return render_template("login_page.html", error=True)
	
	if not user.check_password(request.form["password"]):
		return render_template("login_page.html",error=True)
		
	login_user(user)
	
	return redirect (url_for('index'))
	
@app.route("/logout/")
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))
	
class User(UserMixin,db.Model):
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(128))
	password_hash = db.Column(db.String(128))
	
	def check_password(self,password):
		return check_password_hash(self.password_hash, password)
		
	def get_id(self):
		return self.username
        

		
#for now
#all_users = {"admin": User("admin",generate_password_hash("secret")),"bob": User("bob", generate_password_hash("less-secret")),"caroline": User("caroline", generate_password_hash("completely-secret"))}

@login_manager.user_loader
def load_user(user_id):
	return User.query.filter_by(username=user_id).first()


class Comment(db.Model):
	__tablename__ = "comments"
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(4096))
	posted = db.Column(db.DateTime, default=datetime.now)
	upvote = db.Column(db.Integer)
	downvote = db.Column(db.Integer)
	commenter_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=True)
	commenter = db.relationship('User', foreign_keys=commenter_id)
	
class Comment2(db.Model):
	__tablename__ = "comments2"
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(4096))
	posted = db.Column(db.DateTime, default=datetime.now)
	upvote = db.Column(db.Integer)
	downvote = db.Column(db.Integer)
	commenter_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=True)
	commenter = db.relationship('User', foreign_keys=commenter_id)

class Comment3(db.Model):
	__tablename__ = "comments3"
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(4096))
	posted = db.Column(db.DateTime, default=datetime.now)
	upvote = db.Column(db.Integer)
	downvote = db.Column(db.Integer)
	commenter_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=True)
	commenter = db.relationship('User', foreign_keys=commenter_id)


#class Vote(db.Model)

	
    
#comments= []
if __name__ == '__main__':
    app.run(debug=True)