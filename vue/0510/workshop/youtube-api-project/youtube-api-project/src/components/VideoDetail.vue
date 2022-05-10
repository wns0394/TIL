<template>
  <div class="video-detail" v-if="video">
      <div class="video-container">
        <iframe :src="videoURI" frameborder="0"></iframe>
      </div>

      <div class="detail">
        <h2>{{ video.snippet.title | unEscapeString}}</h2>
        <p>{{ video.snippet.description | unEscapeString}}</p>
      </div>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
    name: 'VideoDetail',
    props: {
        video: Object
    },
    computed: {
        videoURI() {
            // const videoId = this.video.id.videoId
            const { videoId } = this.video.id
            return `https://www.youtube.com/embed/${videoId}`
        }
    },
    filters: {
        unEscapeString(rawText) {
        return _.unescape(rawText)
        }
    },
}
</script>

<style>
    .video-detail {
        width: 70%;
        padding-right: 1rem;
    }
    
    .video-container {
        position: relative;
        padding-top: 56.25%;
    }

    .video-container > iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }

    .detail {
        margin-top: 20px;
        padding: 20px;
        border: solid 1px lightgray;
        border-radius: 10px;
    }
</style>