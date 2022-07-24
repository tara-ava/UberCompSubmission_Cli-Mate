<template>
    <div>
        <b-navbar type="dark" variant="primary">
            <b-navbar-brand to="/">Cli-Mate</b-navbar-brand>
            <b-navbar-nav>
                <b-nav-item to="/about">About Us</b-nav-item>
                <b-nav-item to="/partners">Our Partners</b-nav-item>
                <b-nav-item to="/promos">Promos</b-nav-item>
            </b-navbar-nav>
            <b-navbar-nav class="ml-auto">
                <b-nav-item-dropdown right>
                    <template #button-content>
                    <b-avatar size="sm"></b-avatar>
                    </template>
                    <div>
                        <b-dropdown-item to="login">Login</b-dropdown-item>
                        <b-dropdown-item href="#">Register</b-dropdown-item>

                    </div>
                    <div>
                        <b-dropdown-item>Profile</b-dropdown-item> 
                        <b-dropdown-item>Logout</b-dropdown-item>                        
                    </div>
                </b-nav-item-dropdown>
            </b-navbar-nav>
        </b-navbar>
 
        <b-container fluid>
            <b-row>
                <b-col>
                    <br>
                    <Nuxt />
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>
export default {
    data () {
        return {
            showsb: true,
        }
    },
}
</script>
