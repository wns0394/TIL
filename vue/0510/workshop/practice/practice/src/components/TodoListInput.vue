<template>
  <div>
      <input type="text" v-model='inputData'>
      <button @click="onClick">추가</button>
  </div>
</template>

<script>
export default {
    name: 'TodoListInput',
    data: function () {
        return {
            inputData: '',
        }
    },
    methods: {
        onClick: function () {
            this.$emit('add-todo', this.inputData)
        },
    },
}
</script>

<style>

</style>