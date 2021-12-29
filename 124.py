from flask import Flask,jsonify,request
app=Flask(__name__)
#creating the array of task wich tasks has a diffrent obj
tasks=[
    {
        'id':1,
        'title':'Buy Groceries',
        'description':'milk,pizza',
        'done':False
    },
    {
        'id':2,
        'title':'Study',
        'description':'Coding,coding projects',
        'done':False
    }
]
#giving route to our application(Converting it from get to post )
@app.route('/add-data',methods=["POST"])
def add_task ():
    if not request.json:
        return jsonify({
            "status":'error',
            "message":'PLEASE PROVIDE THE DATA'
        },400)
    task={
        'id':tasks[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get['description'," "],
        'done':False
    }
    tasks.append(task)
    return jsonify ({
        'status':'success',
        'message':'task added succussesfully'
    })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })
if (__name__=='__main__'):
    app.run(debug=True)
