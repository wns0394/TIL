<template>
  <div>
      <todo-list-input @add-todo="onAddTodo"></todo-list-input>
  </div>
</template>

<script>
import TodoListInput from '@/components/TodoListInput'
export default {
    name: 'MyTodoList',
    components: {
        TodoListInput,
    },
    methods: {
        onAddTodo: function (inputData) {
            console.log(inputData)
        },
    },
}
</script>

<style>

</style>