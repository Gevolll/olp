<template lang="html">
  <div class="teacherpracticecreate-wrap">
    <div class="teacherpracticecreate-content">
      <div class="teacherpracticecreate-label" style="text-align: left; padding: 10px 25px 0;">
        <p style="font-size: 1.5em; font-weight: bold;" v-if="this.type === 'create'">新建练习</p>
        <p style="font-size: 1.5em; font-weight: bold;" v-else-if="this.type === 'edit'">编辑练习</p>
      </div>
      <div class="teacherpracticecreate-basic-info">
        <p style="text-align: left; font-size: 1.1rem; font-weight: bold; padding-bottom: 15px;">练习基本信息</p>
        <div class="teacherpracticecreate-title teacherpracticecreate-input">
          <span>练习名</span>
          <div class="teacherpracticecreate-input-wrap">
            <Input v-model="title" size="large" placeholder="练习名" />
          </div>
        </div>
      </div>
      <div class="teacherpracticecreate-button-wrap" style="float:right; padding: 10px;">
        <Button type="success" size="large" @click="handleSave">保存此练习</Button>
      </div>
      <div class="float-clear">
      </div>
      <div class="hr-wrap">
        <hr />
      </div>
      <div class="teacherpracticecreate-problems" id="problemsdetail" style="display: none;">
        <p style="text-align: left; font-size: 1.1rem; font-weight: bold; padding-bottom: 15px;">题目详情 (即时保存)</p>
        <div class="teacherpracticeCreate-list-wrap" id="problemlist" style="display: block;">
          <PracticeCreateItem v-for="problem in problemList" :problem="problem" @editProblem="handleEditProblem" @removeProblem="handleRemoveProblem"/>
        </div>
        <div class="teacherpracticecreate-plus" id="plus" style="float: left;">
          <span @click="handleNewProblem" style="color: #19be6b; font-weight: bold; font-size: 1.05rem; cursor: pointer;"><Icon type="plus" />&nbsp;新增</span>
        </div>
        <div class="teacherpracticecreate-minus" id="minus" style="display: none;">
          <span @click="handleCollapse" style="color: #2d8cf0; font-weight: bold; font-size: 1.05rem; float: left; padding-bottom: 10px; cursor: pointer;"><Icon type="minus" />&nbsp;收起</span>
          <div class="teacherpracticecreate-input" style="clear: both; float: left;">
            <span>题目</span>
            <div class="teacherpracticecreate-input-wrap">
              <Input v-model="problem" type="textarea" placeholder="题目" rows="3" />
            </div>
          </div>
          <div class="teacherpracticecreate-choices">
            <ChoiceItem v-for="(choice, index) in choices" :choiceValue="choice.value" :cid="choice.cid" @remove="handleRemove(index)" />
            <div class="teacherpracticecreate-input-wrap" style="float: left;">
              <div style="height: 36px; border: 1px dashed #dddee1; border-radius: 4px; cursor: pointer;" @click="handleNewChoice">
                <p style="text-align: left; color: #80848f; padding: 9px 10px;"><Icon type="plus" />&nbsp;新增一个选项</p>
              </div>
            </div>
            <div class="teacherpracticecreate-correct-choice">
              <span style="padding-right: 5px;">正确选项</span>
              <Select v-model="correctAnswer" style="width: 500px;">
                <Option v-for="choice in choices" :value="choice.value" :key="choice.value">
                  {{choice.value}}
                </Option>
              </Select>
            </div>
            <div class="float-clear">
            </div>
          </div>
          <div class="teacherpracticecreate-button-wrap" style="float:left; padding: 10px 0;">
            <Button type="success" size="large" @click="handleSaveProblem">保存此题</Button>
            <Button type="error" size="large" @click="handleCollapse">取消</Button>
          </div>
        </div>
      </div>
      <div class="float-clear"></div>
    </div>
  </div>
</template>

<script>
import ChoiceItem from './choiceitem';
import Hub from '../assets/hub.js';
import PracticeCreateItem from './practicecreateitem';
var v;

export default {
  name: 'TeacherPracticeEdit',
  data () {
    return {
      curProblemStatus: 0, // 记录下面的临时变量来自于编辑题目还是新建题目 0-新建，1-编辑
      curProblemIndex: 0, // 记录编辑题目的偏移量
      type: '',
      fakeid: '', // ONLY DEBUGUSE
      title: '',
      problem: '',
      choiceCount: 0, // 临时变量，当前 choice 的数目
      choices: [],
      correctAnswer: '',
      problemList: [
        // {
        //   problem: 'test01',
        //   choices: [
        //     {
        //       cid: 0,
        //       value: "test01"
        //     }
        //   ],
        //   correctAnswer: 'test01'
        // }
      ]
    }
  },
  components: {
    'ChoiceItem': ChoiceItem,
    'PracticeCreateItem': PracticeCreateItem
  },
  methods: {
    initComp: function () {
      if (this.$route.name.indexOf("TeacherPracticeCreate") != -1) {
        // Create Practice
        console.log("Create");
        this.type = 'create';
        this.title = '';
        this.problemList = [];
        this.problem = '';
        this.choices = [];
        this.correctAnswer = '';

      } else if (this.$route.name.indexOf("TeacherPracticeEdit") != -1) {
        // Edit Practice
        this.type = 'edit';
        this.title = 'Practice Title from remote server...';
        this.problemList = [
          {
            id: Math.ceil(Math.random()*100000).toString(),
            problem: 't1',
            choices: [
              {
                cid: 0,
                value: 'ch1'
              }
            ],
            correctAnswer: 'ch1'
          }
        ];
        this.fakeid = this.problemList[0].id;
        document.getElementById('problemsdetail').style.display = "block";
      }
    },
    handleNewChoice: function () {
      this.choices.push({cid: this.choiceCount, value: '', correct: false});
      this.choiceCount += 1;
    },
    handleRemove: function (index) {
      this.choices.splice(index, 1);
    },
    handleNewProblem: function () {
      document.getElementById('plus').style.display = "none";
      document.getElementById('minus').style.display = "block";
      this.curProblemStatus = 0;
    },
    handleCollapse: function () {
      document.getElementById('minus').style.display = "none";
      document.getElementById('plus').style.display = "block";
      document.getElementById('problemlist').style.display = "block";
      this.problem = '';
      this.choices = [];
      this.problemCount = 0;
      this.correctAnswer = '';
    },
    handleEditProblem: function (problemid) {
      // var eles = document.getElementsByTagName("div");
      // for (var i = 0; i < eles.length; i++) {
      //   if (eles[i].getAttribute("data-pid") === problemid) {
      //     console.log(eles[i].children);
      //     return;
      //   }
      // }
      for (var i = 0; i < this.problemList.length; i++) {
        if (this.problemList[i].id === problemid) {
          this.problem = this.problemList[i].problem;
          this.choices = this.problemList[i].choices;
          this.correctAnswer = this.problemList[i].correctAnswer;
          this.choiceCount = this.problemList[i].choices.length;
          // 修改两个状态变量
          this.curProblemStatus = 1;
          this.curProblemIndex = i;
          document.getElementById('problemlist').style.display = "none";
          document.getElementById('plus').style.display = "none";
          document.getElementById('minus').style.display = "block";
          return;
        }
      }
    },
    handleRemoveProblem: function (problemid) {
      // api.deleteProblem
      // callback with id here
      console.log('delete', problemid);
      for (var i = 0; i < this.problemList.length; i++) {
        if (this.problemList[i].id === problemid) {
          console.log('Here');
          this.problemList.splice(i, 1);
          return;
        }
      }
    },
    handleSaveProblem: function () {
      if (this.problem === '' ) {
        alert("题面不得为空");
        return;
      } else if (this.choices.length === 0) {
        alert("请添加至少一个选项");
        return;
      } else if (this.correctAnswer === '') {
        alert("请为题目选择正确选项");
        return;
      }
      document.getElementById('minus').style.display = "none";
      document.getElementById('plus').style.display = "block";
      document.getElementById('problemlist').style.display = "block";

      if (this.curProblemStatus === 0) {
        // create
        // api.createProblem here
        // callback id and content
        var d = {
          id: Math.ceil(Math.random()*1000000).toString(),
          problem: this.problem,
          choices: this.choices,
          correctAnswer: this.correctAnswer
        };
        this.problemList.push(d);
      } else if (this.curProblemStatus === 1) {
        // Edit & Save
        // api.updateProblem here
        // callback id and content
        var da = {
          id: this.fakeid,
          problem: this.problem,
          choices: this.choices,
          correctAnswer: this.correctAnswer
        }
        this.problemList.splice(this.curProblemIndex, 1, da);
      }

      this.problem = '';
      this.choices = [];
      this.problemCount = 0;
      this.correctAnswer = '';
      console.log(this.problemList);
    },
    handleSave: function () {
      if (this.title === '') {
        alert("练习名不得为空");
        return;
      }
      alert("保存成功！");
      this.$router.push({path: '/teachermain/practiceEdit/12487236529384'});
      window.location.reload();
    }
  },
  created () {
    v = this;

    Hub.$on('SetChoice', function(data) {
      var id = data.index;
      var val = data.value;
      var len = v.choices.length
      for (var i = 0; i < len; i++) {
        if (v.choices[i].cid === id) {
          v.choices[i].value = val;
          return;
        }
      }
    })
  },
  mounted () {
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
.teacherpracticecreate-wrap {
  width: 875px;
  height: 100%;
  background-color: #f8f8f9;
  padding: 0 10px;
  float: right;
}
.teacherpracticecreate-content {
  height: 100%;
  overflow-y: auto;
  background-color: #fff;
}
.teacherpracticecreate-basic-info, .teacherpracticecreate-problems {
  padding: 20px 25px 10px;
  float: left;
}
.teacherpracticecreate-input-wrap {
  display: inline-block;
  width: 700px;
  padding-bottom: 5px;
}
.teacherpracticecreate-input>span {
  font-size: 1.1rem;
  padding-right: 5px;
}
.teacherpracticecreate-choices, .teacherpracticecreate-correct-choice {
  float: left;
  padding-top: 10px;
  clear: both;
  width: 100%;
}
</style>
