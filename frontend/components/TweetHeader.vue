<template>
  <header class="py-3" :style="styles">
    <h2 class="text-center">
      <slot />
    </h2>
  </header>
</template>
<script>
export default {
  name: 'DetailHeaderComponent',
  props: {
    color: {
      type: String,
      default: 'blue'
    }
  },
  computed: {
    styles () {
      return {
        '--color': this.color
      }
    }
  },
  methods: {
    onPushBackBtn () {
      this.$router.go(-1)
    }
  }
}
</script>
<style lang="scss" scoped>
header {
  background-color: var(--color);
}
</style>
