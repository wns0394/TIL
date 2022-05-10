<template>
  <div id="parent">
      <h2>App Parent</h2>

      <input type="text" v-model="parentData" @input="onInput">
      <p>appData : {{ appData }}</p>
      <p>childData : {{ childData }}</p>

      <app-child
        :app-data="appData"
        :parent-data="parentData"
        @child-input-change="onChildInputChange"
      >

      </app-child>
  </div>
</template>

<script>
import AppChild from './AppChild.vue'

export default {
    name: 'AppParent',
    components: {
        AppChild,
    },
    data() {
        return {
            parentData: null,
            childData: null,
        }
    },
    props: {
        appData: {
            type: String
        }
    },
    methods: {
        onChildInputChange(childInputData) {
            this.childData = childInputData
            this.$emit('child-input-change',childInputData)
        },
        onInput(event) {
            this.$emit('parent-input-change', event.target.value)
        }
    }
}
</script>

<style>

</style>