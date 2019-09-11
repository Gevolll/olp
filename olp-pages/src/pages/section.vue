<template lang="html">
  <div class="section-main">
    <Header style="position: fixed; z-index: 100;" v-if="entity.type==='doc'"/>
    <Header v-else />
    <div class="content-wrap">
      <div class="section-content">
        <div class="videoplayer-wrap" v-if="entity.type === 'video'">
          <VideoPlayer :videoid="entity.id" :relatedcourse="relatedCourse" />
        </div>
        <div class="doc-wrap" v-if="entity.type === 'doc'">
          <DocReader :docid="entity.id" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Header from '../components/header';
import VideoPlayer from '../components/videoplayer';
import DocReader from '../components/docreader';

export default {
  name: 'Section',
  data () {
    return {
      id: '12345',
      relatedCourse: '23456',
      relatedTopic: '34567',
      entity: {
        id: '12121212',
        type: 'video',
        // type: 'doc',
        duration: 1128
      },
      status: 1
    }
  },
  created () {
    console.log(this.$route.params.id);
  },
  components: {
    'Header': Header,
    'VideoPlayer': VideoPlayer,
    'DocReader': DocReader
  }
}
</script>

<style scoped lang="css">
.section-main {
  height: 100%;
  background-color: #f8f8f9;
}
.content-wrap {
  /* height: 100%; */
  background-color: #f8f8f9;
}
.section-content {
  width: 1175px;
  margin: 0 auto;
  padding: 10px 0;
  background-color: #f8f8f9;
  /* margin-top:  */
}
.videoplayer-wrap {
  width: 1175px;
}
.doc-wrap {
  width: 1175px;
  background-color: #f8f8f9;
}
</style>
