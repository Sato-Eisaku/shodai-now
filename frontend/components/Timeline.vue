<template>
  <a class="twitter-timeline" href="https://twitter.com/k_y_kenzen/timelines/1539667358117433344?ref_src=twsrc%5Etfw">テスト1 - Curated tweets by k_y_kenzen</a>
</template>
<script>
export default {
  name: 'TimelineComponent',
  mounted () {
    const script = document.createElement('script')
    script.src = 'https://platform.twitter.com/widgets.js'
    document.body.appendChild(script)
  }
}
</script>
