<template>
  <a class="twitter-timeline" :href="`https://twitter.com/k_y_kenzen/timelines/${timelineId}?ref_src=twsrc%5Etfw`" />
</template>

<script>
export default {
  name: 'TimelineComponent',
  props: {
    timelineId: {
      type: String,
      default: '',
      require: true
    }
  },
  mounted () {
    const script = document.createElement('script')
    script.src = 'https://platform.twitter.com/widgets.js'
    document.body.appendChild(script)
  }
}
</script>

<style lang="scss" scoped>
#timeline {

}
</style>
