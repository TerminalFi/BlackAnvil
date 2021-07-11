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
        <Client />
        <BlogStyleTwo />
        <Footer />
    </div>
</template>

<script>
import Navbar from '../layouts/Navbar'
import MainBanner from '../components/home-five/MainBanner'
import Partner from '../components/Common/Partner'
import Performance from '../components/home-five/Performance'
import Transform from '../components/home-five/Transform'
import Pricing from '../components/Common/Pricing'
import Choose from '../components/home-five/Choose'
import Team from '../components/Common/Team'
import Solutions from '../components/home-five/Solutions'
import Graph from '../components/home-five/Graph'
import Faq from '../components/home-five/Faq'
import Client from '../components/Common/Client'
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
        Client,
        BlogStyleTwo,
        Footer,
    }
}
</script>
