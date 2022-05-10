<template>
  <input type="text" @keyup.enter="onInputSearch">
</template>

<script>
export default {
    name: 'TheSearchBar',
    methods: {
        onInputSearch(event) {
            this.$emit('input-search', event.target.value)
        }
    }
}
</script>

<style>
    input {
        width: 100%;
        padding: 0.5rem;
        font-size: 2rem;
    }
</style>