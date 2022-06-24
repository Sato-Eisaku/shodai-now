<template>
  <div>
    <v-text-field
      v-model="tlId"
      label="テスト"
    />
    <v-btn
      @click="isShow = true"
    >
      テスト
    </v-btn>
    <v-bottom-sheet
      v-model="isShow"
      scrollable
    >
      <TimelinePane v-if="isShow" :position-tag="'test'" :timeline-id="tlId" />
    </v-bottom-sheet>
  </div>
</template>

<script>
export default {
  data () {
    return {
      isShow: true,
      tlId: ''
    }
  },
  methods: {
    onClickButton () {
      this.isShow = true
    }
  }
}
</script>
