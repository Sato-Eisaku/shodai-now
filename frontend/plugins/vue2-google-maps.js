import Vue from 'vue'
import * as VueGoogleMaps from '~/node_modules/vue2-google-maps'

Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyBxklBL9qoEpCzU_FauMjZ5WG3YmBSGnpY',
    // key: process.env.MAP_API_KEY,
    libraries: 'places'
  }
})
