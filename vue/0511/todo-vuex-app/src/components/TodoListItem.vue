<template>
  <div>
    <span 
      @click="updateTodoStatus(todo)"
      :class="{'is-completed': todo.isCompleted}"
    >
      {{ todo.title }}
    </span>
    <!-- deleteTodo 실행 할 때 todo 같이 넘겨주어야함 -->
    <button @click="deleteTodo(todo)">[x]</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

//  { deleteTodo: function () {}, createTodo: function() {} }

export default {
  name: 'TodoListItem',
  props: {
    todo: Object,
  },
  methods: {
    ...mapActions(['createTodo', 'deleteTodo', 'updateTodoStatus']),
    myMethod() {

    }
  }
}
// export default {
//     name: 'TodoListItem',
//     props: {
//         todo: Object,
//     },
//     methods: {
//         deleteTodo() {
//             this.$store.dispatch('deleteTodo', this.todo)
//         }
//     }
// }
</script>

<style scoped>
  .is-completed {
    text-decoration: line-through;
  }

  div {
    border: 2px solid black;
    margin: 2px;
    padding: 2px;
  }
  span {
    cursor: pointer;
  }
</style>