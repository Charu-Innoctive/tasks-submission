#importing necessary libraries
from flask import jsonify,Flask, request,render_template
from flask_restful import Resource,Api
from sqlalchemy import create_engine
from flask_cors import CORS

#Setting up the flask
app = Flask(__name__) #creating instance of the flask class
app.debug=True

DATABASE_HOSTNAME='localhost'
DATABASE_USERNAME='root'
DATABASE_PASSWORD='#Giveyourbest02'
DATABASE_NAME='cargoFL'


#Creating database engine
app._engine = create_engine('mysql://'+ DATABASE_USERNAME +':'+ DATABASE_PASSWORD +'@'+ DATABASE_HOSTNAME +'/'+ DATABASE_NAME + '?charset=latin1',echo=False,pool_size=50,max_overflow=16,pool_recycle=300)


@app.route('/')
def index():
    return render_template("retrieve_dynamically.html")
#Creating an end point for inserting the records

@app.route('/retrieve_records', methods=['GET']) #here route is a decorator, using it to tell flask what url should trigger the method, be default its get.
def get_data():
    try:
        user_list=[]
        request_data=request.get_json()
        #sql query to retrieve the records
        sql_query="select * from user_master limit {offset}, {limit}".format(offset=request_data['offset'],limit=request_data['limit'])
        result_user=app._engine.execute(sql_query)
        if result_user.rowcount>0:
            for row in result_user:
                user_list.append(dict(row.items()))
            print(user_list)
            return jsonify({"rows" : user_list})
            # jsonify({"message":"Successfully retrived data","status":True,"data":user_list})  
        else:
            return jsonify(user_list)
        
    except Exception as e:
        print(e)

#Creating an end point for inserting the records
@app.route('/retrieve_records_ajax', methods=['GET']) #here route is a decorator, using it to tell flask what url should trigger the method, be default its get.
def get_data_ajax():
    try:
        user_list=[]
        limit = request.args.get('limit')
        offset = request.args.get('offset')
        #sql query to retrieve the records
        #select count(rows) from user_master; 
        sql_total = "select count(*) as total from user_master"
        toal_result = app._engine.execute(sql_total)
        total = toal_result.fetchone()['total']
        sql_query="select * from user_master limit {offset}, {limit}".format(offset=offset,limit=limit)
        result_user=app._engine.execute(sql_query)
        if result_user.rowcount>0:
            for row in result_user:
                user_list.append(dict(row.items()))
            # print(user_list)
            return jsonify({"rows" : user_list,"total":total,"totalNotFiltered":len(user_list)}) 
        else:
            return jsonify(user_list)
    except Exception as e:
        print(e)
@app.route('/delete', methods=['POST'])
def delete_record():
    # response={"status"}
    data = request.get_json()
    # print(data)
    for getid in data["checkdelete"]:
         del_query=('DELETE FROM user_master WHERE id = {0}'.format(getid))
         res_after_delete=app._engine.execute(del_query)     
    return jsonify('Records deleted successfully')

if __name__=="__main__": #__name__ is a special var (it takes values of script name), it makes sure that it is executed in the main gile not whbe other filescall it
    app.run(port=10000)