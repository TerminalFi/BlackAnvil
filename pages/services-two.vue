<template>
    <div>
        <Navbar />
        <PageTitle />
        <Features />
        <Performance />
        <Footer />
    </div>
</template>

<script>
import Navbar from '../layouts/Navbar'
import PageTitle from '../components/services-two/PageTitle'
import Features from '../components/services-two/Features'
import Performance from '../components/services-two/Performance'
import Footer from '../layouts/Footer'
 
export default {
    components: {
        Navbar,
        PageTitle,
        Features,
        Performance,
        Footer,
    }
}
</script>