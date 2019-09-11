<template lang="html">
  <Input width="300px" placeholder="小节名" v-modal="sectionTitle" />
</template>

<script>
export default {
  name: 'ModalInput',
  data () {
    return {
      sectionTitle: this.sName
    }
  },
  props: ['sName']
}
</script>

<style lang="css">
</style>
