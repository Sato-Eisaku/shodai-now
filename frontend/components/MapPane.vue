<template>
  <div class="mapPane">
    <!--マップ-->
    <MapImage
      :center="center"
      :zoom="zoom"
    />
  </div>
</template>

<script>
import MapImage from '@/assets/map.svg'

export default {
  name: 'MapPane',
  components: {
    MapImage
  },
  data () {
    return {
      center: [139.767, 35.681],
      zoom: 13
    }
  }
}
</script>

<style scoped>
    .mapPane {
        height: 600px;
        margin: 0;
        text-align: left;
    }
</style>
