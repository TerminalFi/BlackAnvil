<template>
    <div>
        <Navbar />
        <PageTitle />
        <PricingTwo />
        <Pricing />
        <Footer />
    </div>
</template>

<script>
import Navbar from '../layouts/Navbar'
import PageTitle from '../components/Pricing/PageTitle'
import PricingTwo from '../components/Pricing/PricingTwo'
import Pricing from '../components/Common/Pricing'
import Footer from '../layouts/Footer'

export default {
    components: {
        Navbar,
        PageTitle,
        PricingTwo,
        Pricing,
        Footer,
    }
}
</script>