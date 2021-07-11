<template>
    <div class="blog-area pt-100 pb-70">
        <div class="container">
            <div class="section-title">
                <h2>Latest News From Blog</h2>
                <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Doloribus quam neque quibusdam corrupti aspernatur corporis alias nisi dolorum expedita veritatis voluptates minima.</p>
            </div>

            <div class="row">
                <div class="col-lg-4 col-sm-6">
                    <div class="single-blog">
                        <img src="~/assets/images/blog/blog-4.jpg" alt="Image">

                        <div class="blog-content">
                            <h3>
                                <NuxtLink to="/blog-details">Secure Managed IT</NuxtLink>
                            </h3>
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolorer</p>
                            <NuxtLink to="/blog-details" class="read-more">
                                Read More
                            </NuxtLink>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-sm-6">
                    <div class="single-blog">
                        <img src="~/assets/images/blog/blog-5.jpg" alt="Image">

                        <div class="blog-content">
                            <h3>
                                <NuxtLink to="/blog-details">Cloud Security</NuxtLink>
                            </h3>
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolorer</p>
                            <NuxtLink to="/blog-details" class="read-more">
                                Read More
                            </NuxtLink>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-sm-6 offset-sm-3 offset-lg-0">
                    <div class="single-blog">
                        <img src="~/assets/images/blog/blog-6.jpg" alt="Image">

                        <div class="blog-content">
                            <h3>
                                <NuxtLink to="/blog-details">Secure Managed Web</NuxtLink>
                            </h3>
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolorer</p>
                            <NuxtLink to="/blog-details" class="read-more">
                                Read More
                            </NuxtLink>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'Blog'
}
</script>