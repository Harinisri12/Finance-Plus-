import mysql.connector
mydb= mysql.connector.connect(host="localhost",user="root",passwd="manager",database="quiz_comp")
mycursor= mydb.cursor()
mycursor.execute("create table participants(regno int(5) primary key, pname varchar(30),age_group int(2),city varchar(20),no_of_appearances_made int(20))")