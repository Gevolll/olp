<template lang="html">
  <div class="course-main">
    <Header />
    <div class="content-wrap">
      <div class="course-content">
        <CourseInfo :coursetitle="title" :teachername="teacher" />
        <CourseOutline :coursecontent="content" />
        <div class="float-clear">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Header from '../components/header';
import CourseInfo from '../components/courseinfo';
import CourseOutline from '../components/courseoutline';

export default {
  name: 'Course',
  data () {
    return {
      title: 'Android 项目开发实战 —— 4 个实战项目 7 天学会 Android 经典教程',
      teacher: '老师 A',
      content: [
        {
          topic: '初识 Java',
          sections: [
            {
              id: '12345',
              title: 'Java 简介 I',
              desc: '本课时介绍移动开发操作系统的发展历史，对 Android 的各个版本逐一回顾，简单讲解 Android 系统的构成，帮助大家快速了解 Android 体系的整体情况',
              entity: {
                type: 'video',
                duration: 1128
              },
              status: 2 // 学习完成
            },
            {
              id: '67890',
              title: 'Java 简介 II',
              desc: 'Testtesttest 00000',
              entity: {
                type: 'doc'
              },
              status: 1 // 正在学习
            },
            {
              id: '12345',
              title: 'Java 简介 III',
              desc: 'Testtesttest description',
              entity: {
                type: 'video',
                duration: 128
              },
              status: 0 // 未学习
            }
          ]
        },
        {
          topic: '我认识了 Java 之后呢?',
          sections: [
            {
              id: '67890',
              title: 'Java 进阶 I',
              desc: 'TTTTTTTTTTTTTTTTTTTTT',
              entity: {
                type: 'doc'
              },
              status: 0
            }
          ]
        }
      ]
    }
  },
  created () {
    console.log(this.$route.params.id);
  },
  components: {
    'Header': Header,
    'CourseInfo': CourseInfo,
    'CourseOutline': CourseOutline
  }
}
</script>

<style scoped lang="css">
.course-main {
  height: 100%;
  background-color: #f8f8f9;
}
.content-wrap {
  height: 100%;
  background-color: #f8f8f9;
}
.course-content {
  height: 100%;
  width: 1175px;
  margin: 0 auto;
  padding: 15px 0;
}
.float-clear {
  clear: both;
}
</style>
