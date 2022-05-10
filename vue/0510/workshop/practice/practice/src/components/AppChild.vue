<template>
  <div id="child">
      <h2>App Child</h2>
      <input type="text" v-model="childData" @input="onInput">
      <p>appData : {{ appData }}</p>
      <p>parentData : {{ parentData }}</p>
  </div>
</template>

<script>
export default {
    name: 'AppChild',
    props: {
        appData: {
            type : String
        },
        parentData: {
            type : String
        }
    },
    data() {
        return {
            childData: null
        }
    },
    methods: {
        onInput(event) {
            console.log(event.target.value)
            this.$emit('child-input-change', event.target.value)
        }
    }
}
</script>

<style>

</style>