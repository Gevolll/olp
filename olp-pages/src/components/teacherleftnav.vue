<template lang="html">
  <div class="nav-left">
    <Menu width="300px" theme="light" :open-names="open" :active-name="active" accordion>
      <Submenu name="TeacherCourse">
        <template slot="title">
          <Icon type="ios-book" />
          课程
        </template>
        <router-link :to="{ name: 'TeacherCourseList' }">
          <MenuItem name="TeacherCourseList">课程列表</MenuItem>
        </router-link>
        <router-link :to="{ name: 'TeacherCourseCreate' }">
          <MenuItem name="TeacherCourseCreate">新建课程</MenuItem>
        </router-link>
      </Submenu>
      <Submenu name="TeacherPractice">
        <template slot="title">
          <Icon type="clipboard" />
          练习
        </template>
        <router-link :to="{ name: 'TeacherPracticeList' }">
          <MenuItem name="TeacherPracticeList">练习列表</MenuItem>
        </router-link>
        <router-link :to="{ name: 'TeacherPracticeCreate' }">
          <MenuItem name="TeacherPracticeCreate">新建练习</MenuItem>
        </router-link>
      </Submenu>
    </Menu>
  </div>
</template>

<script>

export default {
  name: "TeacherLeftNav",
  data () {
    return {
      open: [],
      active: ''
    }
  },
  mounted () {
    var curName = this.$route.name;
    this.active = curName;
    if (curName === 'TeacherCourseList' || curName === 'TeacherCourseCreate') {
      this.$set(this.open, 0, 'TeacherCourse');
      console.log(this.open);
    } else if (curName === 'TeacherPracticeList' || curName === 'TeacherPracticeCreate') {
      this.$set(this.open, 0, 'TeacherPractice');
      console.log(this.open);
    }
  },
  watch: {
    '$route' (cur) {
      this.active = cur.name;
    }
  }
}
</script>

<style lang="css">
a, a:hover, a:active, a:visited {
  color: inherit;
}
li {
  text-align: left;
}
.nav-left {
  /* margin: 15px 15px 0 25px; */
  display: inline-block;
  float: left;
  /* box-shadow: 1px 1px 1px 1px #dddee1; */
  /* border: 1px solid #dddee1; */
}
</style>
