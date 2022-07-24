<template>
  <div>
  <b-jumbotron v-bind:header="myname" lead="Available Waste">
    <b-img left src="http://localhost:3000/waste_chart.png" fluid alt="Responsive image"></b-img>
    <br>
    <b-button variant="primary" href="/Buy/">Make Purchase</b-button>
  </b-jumbotron>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        myinfo: [],
        myname: '',
      }
    },
    async fetch() {
      this.myinfo = await fetch(
        'http://127.0.0.1:8888/users_prt/1'
      ).then(res => res.json())
      this.myname = "Hello " + this.myinfo.data.company
      console.log(this.myinfo)
    }
  }

</script>
