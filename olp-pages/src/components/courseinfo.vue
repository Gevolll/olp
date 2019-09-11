<template lang="html">
  <div class="courseinfo-main">
    <div class="courseinfo-title">
      <p>{{title}}</p>
    </div>
    <div class="courseinfo-teacherinfo">
      <SmallTeacherInfo :teachername="teacher" />
    </div>
  </div>
</template>

<script>
import SmallTeacherInfo from './smallteacherinfo';

export default {
  name: 'CourseInfo',
  data () {
    return {
      title: this.coursetitle,
      teacher: this.teachername
    }
  },
  props: ['coursetitle', 'teachername'],
  components: {
    'SmallTeacherInfo': SmallTeacherInfo
  }
}
</script>

<style lang="css">
.courseinfo-main {
  float: left;
  width: 300px;
  background-color: #ffffff;
  padding: 10px 15px;
}
.courseinfo-title {
  padding-bottom: 10px;
}
.courseinfo-title>p {
  white-space: pre-wrap;
  font-size: 1.25rem;
  text-align: left;
  color: #1c2438;
}
.courseinfo-teacherinfo {
  padding-bottom: 20px;
  position: relative;
}
.teacher-avatar {
  float: left;
}
.teacher-name {
  float: left;
  position: absolute;
  left: 34px;
  top: 50%;
  transform: translateY(-19px);
}
.teacher-name>p {
  color: #80848f;
}
</style>
