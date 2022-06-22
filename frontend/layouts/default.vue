<template>
  <!-- アプリ全体をダークモードにする -->
  <v-app dark>
    <v-app-bar
      color="light-blue"
      dark
      dence
      app
    >
      <v-app-bar-nav-icon @click="drawer = true" />
      <v-toolbar-title class="flex text-center">
        #商大なう
      </v-toolbar-title>
      <v-app-bar-nav-icon style="visibility:hidden;" />
    </v-app-bar>
    <v-main>
      <Nuxt />
    </v-main>
    <!-- ハンバーガーメニューの中身 -->
    <v-navigation-drawer
      v-model="drawer"
      absolute
      light
      temporary
    >
      <v-list
        nav
        dense
      >
        <v-list-item-group
          v-model="group"
          active-class="deep-purple--text text--accent-4"
        >
          <!-- 各メニューをループで作成 -->
          <v-list-item @click="drawer = false">
            <v-list-item-action>
              <v-list-item-icon>
                <v-icon>mdi-menu</v-icon>
              </v-list-item-icon>
            </v-list-item-action>
          </v-list-item>
          <v-list-item
            v-for="item in naviItems"
            :key="item.title"
            :to="item.to_page"
            @click="drawer=false"
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </v-app>
</template>

<script>
export default {
  name: 'DefaultLayout',
  data () {
    return {
      drawer: false,
      group: null,
      naviItems: [
        {
          to_page: 'map',
          icon: 'mdi-map-search',
          title: 'マップ'
        },
        {
          to_page: 'tweet_list',
          icon: 'mdi-format-list-text',
          title: 'ツイート一覧'
        }
      ]
    }
  }
}
</script>
