export default {
    // Global page headers: https://go.nuxtjs.dev/config-head
    head: {
        title: 'Black Anvil - Cyber Security Company',
        htmlAttrs: {
            lang: 'en'
        },
        meta: [
            { charset: 'utf-8' },
            { name: 'viewport', content: 'width=device-width, initial-scale=1' },
            { hid: 'description', name: 'description', content: '' }
        ],
        link: [
            { rel: 'icon', type: 'image/x-icon', href: '/favicon.png' },
            {
                rel: 'stylesheet',
                href: 'https://fonts.googleapis.com/css2?family=Rubik:ital,wght@0,300;0,400;0,500;0,700;0,900;1,300;1,400;1,500;1,700;1,900&display=swap',
                href: 'https://fonts.googleapis.com/css2?family=Barlow+Condensed:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,200;1,300;1,400;1,500;1,600;1,700&display=swap'
            }
        ]
    },

    // Global CSS: https://go.nuxtjs.dev/config-css
    css: [
        '~/assets/css/animate.css',
        '~/assets/css/bootstrap.min.css',
        '~/assets/css/boxicons.min.css',
        '~/assets/css/flaticon.css',
        '~/assets/css/meanmenu.css',
        '~/assets/css/style.css',
        '~/assets/css/responsive.css'
    ],

    // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
    plugins: [
        { src: '~/plugins/bootstrap-vue', ssr: false },
        { src: '~/plugins/vue-carousel', ssr: false },
        { src: '~/plugins/vue-backtotop', ssr: false },
        { src: '~/plugins/vue-cool-lightbox', ssr: false },
    ],

    // Globally configure <nuxt-link> default active class.
    router: {
        linkActiveClass: 'active',
        base: '/BlackAnvil/'
    },

    // Auto import components: https://go.nuxtjs.dev/config-components
    components: true,

    // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
    buildModules: [
    ],

    // Modules: https://go.nuxtjs.dev/config-modules
    modules: [
    ],

    // Build Configuration: https://go.nuxtjs.dev/config-build
    build: {
    },
    target: 'static'
}
