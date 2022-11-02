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
@app.route('/insert_records', methods=['POST']) #here route is a decorator, using it to tell flask what url should trigger the method, be default its get.
def insert_records():
    try:
        #get the request data
        request_data=request.get_json()
        #sql query for user_master
        # sql_query="insert into user_master (id, name,contact_number,email_id,blood_group,city_id,added_date) values('{id}', '{name}','{contact_number}','{email_id}','{blood_group}','{city_id}','{added_date}')".format(id = request_data['id'],name = request_data['name'],contact_number= request_data['contact_number'],email_id = request_data['email_id'],blood_group = request_data['blood_group'],city_id = request_data['city_id'],added_date = request_data['added_date'])
        # result_user = app._engine.execute(sql_query)

        #sql query for city_master
        sql_query2="insert into city_master (id,city_name,city_state,added_date) values('{id}','{city_name}','{city_state}','{added_date}')".format(id = request_data['id'],city_name = request_data['city_name'],city_state= request_data['city_state'],added_date = request_data['added_date'])
        result_user2 = app._engine.execute(sql_query2)
        return "Inserted Success"

    except Exception as e:
        print(str(e))
        return jsonify({"message": "Failed to insert records","status": False})

if __name__=="__main__": #__name__ is a special var (it takes values of script name), it makes sure that it is executed in the main gile not whbe other filescall it
    app.run(port=5000)

    