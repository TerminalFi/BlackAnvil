<template>
    <div>
        <NavbarStyleTwo />
        <MainBanner />
        <Features />
        <Security />
        <Transform />
        <Performance />
        <Team />
        <ManualArea />
        <Faq />
        <Choose />
        <Cybersecurity />
        <BlogStyleTwo />
        <Footer />
    </div>
</template>

<script>
import NavbarStyleTwo from '../layouts/NavbarStyleTwo'
import MainBanner from '../components/home-three/MainBanner'
import Features from '../components/home-three/Features'
import Security from '../components/home-three/Security'
import Transform from '../components/home-three/Transform'
import Performance from '../components/home-three/Performance'
import Team from '../components/Common/Team'
import ManualArea from '../components/home-three/ManualArea'
import Faq from '../components/home-three/Faq'
import Choose from '../components/home-three/Choose'
import Cybersecurity from '../components/home-three/Cybersecurity'
import BlogStyleTwo from '../components/Common/BlogStyleTwo'
import Footer from '../layouts/Footer'

export default {
    components: {
        NavbarStyleTwo,
        MainBanner,
        Features,
        Security,
        Transform,
        Performance,
        Team,
        ManualArea,
        Faq,
        Choose,
        Cybersecurity,
        BlogStyleTwo,
        Footer,
    }
}
</script>
