<template>
    <div>
        <Navbar />
        <PageTitle />
        <ServicesDetails />
        <Footer />
    </div>
</template>

<script>
import Navbar from '../layouts/Navbar'
import PageTitle from '../components/services-details/PageTitle'
import ServicesDetails from '../components/services-details/ServicesDetails'
import Footer from '../layouts/Footer'
 
export default {
    components: {
        Navbar,
        PageTitle,
        ServicesDetails,
        Footer,
    }
}
</script>