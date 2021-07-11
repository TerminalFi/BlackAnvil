<template>
    <div>
        <Navbar />
        <PageTitle />
        <Client />
        <Footer />
    </div>
</template>

<script>
import Navbar from '../layouts/Navbar'
import PageTitle from '../components/Testimonials/PageTitle'
import Client from '../components/Testimonials/Client'
import Footer from '../layouts/Footer'

export default {
    components: {
        Navbar,
        PageTitle,
        Client,
        Footer,
    }
}
</script>