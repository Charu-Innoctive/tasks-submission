#importing necessary libraries
from flask import jsonify,Flask, request
from flask_restful import Resource,Api
from sqlalchemy import create_engine

#Setting up the flask
app = Flask(__name__) #creating instance of the flask class
app.debug=True

#database configuration
DATABASE_HOSTNAME='localhost'
DATABASE_USERNAME='root'
DATABASE_PASSWORD='#Giveyourbest02'
DATABASE_NAME='cargoFL'


#Creating database engine
app._engine = create_engine('mysql://'+ DATABASE_USERNAME +':'+ DATABASE_PASSWORD +'@'+ DATABASE_HOSTNAME +'/'+ DATABASE_NAME + '?charset=latin1',echo=False,pool_size=50,max_overflow=16,pool_recycle=300)

#Creating an end point for inserting the records
@app.route('/update_records', methods=['PUT']) #here route is a decorator, using it to tell flask what url should trigger the method, be default its get.
def insert_records():
    try:
        #update the request data
        request_data=request.get_json()
        #sql query for user_master
        sql_query="update user_master set `contact_number`={contact_number} where id={id}".format(id = request_data['id'],contact_number= request_data['contact_number'])
        result_user = app._engine.execute(sql_query)
        return "Updated Successfully"

    except Exception as e:
        print(str(e))
        return jsonify({"message": "Failed to insert records","status": False})

if __name__=="__main__": #__name__ is a special var (it takes values of script name), it makes sure that it is executed in the main gile not whbe other filescall it
    app.run(port=5000)

    