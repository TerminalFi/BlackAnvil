<template>
    <div>
        <Navbar />
        <MainBanner />
        <Partner />
        <Cybersecurity />
        <Security />
        <Solutions />
        <Complete />
        <Manual />
        <Counter />
        <Pricing />
        <Client />
        <Blog />
        <FooterTop />
        <Footer />
    </div>
</template>

<script>
import Navbar from '../layouts/Navbar'
import MainBanner from '../components/home-two/MainBanner'
import Partner from '../components/Common/Partner'
import Cybersecurity from '../components/home-two/Cybersecurity'
import Security from '../components/home-two/Security'
import Solutions from '../components/home-two/Solutions'
import Complete from '../components/home-two/Complete'
import Manual from '../components/home-two/Manual'
import Counter from '../components/home-two/Counter'
import Pricing from '../components/Common/Pricing'
import Client from '../components/Common/Client'
import Blog from '../components/Common/Blog'
import Footer from '../layouts/Footer'

export default {
    components: {
        Navbar,
        MainBanner,
        Partner,
        Cybersecurity,
        Security,
        Solutions,
        Complete,
        Manual,
        Counter,
        Pricing,
        Client,
        Blog,
        Footer,
    }
}
</script>
