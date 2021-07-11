<template>
    <div>
        <Navbar />
        <PageTitle />
        <LogIn />
        <Footer />
    </div>
</template>

<script>
import Navbar from '../layouts/Navbar'
import PageTitle from '../components/log-in/PageTitle'
import LogIn from '../components/log-in/LogIn'
import Footer from '../layouts/Footer'
 
export default {
    components: {
        Navbar,
        PageTitle,
        LogIn,
        Footer,
    }
}
</script>