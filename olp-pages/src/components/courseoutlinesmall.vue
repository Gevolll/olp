<template lang="html">
  <div class="courseoutlinesmall-list">
    <div class="courseoutlinesmall-item courseoutlinesmall-item-mid" v-for="(section, index) in sections">
      <div class="courseoutlinesmall-item-section-info">
        <div class="courseoutlinesmall-item-section-number section-number-off" v-if="section.status === 0">
          <p>{{ index+1 }}</p>
        </div>
        <div class="courseoutlinesmall-item-section-number section-number-learning" v-if="section.status === 1">
          <p>{{ index+1 }}</p>
        </div>
        <div class="courseoutlinesmall-item-section-number section-number-finish" v-if="section.status === 2">
          <p>{{ index+1 }}</p>
        </div>
        <div class="courseoutlinesmall-item-section-title">
          <p><router-link :to="{ name: 'Section', params: {id: section.id} }">{{ section.title }}</router-link></p>
        </div>
        <div class="courseoutlinesmall-item-section-other" v-if="section.entity.type === 'video'">
          <p>{{ parseDuration(section.entity.length) }}</p>
        </div>
        <div class="courseoutlinesmall-item-section-other" v-else-if="section.entity.type === 'doc'">
          <p>{{ 讲义 }}</p>
        </div>
        <div class="float-clear">
        </div>
      </div>
      <div class="courseoutlinesmall-item-section-description">
        <div class="courseoutlinesmall-item-section-description-wrap">
          <p>{{ section.desc }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CourseOutlineSmall',
  data () {
    return {
      sections: [
        {
          id: '123456787654',
          title: 'Java 基础 1',
          desc: '本课时介绍移动开发操作系统的发展历史，对 Android 的各个版本逐一回顾，简单讲解 Android 系统的构成，帮助大家快速了解 Android 体系的整体情况',
          entity: {
            type: 'video',
            length: 1182
          },
          status: 0
        }
      ]
    }
  },
  props: ['relatedcourse'],
  methods: {
    parseDuration: function (dur) {
      var min = parseInt(dur/60);
      var sec = dur%60;
      var smin, ssec;
      if (min < 10) {
        smin = '0'+min.toString();
      } else {
        smin = min.toString();
      }
      if (sec < 10) {
        ssec = '0'+sec.toString();
      } else {
        ssec = sec.toString();
      }
      return smin+':'+ssec;
    }
  }
}
</script>

<style lang="css">
a, a:hover, a:visited, a:active {
  color: inherit;
}
.courseoutlinesmall-list {
  width: 415px;
  height: 489px;
  overflow-y: auto;
  padding: 10px 5px 0;
}
.courseoutlinesmall-item-mid {
  padding-bottom: 15px;
}
.courseoutlinesmall-item-section-info {
  padding-bottom: 5px;
}
.courseoutlinesmall-item-section-number {
  float: left;
  height: 20px;
  width: 20px;
  border-radius: 50%;
  padding: 1px 0 2px;
}
.section-number-off {
  background-color: #bbbec4;
}
.section-number-on {
  background-color: #2d8cf0;
}
.courseoutlinesmall-item-section-number>p {
  padding: 1px 0;
  font-weight: bold;
  color: #fff;
}
.courseoutlinesmall-item-section-title {
  float: left;
}
.courseoutlinesmall-item-section-title>p {
  padding-left: 10px;
  font-size: 1.1rem;
  white-space: pre-wrap;
}
.courseoutlinesmall-item-section-other {
  float: right;
}
.courseoutlinesmall-item-section-other>p {
  padding: 2px 0 3px;
  color: #80848f;
}
.courseoutlinesmall-item-section-description {
  padding-left: 30px;
}
.courseoutlinesmall-item-section-description-wrap>p {
  text-align: left;
  color: #80848f;
}
</style>
