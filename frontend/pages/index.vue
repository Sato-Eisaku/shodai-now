<template>
  <div id="mapwrapper" ref="mapview" :style="{ height: `${mapHeight}vh` }">
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
    <v-bottom-sheet
      v-model="isShow"
      scrollable
    >
      <TimelinePane v-if="isShow" :position-tag="hashtag" :timeline-id="collection" />
    </v-bottom-sheet>
  </div>
</template>

<script>
export default {
  name: 'IndexPage',
  data () {
    return {
      isShow: false,
      hashtag: '',
      collection: '',
      mapHeight: 100,
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
          position: { lat: 43.1907916429676, lng: 140.97981462865556 },
          hashtag: '図書館前',
          collection: '1540351285010255873'
        },
        {
          id: 'booth_front_build3',
          position: { lat: 43.190670455840014, lng: 140.97955199082952 },
          hashtag: '3号館前',
          collection: '1540351184464400384'
        },
        {
          id: 'booth_front_buidl4',
          position: { lat: 43.19089662719827, lng: 140.97955477719526 },
          hashtag: '4号館前',
          collection: '1540351325091020801'
        },
        {
          id: 'build3',
          position: { lat: 43.19049292413861, lng: 140.9796521870865 },
          hashtag: '3号館',
          collection: '1540351089069162496'
        },
        {
          id: 'stage',
          position: { lat: 43.19118755139948, lng: 140.9801785173844 },
          hashtag: 'ステージ',
          collection: '1540351357831753728'
        }
      ]
    }
  },
  watch: {
    isShow (newValue) {
      if (newValue === true) {
        this.mapHeight = 20
      } else {
        this.mapHeight = 100
      }
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
      this.isShow = true
      this.hashtag = this.markers[index].hashtag
      this.collection = this.markers[index].collection
    }
  }
}
</script>

<style lang="scss" scoped>
</style>
