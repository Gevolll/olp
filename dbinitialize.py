# -*- coding: utf-8 -*-

"""
    初始化数据库
    建数据库
    建数据库表
    PyMySQL Module 支持 MySQL 5.x，不支持 8.x
"""

import pymysql

config = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "database": "olp",
    "charset": "utf8mb4"
}

userSql = """
    create table if not exists `User` (
        `user_id` bigint unsigned not null,
        `school_id` bigint unsigned not null,
        `password` varchar(20) not null,
        `character` int unsigned not null,
        `course_count` int unsigned,
        `practice_count` int unsigned,
        `icon` text,
        `name` text,
        primary key (`user_id`)
    )engine=InnoDB default charset=utf8;
"""

# User 表 character 0-student, 1-teacher

courseSql = """
    create table if not exists `Course` (
        `course_id` bigint unsigned not null,
        `title` text not null,
        `description` text not null,
        `teacher_id` bigint unsigned not null,
        `topic_count` int unsigned,
        `section_count` int unsigned,
        `practice_count` int unsigned,
        `student_count` int unsigned,
        `is_valid` int unsigned not null,
        primary key (`course_id`)
    )engine=InnoDB default charset=utf8;
"""

topicSql = """
    create table if not exists `Topic` (
        `topic_id` bigint unsigned not null,
        `title` text not null,
        `course_id` bigint unsigned not null,
        `section_count` int unsigned,
        primary key (`topic_id`)
    )engine=InnoDB default charset=utf8;
"""

sectionSql = """
    create table if not exists `Section` (
        `section_id` bigint unsigned not null,
        `title` text not null,
        `topic_id` bigint unsigned not null,
        `entity_type` int unsigned not null,
        `entity_id` bigint unsigned,
        primary key (`section_id`)
    )engine=InnoDB default charset=utf8;
"""
# entity_type  0-video, 1-doc, 2-attachment

entitySql = """
    create table if not exists `Entity` (
        `entity_id` bigint unsigned not null,
        `entity_type` int unsigned not null,
        `url` text,
        `content` longtext,
        `section_id` bigint unsigned not null,
        primary key (`entity_id`)
    )engine=InnoDB default charset=utf8;
"""
# url video, attachment
# content doc-html

studentCourseSql = """
    create table if not exists `StudentCourse` (
        `student_id` bigint unsigned not null,
        `course_id` bigint unsigned not null,
        `status` int unsigned not null,
        `last_section_id` bigint unsigned,
        `process_detail` longtext,
        primary key (`student_id`)
    )engine=InnoDB default charset=utf8;
"""

practiceSql = """
    create table if not exists `Practice` (
        `practice_id` bigint unsigned not null,
        `title` text not null,
        `teacher_id` bigint unsigned not null,
        `relation` int unsigned,
        `topic_id` bigint unsigned,
        `section_id` bigint unsigned,
        `course_id` bigint unsigned,
        primary key (`practice_id`)
    )engine=InnoDB default charset=utf8;
"""
# relation 0-course, 1-topic, 2-section

problemSql = """
    create table if not exists `Problem` (
        `problem_id` bigint unsigned not null,
        `position` int unsigned,
        `content` text,
        `choices` longtext,
        `answer` text,
        `comment` text,
        `practice_id` bigint unsigned not null,
        primary key (`problem_id`)
    )engine=InnoDB default charset=utf8;
"""

studentPracticeSql = """
    create table if not exists `StudentPractice` (
        `student_id` bigint unsigned not null,
        `pracitce_id` bigint unsigned not null,
        `status` int unsigned not null,
        `draft` longtext,
        `score` int unsigned,
        `duration` int unsigned,
        primary key (`student_id`)
    )engine=InnoDB default charset=utf8;
"""
# status 0-new 1-draft 2-finished

class DbInitilization(object):
    """
        数据库初始化操作对象
    """
    def __init__(self):
        """
            Connect Database and get cursor
        """
        self._conn = pymysql.Connect(**config)
        self._cursor = self._conn.cursor()

    def createTable(self, sql):
        """
            @Summary: Create table
            @param sql, params
            @return Row affected counts
        """
        count = self._cursor.execute(sql)
        return "success"

if __name__ == "__main__":
    db = DbInitilization()
    db.createTable(userSql)
    db.createTable(courseSql)
    db.createTable(topicSql)
    db.createTable(sectionSql)
    db.createTable(entitySql)
    db.createTable(studentCourseSql)
    db.createTable(practiceSql)
    db.createTable(problemSql)
    db.createTable(studentPracticeSql)
