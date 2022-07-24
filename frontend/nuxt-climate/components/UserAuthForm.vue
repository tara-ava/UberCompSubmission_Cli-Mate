<template>
    <div>
        <b-form v-if="show">
            <b-form-group
                id="input-group-1" label="E-Mail:" label-for="user-email" >
                <b-form-input id="user-email" type="email" v-model="user.email"
                    placeholder="Your e-mail" required >
                </b-form-input>
            </b-form-group>
            <b-form-group
                id="input-group-3" label="Password:" label-for="user-password" >
                <b-form-input id="user-password" type="password" v-model="user.password"
                    placeholder="User password" required >
                </b-form-input>
            </b-form-group>

            <b-button-group>
                <b-button :to="getUserLink()">User</b-button>
                <b-button :to="getPartnerLink()">Partner</b-button>
            </b-button-group>
        </b-form>
    </div>
</template>

<script>
export default {
    props: ["submitFunc"],
    data() {
        return {
            show: true,
            user: {
                username: 'isorano@gmail.com',
                password: 'kud4lump1ng'
            },
        }
    },
    methods: {
        countDownChanged(dismissCountDown) {
            this.dismissCountDown = dismissCountDown
        },
        showAlert() {
            this.dismissCountDown = this.dismissSecs
        },

        onSubmit() {
            alert("login submitted")
        },
        getUserLink () {
            return ('/house')
        },
        getPartnerLink () {
            return ('/partner1')
        },
 
        loginuser(u) {
			
        },
    },
}
</script>
