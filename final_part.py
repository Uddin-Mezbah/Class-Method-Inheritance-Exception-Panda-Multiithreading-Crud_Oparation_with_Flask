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

@app.route('/update', methods=['PUT'])
def update():
    for student in students:
        if student.get('id') == request.get_json().get('id'):
            print("yes")
            student.update(request.get_json())
    return 'Student updated succesfully'

@app.route('/delete',methods=['DELETE'])
def delete():
    for i in range(len(students)):
        if students[i].get('id') == request.args.get('id'):
            del students[i]
            break
    return "student delete succesfully"

app.run(debug=True)












