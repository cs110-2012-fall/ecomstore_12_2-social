##Our full django project, with front code in template folder

In order to run the project, please install **django1.4** and **python** first. Also you need a **Mysql database**
running on your local computer.

After setting up all the previous requirement and tested they are working properly.

Please follow below instructions:
* create data table in Mysql, Create a new MySQL user with password(**Don't change username, we use admin for entire team**), Grant the new MySQL user permissions to manipulate the database
* Using terminal, first login mysql command-line then
* mysql> CREATE DATABASE ecomstore CHARACTER SET utf8;
Query OK, 1 row affected(0.00 sec)

mysql> CREATE USER 'admin'@'localhost' IDENTIFIED BY '123456';
Query OK, 0 rows affected(0.00 sec)

mysql> GRANT ALL ON ecomstore.* TO 'admin'@'localhost';
Query OK, 0 rows affected (0.00sec)

* Then using terminal go to the ecomstore's root folder, make sure that manage.py is in your current path
type **python manage.py validate**
* If no errors comes up then type **python manage.py sqlall catalog**
* If no errors comes up then type **python manage.py syncdb**
* If no errors comes up then start the development server by **python manage.py runserver** (linux or mac user may need sudo)
###Fire up browser and type localhost:8000/catalog and localhost:8000/admin to see whether running properly

**Shopping cart module finished**
