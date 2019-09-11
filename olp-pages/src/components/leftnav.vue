<template lang="html">
  <div class="nav-left">
    <Menu width="300px" theme="light" :active-name="active">
      <router-link :to="{ name: 'StudentCourse' }">
        <MenuItem name="StudentCourse">
          <Icon type="ios-book" />
          课程
        </MenuItem>
      </router-link>
      <router-link :to="{ name: 'StudentPractice' }">
        <MenuItem name="StudentPractice">
          <Icon type="clipboard" />
          练习
        </MenuItem>
      </router-link>
    </Menu>
  </div>
</template>

<script>
export default {
  name: "LeftNav",
  data () {
    return {
      active: ''
    }
  },
  mounted () {
    this.active = this.$route.name;
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
