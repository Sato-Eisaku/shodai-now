import Vue from 'vue'
import * as VueGoogleMaps from '~/node_modules/vue2-google-maps'

Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyBxklBL9qoEpCzU_FauMjZ5WG3YmBSGnpY',
    libraries: 'places',
    v: 'beta',
    map_id: 'e19735a90eb9d837'
  }
})
