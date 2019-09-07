from flask import Flask, Response
from flask.ext.restful import Api, Resource
from flask_cors import CORS
from course import CreateCourse, TeacherCourseList, StudentCourseList
from login import Login
from dbop import Mysql

application = app = Flask(__name__)
# app.response_class = MyResponse
api = Api(app)
CORS(app, origins='*', allow_headers='*')

# Database Connector Pool Initialize
db = Mysql()

api.add_resource(CreateCourse, '/createCourse', endpoint="createCourse")
api.add_resource(TeacherCourseList, '/teacherCourseList')
api.add_resource(StudentCourseList, '/studentCourseList')
api.add_resource(Login, '/login')

if __name__ == '__main__':
    app.run(debug=True)
