<template lang="html">
  <div class="problemcard-wrap">
    <div class="problemcard-title-wrap">
      <p>答题卡</p>
    </div>
    <div class="problemcard-nav-wrap" id="practicecard">
      <div v-for="i in handleCreate" class="problemcard-nav" :id="'pc'+i" style="cursor: pointer;" @click="pSelected($event)">
        <p>{{ i+1 }}</p>
      </div>
      <!-- <div id="pc1" class="problemcard-nav problemcard-cur" @click="pSelected($event)">
        <p>1</p>
      </div>
      <div id="pc2" class="problemcard-nav problemcard-no" @click="pSelected($event)">
        <p>2</p> -->
      </div>
      <div class="float-clear">
      </div>
    </div>
  </div>
</template>

<script>
import $ from 'jquery';

export default {
  name: 'ProblemCard',
  data () {
    return {
      handleCreate: []
    }
  },
  props: ['problemcount', 'curproblem'],
  methods: {
    pSelected: function (e) {
      var pid = e.path[1].attributes["id"].value;
      var ele = document.getElementById(pid);
      var className = ele.attributes["class"].value;
      var curid, nxtid;
      console.log(pid, ele, className);
      if (className.indexOf('problemcard-cur') != -1) {
        return;
      } else {
        var l = $("#practicecard").children();
        console.log(l);
        for (var i = 0; i < l.length; i++) {
          if (l[i].id === pid) {
            $("#"+pid).addClass("problemcard-cur");
            nxtid = i;
          } else if (l[i].className.indexOf("problemcard-cur") != -1) {
            $("#"+l[i].id).removeClass("problemcard-cur");
            curid = i;
          }
        }
        this.$emit('change', {next: nxtid});
        curid = "p"+curid;
        nxtid = "p"+nxtid;
        document.getElementById(curid).style.display = "none";
        document.getElementById(nxtid).style.display = "block";
      }
    },
    initCard: function () {
      // $("#pc0").attr({style: "display: block; cursor: pointer;"}).addClass("problemcard-cur");
      // $("#p0").attr({style: "display: block;"});
      document.getElementById('pc0').style.display = 'block';
      document.getElementById('pc0').style.cursor = 'pointer';
      document.getElementById('pc0').className += ' problemcard-cur';
      document.getElementById('p0').style.display = 'block';
    }
  },
  created () {
    for (var i = 0; i < this.problemcount; i++) {
      this.handleCreate.push(i);
      // console.log('push here');
    }
    // this.initCard();
    // console.log(this.handleCreate);
  },
  mounted () {
    this.initCard();
  },
  watch: {
    // curproblem: function (cur) {
    //   var curid = "pc"+cur;
    //   var eles = document.getElementById('practice-card').children;
    //   for (var i = 0; i < eles.length; i++) {
    //     if (eles[i].id === curid)
    //   }
    // }
  }
}
</script>

<style lang="css">
.problemcard-wrap {
  background-color: #fff;
  padding: 15px 20px;
  margin-bottom: 15px;
}
.problemcard-title-wrap>p {
  text-align: left;
  font-size: 1.2rem;
  font-weight: bold;
}
.problemcard-nav-wrap {
  padding: 10px 0;
}
.problemcard-nav {
  float: left;
  width: 41px;
  height: 41px;
  /* background-color: #2d8cf0; */
  margin-right: 5px;
  /* color: #fff; */
}
.problemcard-nav>p, .problemcard-yes>p, .problemcard-no>p {
  font-size: 1.2rem;
  color: inherit;
  font-weight: bold;
  padding: 8px 0;
}
.problemcard-cur, .problemcard-yes {
  transition-property: background-color,color;
  transition-duration: 300ms;
  background-color: #2d8cf0;
  color: #fff;
}
.problemcard-no {
  background-color: #fff;
  color: #2d8cf0;
}
.problemcard-correct {
  background-color: #19be6b;
  color: #fff;
}
.problemcard-false {
  background-color: #ed3f14;
  color: #fff;
}
</style>
