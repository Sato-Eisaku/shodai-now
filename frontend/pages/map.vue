<template>
  <div>
    <v-container class="white">
      <MapImage />
    </v-container>
  </div>
</template>

<script>
import MapImage from '@/assets/map.svg'

export default {
  name: 'MapPage',
  components: {
    MapImage
  }
}
</script>
