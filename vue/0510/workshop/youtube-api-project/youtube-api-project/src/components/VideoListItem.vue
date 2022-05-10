<template>
  <li @click="selectedVideo">
      <img :src="imgSrc" alt="Thumbnail">
      <!-- <span>{{ video.snippet.title }}</span> -->
      <span>{{ video.snippet.title | unEscapeString }}</span>
  </li>
</template>

<script>
import _ from 'lodash'
// console.log(_.unescape(video.snippet.title))
export default {
    name: 'VideoListItem',
    props: {
        video: Object
    },
    methods: {
        selectedVideo() {
            this.$emit('select-video', this.video)
        }
    },
    filters: {
        unEscapeString(rawText) {
        return _.unescape(rawText)
        }
    },
    computed: {
        imgSrc() {
            return this.video.snippet.thumbnails.default.url
        },
        // unEscapeString() {
        //     return _.unescape(this.video.snippet.title)
        // }
    }
}
</script>

<style>

</style>