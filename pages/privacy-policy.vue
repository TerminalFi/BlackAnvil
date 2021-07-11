<template>
    <div>
        <Navbar />
        <PageTitle />
        <PrivacyPolicy />
        <Footer />
    </div>
</template>

<script>
import Navbar from '../layouts/Navbar'
import PageTitle from '../components/privacy-policy/PageTitle'
import PrivacyPolicy from '../components/privacy-policy/PrivacyPolicy'
import Footer from '../layouts/Footer'
 
export default {
    components: {
        Navbar,
        PageTitle,
        PrivacyPolicy,
        Footer,
    }
}
</script>