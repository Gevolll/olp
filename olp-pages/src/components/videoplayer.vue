<template lang="html">
  <div class="videoplayer-main">
    <div class="video-player">
      <video id="videoElement" width="720" height="540" controls>
      </video>
    </div>
    <div class="video-control-pad">
      <div class="control-title-label">
        <p>课程目录</p>
      </div>
      <div class="control-section-list-wrap">
        <CourseOutlineSmall :relatedcourse="this.relatedcourse" />
      </div>
    </div>
    <div class="float-clear">
    </div>
  </div>
</template>

<script>
import flvjs from 'flv.js';
import CourseOutlineSmall from './courseoutlinesmall';

export default {
  name: 'VideoPlayer',
  data () {
    return {
      videoId: '12376345',
      vlength: 1126,
      url: '/static/test400k.mp4'
    }
  },
  props: ['videoid', 'relatedcourse'],
  created () {
    console.log(this.videoid);
    console.log(this.relatedcourse);
  },
  mounted () {
    var player = document.getElementById('videoElement');
    console.log("videoelement: "+player);
    if (flvjs.isSupported()) {
      console.log("here!");
      var flvPlayer = flvjs.createPlayer({
        type: 'mp4',
        url: '/static/test400k.mp4'
      });
      flvPlayer.attachMediaElement(player);
      flvPlayer.load();
      // this.vp = player;
    }
  },
  components: {
    'CourseOutlineSmall': CourseOutlineSmall
  }
}
</script>

<style lang="css">
#videoElement {
  background-color: black;
}
.video-player {
  float: left;
}
.float-clear {
  clear: both;
}
.video-control-pad {
  float: right;
  height: 540px;
  width: 455px;
  background-color: #ffffff;
  box-shadow: 0 0 8px #e2e2e2;
  padding: 10px 20px;
}
.control-title-label {
  padding-bottom: 5px;
}
.control-title-label>p {
  font-size: 1.25rem;
  font-weight: bold;
  text-align: left;
  color: #80848f;
}
</style>
