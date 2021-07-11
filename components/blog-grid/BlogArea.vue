<template>
    <div class="blog-area ptb-100">
        <div class="container">
            <div class="section-title">
                <h2>Latest News From Blog</h2>
                <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Doloribus quam neque quibusdam corrupti aspernatur corporis alias nisi dolorum expedita veritatis voluptates minima.</p>
            </div>

            <div class="row">
                <div class="col-lg-4 col-sm-6">
                    <div class="single-blog">
                        <img src="~/assets/images/blog/blog-1.jpg" alt="Image">

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
                        <img src="~/assets/images/blog/blog-2.jpg" alt="Image">

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

                <div class="col-lg-4 col-sm-6">
                    <div class="single-blog">
                        <img src="~/assets/images/blog/blog-3.jpg" alt="Image">

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
                        <img src="~/assets/images/blog/blog-4.jpg" alt="Image">
                        <span>Cyber Security</span>
                        <div class="blog-content">
                            <div class="date">
                                <i class="bx bx-calendar"></i>
                                Jun 20 2020
                            </div>

                            <h3>
                                <NuxtLink to="/blog-details">DHS issues emergency directive to prevent hacking attack</NuxtLink>
                            </h3>

                            <NuxtLink to="/blog-details" class="read-more mt-use">
                                Read More
                            </NuxtLink>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-sm-6">
                    <div class="single-blog">
                        <img src="~/assets/images/blog/blog-5.jpg" alt="Image">
                        <span>Cyber Crime</span>
                        <div class="blog-content">
                            <div class="date">
                                <i class="bx bx-calendar"></i>
                                Jun 21 2020
                            </div>

                            <h3>
                                <NuxtLink to="/blog-details">Drughydrus  add google drive to roughrobin torjan</NuxtLink>
                            </h3>
                            
                            <NuxtLink to="/blog-details" class="read-more mt-use">
                                Read More
                            </NuxtLink>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-sm-6">
                    <div class="single-blog">
                        <img src="~/assets/images/blog/blog-6.jpg" alt="Image">
                        <span>Hacking Protection</span>
                        <div class="blog-content">
                            <div class="date">
                                <i class="bx bx-calendar"></i>
                                Jun 22 2020
                            </div>

                            <h3>
                                <NuxtLink to="/blog-details">Security in a fragment world of workload</NuxtLink>
                            </h3>
                            
                            <NuxtLink to="/blog-details" class="read-more mt-use">
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
</template>

<script>

export default {
    name: 'BlogArea'
}
</script>