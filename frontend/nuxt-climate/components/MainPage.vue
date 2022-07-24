<template>
<h1>Hello World</h1>
</template>

<script>
export default {
    data() {
        return {
            perPage: 5,
            currentPage: 1,
            items: [], // cards
            tmp1: [],

        }
    },
    methods: {
    },
    computed: {
        rows() {
            return this.items.length
        }
    },
  }
</script>

