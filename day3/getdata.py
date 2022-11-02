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
@app.route('/view_records', methods=['GET']) #here route is a decorator, using it to tell flask what url should trigger the method, be default its get.
def get_data():
    try:
        user_list=[]
        #sql query to retrieve the records
        sql_query="select * from city_master"
        sql_query2="select * from user_master"
        result_user=app._engine.execute(sql_query)
        result_user2=app._engine.execute(sql_query2)
        if result_user.rowcount>0:
            for row in result_user:
                user_list.append(dict(row.items()))
            return jsonify({"message":"Successfully retrived data","status":True,"data":user_list})  
        else:
            return jsonify({"message":"No records were found","status":True})
        
    except Exception as e:
        print(e)
if __name__=="__main__": #__name__ is a special var (it takes values of script name), it makes sure that it is executed in the main gile not whbe other filescall it
    app.run(port=5000)
