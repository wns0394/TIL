<template>
  <div>
      <h1>점심 메뉴</h1>
      <button @click="pickLunchMenu">메뉴 추천</button>
      <p>{{ selectedMenu }}</p>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
    name: 'TheLunch',
    data() {
      return {
        lunch: ['돼지국밥', '순대국밥', '내장국밥', '섞어국밥'],
        selectedMenu: null,
      }
    },
    methods: {
      pickLunchMenu() {
        this.selectedMenu = _.sample(this.lunch)
      }
    }
}
</script>

<style>

</style>