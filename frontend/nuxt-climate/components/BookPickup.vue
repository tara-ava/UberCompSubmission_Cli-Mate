<template>
  <div>
    <b-form @submit.prevent="onSubmit">
    <b-form-select v-model="selected" :options="puoptions"></b-form-select>
      <div class="mt-3">Selected: <strong>{{ selected }}</strong></div>
    
      <b-button type="submit">Book</b-button>
   </b-form>
 </div>
</template>

<script>
  export default {
    data() {
      return {
        selected: null,
        allpickup: [],
        pickup: {},
      }
    },
    methods: {
      async storePickup() {
        this.pickup =
        {
          "user": 1,
          "pickup": 1
        }
        let rc = 200
        const res = this.$axios.$post(
          'http://127.0.0.1:8888/pbook', this.pickup)
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
        const res = await this.storePickup()
          .then (res => {
         //console.log("storePickup no error")
          console.log(res)
          if (res == 200) {
            this.$bvToast.toast('Pickup booked', {
            autoHideDelay: 5000,
            noCloseButton: true, variant: "info" })
          }
          else {
            this.$bvToast.toast('Insert error', {
            autoHideDelay: 5000,
            noCloseButton: true, variant: "warning" })
          }
       })
       this.pickup = {}
     },
   },
    computed : {
      puoptions() {
        for (let i=0; i < this.allpickup.data.length; i++) {
          this.allpickup.data[i].value = this.allpickup.data[i].id
          this.allpickup.data[i].text = this.allpickup.data[i].date + ' - ' + this.allpickup.data[i].area
        }
        //this.allpickup.data.unshift({value: null, text: 'Select a pickup schedule'})
        return this.allpickup.data
      },
    },
    
    async fetch() {
      // fetch user hh data from backend
      this.allpickup = await fetch(
        'http://127.0.0.1:8888/pschedule'
      ).then(res => res.json())
    },    

  }

</script>
