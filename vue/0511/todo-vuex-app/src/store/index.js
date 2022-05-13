import Vue from 'vue'
import Vuex from 'vuex'

import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: { // data
    todos: [
      
    ]
  },
  getters: { // computed
    //현재 끝난 일의 개수
    allTodosCount(state) {
      return state.todos.length
    },
    completedTodosCount(state) {
      return state.todos.filter(todo => {
        return todo.isCompleted
      }).length
    },
    uncompletedTodosCount(state) {
      return state.todos.filter(todo => {
        return !todo.isCompleted
      }).length
    },
  },
  mutations: { // change!
    // LOAD_TODOS(state) {
    //   const todosString = localStorage.getItem('todos')
    //   문자형이니까 json모양으로 parse해주자
    //   state.todos = JSON.parse(todosString)
    // },
    CREATE_TODO(state, newTodo) {
      state.todos.push(newTodo)
    },
    DELETE_TODO(state, todoItem) {
      const index = state.todos.indexOf(todoItem)
      // console.log(index)
      // console.log(index)
      state.todos.splice(index,1)
    },
    UPDATE_TODO_STATUS(state, todoItem) {
      // todoItem
      state.todos.map(todo => {
        if (todo === todoItem) {
          todo.isCompleted = !todo.isCompleted
        }
        return todo
      })
      // console.log(newTodos)
    }
  },
  actions: { // methods
    // 구조분해한다면
    saveTodos( {state}) {
      const jsonData = JSON.stringify(state.todos)
      localStorage.setItem('todos', jsonData)
    },
    createTodo(context, newTodo) {
      context.commit('CREATE_TODO', newTodo)
      // context.dispatch('saveTodos')
      // const JsonData = Json.stringify(conext.state.todos)
      // localStorage.setItem('todos', JsonData)
    // createTodo(context) {
      // context => 맥가이버 칼
      // context.commit('CREATE_TODO')
      // this.commit('CREATE_TODO')
      // mutations.CREATE_TODO()
    //}
    },
    deleteTodo({ commit }, todoItem) {
      if (confirm('진짜로 삭제할꺼야?')) {
        commit('DELETE_TODO', todoItem)
        // dispatch('saveTodos')
      }
    },
    updateTodoStatus({ commit }, todoItem) {
      console.log(todoItem)
      commit('UPDATE_TODO_STATUS', todoItem)
      // dispatch('saveTodos')
    }
  },
  modules: {
  }
})
