<template>
  <div>
      <h1>로또 번호 추천</h1>
      <button @click="pickLottoNums">번호 추천</button>
      <p>{{ numbers }}</p>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
    name: 'TheLotto',
    data() {
        return {
            numbers: [],
        }
    },
    methods: {
        pickLottoNums() {
            this.numbers = _.sampleSize(_.range(1, 46), this.$route.params.lottoNum)
        }
    }
}
</script>

<style>

</style>