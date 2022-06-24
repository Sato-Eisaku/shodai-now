<template>
  <div id="mapwrapper" ref="mapview">
    <GmapMap
      ref="map"
      map-type-id="roadmap"
      :center="maplocation"
      :zoom="zoom"
      :style="styleMap"
      :options="mapOptions"
    >
      <GmapMarker
        v-for="(m,index) in markers"
        :key="index"
        :position="m.position"
        :clickable="true"
        @click="onClickMarker(index)"
      />
    </GmapMap>
  </div>
</template>

<script>
export default {
  name: 'IndexPage',
  data () {
    return {
      maplocation: { lat: 43.190795509654166, lng: 140.97981892674588 },
      zoom: 19,
      styleMap: {
        width: '100%',
        height: '100%'
      },
      mapOptions: {
        fullscreenControl: false,
        streetViewControl: false,
        styles: [],
        zoomControl: false,
        gestureHandling: 'greedy',
        mapTypeControl: false,
        restriction: {
          latLngBounds: {
            north: 43.19232016564403,
            south: 43.18937670561365,
            west: 140.97875719737712,
            east: 140.98104635954286
          }
        }
      },
      markers: [
        {
          id: 'booth_front_library',
          position: { lat: 43.1907916429676, lng: 140.97981462865556 }
        },
        {
          id: 'booth_front_build3',
          position: { lat: 43.190670455840014, lng: 140.97955199082952 }
        },
        {
          id: 'booth_front_buidl4',
          position: { lat: 43.19089662719827, lng: 140.97955477719526 }
        },
        {
          id: 'build3',
          position: { lat: 43.19049292413861, lng: 140.9796521870865 }
        },
        {
          id: 'stage',
          position: { lat: 43.19118755139948, lng: 140.9801785173844 }
        }
      ]
    }
  },
  mounted () {
    const dom = this.$refs.mapview

    const rect = dom.getBoundingClientRect()
    this.styleMap = {
      width: '100%',
      height: rect.offsetHeight + 'px'
    }
  },
  methods: {
    onClickMarker (index) {
      this.$refs.map.$mapPromise.then((map) => {
        map.panTo(this.markers[index].position)
      })
    }
  }
}
</script>

<style lang="scss" scoped>
  #mapwrapper{
    height: 100vh
  }
</style>
