<template>
    <div>
        <Navbar />
        <PageTitle />
        <SignUp />
        <Footer />
    </div>
</template>

<script>
import Navbar from '../layouts/Navbar'
import PageTitle from '../components/log-in/PageTitle'
import SignUp from '../components/sign-in/SignUp'
import Footer from '../layouts/Footer'
 
export default {
    components: {
        Navbar,
        PageTitle,
        SignUp,
        Footer,
    }
}
</script>