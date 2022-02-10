from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app import app
bcrypt=Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.password=data['password']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

        self.quotes=[]

    @staticmethod
    def validate_user(user):
        is_valid=True
        if len(user['first_name']) < 2:
            is_valid=False
            flash('First Name must be at least 2 characters')
        if len(user['last_name']) < 2:
            is_valid=False
            flash('Last Name must be at least 2 characters')
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid=False
        elif User.get_by_email(user['email']):
            flash('Email already exists')
            is_valid = False
        if len(user['password'])< 8:
            is_valid=False
            flash('Password must be at least 8 characters')
        if user['password'] != user['confirm_pw']:
            is_valid=False
            flash('Password and confirm password must match')
        return is_valid

    @classmethod
    def get_by_email(cls, email):
        query='select * from users where email = %(email)s'
        data={
            'email':email
        }
        result=connectToMySQL('log_reg').query_db(query, data)
        if result:
            return cls(result[0])
        else:
            return False

    @classmethod
    def get_by_id(cls, id):
        query='select * from users where id = %(id)s'
        data={
            'id':id
        }
        result=connectToMySQL('log_reg').query_db(query, data)
        if result:
            return cls(result[0])
        else:
            return False

    @classmethod
    def save(cls,data):
        query="""
            INSERT INTO users (first_name, last_name, email, password)
            VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s)
        """
        return connectToMySQL('log_reg').query_db(query, data)
    
    @classmethod
    def authenticate_user(cls,email, password):
        user=User.get_by_email(email)
        if user:
            if bcrypt.check_password_hash(user.password, password):
                return user
        flash('Invalid Email/Password combination')
        return False
        