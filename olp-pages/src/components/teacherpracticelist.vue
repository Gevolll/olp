<template lang="html">
  <div class="teacherpracticelist-wrap">
    <div class="teacherpracticelist-content">
      <div class="teacherpracticelist-padding-top" style="padding:10px;">
      </div>
      <div class="teacherpracticelist-item" v-for="item in practiceList" :data-pid="item.id">
        <div class="teacherpracticelist-item-title">
          <p>{{item.title}}</p>
        </div>
        <div class="teacherpracticelist-item-relation">
          <p>{{item.relation}}</p>
        </div>
        <div class="teacherpracticelist-item-info">
          <p>{{item.info}}</p>
        </div>
        <div class="teacherpracticelist-button-wrap">
          <Button type="primary" size="default" @click="handleEdit($event)">编辑</Button>
          <Button type="primary" size="default" @click="handleDetail($event)">答题情况</Button>
        </div>
        <div class="float-clear">
        </div>
        <div class="hr-wrap">
          <hr />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TeacherPracticeList',
  data () {
    return {
      practiceList: []
    }
  },
  methods: {
    initComp: function () {
      this.practiceList = [
        {
          title: "课后练习",
          relation: "Android 应用开发工程师职业规划",
          info: "36 人完成 · 平均 90 分 · 平均用时 12 分钟",
          id: "1234567"
        },
        {
          title: "课后练习",
          relation: "Android 应用开发工程师职业规划",
          info: "xxxxxxx",
          id: "34762839490"
        }
      ];
    },
    handleEdit: function(e) {
      console.log(e.path[3].dataset.pid);
      
    },
    handleDetail: function(e) {
      // console.log(e.path[3].children[3].innerText);
      console.log(e.path[3].dataset.pid);
    }
  },
  mounted () {
    this.initComp();
  }
}
</script>

<style lang="css">
.teacherpracticelist-wrap {
  height: 100%;
  width: 875px;
  float: right;
  background-color: #f8f8f9;
  padding: 0 10px;
}
.teacherpracticelist-content {
  height: 100%;
  background-color: #fff;
}
.teacherpracticelist-item-title>p {
  padding-left: 25px;
  padding-bottom: 5px;
  text-align: left;
  font-size: 1.5rem;
  color: #1c2438;
}
.teacherpracticelist-item-relation>p, .teacherpracticelist-item-info>p {
  padding-left: 25px;
  text-align: left;
  color: #80848f;
  padding-bottom: 5px;
}
/* .teacherpracticelist-item-id {
  display: none;
} */
.teacherpracticelist-button-wrap {
  float: left;
  /* padding-left: 25px; */
  padding: 10px 0 10px 25px;
}
.hr-wrap {
  padding: 5px;
}
hr {
  height: 1px;
  border: none;
  border-bottom: 1px solid #dddee1;
}
.float-clear {
  clear: both;
}
</style>
