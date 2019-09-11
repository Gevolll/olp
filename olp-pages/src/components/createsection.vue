<template lang="html">
  <Modal :value="clicked" title="新建小节" width="1000px" @on-ok="handleOk" @on-cancel="handleCancel" mask-closable="false">
    <div class="createsection-input-wrap" style="padding-bottom: 10px;">
      <p style="float: left; padding: 7px 5px 7px 0; font-weight: bold;">小节名</p>
      <Input placeholder="小节名" style="width: 300px;" id="inputSectionTitle" />
    </div>
    <div class="createsection-entity-type" style="padding-bottom: 10px;">
      <p style="float: left; padding-right: 5px; font-weight: bold;">内容类型</p>
      <RadioGroup v-model="entityType" @on-change="handleChange">
        <Radio label="video">
          <span>视频</span>
        </Radio>
        <Radio label="doc">
          <span>文档</span>
        </Radio>
      </RadioGroup>
    </div>
    <div class="createsection-insert-video" style="display: block;" id="insert-video">
      <Upload type="drag" format=".mp4, .flv">
        <div style="padding: 20px 0;">
          <Icon type="ios-cloud-upload" size="52" style="color: #3399ff;" />
          <p>点击选择文件或拖拽文件到此处</p>
        </div>
      </Upload>
    </div>
    <div class="createsection-insert-doc" style="display: none;" id="insert-doc">
      <mavon-editor style="height: 640px; width: 970px;" />
    </div>
  </Modal>
</template>

<script>
import mavonEditor from 'mavon-editor';
import 'mavon-editor/dist/css/index.css';

export default {
  name: 'CreateSection',
  data () {
    return {
      entityType: 'video',
      sTitle: ''
    }
  },
  props:['clicked'],
  mounted () {
  },
  components: {
    'mavon-editor': mavonEditor.mavonEditor
  },
  methods: {
    handleChange: function (cur) {
      // console.log(cur);
      if (cur === 'video') {
        document.getElementById('insert-doc').style.display = "none";
        document.getElementById('insert-video').style.display = "block";
      } else if (cur === 'doc') {
        document.getElementById('insert-video').style.display = "none";
        document.getElementById('insert-doc').style.display = "block";
      }
    },
    handleOk: function () {
      this.$emit('close');
      // console.log(this.sTitle);
      this.sTitle = document.getElementById('inputSectionTitle').children[1].value;
      var d = {
        id: '',
        sectionTitle: this.sTitle,
        entityType: this.entityType
      };
      this.$emit('save', d);
    },
    handleCancel: function () {
      this.$emit('close');
    }
  }
}
</script>

<style lang="css">
</style>
