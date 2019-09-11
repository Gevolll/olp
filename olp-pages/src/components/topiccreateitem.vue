<template lang="html">
  <li style="font-size: 1rem; padding-bottom: 2px;">
    {{lititle}}
    <span style="color: #ed3f14; cursor: pointer;" @click="$emit('remove')">
      &nbsp;&nbsp;&nbsp;
      <Icon type="minus" />
      &nbsp;删除
    </span>
  </li>
</template>

<script>
export default {
  name: 'TopicCreateItem',
  props: ['lititle']
}
</script>

<style lang="css">
</style>
