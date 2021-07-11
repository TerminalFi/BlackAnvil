<template>
    <div>
        <Navbar />
        <PageTitle />
        <Security />
        <Solutions />
        <Footer />
    </div>
</template>

<script>
import Navbar from '../layouts/Navbar'
import PageTitle from '../components/services-one/PageTitle'
import Security from '../components/services-one/Security'
import Solutions from '../components/services-one/Solutions'
import Footer from '../layouts/Footer'
 
export default {
    components: {
        Navbar,
        PageTitle,
        Security,
        Solutions,
        Footer,
    }
}
</script>