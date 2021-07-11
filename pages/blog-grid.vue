<template>
    <div>
        <Navbar />
        <PageTitle />
        <BlogArea />
        <Footer />
    </div>
</template>

<script>
import Navbar from '../layouts/Navbar'
import PageTitle from '../components/blog-grid/PageTitle'
import BlogArea from '../components/blog-grid/BlogArea'
import Footer from '../layouts/Footer'
 
export default {
    components: {
        Navbar,
        PageTitle,
        BlogArea,
        Footer,
    }
}
</script>