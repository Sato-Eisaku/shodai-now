<template>
  <v-container>
    <v-row justify="center">
      <v-btn
        color="primary"
        :href="`https://twitter.com/intent/tweet?hashtags=商大なう,${positionTag}&ref_src=twsrc%5Etfw`"
      >
        <v-icon>
          mdi-twitter
        </v-icon>
        ここでつぶやく
      </v-btn>
    </v-row>
  </v-container>
</template>

<script>
export default {
  props: {
    positionTag: {
      type: String,
      default: '',
      require: true
    }
  }
}
</script>
