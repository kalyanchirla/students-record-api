from flask import Flask, request
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)

class StudentRecordsModel(db.Model):
    student_id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(16),nullable=False)
    gender = db.Column(db.String(8),nullable=True)
    course = db.Column(db.String(6),nullable=False)
    major = db.Column(db.String(30),nullable=False)
    grade = db.Column(db.String(12),nullable=False)
    
    def __repr__(self):
        return f'StudentRecord(name={name},gender={gender},course={course},major={major},grade={grade})'
#db.create_all()

student_put_data = reqparse.RequestParser()
student_put_data.add_argument("name",type=str,help="Name of the student",required=True)
student_put_data.add_argument("gender",type=str,help="Gender of the student")
student_put_data.add_argument("course",type=str,help="Course of the student",required=True)
student_put_data.add_argument("major",type=str,help="Major",required=True)
student_put_data.add_argument("grade",type=str,help="Grade achieved by the student",required=True)

resource_fields = {
    'student_id': fields.Integer,
    'name': fields.String,
    'gender': fields.String,
    'course': fields.String,
    'major': fields.String,
    'grade': fields.String
}

class StudentRecord(Resource):
    @marshal_with(resource_fields)
    def get(self,student_id):
        #print(student_id)
        result = session.query(db.id).filter(db.name=='Kalyan').first()
        #print(f'Name: {result.name}, Gender: {result.gender}, Course: {result.course}')
        print(result)
        return result

    @marshal_with(resource_fields)
    def put(self, student_id):
        args = student_put_data.parse_args()
        student_data = StudentRecordsModel(student_id=student_id,name=args['name'],gender=args['gender'],course=args['course'],major=args['major'],grade=args['grade'])
        db.session.add(student_data)
        db.session.commit()
        return student_data, 201

    #def delete(self,student_id):
        
api.add_resource(StudentRecord,"/info/<int:student_id>")

if __name__ == "__main__":
    app.run()