<template>
    <div>
        <Navbar />
        <PageTitle />
        <TermsConditions />
        <Footer />
    </div>
</template>

<script>
import Navbar from '../layouts/Navbar'
import PageTitle from '../components/terms-conditions/PageTitle'
import TermsConditions from '../components/terms-conditions/TermsConditions'
import Footer from '../layouts/Footer'
 
export default {
    components: {
        Navbar,
        PageTitle,
        TermsConditions,
        Footer,
    }
}
</script>