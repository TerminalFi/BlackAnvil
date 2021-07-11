<template>
    <div>
        <NavbarStyleThree />
        <MainBanner />
        <Partner />
        <ServicesSlider />
        <Serve />
        <Counter />
        <ChooseUs />
        <Testimonials />
        <Video />
        <Blog />
        <LetsTalk />
        <FooterStyleTwo />
        <CopyRight />
    </div>
</template>

<script>
import NavbarStyleThree from '../layouts/NavbarStyleThree'
import MainBanner from '../components/home-six/MainBanner'
import Partner from '../components/home-six/Partner'
import ServicesSlider from '../components/home-six/ServicesSlider'
import Serve from '../components/home-six/Serve'
import Counter from '../components/home-six/Counter'
import ChooseUs from '../components/home-six/ChooseUs'
import Testimonials from '../components/home-six/Testimonials'
import Video from '../components/home-six/Video'
import Blog from '../components/home-six/Blog'
import LetsTalk from '../components/home-six/LetsTalk'
import FooterStyleTwo from '../layouts/FooterStyleTwo'
import CopyRight from '../layouts/CopyRight'

export default {
    components: {
        NavbarStyleThree,
        MainBanner,
        Partner,
        ServicesSlider,
        Serve,
        Counter,
        ChooseUs,
        Testimonials,
        Video,
        Blog,
        LetsTalk,
        FooterStyleTwo,
        CopyRight,
    }
}
</script>
