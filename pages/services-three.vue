<template>
    <div>
        <Navbar />
        <PageTitle />
        <Approach />
        <Complete />
        <Cybersecurity />
        <Solutions />
        <Footer />
    </div>
</template>

<script>
import Navbar from '../layouts/Navbar'
import PageTitle from '../components/services-three/PageTitle'
import Approach from '../components/services-three/Approach'
import Complete from '../components/services-three/Complete'
import Cybersecurity from '../components/services-three/Cybersecurity'
import Solutions from '../components/services-three/Solutions'
import Footer from '../layouts/Footer'
 
export default {
    components: {
        Navbar,
        PageTitle,
        Approach,
        Complete,
        Cybersecurity,
        Solutions,
        Footer,
    }
}
</script>