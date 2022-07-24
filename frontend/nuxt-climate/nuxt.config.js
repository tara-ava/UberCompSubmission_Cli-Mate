export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'nuxt-tap',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/bootstrap
    'bootstrap-vue/nuxt',
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    '@nuxtjs/auth-next',
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
      //credentials: true,
      baseURL: 'http://localhost:8888'
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  server: {
    host: 'localhost'
  },

  auth: {
    strategies: {
        local: {
            endpoints: {
                login: { url: '/login', method: 'post', propertyName: 'data.access_token' },
                logout: { url: '/logout', method: 'delete' },
                user: { url: '/users/me', method: 'get', propertyName: 'data.attributes' }
            },
            tokenRequired: true,
            tokenType: 'bearer'
        }
    }
  },
  build: {
  }
}
