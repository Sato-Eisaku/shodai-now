<template>
  <div>
    <div>
      <GmapMap
        map-type-id="roadmap"
        :center="maplocation"
        :zoom="zoom"
        :style="windowSize"
        :options="mapOptions"
      />
    </div>
    <div>
      {{ width }}
      {{ height }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'IndexPage',
  data () {
    return {
      maplocation: { lng: 140.97968100823005, lat: 43.190798914709084 },
      zoom: 21,
      styleMap: {
        width: '100%',
        height: '1000px'
      },
      mapOptions: {
        fullscreenControl: false,
        streetViewControl: false,
        styles: []
      },
      windowSize: {
        width: '100%',
        height: window.innerHeight + 'px'
      }
    }
  },
  mounted () {
    window.addEventListener('resize', this.handleResize)
  },
  beforeDestroy () {
    window.removeEventListener('resize', this.handleResize)
  },
  methods: {
    handleResize () {
      this.width = window.innerWidth
      this.height = window.innerHeitht
    }
  }
}
</script>
