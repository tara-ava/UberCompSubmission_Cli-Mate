<template>
    <UserAuthForm :submitFunc="loginUser" />
</template>

<script>
export default {
    methods: {
        async loginUser(myuser) {
            try {
                let res = await this.$auth.loginWith('local', { data: myuser })
                console.log(res)
                console.log("await loginWith")
                this.$router.push("/")
            } catch (err) {
                console.log(myuser.password)
                console.log(myuser.name)
                console.log("error loginWith")
            }
        }
    }
}
</script>
