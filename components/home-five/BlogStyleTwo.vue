<template>
    <div class="blog-area pt-100 pb-70">
        <div class="container">
            <div class="section-title">
                <h2>Latest News From Blog</h2>
                <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Doloribus quam neque quibusdam corrupti aspernatur corporis alias nisi dolorum expedita veritatis voluptates minima.</p>
            </div>

            <div class="row">
                <div class="col-lg-4 col-md-6">
                    <div class="single-blog">
                        <img src="~/assets/images/blog/blog-4.jpg" alt="Image">
                        <span>Cyber Security</span>
                        <div class="blog-content">
                            <div class="date">
                                <i class="bx bx-calendar"></i>
                                Jun 20 2020
                            </div>

                            <h3>
                                <NuxtLink to="/blog-details">
                                    DHS issues emergency directive to prevent hacking attack
                                </NuxtLink>
                            </h3>
  
                            <NuxtLink to="/blog-details" class="read-more mt-use">
                                Read More
                            </NuxtLink>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6">
                    <div class="single-blog">
                        <img src="~/assets/images/blog/blog-5.jpg" alt="Image">
                        <span>Cyber Crime</span>
                        <div class="blog-content">
                            <div class="date">
                                <i class="bx bx-calendar"></i>
                                Jun 21 2020
                            </div>

                            <h3>
                                <NuxtLink to="/blog-details">
                                    Drughydrus  add google drive to roughrobin torjan
                                </NuxtLink>
                            </h3>
                            
                            <NuxtLink to="/blog-details" class="read-more mt-use">
                                Read More
                            </NuxtLink>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6 offset-md-3 offset-lg-0">
                    <div class="single-blog">
                        <img src="~/assets/images/blog/blog-6.jpg" alt="Image">
                        <span>Hacking Protection</span>
                        <div class="blog-content">
                            <div class="date">
                                <i class="bx bx-calendar"></i>
                                Jun 22 2020
                            </div>

                            <h3>
                                <NuxtLink to="/blog-details">
                                    Security in a fragment world of workload
                                </NuxtLink>
                            </h3>
                            
                            <NuxtLink to="/blog-details" class="read-more mt-use">
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
    name: 'BlogStyleTwo'
}
</script>