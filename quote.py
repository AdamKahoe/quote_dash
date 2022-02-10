from flask_app.config.mysqlconnection import connectToMySQL

db_name='quote_dash'

# [
# {'id': 2, 'user_id': 1, 'author': 'drew', 'content': 'take your first exam attempt early', 'created_at': datetime.datetime(2022, 2, 8, 20, 35, 26), 'updated_at': datetime.datetime(2022, 2, 8, 20, 35, 26), 'users.id': 1, 'first_name': 'drew', 'last_name': 'adorno', 'email': 'drew@gmail.com', 'password': 'password', 'users.created_at': datetime.datetime(2022, 2, 8, 20, 35, 12), 'users.updated_at': datetime.datetime(2022, 2, 8, 20, 35, 12)},

#  {'id': 3, 'user_id': 1, 'author': 'drew', 'content': 'password is not a good password', 'created_at': datetime.datetime(2022, 2, 8, 20, 36, 24), 'updated_at': datetime.datetime(2022, 2, 8, 20, 36, 24), 'users.id': 1, 'first_name': 'drew', 'last_name': 'adorno', 'email': 'drew@gmail.com', 'password': 'password', 'users.created_at': datetime.datetime(2022, 2, 8, 20, 35, 12), 'users.updated_at': datetime.datetime(2022, 2, 8, 20, 35, 12)}]

class Quote:
    def __init__(self, data):
        self.id=data['id']
        self.author=data['author']
        self.content=data['content']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

        self.poster_first_name=data['first_name']
        self.poster_last_name=data['last_name']
        self.poster_id=data['users.id']

    @classmethod
    def get_all_with_users(cls):
        query='''
        SELECT * from quotes 
        join users on users.id = quotes.user_id
        '''
        results=connectToMySQL(db_name).query_db(query)
        
        quotes=[]
        for row in results:
            quotes.append(cls(row))
        return quotes

    @classmethod
    def save():
        pass