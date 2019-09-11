<template lang="html">
  <div class="teacherpracticecreate-item" :data-pid="this.id">
    <div class="problem-label">
      <p>{{p}}</p>
    </div>
    <div class="choices">
      <p v-for="choice in choices">{{choice.value}}<span class="correct-answer" v-if="choice.value === correctAnswer">(正确答案)</span>
      </p>
    </div>
    <div class="op-wrap">
      <p style="text-align:left; white-space: pre-wrap;"><span style="margin-right: 10px; color: #2d8cf0; cursor: pointer;" @click="handleEdit($event)">编辑此题</span><span style="color: #ed3f14; cursor: pointer;" @click="handleRemove($event)">删除此题</span></p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PracticeCreateItem',
  data () {
    return {
      id: this.problem.id,
      p: this.problem.problem,
      choices: this.problem.choices,
      correctAnswer: this.problem.correctAnswer
    }
  },
  props: ['problem'],
  mounted () {

  },
  methods: {
    handleEdit: function (e) {
      console.log(e.path[3].dataset.pid);
      var problemid = e.path[3].dataset.pid;
      this.$emit('editProblem', problemid);
    },
    handleRemove: function (e) {
      var problemid = e.path[3].dataset.pid;
      this.$emit('removeProblem', problemid);
    }
  }
}
</script>

<style lang="css">
.teacherpracticecreate-item {
  padding-bottom: 15px;
}
.problem-label>p, .choices>p {
  text-align: left;
  white-space: pre-wrap;
}
span.correct-answer {
  color: #19be6b;
}
</style>
