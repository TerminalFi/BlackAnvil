<template>
    <div>
        <Navbar />
        <PageTitle />
        <BlogRightSidebar />
        <Footer />
    </div>
</template>

<script>
import Navbar from '../layouts/Navbar'
import PageTitle from '../components/blog-right-sidebar/PageTitle'
import BlogRightSidebar from '../components/blog-right-sidebar/BlogRightSidebar'
import Footer from '../layouts/Footer'
 
export default {
    components: {
        Navbar,
        PageTitle,
        BlogRightSidebar,
        Footer,
    }
}
</script>