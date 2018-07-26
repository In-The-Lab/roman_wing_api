# Setting up the database environment

## Getting mySQL installed

In order to get this stuff up and running, you need to have mySQL set up on your computer. If you don't have that set up, here's how you do that:

Install mySQL here: https://dev.mysql.com/downloads/mysql/ (you want to choose the DMG archive)

Once that's downloaded, follow the installation instructions. Be sure to set a password you remember.

Once that's done, type in the following commands:

`echo 'export PATH=/usr/local/mysql/bin:$PATH' >> ~/.bash_profile`

`. ~/.bash_profile`

You should be all set up with mySQL now. Just to test the installation, type in `mysql -u root -p`, press enter, type in your password, press enter, and you should be met with the mySQL console. To exit, just type in `\q` and press enter. 

## Creating the actual database

Go to the command line, type in `mysql -u root -p`, and type in your database password.

Execute the following command: `CREATE DATABASE romanwing;`, and you should have the database all created. Great! Now, type in `\q` to exit.

## Putting your credentials somewhere

In this folder, create a file called `config.ini`. Don't worry, as long as you don't fuck with the .gitignore file, your config file won't show up on github. Okay? Okay.

The contents of your config.ini file should look something like this:

```
user='root'
database='romanwing'
password='<YOUR_DATABASE_PASSWORD>'
```