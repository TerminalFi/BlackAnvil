<template>
    <div>
        <Navbar />
        <PageTitle />
        <ContactInfo />
        <Contact />
        <Footer />
    </div>
</template>

<script>
import Navbar from '../layouts/Navbar'
import PageTitle from '../components/Contact/PageTitle'
import ContactInfo from '../components/Contact/ContactInfo'
import Contact from '../components/Contact/Contact'
import Footer from '../layouts/Footer'
 
export default {
    components: {
        Navbar,
        PageTitle,
        ContactInfo,
        Contact,
        Footer,
    }
}
</script>