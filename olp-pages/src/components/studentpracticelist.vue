<template lang="html">
  <div class="list-wrap student-practice-list">
    <div style="padding-top: 20px;">
    </div>
    <div class="student-practice-item" v-for="practice in practices">
      <div class="student-practice-item-content">
        <div class="practice-title">
          <p>{{ practice.title }}</p>
        </div>
        <div class="practice-relation">
          <p>{{ practice.relation }}</p>
        </div>
        <div class="practice-info">
          <p>{{ practice.info }}</p>
        </div>
      </div>
      <div class="practice-status" v-if="practice.status === 0">
        <router-link :to="{ name: 'Practice', params: {id: practice.id} }"><Button type="primary">去完成</Button></router-link>
      </div>
      <div class="practice-status" v-else-if="practice.status === 1">
        <p style="color: #19be6b;">已完成</p>
        <p>查看结果</p>
      </div>
      <div class="float-clear">
      </div>
      <div class="hr-wrap">
        <hr />
      </div>
    </div>
    <!-- <div class="student-practice-item">
      <div style="padding: 10px;">
      </div>
      <div class="student-practice-item-content">
        <div class="practice-title">
          <p>课后练习</p>
        </div>
        <div class="practice-relation">
          <p>Android 应用工程师职业规划 / Android 应用工程师职业规划 / Android 应用工程师职业规划</p>
        </div>
        <div class="practice-info">
          <p>36 人完成 · 平均 90 分 · 平均用时 12 分钟</p>
        </div>
      </div>
      <div class="practice-status item-first">
        <Button type="primary">去完成</Button>
      </div>
      <div class="float-clear">
      </div>
      <div class="hr-wrap">
        <hr />
      </div>
    </div>
    <div class="student-practice-item">
      <div class="student-practice-item-content item-first">
        <div class="practice-title">
          <p>课后练习</p>
        </div>
        <div class="practice-relation">
          <p>Android 应用工程师职业规划 / Android 应用工程师职业规划 / Android 应用工程师职业规划</p>
        </div>
        <div class="practice-info">
          <p>36 人完成 · 平均 90 分 · 平均用时 12 分钟 · <span class="my-score">我的成绩 90 分</span></p>
        </div>
      </div>
      <div class="practice-status item-first">
        <p>已完成</p>
      </div>
      <div class="float-clear">
      </div>
      <div class="hr-wrap">
        <hr />
      </div>
    </div> -->
  </div>
</template>

<script>
export default {
  name: 'StudentPracticeList',
  data () {
    return {
      practices: [
        {
          id: '12365',
          title: '课后练习',
          relation: 'Android 应用工程师职业规划 / Android 应用工程师职业规划 / Android 应用工程师职业规划',
          info: '36 人完成 · 平均 90 分 · 平均用时 12 分钟',
          status: 0
        },
        {
          id: '123756',
          title: '课程练习 II',
          relation: 'TTTTEEEESSSSTTTT',
          info: '36 人完成 · 平均 90 分 · 平均用时 12 分钟',
          status: 1
        }
      ]
    }
  }
}
</script>

<style lang="css">
hr {
  height: 1px;
  border: none;
  border-bottom: 1px solid #dddee1;
}
.hr-wrap {
  padding: 5px;
}

.student-practice-list {
  float: right;
  width: 860px;
  height: 100%;
  background-color: #ffffff;
}

.student-practice-item {
  position: relative;
}

.student-practice-item-content {
  padding: 5px 25px;
  width: 700px;
  float:left;
}
.item-first {
  padding-top: 20px;
}
.item-last {
  padding-bottom: 20px;
}

.practice-title {
  padding-bottom: 5px;
}
.practice-title>p {
  color: #495060;
  font-size: 1.5rem;
  text-align: left;
}

.practice-relation {
  padding-bottom: 10px;
}
.practice-relation>p {
  color: #80848f;
  text-align: left;
}

.practice-info>p {
  text-align: left;
}
.my-score {
  color: #268cf0;
  font-weight: bold;
}

.practice-status {
  position: absolute;
  right: 0;
  top: 50%;
  height: 32px;
  transform: translateY(-16px);
  width: 160px;
}
.practice-status>p {
  color: #2d8cf0;
  font-size: 0.8rem;
  font-weight: bold;
  padding-bottom: 5px;
  /* line-height: 32px; */
}


</style>
