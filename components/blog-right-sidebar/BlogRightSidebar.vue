<template>
    <div class="blog-details-area ptb-100">
        <div class="container">
            <div class="row">
                <div class="col-lg-8 col-md-12">
                    <div class="blog-details-desc blog-right-sidebar-area">
                        <div class="row">
                            <div class="col-lg-12 col-md-6">
                                <div class="single-blog">
                                    <img src="~/assets/images/blog/blog-10.jpg" alt="Image">
        
                                    <div class="blog-content">
                                        <h3>
                                            <NuxtLink to="/blog-details">DHS Issues Emergency Directive To Prevent Hacking Attack</NuxtLink>
                                        </h3>
                                        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Beatae, cum excepturi ipsum, asperiores placeat quidem deleniti doloremque neque, voluptas ut earum atque</p>
                                        <NuxtLink to="/blog-details" class="read-more">
                                            Read More
                                        </NuxtLink>
                                    </div>
                                </div>
                            </div>
        
                            <div class="col-lg-12 col-md-6">
                                <div class="single-blog">
                                    <img src="~/assets/images/blog/blog-11.jpg" alt="Image">
        
                                    <div class="blog-content">
                                        <h3>
                                            <NuxtLink to="/blog-details">Drughydrus Add Google Drive To Roughrobin Torjan</NuxtLink>
                                        </h3>
                                        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Beatae, cum excepturi ipsum, asperiores placeat quidem deleniti doloremque neque, voluptas ut earum atque</p>
                                        <NuxtLink to="/blog-details" class="read-more">
                                            Read More
                                        </NuxtLink>
                                    </div>
                                </div>
                            </div>
        
                            <div class="col-lg-12 col-md-6 offset-md-3 offset-lg-0">
                                <div class="single-blog">
                                    <img src="~/assets/images/blog/blog-12.jpg" alt="Image">
        
                                    <div class="blog-content">
                                        <h3>
                                            <NuxtLink to="/blog-details">Security In A Fragment World Of Workload</NuxtLink>
                                        </h3>
                                        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Beatae, cum excepturi ipsum, asperiores placeat quidem deleniti doloremque neque, voluptas ut earum atque</p>
                                        <NuxtLink to="/blog-details" class="read-more">
                                            Read More
                                        </NuxtLink>
                                    </div>
                                </div>
                            </div>
        
                            <div class="col-lg-12">
                                <div class="page-navigation-area">
                                    <nav aria-label="Page navigation example text-center">
                                        <ul class="pagination">
                                            <li class="page-item">
                                                <a class="page-link page-links" href="#">
                                                    <i class='bx bx-chevrons-left'></i>
                                                </a>
                                            </li>
                                            <li class="page-item active">
                                                <a class="page-link" href="#">1</a>
                                            </li>
                                            <li class="page-item">
                                                <a class="page-link" href="#">2</a>
                                            </li>
                                            <li class="page-item">
                                                <a class="page-link" href="#">3</a>
                                            </li>
                                            <li class="page-item">
                                                <a class="page-link" href="#">
                                                    <i class='bx bx-chevrons-right'></i>
                                                </a>
                                            </li>
                                        </ul>
                                    </nav>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-md-12">
                    <div class="blog-right-sidebar">
                        <BlogSidebar />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import BlogSidebar from '../Common/BlogSidebar'

export default {
    name: 'BlogRightSidebar',
    components: {
        BlogSidebar
    }
}
</script>