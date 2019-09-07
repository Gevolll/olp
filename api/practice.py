# -*- coding: utf-8 -*-
from flask import request
from flask.ext.restful import Resource
from uuid import uuid4
from app import db
import snowflake.client

# -*- API LIST -*-

# GET /api/teacherPracticeList {userId}
# GET /api/studentPracticeList {userId}
# POST /api/createPractice {}

def get_id():
    return snowflake.client.get_guid()

class TeacherPracticeList(Resource):
    def get(self):
        userId = request.args.get("userId")

        practiceCount = db.getOne(
            """
            select practice_count from User where user_id=%s;
            """,
            (userId,)
        )['practice_count']

        if practiceCount <= 5:
            page = 0
            res = db.getAll(
                """
                select * from Practice where teacher_id=%s;
                """,
                (userId,)
            )
        else:
            page = practiceCount/5+1 if practice%5 else practiceCount/5
            res = db.getSome(
                """
                select * from Practice where teacher_id=%s;
                """, 5, (userId,)
            )

        respData = {
            "state": "success",
            "count": practiceCount if practiceCount<5 else 5,
            "page": page,
            "detail": res
        }

        return respData

class StudentPracticeList(Resource):
    def get(self):
        userId = request.args.get("userId")

        practiceCount = db.getOne(
            """
            select practice_count from User where user_id=%s;
            """, (userId,)
        )['practice_count']

        if practiceCount < 5:
            page = 0
            res = db.getAll(
                """
                select * from StudentPractice where student_id=%s;
                """, (userId,)
            )
        else:
            page = practiceCount/5+1 if practiceCount%5 else practiceCount/5
            res = db.getSome(
                """
                select * from StudentPractice where student_id=%s;
                """, 5, (userId,)
            )

        respData = {
            "state": "success",
            "count": practiceCount if practiceCount<5 else 5,
            "page": page,
            "detail": res
        }

        return respData

class CreatePractice(Resource):
    def post(self):
        data = request.get_json() or request.form
        userId = data['userId']
        title = data['title']
        problemList = data['problems']
        relation = data['relation']
        topicId = data['topicId']
        sectionId = data['sectionId']
        courseId = data['courseId']

        practiceId = get_id()

        db.insertOne(
            """
            insert into Practice (practice_id, title, teacher_id, relation, topic_id, section_id, course_id)
            values (%s, %s, %s, %s, %s, %s, %s);
            """, (practiceId, title, userId, relation, topicId, sectionId, courseId)
        )

        position = 0

        for eachp in problemList:
            problemId = get_id()

            content = eachp['content']
            choices = eachp['choices']
            answer = eachp['answer']

            db.insertOne(
                """
                insert into Problem (problem_id, position, content, choices, answer, practice_id)
                values (%s, %s, %s, %s, %s, %s);
                """, (problemId, position, content, choices, answer, practiceId)
            )

            position += 1

        studentList = db.getAll(
            """
            select student_id from StudnetCourse where course_id=%s;
            """, (courseId)
        )

        for each in studentList:
            db.insertOne(
                """
                insert into StudentPractice (student_id, practice_id, status)
                values (%s, %s, %s);
                """, (each['student_id'], practiceId, 0)
            )
            db.modify(
                """
                update User set practice_count=practice_count+1 where user_id=%s;
                """, (each['student_id'],)
            )

        return {
            "state": "success"
        }

class FetchProblems(Resource):
    def get(self):
        practiceId = data['practiceId']
        userId = data['userId']

        draft = db.getOne(
            """
            select * from StudentPractice where student_id=%s and practice_id=%s;
            """, (userId, practiceId)
        )

        problemSet = db.getAll(
            """
            select * from Problem where practice_id=%s;
            """, (practiceId,)
        )

        respData = {
            "state": "success",
            "problemSet": problemSet,
            "draft": draft
        }

        return respData

class UploadPractice(Resource):
    def post(self):
        data = request.get_json() or request.form
        userId = data['userId']
        detail = data['detail']
        duration = data['duration']

        correctCount = 0

        for each in detail:
            problemId = each['problemId']
            answer = each['answer']

            correctAnswer = db.getOne(
                """
                select answer from Problem where problem_id=%s;
                """, (problemId,)
            )

            if answer == correctAnswer:
                each['status'] = True
                correctCount += 1
            else:
                each['status'] = False

            each['correctAnswer'] = correctAnswer

        db.modify(
            """
            update StudentPractice set status=%s, draft=%s, score=%s, duration=%s where student_id=%s and practice_id=%s;
            """, (2, detail, correctCount, duration, userId, practiceId)
        )

        respData = {
            "state": "success",
            "detail": detail,
            "score": correctCount
        }

        return respData

class SavePracticeDraft(Resource):
    def post(self):
        data = request.get_json() or request.form
        userId = data['userId']
        detail = data['detail']
        duration = data['duration']

        db.modify(
            """
            update StudentPractice set status=%s, draft=%s, duration=%s where student_id=%s and practice_id=%s;
            """, (1, detail, duration, student_id, practice_id=%s)
        )

        respData = {
            "state": "success",
            "detail": detail
        }
