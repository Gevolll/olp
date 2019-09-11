<template lang="html">
  <div class="problem-wrap">
    <div class="problem-content">
      <p>{{ p.content }}</p>
    </div>
    <div class="problem-choices-wrap">
      <template v-for="(ch, index) in p.choices">
        <Choice :choiceid="'p'+problemid+'ch'+index" :ch="ch" choiceclass="choice-content" @choiceselected="listenToSelected" />
      </template>
      <!-- <Choice v-for="(ch, index) in p.choices" :choiceid="'p'+problemid+'ch'+index" :ch="ch" choiceclass="choice-content" @choiceselected="listenToSelected" /> -->
      <!-- <Choice choiceid="1" choiceclass="choice-content" @choiceselected="listenToSelected" />
      <Choice choiceid="2" choiceclass="choice-content" @choiceselected="listenToSelected" />
      <Choice choiceid="3" choiceclass="choice-content" @choiceselected="listenToSelected" />
      <Choice choiceid="4" choiceclass="choice-content" @choiceselected="listenToSelected" /> -->
    </div>
  </div>
</template>

<script>
import Choice from './choice';

export default {
  name: 'Problem',
  props: ['p', 'problemid'],
  data () {
    return {
      selectedValue: ''
    }
  },
  components: {
    'Choice': Choice
  },
  methods: {
    listenToSelected: function (op) {
      if (op["status"] === 1) {
        // Handle with clearing THE choice
        // console.log(op["choiceid"]);
        choiceid = op["choiceid"];
        this.selectedValue = '';
      } else {
        // Handle with select THE choice
        // console.log(op["choiceid"]);
        var choiceid = op["choiceid"];
        this.selectedValue = op["val"];
        var eleList = document.getElementById('p'+this.problemid).children[1].children;
        var eleCount = eleList.length;
        for (var i = 0; i < eleCount; i++) {
          if (eleList[i].children[0].id === choiceid) {
            eleList[i].children[0].className = "choice-content choice-content-active";
          } else {
            eleList[i].children[0].className = "choice-content";
          }
        }
      }
    }
  },
  mounted () {
    if (this.p.status === 1) {
      this.selectedValue = this.p.choices[this.p.draft];
      document.getElementById('p'+this.problemid+'ch'+this.p.draft).className = "choice-content choice-content-active";
      console.log(this.selectedValue);
    }
  },
  watch: {
    selectedValue: function (curVal) {
      if (curVal === '') {
        this.$emit('remove', {index: this.problemid});
      } else {
        console.log("problem emit", this.selectedValue);
        this.$emit('choose', {index: this.problemid, val: this.selectedValue});
      }
    }
  }
}
</script>

<style lang="css">
.problem-wrap {
  background-color: #fff;
  padding: 15px 20px;
  height: 350px;
  overflow-y: auto;
}
.problem-content {
  padding-bottom: 20px;
}
.problem-content>p {
  text-align: left;
  font-size: 1.1rem;
  white-space: pre-wrap;
  color: #1c2438;
  padding: 0 10px;
}

</style>
