from db.dao import UserDAO, AuthDAO
from email.utils import parseaddr
import bcrypt
import json
import re

def get_user(email):
	# TODO: make use of user token
	try:
		usr = UserDAO.get_user_by_email(email)
		return usr.to_json()
	except:
		print("Failed to get user with email {}.".format(email))
		return None

def valid_pword(pword):
	return re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', pword)

def create_user(first_name, last_name, email, password):
	if parseaddr(email)[1] == "":
		print("Failed to create user: malformed email.")
		return 400
	if UserDAO.get_user_by_email(email) is not None:
		print("User already exists.")
		return 400
	if not valid_pword(password):
		print("Failed to create user: shitty password.")
		return 400
	UserDAO.insert_user(first_name, last_name, email)
	id_ = UserDAO.get_user_by_email(email).id
	hash_ = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
	AuthDAO.insert_hash(id_, hash_)
	return 201

def validate_user(email, password):
	usr = UserDAO.get_user_by_email(email)
	hash_ = AuthDAO.get_hash(usr.id)
	if usr is None:
		print("No such user exists.")
		return (404, None)
	if bcrypt.checkpw(password.encode('utf-8'), hash_):
		# TODO: create user token
		return (200, "token")
	return (401, None)
