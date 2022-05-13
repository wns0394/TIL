<template>
  <div>
    
    <input type="text" v-model.trim="todoTitle" @keyup.enter="uncreateTodo">
    <button @click="createTodo">Add</button>
  </div>
</template>

<script>
export default {
    name: 'TodoForm',
    data() {
      return {
        todoTitle: ''
      }
    },
    methods: {
      createTodo() {
        const newTodo = {
                title: this.todoTitle,
                isCompleted: false,
                date: new Date().getTime()
            }
        this.$store.dispatch('createTodo', newTodo)
        this.todoTitle=''
      },
      uncreateTodo() {
        alert('enter말고 click해라~~')
      }
    }

}
</script>

<style>

</style>