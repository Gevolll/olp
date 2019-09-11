import Vue from 'vue';
import Router from 'vue-router';
import HelloWorld from '../components/HelloWorld';

// Pages
import Login from '../pages/login';
import StudentMain from '../pages/studentmain';
import Practice from '../pages/practice';
import Course from '../pages/course';
import Section from '../pages/section';
import PracticeDetail from '../pages/practicedetail';
import TeacherMain from '../pages/teachermain';

// Components
import StudentCourseList from '../components/studentcourselist';
import StudentPracticeList from  '../components/studentpracticelist';
import TeacherCourseList from '../components/teachercourselist';
import TeacherPracticeList from '../components/teacherpracticelist';
import TeacherCourseCreate from '../components/teachercoursecreate';
import TeacherTopicEdit from '../components/teachertopicedit';
import TeacherPracticeEdit from '../components/teacherpracticeedit';
import TeacherCourseEdit from '../components/teachercourseedit';
import TeacherSectionEdit from '../components/editsection';


Vue.use(Router);

var cookieop = require('../utils/cookieop');

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      redirect: function (to) {
        var username = cookieop.methods.getCookie("username");
        var character = cookieop.methods.getCookie("character");
        // console.log(username);
        // console.log(character);
        if (username === null) {
          return '/login';
        } else if (parseInt(character) === 0) {
          // Student
          return '/studentmain';
        } else if (parseInt(character) === 1) {
          // Teacher
          return '/teachermain';
        }
      }
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/studentmain',
      name: 'StudentMain',
      component: StudentMain,
      children: [
        {
          path:'',
          name: 'StudentCourse',
          component: StudentCourseList
        },
        {
          path: 'course',
          name: 'StudentCourse',
          component: StudentCourseList
        },
        {
          path: 'practice',
          name: 'StudentPractice',
          component: StudentPracticeList
        }
      ]
    },
    {
      path:'/practice/:id',
      name: 'Practice',
      component: Practice
    },
    {
      path: '/course/:id',
      name: 'Course',
      component: Course
    },
    {
      path: '/section/:id',
      name: 'Section',
      component: Section
    },
    {
      path: '/practice/:id/detail',
      name: 'PracticeDetail',
      component: PracticeDetail
    },
    {
      path: '/teachermain',
      name: 'TeacherMain',
      component: TeacherMain,
      children: [
        {
          path: '',
          name: 'TeacherCourseList',
          component: TeacherCourseList
        },
        {
          path: 'course',
          name: 'TeacherCourseList',
          component: TeacherCourseList
        },
        {
          path: 'practice',
          name: 'TeacherPracticeList',
          component: TeacherPracticeList
        },
        {
          path: 'courseCreate',
          name: 'TeacherCourseCreate',
          component: TeacherCourseEdit
        },
        {
          path: 'topicCreate/:courseid',
          name: 'TeacherTopicCreate',
          component: TeacherTopicEdit
        },
        {
          path: 'sectionCreate/:courseid/:topicid',
          name: 'TeacherSectionCreate',
          component: TeacherSectionEdit
        },
        {
          path: 'practiceCreate',
          name: 'TeacherPracticeCreate',
          component: TeacherPracticeEdit
        },
        {
          path: 'courseEdit/:id',
          name: 'TeacherCourseEdit',
          component: TeacherCourseEdit
        },
        {
          path: 'topicEdit/:courseid/:topicid',
          name: 'TeacherTopicEdit',
          component: TeacherTopicEdit
        },
        {
          path: 'sectionEdit/:courseid/:topicid/:sectionid',
          name: 'TeacherSectionEdit',
          component: TeacherSectionEdit
        },
        {
          path: 'practiceEdit/:practiceid',
          name: 'TeacherPracticeEdit',
          component: TeacherPracticeEdit
        }
      ]
    }
  ]
})
