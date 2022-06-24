<template>
  <v-bottom-sheet
    v-model="isShow"
    scrollable
  >
    <TimelinePane />
  </v-bottom-sheet>
</template>

<script>
export default {
  data () {
    return {
      isShow: true
    }
  }
}
</script>
