<template>
    <div>
        <Navbar />
        <PageTitle />
        <Team />
        <Footer />
    </div>
</template>

<script>
import Navbar from '../layouts/Navbar'
import PageTitle from '../components/Team/PageTitle'
import Team from '../components/Team/Team'
import Footer from '../layouts/Footer'

export default {
    components: {
        Navbar,
        PageTitle,
        Team,
        Footer,
    }
}
</script>