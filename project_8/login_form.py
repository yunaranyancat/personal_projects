#!/usr/bin/python3

import cgi
import time
from selenium import webdriver
from selenium.common.keys import Keys

localhost = '127.0.0.1'

# driver = webdriver.Firefox()
# driver.get(localhost)

print("Content-type:text/html\r\n\r\n")
print("<html><head>")
print("<title> Login Page </title>")

#some style
print("""<style>
  .login{
    display: inline-block;
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    width: 200px;
    height: 250px;
    margin: auto;
    background-color:  #05f9d8 ;
    border-radius:25px;
    border-style: solid;
  }

  .btn-style{
    height:40px;
    border : solid 2px #ffffff;
    border-radius : 20px;
    font-size : 20px;
    color : #ffffff;
    padding : 0px 20px;
    background-color : black ;
    width : 100%;
  }

  .inputstyle{
    width:100%;
  }
</style>""")

print("</head><body>")

list_of_data = [[]]

form = cgi.FieldStorage()

if form.getvalue("name"):
    name = form.getvalue("name")
    #print(name)
if form.getvalue("password"):
    password = form.getvalue("password")
    #print(password)

list_of_data.append([name,password])

print(list_of_data)
#time.sleep(3)
#driver.refresh()

print("""
<div class='login'>
    <form method='post' action='login_form.py'>
""")

print("<p> Username  : <input class='inputstyle' type='text' name='name' /> </p>")
print("<p> Password  : <input class='inputstyle' type='password' name='password' /> </p>")
print("<input class='btn-style' type='submit' name='submit' value='Log in'/>")

print("""
    </form>
</div>
</body>
</html>
""")
