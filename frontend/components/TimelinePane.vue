<template>
  <v-card>
    <TweetHeader color="#000000">
      #商大なう
    </TweetHeader>
    <TweetButton class="my-5" />
    <v-card-text style="height: 60vh;">
      <Timeline />
    </v-card-text>
    <v-divider />
  </v-card>
</template>

<script>
export default {
  mounted () {
    const script = document.createElement('script')
    script.src = 'https://platform.twitter.com/widgets.js'
    document.body.appendChild(script)
  }
}
</script>
