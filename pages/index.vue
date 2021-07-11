<template>
    <div>
        <Navbar />
        <MainBanner />
        <Security />
        <Approach />
        <Counter />
        <Solutions />
        <Electronic />
        <Complete />
        <Client />
        <Cybersecurity />
        <!-- <Blog /> -->
        <Footer />
    </div>
</template>

<script>
import Navbar from '../layouts/Navbar'
import MainBanner from '../components/Index/MainBanner'
// import Partner from '../components/Common/Partner'
import Counter from '../components/Common/Counter'
import Security from '../components/Index/Security'
import Approach from '../components/Index/Approach'
// import Solutions from '../components/Index/Solutions'
import Electronic from '../components/Index/Electronic'
import Complete from '../components/Index/Complete'
// import Client from '../components/Common/Client'
// import Cybersecurity from '../components/Index/Cybersecurity'
// import Blog from '../components/Common/Blog'
import Footer from '../layouts/Footer'

export default {
    components: { 
        Navbar,
        MainBanner,
        // Partner,
        Security,
        Approach,
        Counter,
        // Solutions,
        Electronic,
        Complete,
        // Client,
        // Cybersecurity,
        // Blog,
        Footer,
    }
}
</script>
