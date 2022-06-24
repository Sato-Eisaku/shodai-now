<template>
  <v-card>
    <TweetHeader color="#ffffff" class="">
      #商大なう #{{ positionTag }}
    </TweetHeader>
    <TweetButton class="my-5" :position-tag="positionTag" />
    <v-card-text style="height: 60vh;">
      <Timeline :timeline-id="timelineId" />
    </v-card-text>
    <v-divider />
  </v-card>
</template>

<script>
export default {
  props: {
    positionTag: {
      type: String,
      default: '',
      require: true
    },
    timelineId: {
      type: String,
      default: '',
      require: true
    }
  },
  mounted () {

  }
}
</script>
