<template>
    <div>
        <Navbar />
        <PageTitle />
        <BlogLeftSidebar />
        <Footer />
    </div>
</template>

<script>
import Navbar from '../layouts/Navbar'
import PageTitle from '../components/blog-left-sidebar/PageTitle'
import BlogLeftSidebar from '../components/blog-left-sidebar/BlogLeftSidebar'
import Footer from '../layouts/Footer'
 
export default {
    components: {
        Navbar,
        PageTitle,
        BlogLeftSidebar,
        Footer,
    }
}
</script>