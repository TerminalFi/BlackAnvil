<template>
    <div>
        <Navbar />
        <PageTitle />
        <Faq />
        <Contact />
        <Footer />
    </div>
</template>

<script>
import Navbar from '../layouts/Navbar'
import PageTitle from '../components/Faq/PageTitle'
import Faq from '../components/Faq/Faq'
import Contact from '../components/Faq/Contact'
import Footer from '../layouts/Footer'

export default {
    components: {
        Navbar,
        PageTitle,
        Faq,
        Contact,
        Footer,
    }
}
</script>