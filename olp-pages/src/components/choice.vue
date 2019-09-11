<template lang="html">
  <div class="choice-wrap">
    <div :id="choiceid" :class="choiceclass" @click="onSelected($event)">
      <p>{{ ch }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Choice',
  data () {
    return {

    }
  },
  props: ["choiceid", "choiceclass", 'ch'],
  methods: {
    onSelected: function(e) {
      // console.log(e.path[1]);
      var choiceid = e.path[1].attributes["id"].value;
      var ele = document.getElementById(choiceid);
      var classNames = ele.attributes["class"].value;
      if (classNames.indexOf("choice-content-active") != -1) {
        this.$emit("choiceselected", {status: 1, choiceid: choiceid, val: this.ch});
        ele.className = "choice-content";
      }
      else {
        this.$emit("choiceselected", {status: 0, choiceid: choiceid, val: this.ch});
      }
    }
  }
}
</script>

<style lang="css">
.choice-wrap {
  width: 1135px;
  padding-bottom: 15px;
}
.choice-content {
  width: 100%;
  height: 50px;
  border: 1px solid #dddee1;
  border-radius: 8px;
  color: #495060;
  transition-property: border,color;
  -webkit-transition-property: border,color;
  transition-duration: 300ms;
  -webkit-transition-duration: 300ms;
}
.choice-content>p {
  text-align: left;
  font-size: 1.1rem;
  padding: 13px 15px;
  color: inherit;
}
.choice-content:hover {
  border: 1px solid #2d8cf0;
  cursor: pointer;
  color: #2d8cf0;
  transition-property: border,color;
  -webkit-transition-property: border,color;
  transition-duration: 300ms;
  -webkit-transition-duration: 300ms;
}
.choice-content-active {
  border: 1px solid #2d8cf0;
  color: #2d8cf0;
}
.choice-content-correct {
  border: 1px solid #19be6b;
  color: #19be6b;
}
.choice-content-false {
  border: 1px solid #ed3f14;
  color: #ed3f14;
}
</style>
