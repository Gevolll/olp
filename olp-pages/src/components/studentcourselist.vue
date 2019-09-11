<template lang="html">
  <div class="student-course-list">
    <!-- <div class="student-course-item">
      <div class="student-course-item-content item-first">
        <div class="course-title">
          <p>Android 应用开发工程师职业规划</p>
        </div>
        <div class="course-description">
          <p>本课程主要向大家介绍 Android 应用开发工程师的职业背景、行业前景、团队中的定位及所需的技能，同时分享 Android 应用开发的学习方法和路径以及将来的职业规划</p>
        </div>
        <div class="course-info">
          <div class="courselist-teacher-info">
            <SmallTeacherInfo />
          </div>
          <div class="last-progress">
            <p>上次学到   <span class="last-progress-section">Android 应用开发工程师职业规划</span></p>
          </div>
          <div class="float-clear">
          </div>
        </div>
      </div> -->
    <div style="padding-top: 15px;">
    </div>
    <div class="student-course-item-wrap" v-for="course in courses">
      <div class="student-course-item">
        <div class="student-course-item-content">
          <div class="course-title">
            <p><router-link :to="{ name: 'Course', params: {id: course.id} }"><span>{{ course.title }}</span></router-link></p>
          </div>
          <div class="course-description">
            <p>{{ course.desc }}</p>
          </div>
          <div class="class-info">
            <div class="courselist-teacher-info">
              <SmallTeacherInfo :teachername="course.teacher" />
            </div>
            <div class="last-progress" v-if="JSON.stringify(course.lastProgress) != '{}'">
              <p>上次学到   <router-link :to="{ name: 'Section', params: {id: course.lastProgress.id} }"><span class="last-progress-section">{{course.lastProgress.title}}</span></router-link></p>
            </div>
            <div class="last-progress" v-else>
              <p style="color: #80848f;">还未开始学习</p>
            </div>
            <div class="float-clear">
            </div>
          </div>
        </div>
      </div>
      <div class="hr-wrap">
        <hr />
      </div>
    </div>
  </div>
</template>

<script>
import SmallTeacherInfo from './smallteacherinfo';

export default {
  name: 'StudentCourseList',
  data () {
    return {
      // 请求远端接口，返回每个课程的信息
      courses: [
        {
          id: '123',
          title: 'Android 应用开发工程师职业规划',
          desc: '本课程主要向大家介绍 Android 应用开发工程师的职业背景、行业前景、团队中的定位及所需的技能，同时分享 Android 应用开发的学习方法和路径以及将来的职业规划',
          teacher: '老师 A',
          lastProgress: {
            id: '234',
            title: 'Android 应用开发工程师职业规划'
          }
        },
        {
          id: '345',
          title: 'Android 应用开发工程师 II',
          desc: 'Test 课程描述在这里',
          teacher: '老师 B',
          lastProgress: {
          }
        }
      ],
      page: 0,
      totalPage: 10
    }
  },
  components: {
    'SmallTeacherInfo': SmallTeacherInfo
  }
}
</script>

<style lang="css">
.hr-wrap {
  padding: 5px;
}
hr {
  height: 1px;
  border: none;
  border-bottom: 1px solid #dddee1;
}

.student-course-list {
  float: right;
  width: 860px;
  height: 100%;
  background-color: #ffffff;
}
.student-course-item-content {
  padding: 5px 25px;
}
.item-first {
  padding-top: 20px;
}
.item-last {
  padding-bottom: 20px;
}

.course-title {
  padding-bottom: 5px;
}
.course-title>p {
  color: #495060;
  font-size: 1.5rem;
  text-align: left;
}

.course-description{
  padding-bottom: 10px;
}
.course-description>p {
  color: #80848f;
  text-align: left;
}

.courselist-teacher-info {
  float: left;
  width: 200px;
  display: inline-block;
}

.last-progress {
  float: right;
  padding: 3px 0;
}
.last-progress>p {
  text-align: right;
  white-space: pre-wrap;
}
.last-progress-section {
  color: #2d8cf0;
  font-weight: bold;
}

</style>
