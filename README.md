# HIT4002022
HIT 400 2021-2022

This branch has the 2 projects needed to run the gate system. 
An additional application XAMPP will be required to run the DB
and the webapp (.war file)

# The ALPR-system
- Which is a python project
- It is responsible for the detection of a license plates from the video feed provided using a video link 
- sending the results as a json to the api 

### How to use:
- The requirements for the project are stated in the requirements.txt file
  - There must be fulfilled first before running the project
    - `Python 3.6.8` is recommended 
    - Failure to do so will result in errors when running the project
- to run it enter the url of link to the video on line 73 of the test.py file
- execute the following command to run it
`pathToPython.exe file test.py`

# VI-Core-System
- It is a maven project written in:
  - java for the logic 
  - html for the web view 
  - build output put id a war file 
- This project is responsible for managing:
  - the repository (The Database)
  - web view
  - managing requests and responses that are sent 

### How to use
- As it is a maven project to build it or build a war file:
  - first clean the project 
  - second compile the project 
  - third build the project
- The output will be a .war file


# XAMPP
- start the xampp app
- start apache
- start mysql
- start tomcat
### mysql
- open mysql admin
- create database called `gatesystem`
- tables will be updated when 
### 
- out the war file into the webapps folder under tomcat 
- go to http://localhost:8080/vicore/login