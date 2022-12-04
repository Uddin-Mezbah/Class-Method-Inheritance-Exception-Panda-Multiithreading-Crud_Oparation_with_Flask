from flask import Flask,jsonify,request

app = Flask(__name__)

students = [{'id':1,'name': 'rain'},{'id':2,'name': 'karim'}]

@app.route('/')
def home():
    # return "Welcome home"
    return jsonify(students)

@app.route('/add',methods=['POST'])
def add():
    students.append(request.get_json())
    print(request.get_json())
    return "Student added succesfully.",200

@app.route('/update',methods=['GET','PUT'])
def update():
    for student in students:
        if str(student.get('id')) == request.get_json().get('id'):
        # if str(student.get('id')) == request.get_json().get('id'):
            student.update(request.get_json())

    return "student updated succesfully"

@app.route('/delete',methods=['GET','DELETE'])
def delete():
    for i in range(len(students)):
        if str(students[i].get('id')) == request.args.get('id'):
            del students[i]
            break
    return "student delete succesfully"

app.run(debug=True)