<template>
  <div id="app">
    <hello-World @click="onClick"></hello-World>
    <hello-World @click.native="onClick"></hello-World>
    <todo-List></todo-List>
    <hr>
    <h2>App</h2>
    <!--  v-model 을 사용하면 양방향 바인딩 -->
    <input type="text" v-model="appData">
    <p>parentData : {{ parentData }}</p>
    <p>childData : {{ childData }}</p>

    <app-parent
      :app-data="appData"
      :parent-data="parentData"
      :child-data="childData"
      @child-input-change="onChildInputChange"
      @parent-input-change="onParentInputChange"
    >

    </app-parent>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import TodoList from './components/TodoList.vue'

import AppParent from './components/AppParent.vue'
export default {
  name: 'App',
  components: {
    HelloWorld,
    TodoList,
    AppParent,
  },
  //  data function 형태로 만들어야한다.
  data: function () {
    return {
      // return 값으로 처리한다. 왜 이렇게 해야할까 왜 component로 할때는 이렇게 해야할까
      // 함수로 처리 안하고 데이터 값으로 하면 모든 컴포넌트가 영향을 받아서 그렇다
      appData: null,
      parentData: null,
      childData: null,
    }
  },
  methods: {
    onClick: function () {
      console.log('Hello!')
    },
    onChildInputChange(childInputData) {
      this.childData = childInputData
    },
    onParentInputChange(parentInputData) {
      this.parentData = parentInputData
    },
  }
}
</script>

<style>
</style>


