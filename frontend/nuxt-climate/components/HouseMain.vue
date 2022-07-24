<template>
  <div>
  <b-jumbotron v-bind:header="myname" v-bind:lead="mypts">
    <b-button variant="primary" href="/redeem">Redeem Points</b-button>
  </b-jumbotron>
  <b-card title="Your Rewards">
    <b-table dark striped hover :items="items" :fields="fields"></b-table>
  </b-card>
  <br>
  <b-card title="Pickup Notification">
    <b-card-text>
      Last successful pickup is Monday 17 June 2022
      <br>
      Next pickup schedule is Friday 30 July 2022
    </b-card-text>
    <b-button href="/bookpick" variant="primary">Book Your Next Pickup</b-button>
  </b-card>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        myinfo: [],
        tmp1: [],
        tmp2: [],
        tmp3: [],
        rewards: [],
        myname: 'n/a',
        mypts: -1,
        items: [],
        nextpu: '',
        fields: [
          'desc',
          'expiry',
          'used',
        ],

      }
    },
    methods: {
      findReward(rws, id) {
        //
      },
    },
    async fetch() {
      // fetch user hh data from backend
      this.myinfo = await fetch(
        'http://127.0.0.1:8888/users_hh/1'
      ).then(res => res.json())
      this.myname = "Hello " + this.myinfo.data.name + " ..."
      this.mypts = "Your points: " + this.myinfo.data.points
      this.tmp2 = await fetch(
        'http://127.0.0.1:8888/reward'
      ).then(res => res.json())
      this.rewards = this.tmp2.data
      this.tmp1 = await fetch(
        'http://127.0.0.1:8888/redeem'
      ).then(res => res.json())
      this.items = this.tmp1.data
      let i = 0
      let j = 0
      for (i = 0; i < this.items.length; i++) {
        for (j = 0; j < this.rewards.length; j++) {
          if (this.items[i].reward == this.rewards[j].id)
            this.items[i].desc = this.rewards[j].desc
        }
      }      
    }
  }
</script>
