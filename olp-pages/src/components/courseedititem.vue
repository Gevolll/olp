<template lang="html">
  <div class="teachercourseedit-list-item">
    <div class="topictitle-label" :data-tid="id">
      <p>{{topicTitle}}</p>
      <p style="font-size: 0.6rem;"><span class="span-edit" @click="handleEditTopic">编辑  </span><span class="span-remove" @click="handleRemoveTopic($event)">删除  </span><span class="span-open" @click="handleOpen">展开</span></p>
    </div>
    <div class="section-list" style="display: none;">
      <p v-for="section in sections" :data-sid="section.id">    {{section.sectionTitle}}<span class="span-edit" @click="handleEditSection($event)">    编辑  </span><span class="span-remove" @click="handleRemoveSection($event)">删除  </span></p>
      <p><span style="cursor: pointer" @click="handleAddSection"><Icon type="plus" /> 新增小节</span></p>
      <!-- <CreateSection :clicked="onCreateSection" @close="handleClose" @save="handleSave" /> -->
    </div>
  </div>
</template>

<script>
import CreateSection from './createsection.vue';
import EditSection from './editsection.vue';
import Hub from '../assets/hub.js';

export default {
  name: 'CourseEditItem',
  data () {
    return {
      courseid: '',
      id: '',
      topicTitle: '',
      sections: ''
      // onCreateSection: false,
      // onEditSection: false,
      // onCreateTopic: false,
      // onEditTopic: false
      // sectionTemp: {}
    }
  },
  props: ['topic'],
  methods: {
    initComp: function () {
      this.courseid = this.$route.params.id;
      this.id = this.topic.id;
      this.topicTitle = this.topic.topicTitle;
      this.sections = this.topic.sections;
    },
    handleOpen: function (e) {
      var cur = e.path[0].className;
      // console.log(cur);
      if(cur.indexOf('span-open') != -1) {
        // Open
        e.path[3].children[1].style.display = "block";
        e.path[0].className = "span-close";
        e.path[0].innerText = "收起";
      } else if (cur.indexOf('span-close') != -1) {
        // Collapse
        e.path[3].children[1].style.display = "none";
        e.path[0].className = "span-open";
        e.path[0].innerText = "展开";
      }
      // console.log(e.path[3].children[1]);
    },
    handleEditTopic: function () {
      this.$router.push({path: '/teachermain/topicEdit/'+this.courseid+"/"+this.id});
    },
    handleRemoveTopic: function (e) {
      console.log(e.path[2].dataset.tid);
      var topicid = e.path[2].dataset.tid;
      this.$emit("removetopic", topicid);
    },
    handleEditSection: function (e) {
      console.log(e.path[1].dataset.sid);
      var sectionid = e.path[1].dataset.sid;
      this.$router.push({path: '/teachermain/sectionEdit/'+this.courseid+'/'+this.id+'/'+sectionid});
    },
    handleRemoveSection: function (e) {
      console.log(e.path[1].dataset.sid);
      var sectionid = e.path[1].dataset.sid;
      this.$emit("removesection", sectionid);
    },
    handleAddSection: function () {
      this.$router.push({path: '/teachermain/sectionCreate/'+this.courseid+'/'+this.id});
    }
    // handleEdit: function (e) {
    //   var sectionTemp;
    //   console.log(e.path[2].className);
    //   var outerClass = e.path[2].className;
    //   if (outerClass.indexOf('topic') != -1) {
    //     // editTopic
    //     console.log('Edit topic..');
    //     this.$router.push({path: '/teachermain/topicEdit/'});
    //   } else if (outerClass.indexOf('section') != -1) {
    //     // editSection
    //     console.log('Edit Section...');
    //     var sid = e.path[1].dataset.sid;
    //     for (var i = 0; i < this.sections.length; i++) {
    //       if (sid === this.sections[i].id) {
    //         sectionTemp = this.sections[i];
    //         this.$router.push({name: 'TeacherSectionEdit', params:{id:sid}});
    //         Hub.$emit('EditSection', sectionTemp);
    //         // this.onEditSection = true;
    //         // window.location.assign("localhost:8080/#/teachermain/sectionEdit/123")
    //         return;
    //       }
    //     }
    //     // this.onModal = true;
    //   }
    //   // var outer = e.path[].
    // },
    // handleRemove: function (e) {
    //   var outerClass = e.path[2].className;
    //   if (outerClass.indexOf('topic') != -1) {
    //     // remove all topic
    //     this.$emit('removetopic', this.id.toString());
    //   } else if (outerClass.indexOf('section') != -1) {
    //     // remove this section
    //     // console.log(e.path[1].dataset.sid);
    //     this.$emit('removesection', e.path[1].dataset.sid);
    //   }
    // },
    // handleNewSection: function (e) {
    //   this.onCreateSection = true;
    // },
    // handleClose: function () {
    //   this.onCreateSection = false;
    //   this.onCreateTopic = false;
    //   this.onEditSection = false;
    //   this.onEditTopic = false;
    // },
    // handleSave: function (d) {
    //   this.sections.push(d);
    //   console.log(d);
    //   console.log(this.sections);
    // }
  },
  components: {
    'CreateSection': CreateSection,
    'EditSection': EditSection
  },
  mounted () {
    console.log(this.topic);
    this.initComp();
  }
}
</script>

<style lang="css">
</style>
