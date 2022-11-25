from flask import Flask


app = Flask(__name__)
app.secret_key = b'\xf8d\xbc\x02\xb0:a\xac\xf4Y\xac\x84\xe7N\x1dX'


#routes
from user import routes
