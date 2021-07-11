<template>
    <div>
        <Navbar />
        <PageTitle />
        <RecoverPassword />
        <Footer />
    </div>
</template>

<script>
import Navbar from '../layouts/Navbar'
import PageTitle from '../components/recover-password/PageTitle'
import RecoverPassword from '../components/recover-password/RecoverPassword'
import Footer from '../layouts/Footer'
 
export default {
    components: {
        Navbar,
        PageTitle,
        RecoverPassword,
        Footer,
    }
}
</script>