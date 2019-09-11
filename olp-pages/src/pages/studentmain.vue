<template lang="html">
  <div class="main">
    <Header />
    <div class="content-wrap">
      <div class="content">
        <LeftNav />
        <router-view />
        <div class="float-clear">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Header from '../components/header';
import LeftNav from '../components/leftnav';

export default {
  name: 'StudentMain',
  data () {
    return {

    }
  },
  components: {
    'Header': Header,
    'LeftNav': LeftNav
  }
}
</script>

<style scoped lang="css">
.main {
  background-color: #f8f8f9;
  height: 100%;
}
.content-wrap {
  background-color: #f8f8f9;
  height: 100%;
}
.content {
  width: 1175px;
  height: 100%;
  margin: 0 auto;
  padding-top: 15px;
  padding-bottom: 15px;
}
</style>
