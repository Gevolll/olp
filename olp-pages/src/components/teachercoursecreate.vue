<template lang="html">
  <div class="teachercoursecreate-wrap">
    <div class="teachercoursecreate-content">
      <div class="teachercoursecreate-basic-info-wrap">
        <div class="teachercoursecreate-label">
          <p>课程基本信息</p>
        </div>
        <div class="teachercoursecreate-input">
          <span>课程名</span>
          <div class="teachercoursecreate-input-wrap">
            <Input size="large" placeholder="课程名" v-model="title"/>
          </div>
        </div>
        <div class="teachercoursecreate-input">
          <span>课程简介</span>
          <div class="teachercoursecreate-input-wrap">
            <Input type="textarea" placeholder="课程简介" rows="5" v-model="desc"/>
          </div>
        </div>
        <div class="float-clear">
        </div>
      </div>
      <div class="hr-wrap">
        <hr />
      </div>
      <div class="teachercoursecreate-structure-wrap">
        <div class="teachercoursecreate-label">
          <p>课程基本结构</p>
        </div>
        <div class="teachercoursecreate-structure-detail" style="padding: 0 45px;">
          <ul>
            <li is="TopicCreateItem" v-for="(item, index) in topicList" :lititle="item" @remove="topicList.splice(index, 1)"></li>
          </ul>
        </div>
        <div class="teachercoursecreate-create-wrap">
          <div class="teachercoursecreate-plus" id="plus">
            <span @click="handleCreate"><Icon type="plus" color="#19be6b" /> 新增</span>
          </div>
          <div class="teachercoursecreate-topic-create" id="minus">
            <div class="teachercoursecreate-minus">
              <span @click="handleCollapse"><Icon type="minus" color="#2d8cf0" /> 收起</span>
            </div>
            <div class="teachercoursecreate-input">
              <span>章节主题</span>
              <div class="teachercoursecreate-input-wrap">
                <Input size="large" placeholder="章节主题" v-model="topictitle" />
              </div>
            </div>
            <div class="teachercoursecreate-button-wrap" style="clear:both; float:left; padding-left: 25px;">
              <Button type="success" @click="handleSaveTopic">保存此章节</Button>
            </div>
            <div class="float-clear">
            </div>
          </div>
          <div class="float-clear">
          </div>
        </div>
      </div>
      <div class="hr-wrap">
        <hr />
      </div>
      <div class="teachercoursecreate-button-wrap" style="float:right; padding:10px 10px 0 0;">
        <Button type="success">保存此课程</Button>
      </div>
    </div>
  </div>
</template>

<script>
import TopicCreateItem from './topiccreateitem';

export default {
  name: 'TeacherCourseCreate',
  data () {
    return {
      title: '',
      desc: '',
      topicList: [],
      topictitle: ''
    }
  },
  methods: {
    handleCreate: function () {
      console.log("HandleCreate");
      document.getElementById("plus").style.display = "none";
      document.getElementById("minus").style.display = "block";

    },
    handleCollapse: function () {
      console.log("HandleCollapse");
      document.getElementById("minus").style.display = "none";
      document.getElementById("plus").style.display = "block";
      this.topictitle = "";
    },
    handleSaveTopic: function () {
      console.log("HandleSaveTopic");
      document.getElementById("minus").style.display = "none";
      document.getElementById("plus").style.display = "block";
      this.topicList.push(this.topictitle);
      this.topictitle = "";
    }
  },
  components: {
    'TopicCreateItem': TopicCreateItem
  }
}
</script>

<style lang="css">
.hr-wrap {
  padding: 10px;
}
hr {
  height: 1px;
  border: none;
  border-bottom: 1px solid #dddee1;
}
.teachercoursecreate-wrap {
  width: 875px;
  float: right;
  padding: 0 10px;
  /* background-color: #fff; */
  height: 100%;
}
.teachercoursecreate-content {
  background-color: #fff;
  height: 100%;
}
.teachercoursecreate-label {
  /* float: left; */
  font-size: 1.1rem;
  font-weight: bold;
  padding: 20px 25px 5px;
}
.teachercoursecreate-label>p {
  text-align: left;
}
.teachercoursecreate-input {
  padding: 10px 25px;
  float: left;
  clear: both;
}
.teachercoursecreate-input>span {
  font-size: 1.1rem;
  padding: 8px 5px 7px 0;
}
.teachercoursecreate-input-wrap {
  width: 400px;
  display: inline-block;
}
.teachercoursecreate-create-wrap {
  padding: 10px 100px;
}
.teachercoursecreate-plus {
  /* display: none; */
}
.teachercoursecreate-topic-create {
  display: none;
}
.teachercoursecreate-plus>span, .teachercoursecreate-minus>span{
  white-space: pre-wrap;
  font-weight: bold;
  font-size: 1.05rem;
  text-align: left;
  cursor: pointer;
  float: left;
}
.teachercoursecreate-plus>span {
  color: #19be6b;
}
.teachercoursecreate-minus>span {
  color: #2d8cf0;
}
</style>
