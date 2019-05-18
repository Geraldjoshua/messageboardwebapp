# messageboardwebpage #
first attempt on creating a meassageboard web page using python.
## messageboard web page build using python, flask with a database ##

* How to run it:
  * download the whole repository open it and run python app.py(if in windows) or ./app.py in ubuntu.
  ***note: flask_Sqlalchemy should be installed, flask as a whole should be installed,pip as well.***
  * prerequisites:
    * python 2.7, flask and virtualenv
  * on the folder with app.py( open terminal and run app.py)
  * copy local host http://127.0.0.1:5000 and you will be fine. ***it only runs on this http***
  
## ***username and passwords*** ##
user          | password
------------- | -------------
gerald        | python
esther        | angular
joshua        | flask
jane          | sql
carol         | citiq

## ***group password to join*** ##
group         | password
------------- | -------------
group1        | flask
group2        | python
group3        | angular

* used flask to establish a python restAPI and used an sqlALchemy for my database
* used plain html instead of angular.io. (later on i would like to use angular to make my frontend pretty and add more features
* linked my html templates to flask and used a localhost:5000 to run my webpage.
* did not implemet the upvote and the downvote, i was not sure how and i ran out of time.(something i definitely want to implement later on as i build this page)
* did not finish other features such as seeing all users online, newsfeed and all groups plus if one wants to create a group.(something i will work on in the future.

## features that are yet to be added ##
* upvoting and downvoting a comment
* seeing all users online
* having a news feed and ability to create a group

## when user hasn't logged in ##
![whenuserhasnt logged in](https://user-images.githubusercontent.com/31729023/57971966-2fc46980-7995-11e9-87f8-7cb28e7995cb.PNG)

## login page ##
![loginpage](https://user-images.githubusercontent.com/31729023/57971977-508cbf00-7995-11e9-8efb-15d6e2d0edd2.PNG)

## when user has logged in ##
![whenuser has logged in](https://user-images.githubusercontent.com/31729023/57971936-d0fef000-7994-11e9-96cd-5850411f42f6.PNG)

## inside the group ##
![insideagroup](https://user-images.githubusercontent.com/31729023/57971985-6bf7ca00-7995-11e9-9b81-50ec7bc937be.PNG)
