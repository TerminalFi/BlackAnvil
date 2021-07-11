<template>
    <section class="blog-area pb-70">
        <div class="container">
            <div class="section-title-six">
                <span>Latest News</span>
                <h2>Our Latest Insights Are On Top</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
            </div>

            <div class="row">
                <div class="col-lg-4 col-sm-6">
                    <div class="single-blog-post">
                        <NuxtLink to="/blog-details">
                            <img src="~/assets/images/blog/blog-1.jpg" alt="Image">
                        </NuxtLink>

                        <div class="blog-content">
                            <ul>
                                <li>
                                    <i class="bx bx-purchase-tag"></i>
                                    Security
                                </li>
                                <li>
                                    <i class="bx bx-time"></i>
                                    5 min read
                                </li>
                            </ul>
                            <h3>
                                <NuxtLink to="/blog-details">DHS Issues Emergency Directive To Prevent Hacking Attack</NuxtLink>
                            </h3>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-sm-6">
                    <div class="single-blog-post">
                        <NuxtLink to="/blog-details">
                            <img src="~/assets/images/blog/blog-2.jpg" alt="Image">
                        </NuxtLink>

                        <div class="blog-content">
                            <ul>
                                <li>
                                    <i class="bx bx-purchase-tag"></i>
                                    Hunter
                                </li>
                                <li>
                                    <i class="bx bx-time"></i>
                                    5 min read
                                </li>
                            </ul>
                            <h3>
                                <NuxtLink to="/blog-details">Drughydrus Add Google Drive To Roughrobin Torjan</NuxtLink>
                            </h3>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-sm-6 offset-sm-3 offset-lg-0">
                    <div class="single-blog-post">
                        <NuxtLink to="/blog-details">
                            <img src="~/assets/images/blog/blog-3.jpg" alt="Image">
                        </NuxtLink>

                        <div class="blog-content">
                            <ul>
                                <li>
                                    <i class="bx bx-purchase-tag"></i>
                                    Hacker
                                </li>
                                <li>
                                    <i class="bx bx-time"></i>
                                    5 min read
                                </li>
                            </ul>
                            <h3>
                                <NuxtLink to="/blog-details">Security In A Fragment World Of Workload For Your Business</NuxtLink>
                            </h3>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>

export default {
    name: 'Blog'
}
</script>