import Vue from 'vue'
import Vuex from 'vuex'

import createPersistedState from 'vuex-persistedstate'
Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    todos: [
      // {title: '1번', isCompleted: false, date: new Date().getTime() },
      // {title: '2번', isCompleted: false, date: new Date().getTime()+1},
    ]
  },
  getters: {
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
  mutations: {
    CREATE_TODO: function (state, newTodo) {
      state.todos.push(newTodo)
    },
    DELETE_TODO(state, todoItem) {
      const index = state.todos.indexOf(todoItem)
      state.todos.splice(index, 1)
    },
    UPDATE_TODO_STATUS(state, todoItem) {
      state.todos.map(todo => {
        if (todo === todoItem) {
          todo.isCompleted = !todo.isCompleted
        }
        return todo
      })
    }
  },
  actions: {
    createTodo: function ({ commit }, newTodo) {
      commit('CREATE_TODO', newTodo)
    },
    deleteTodo({ commit }, todoItem) {
      commit('DELETE_TODO', todoItem)
    },
    updateTodoStatus({ commit }, todoItem) {
      console.log(todoItem)
      commit('UPDATE_TODO_STATUS', todoItem)
    }
  },
  modules: {
  }
})
