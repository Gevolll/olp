<template lang="html">
  <div class="teachercourseedit-wrap">
    <div class="teachercourseedit-content">
      <div style="padding: 10px;">
      </div>
      <div class="teachercourseedit-label" style="text-align: left; padding-left: 25px;">
        <p style="font-size: 1.5em; font-weight: bold;" v-if="this.type === 'edit'">编辑课程</p>
        <p style="font-size: 1.5em; font-weight: bold;" v-if="this.type === 'create'">新建课程</p>
        <!-- <p style="font-size: 1.2em; color: #80848f; padding-bottom: 15px;">{{title}}</p> -->
        <div class="teachercourseedit-input-wrap" style="padding: 10px 0;">
          <span style="padding-right: 10px;">课程名</span>
          <Input v-model="title" placeholder="课程名" style="width: 500px; padding: 10px 0;" />
        </div>
        <div class="teachercourseedit-input-wrap">
          <span style="padding-right: 10px;">课程简介</span>
          <Input v-model="desc" type="textarea" placeholder="课程简介" style="width: 500px;" rows="4" />
        </div>
      </div>
      <div class="button-wrap" style="float: right; padding: 10px 20px;">
        <Button type="error" @click="handleCancel">取消</Button>
        <Button type="success" @click="handleSave">保存</Button>
      </div>
      <div class="float-clear">
      </div>
      <div class="hr-wrap" style="padding-top: 10px;">
        <hr />
      </div>
      <div class="teachercourseedit-topic-edit" style="display: none;" v-if="this.type === 'create'">
        <div class="teachercourseedit-label" style="text-align: left; padding: 10px 25px;">
          <p style="font-size: 1.2em; font-weight: bold; color: #80848f; white-space:pre-wrap;">章节结构 (创建后即保存)</p>
        </div>
        <CourseEditItem v-for="topic in courseDetail" :topic="topic" @removetopic="handleRemoveTopic" @removesection="handleRemoveSection"/>
        <p style="text-align: left; font-size: 1.1em; padding-left: 25px; padding-top: 10px; white-space: pre-wrap;"><router-link :to="{ name: 'TeacherTopicCreate', params: {courseid: this.id} }"><span style="cursor: pointer;"><Icon type="plus" /> 新增章节</span></router-link></p>
      </div>
      <div class="teachercourseedit-topic-edit" style="display: block;" v-if="this.type === 'edit'">
        <div class="teachercourseedit-label" style="text-align: left; padding: 10px 25px;">
          <p style="font-size: 1.2em; font-weight: bold; color: #80848f; white-space:pre-wrap;">章节结构 (创建后即保存)</p>
        </div>
        <CourseEditItem v-for="topic in courseDetail" :topic="topic" @removetopic="handleRemoveTopic" @removesection="handleRemoveSection"/>
        <p style="text-align: left; font-size: 1.1em; padding-left: 25px; padding-top: 10px; white-space: pre-wrap;"><router-link :to="{ name: 'TeacherTopicCreate', params: {courseid: this.id} }"><span style="cursor: pointer;"><Icon type="plus" /> 新增章节</span></router-link></p>
      </div>
    </div>
  </div>
</template>

<script>
import CourseEditItem from './courseedititem.vue';

export default {
  name: 'TeacherCourseEdit',
  data () {
    return {
      id: this.$route.params.id,
      type: '',
      title: 'Android 工程师职业规划',
      desc: 'askdhgpaidofhapisdugfhdogihaosidfuhasdgf',
      courseDetail: []
    }
  },
  components: {
    'CourseEditItem': CourseEditItem
  },
  methods: {
    initComp: function () {
      if (this.$route.name.indexOf("TeacherCourseCreate") != -1) {
        // Create Course
        this.type = 'create';
        this.id = '';
        this.title = '';
        this.desc = '';
        this.courseDetail = '';
      } else if (this.$route.name.indexOf("TeacherCourseEdit") != -1) {
        // Edit Course
        this.type = 'edit';
        this.id = '1237651932';
        this.title = 'Android 工程师职业规划';
        this.desc = 'asdfhi23r7fshdf';
        this.courseDetail = [
          {
            id: "18273434512938123",
            topicTitle: 'TestTitle01',
            sections: [
              {
                id: "iudfhfia18236429",
                sectionTitle: 'SectionTitle01',
                entityType: 'video'
              },
              {
                id: "128765923841042",
                sectionTitle: 'SectionTitle02',
                entityType: 'doc',
                content: 'blah'
              }
            ]
          },
          {
            id: "12u36549w8sdfhs",
            topicTitle: '1284762934test_title',
            sections: [
              {
                id: '1237648dhufg1',
                sectionTitle: '2-1',
                entityType: 'video'
              },
              {
                id: '128376419283352',
                sectionTitle: '2-2',
                entityType: 'video'
              }
            ]
          }
        ];
      }
    },
    handleRemoveTopic: function (topicid) {
      for (var i = 0; i < this.courseDetail.length; i++) {
        if (this.courseDetail[i].id === topicid) {
          if (confirm("确定要删除？")) {
            this.courseDetail.splice(i, 1);
            // upload and callback !
            // 这里单独做一个接口请求 topic 和 section 数据，因为强制刷新页面会丢失上面课程信息的保存
            // 这里删除的 callback 只更新 courseDetail
            return;
          }
        }
      }
    },
    handleRemoveSection: function (sectionid) {
      var s;
      console.log("Here!");
      for (var i = 0; i < this.courseDetail.length; i++) {
        s = this.courseDetail[i].sections;
        // console.log(s);
        for (var j = 0; j < s.length; j++) {
          if (s[j].id === sectionid) {
            if (confirm("确定要删除？")) {
              this.courseDetail[i].sections.splice(j, 1);
              // upload and callback!
              console.log(this.courseDetail);
              return;
            }
          }
        }
      }
    },
    handleCancel: function () {
      if(confirm("确认要取消？")) {
        this.$router.push({path: '/teachermain'});
      }
    },
    handleSave: function () {
      console.log(this.courseDetail);
      alert("保存成功");
      // 创建新课程，回调返回 courseid，跳转到编辑页
      this.$router.push({path: '/teachermain/courseEdit/123t64192301'});
      window.location.reload();
    }
  },
  mounted () {
    console.log(this.$route);
    this.initComp();
  }
}
</script>

<style lang="css">
.float-clear {
  clear: both;
}
.hr-wrap {
  padding: 5px;
}
hr {
  height: 1px;
  border: none;
  border-bottom: 1px solid #dddee1;
}
.teachercourseedit-wrap {
  height: 100%;
  background-color: #f8f8f9;
  width: 875px;
  padding: 0 10px;
  float: right;
}
.teachercourseedit-content {
  height: 100%;
  background-color: #fff;
}
.teachercourseedit-list-item {
  padding: 5px 25px;
}
.topictitle-label {
  padding-bottom: 5px;
}
.topictitle-label>p, .section-list>p {
  text-align: left;
  white-space: pre-wrap;
}
.topictitle-label>p {
  font-weight: bold;
  font-size: 1.1rem;
}
.section-list>p {
  font-size: 1rem;
  padding-top: 5px;
}
.span-edit {
  color: #2d8cf0;
  cursor: pointer;
}
.span-remove {
  color: #ed3f14;
  cursor: pointer;
}
.span-open, .span-close {
  cursor: pointer;
}
</style>
