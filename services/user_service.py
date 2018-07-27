from db.dao import UserDAO, AuthDAO
from tokens.tokens import create_user_token
from email.utils import parseaddr
from tokens.tokens import create_user_token, get_id_from_token
import bcrypt
import json
import re

def get_user(email):
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
		return (200, create_user_token(usr.id, usr.is_admin))
	return (401, None)

def get_posts(id_):
	posts = UserDAO.get_posts(id_)
	return json.dumps([post.to_json for post in posts])
