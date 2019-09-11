<template lang="html">
  <div class="editsection-wrap">
    <div class="editsection-content" style="overflow-y: auto;">
      <!-- <div style="padding-top: 15px;">
      </div> -->
      <div class="editsection-label" style="text-align: left; padding: 15px 0;">
        <p style="font-size: 1.5em; font-weight: bold;" v-if="this.type === 'create'">新建小节</p>
        <p style="font-size: 1.5em; font-weight: bold;" v-else-if="this.type === 'edit'">编辑小节</p>
        <!-- <p style="font-size: 1.2em; font-weight: bold; color: #80848f;"></p> -->
      </div>
      <div class="editsection-title" style="padding-bottom: 10px;">
        <p style="float: left; text-align: left; padding: 7px 10px 7px 0;">小节名</p>
        <Input v-model="sectionTitle" placeholder="小节名" style="width: 300px; float: left;"/>
        <div class="float-clear">
        </div>
      </div>
      <div class="editsection-entity-type" style="padding-bottom: 10px;">
        <p style="float:left; text-align:left; padding-right: 10px;">内容类型</p>
        <RadioGroup v-model="entity.entityType" style="float: left;" @on-change="handleChange">
          <Radio label="video">
            <span>视频</span>
          </Radio>
          <Radio label="doc">
            <span>文档</span>
          </Radio>
        </RadioGroup>
        <div class="float-clear">
        </div>
      </div>
      <div class="editSection-insert-video" style="display: block;" id="editVideo">
        <Upload type="drag" format=".mp4, .flv">
          <div style="padding: 20px 0;">
            <Icon type="ios-cloud-upload" size="52" style="color: #3399ff;" />
            <p>点击选择文件或拖拽文件到此处</p>
          </div>
        </Upload>
      </div>
      <div class="createsection-insert-doc" style="display: none; width: 790px;" id="editDoc">
        <!-- <mavon-editor style="height: 500px; width: 805px;" /> -->
        <EditorMd :isView="docshow" :initData="entity.content" style="z-index: 10000;"/>
      </div>
      <div class="hr-wrap">
        <hr />
      </div>
      <Button type="success" style="margin-bottom: 20px; float:right;" @click="handleSave">保存此节</Button>
    </div>
  </div>
</template>

<script>
import mavonEditor from 'mavon-editor';
import 'mavon-editor/dist/css/index.css';
import EditorMd from './mdeditor';
import Hub from '../assets/hub.js';

export default {
  name: 'TeacherSectionEdit',
  data () {
    return {
      type: '',
      entity: {
        entityType: 'video',
        url: ''
      },
      sectionid: '',
      topicid: '',
      courseid: '',
      sectionTitle: '',
      docshow: false
    }
  },
  components: {
    'mavon-editor': mavonEditor.mavonEditor,
    'EditorMd': EditorMd
  },
  methods: {
    initComp: function () {
      if (this.$route.name.indexOf("TeacherSectionCreate") != -1) {
        // Create Section
        this.type = 'create';
      } else if (this.$route.name.indexOf("TeacherSectionEdit") != -1) {
        // Edit Section
        this.type = 'edit';
        this.sectionTitle = 'SectionTitle from remote server...';
        this.sectionid = this.$route.params.sectionid;
        this.topicid = this.$route.params.topicid;
        this.courseid = this.$route.params.courseid;
        // load data from remote server
        // this.entity = {
        //   entityType: 'doc',
        //   content: 'asdjfhgausdyfgasdjhfbasdf'
        // }
        this.entity = {
          entityType: 'video',
          url: '1287436410283'
        }
        if (this.entity.entityType === 'doc') {
          document.getElementById('editVideo').style.display = "none";
          document.getElementById('editDoc').style.display = "block";
          this.docshow = true;
        } else if (this.entityType === 'video') {

        }
      }
    },
    handleChange: function (cur) {
      if (cur === 'video') {
        document.getElementById('editDoc').style.display = "none";
        document.getElementById('editVideo').style.display = "block";
      } else if (cur === 'doc') {
        document.getElementById('editVideo').style.display = "none";
        document.getElementById('editDoc').style.display = "block";
        this.docshow = true;
      }
    },
    handleSave: function () {
      if (this.sectionTitle === '') {
        alert("小节名不能为空");
      } else if (this.entity.entityType === 'video' && this.entity.url === '') {
        alert("请上传视频");
      }
      console.log("保存~");
    }
  },
  mounted () {
    console.log(this.$route.name);
    this.initComp();
  }
}
</script>

<style lang="css">
.hr-wrap {
  padding: 10px 0;
}
hr {
  height: 1px;
  border: none;
  border-bottom: 1px solid #dddee1;
}
.float-clear {
  clear: both;
}
.editsection-wrap {
  width: 875px;
  height: 100%;
  background-color: #f8f8f9;
  float: right;
  padding: 0 10px;
}
.editsection-content {
  height: 100%;
  background-color: #fff;
  padding: 0 25px;
}
</style>
