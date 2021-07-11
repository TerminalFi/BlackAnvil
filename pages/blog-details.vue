<template>
    <div>
        <Navbar />
        <PageTitle />
        <BlogDetails />
        <Footer />
    </div>
</template>

<script>
import Navbar from '../layouts/Navbar'
import PageTitle from '../components/blog-details/PageTitle'
import BlogDetails from '../components/blog-details/BlogDetails'
import Footer from '../layouts/Footer'
 
export default {
    components: {
        Navbar,
        PageTitle,
        BlogDetails,
        Footer,
    }
}
</script>