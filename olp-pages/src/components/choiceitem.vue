<template lang="html">
  <div class="teacherpracticecreate-input-wrap">
    <Input v-model='value' :value='choiceValue' size="large" placeholder="选项" />
    <span style="color: #ed3f14; cursor: pointer;" @click="$emit('remove');"><Icon type="close" />&nbsp;删除</span>
    <!-- <span style="color: #19be6b; cursor: pointer;" @click="handleInCorrect($event)"><Icon type="checkmark" />&nbsp;设为正确选项</span> -->
    <!-- <span>{{correctness}}</span> -->
  </div>
</template>

<script>
import Hub from '../assets/hub.js';

export default {
  name: 'ChoiceItem',
  data () {
    return {
      // comp = this,
      correctness: false,
      value: this.choiceValue
    }
  },
  props: ['choiceValue', 'cid'],
  methods: {
    handleInCorrect: function(e) {
      var ele = e.path[0];
      if(ele.className.indexOf("choice-correct") != -1) {
        ele.innerHTML = "<i class='ivu-icon ivu-icon-checkmark'></i>&nbsp设为正确选项";
        ele.className = "";
        ele.style.color = "#19be6b";
        this.$emit("cancel");
      } else {
        ele.innerHTML = "<i class='ivu-icon ivu-icon-close'></i>&nbsp取消设为正确选项";
        ele.className = "choice-correct";
        ele.style.color = "#ed3f14";
        this.$emit("correct");
      }
    }
  },
  watch: {
    value: function(cur) {
      // console.log(comp);
      Hub.$emit("SetChoice", {index: this.cid, value: cur});
    }
  },
  created () {
  }
}
</script>

<style lang="css">
.teacherpracticecreate-input-wrap>span {
  font-size: 1rem;
  float: left;
  padding: 5px 10px 0 0;
}
</style>
