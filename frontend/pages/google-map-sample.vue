<template>
  <div id="map" />
</template>

<script>
import { Loader } from '@googlemaps/js-api-loader'

export default {
  data () {
    return {
      loader: null,
      map: null
    }
  },
  mounted () {
    this.loader = new Loader({
      apiKey: this.$config.mapApiKey,
      version: 'weekly',
      libraries: ['places']
    })

    this.loader
      .load()
      .then(function (google) {
        const myLatLng = { lat: -25.363, lng: 131.044 }
        this.map = new google.maps.Map(document.getElementById('map'), {
          zoom: 4,
          center: myLatLng,
          disableDefaultUI: true,
          gestureHandling: 'greedy'
        })
      })
      .catch((e) => {
        // do something
      })
  }
}
</script>

<style scoped>
#map {
  height: 100vh;
}
</style>
