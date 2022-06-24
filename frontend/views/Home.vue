<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App" />
    <MapPane />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import MapPane from '@/components/MapPane.vue'

export default {
  name: 'HomePage',
  components: {
    HelloWorld,
    MapPane
  }
}
</script>
