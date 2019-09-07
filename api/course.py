# -*- coding: utf-8 -*-

from flask import request
from flask.ext.restful import Resource
from uuid import uuid4
from app import db
import json
import snowflake.client

# -*- API LIST -*-

# POST /api/createCourse {userId, courseTitle, courseDescription, topicCount, topics{topicTitle}}
# PUT /api/editCourse {courseId, title, description}
# GET /api/envalidCourse {state, courseId}
# GET /api/teacherCourseList {userId, character}
# GET /api/studentCourseList {userId, character}
# POST /api/editTopic {courseId, title}
# PUT /api/editTopic {topicId, title}
# DELETE /api/editTopic {topicId}
# POST /api/editSection {userId, courseId, topicId, sectionTitle, entityType, entityId}
# PUT /api/editSection {userId, courseId, topicId, sectionTitle, entityType, entityId}
# DELETE /api/editSection {sectionId}
# POST /api/importStudent {importType, courseId, students{id:school_id}}
# GET /api/sectionList {userId, courseId}

def get_id():
    return snowflake.client.get_guid()

class CreateCourse(Resource):
    # 新建课程
    def post(self):
        """
            POST /api/createCourse
        """

        # Deal with request.data

        data = request.get_json() or request.form
        userId = data['userId']
        courseTitle = data['courseTitle']
        courseDescription = data['courseDescription']
        topicCount = data['topics']['count']
        topics = data['topics']['details']

        # Generate course_id
        courseId = get_id()
        respData = {}


        # SQL Statements
        db.insertOne(
            """
            insert into Course (course_id, title, description, teacher_id, is_valid)
            values
            (%s, %s, %s, %s, %s);
            """,
            (courseId, courseTitle, courseDescription, userId, 0)
        )
        res = db.getOne(
            """
            select course_count from User where user_id=%s;
            """,
            (userId,)
        )
        if res:
            courseCount = res['course_count']+1
            db.modify(
                """
                update User set course_count=%s where user_id=%s;
                """,
                (courseCount, userId)
            )

        if topicCount > 0:
            db.insertOne(
                """
                insert into Topic (topic_id, title, course_id)
                values
                (%s, %s, %s);
                """,
                (get_id(), topics[0]['topicTitle'], courseId)
            )

        respData = {
            "status": "success",
            "course_id": courseId,
            "location": "/courseList"
        }
        return respData

class EditCourse(Resource):
    # Edit course
    def put(self):
        data = request.get_json() or request.form
        courseId = data['courseId']
        title = data['title']
        description = data['description']

        db.modify(
            """
            update Course set title=%s, description=%s where course_id=%s;
            """,
            (title, description, courseId)
        )

        return {
            "state": "success"
        }

class EnvalidCourse(Resource):
    # 上线/下线课程
    def get(self):
        state = request.args.get("state")
        courseId = request.args.get("courseId")

        cur = 1 if state == False else 0

        db.modify(
            """
            update Course set is_valid=%s where course_id=%s;
            """,
            (cur, courseId)
        )

        return {
            "state": "success",
            "cur": True if cur == 1 else False
        }

class TeacherCourseList(Resource):
    # Fetch 课程列表
    def get(self):
        # data = request.args.get("userId")
        userId = request.args.get("userId")
        character = request.args.get("character")

        # Query Statements
        res = db.getOne(
            """
            select course_count from User where user_id=%s;
            """,
            (userId,)
        )['course_count']
        if res:
            if res <= 5:
                page = 0
                courseRes = db.getAll(
                    """
                    select * from Course where teacher_id=%s;
                    """,
                    (userId,)
                )
                courseCount = res
            else:
                page = res/5+1 if res%5 else res/5
                courseRes = db.getSome(
                    """
                    select * from Course where teacher_id=%s;
                    """,
                    5, (userId,)
                )
                courseCount = 5

        courseDetail = []
        for i in range(0, courseCount):
            courseDetail.append({
                "title": courseRes[i]['title'],
                "count": [courseRes[i]['topic_count'], courseRes[i]['section_count'], courseRes[i]['practice_count'], courseRes[i]['student_count']]
            })

        respData = {
            "state": "success",
            "count": courseCount,
            "page": page,
            "courses": courseDetail
        }
        return respData

class StudentCourseList(Resource):
    # Fetch Student Course List
    def get(self):
        userId = request.args.get("userId")
        character = request.args.get("character")

        # Query Statements
        res = db.getOne(
            """
            select course_count from User where user_id=%s;
            """,
            (userId,)
        )['course_count']

        if res:
            if res <= 5:
                page = 0
                # courseRes = db.getAll(
                #     """
                #     select * from Course where course_id in (
                #         select course_id from StudentCourse where student_id=%s
                #     );
                #     """,
                #     (userId,)
                # )
                # User JOIN instead of Sub-query --> faster
                courseRes = db.getAll(
                    """
                    select a.* from Course a inner join StudentCourse b
                    on a.course_id=b.course_id
                    where b.student_id=%s;
                    """,
                    (userId,)
                )
                courseCount = res
            else:
                page = res/5+1 if res%5 else res/5
                courseRes = db.getSome(
                    """
                    select a.*, b.status, b.last_section_id from Course a inner join StudentCourse b
                    on a.course_id=b.course_id
                    where b.student_id=%s;
                    """,
                    5, (userId,)
                )
                courseCount = 5

        courseDetail = []
        for i in range(0, courseCount):
            courseId = course[i]['course_id']
            teacherId = course[i]['teacher_id']
            teacherRes = db.getOne(
                """
                select name, icon from User where user_id=%s;
                """,
                (teacherId,)
            )
            if courseRes[i]['section_id'] != '':
                sectionTitle = db.getOne(
                    """
                    select title from Section where section_id=%s;
                    """,
                    (courseRes[i]['section_id'],)
                )
            else:
                sectionTitle = ''

            courseDetail.append({
                "title": courseRes[i]['title'],
                "description": courseRes[i]['description'],
                "id": courseRes[i]['course_id'],
                "teacher": {
                    "icon": teacherRes['icon']
                    "name": teacherRes['name']
                },
                "last": {
                    "title": sectionTitle,
                    "id": courseRes[i]['section_id']
                }
            })

        respData = {
            "state": "success",
            "count": courseCount,
            "page": page,
            "courses": courseDetail
        }
        return respData

class EditTopic(Resource):
    # 编辑章节
    def post(self):
        data = request.get_json() or request.form
        courseId = data['courseId']
        title = data['topicTitle']

        # Generate ID
        topicId = get_id()

        res = db.insertOne(
            """
            insert into Topic (topic_id, title, course_id, section_count)
            values
            (%s, %s, %s, %s);
            """,
            (topicId, title, courseId, 0)
        )
        if res:
            db.modify(
                """
                update Course set course_count=course_count+1 where course_id=%s;
                """,
                (courseId,)
            )
            return {
                "state": "success",
                "topicId": topicId,
                "title": title
            }

    def put(self):
        data = request.get_json() or request.form
        topicId = data['topicId']
        title = data['topicTitle']

        res = db.modify(
            """
            update Topic set title=%s where topic_id=%s;
            """,
            (title, topicId)
        )

        if res:
            return {"state": "success", "topicId": topicId, "title": title}

    def delete(self):
        topicId = request.args.get("topicId")
        courseId = request.args.get("courseId")

        res = db.delete(
            """
            delete from Topic where topic_id=%s;
            """,
            (topicId,)
        )

        if res:
            sectionIds = db.getAll(
                """
                select section_id from Section where topic_id=%s;
                """,
                (topicId,)
            )
            cnt = len(sectionIds)
            db.delete(
                """
                delete from Section where topic_id=%s;
                """,
                (topicId,)
            )
            for i in range(0, cnt):
                db.delete(
                    """
                    delete from Entity where section_id=%s;
                    """,
                    (sectionIds[i]['section_id'],)
                )
            db.modify(
                """
                update Course set topic_count=topic_count-1, section_count=section_count-%s;
                """
            )

            return {
                "state": "success"
            }

class EditSection(Resource):
    # 编辑小节
    def post(self):
        data = request.get_json() or request.form
        userId = data['userId']
        courseId = data['courseId']
        topicId = data['topicId']
        sectionTitle = data['sectionTitle']
        entityType = data['entityType']
        entityId = data['entityId']

        sectionId = get_id()
        if entityId != '':
            db.insertOne(
                """
                insert into Section (section_id, title, topic_id, entity_type, entity_id)
                values
                (%s, %s, %s, %s, %s);
                """,
                (sectionId, sectionTitle, topicId, entityType, entityId)
            )
            db.modify(
                """
                update Topic set section_count=section_count+1 where topic_id=%s;
                """,
                (topicId,)
            )
            db.modify(
                """
                update Course set section_count=section_count+1 where course_id=%s;
                """,
                (courseId,)
            )

            return {"state": "success", "section_id": sectionId}

    def put(self):
        data = request.get_json() or request.form
        userId = data['userId']
        courseId = data['courseId']
        topicId = data['topicId']
        sectionId = data['sectionId']
        sectionTitle = data['sectionTitle']
        entityType = data['entityType']
        entityId = data['entityId']

        db.modify(
            """
            update Section set title=%s, entity_type=%s, entity_id=%s where section_id=%s;
            """,
            (sectionTitle, entityType, entityId, sectionId)
        )

        resp = {
            "state": "success"
        }

        return resp

    def delete(self):
        sectionId = request.args.get('sectionId')

        topicId = db.getOne(
            """
            select topic_id from Section where section_id=%s;
            """,
            (sectionId,)
        )['section_id']
        courseId = db.getOne(
            """
            select course_id from Topic where topic_id=%s;
            """,
            (topicId,)
        )

        db.delete(
            """
            delete from Section where section_id=%s;
            """,
            (sectionId,)
        )
        db.delete(
            """
            delete from Entity where section_id=%s;
            """,
            (sectionId,)
        )
        db.modify(
            """
            update Topic set section_count=section_count-1 where topic_id=%s;
            """,
            (topicId,)
        )
        db.modify(
            """
            update Course set section_count=section_count-1 where course_id=%s;
            """,
            (courseId,)
        )

        return {
            "state": "success"
        }

class ImportStudent(Resource):
    def post(self):
        data = request.get_json() or request.form
        if data['importType'] == 'batch':
            # Batch Import
            return {
                "reason": "Not Supported Temporarily..."
            }
        else:
            # Single Import
            courseId = data['courseId']
            studentList = data['students']
            studentCount = len(studentList)

            for i in range(0, studentCount):
                studentId = studentList[i]['id']
                res = db.query(
                    """
                    select 1 from User where school_id=%s limit 1;
                    """,
                    (studentId,)
                )
                if res:
                    isIn = db.query(
                        """
                        select 1 from StudentCourse where student_id=%s and course_id=%s;
                        """,
                        (studentId, courseId)
                    )
                    if isIn:
                        studentList[i]['state'] = False
                        studentList[i]['reason'] = 'Already Involved.'
                    else:
                        db.insert(
                            """
                            insert into StudentCourse (student_id, course_id, status)
                            values
                            (%s, %s, %s);
                            """,
                            (studentId, courseId, 0)
                        )
                        db.modify(
                            """
                            update User set course_count=course_count+1 where school_id=%s;
                            """,
                            (studentId,)
                        )
                        studentList[i]['state'] = True
                else:
                    studentList[i]['state'] = False
                    studentList[i]['reason'] = 'User not Found.'

            resp = {
                "state": "success",
                "students": studentList
            }

            return resp

class SectionList(Resource):
    # Get Section List in Course Detail Page
    def get(self):
        userId = request.args.get("userId")
        courseId = request.args.get("courseId")

        processDetail = json.loads(db.getOne(
            """
            select process_detail from StudentCourse where student_id=%s and course_id=%s;
            """,
            (userId, courseId)
        )['process_detail'])

        return {
            "state": "success",
            "processDetail": processDetail
        }
