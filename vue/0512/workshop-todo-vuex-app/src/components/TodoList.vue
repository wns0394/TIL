<template>
  <div>
      <todo-list-item
        v-for="todo in todos" :key="todo.date" :todo="todo"
      >
      </todo-list-item>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import TodoListItem from '@/components/TodoListItem'
export default {
    name: 'TodoList',
    components: {
        TodoListItem,
    },
    computed: {
        ...mapState(['todos']),
        // todos: function () {
        //     return this.$store.state.todos
        // }
    }
}
</script>

<style>

</style>