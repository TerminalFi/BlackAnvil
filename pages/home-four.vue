<template>
    <div>
        <Navbar />
        <MainBanner />
        <Partner />
        <Performance />
        <Transform />
        <Pricing />
        <Choose />
        <Team />
        <Solutions />
        <Graph />
        <Faq />
        <BlogStyleTwo />
        <Footer />
    </div>
</template>

<script>
import Navbar from '../layouts/Navbar'
import MainBanner from '../components/home-four/MainBanner'
import Partner from '../components/Common/Partner'
import Performance from '../components/home-four/Performance'
import Transform from '../components/home-four/Transform'
import Pricing from '../components/Common/Pricing'
import Choose from '../components/home-four/Choose'
import Team from '../components/Common/Team'
import Solutions from '../components/home-four/Solutions'
import Graph from '../components/home-four/Graph'
import Faq from '../components/home-four/Faq'
import BlogStyleTwo from '../components/Common/BlogStyleTwo'
import Footer from '../layouts/Footer'

export default {
    components: {
        Navbar,
        MainBanner,
        Partner,
        Performance,
        Transform,
        Pricing,
        Choose,
        Team,
        Solutions,
        Graph,
        Faq,
        BlogStyleTwo,
        Footer,
    }
}
</script>
