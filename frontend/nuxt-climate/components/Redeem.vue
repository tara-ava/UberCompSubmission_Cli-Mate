<template>
 <div>
  <b-form @submit.prevent="onSubmit">
    <b-form-select v-model="selected" :options="rwoptions"></b-form-select>
    <div class="mt-3">Selected: <strong>{{ selected }}</strong></div>

	<b-button type="submit">Redeem</b-button>
  </b-form>
</div>
</template>

<script>
  export default {
    data() {
      return {
        selected: null,
        allrewards: [],
        myinfo: [],
        reward: {},
        userhh: {},
        z: 0,
      }
    },
    methods: {
      async storeReward() {
        this.reward =
        {
          "user": 1,
          "reward": this.selected,
          "used": "N",
          "expiry": new Date()
        }
        let rc = 200
        const res = this.$axios.$post(
          'http://127.0.0.1:8888/redeem', this.reward)
          .catch(err => {
            console.log("error")
            //console.log(err.response.status)
            rc = err.response.status
          })
        console.log("rc before return: " + rc)
        return rc
      },
      async onSubmit() {
        //event.preventDefault()
        console.log(this.latestpoints)
        const res = await this.storeReward()
          .then (res => {
         //console.log("storeReward no error")
          console.log(res)
          if (res == 200) {
            this.$bvToast.toast('Reward added', {
            autoHideDelay: 5000,
            noCloseButton: true, variant: "info" })
          }
          else {
            this.$bvToast.toast('Insert error', {
            autoHideDelay: 5000,
            noCloseButton: true, variant: "warning" })
          }
       })
       this.reward = {}
     },
   },
        
    computed : {
      rwoptions() {
        for (let i=0; i < this.allrewards.data.length; i++) {
          this.allrewards.data[i].value = this.allrewards.data[i].id
          this.allrewards.data[i].text = this.allrewards.data[i].desc + ' (' + this.allrewards.data[i].points + ' points) '
        }
        //this.allrewards.data.unshift({value: null, text: 'Select reward'})
        return this.allrewards.data
      },
      latestpoints() {
         let y = this.selected
         //this.z = this.myinfo.data.points - this.allrewards.data[this.selected].points
         //return (this.myinfo.data.points - this.allrewards.data[this.selected].points)
      }
    },
    async fetch() {
      // fetch rewards data from backend
      this.allrewards = await fetch(
        'http://127.0.0.1:8888/reward'
      ).then(res => res.json())
      this.myinfo = await fetch(
        'http://127.0.0.1:8888/users_hh/1'
      ).then(res => res.json())
      console.log(this.myinfo.data.points)
      console.log(this.allrewards.data[0].points)
    },    
  }
</script>
