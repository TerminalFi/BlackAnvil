<template>
    <div class="blog-details-area ptb-100">
        <div class="container">
            <div class="row">
                <div class="col-lg-8 col-md-12">
                    <div class="services-details">
                        <h3>Secure Manged IT</h3>

                        <img src="~/assets/images/services-details1.jpg" alt="Image">

                        <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.  but also leap into electronic</p>

                        <div class="choose-wrap">
                            <h2>Why Choose Us</h2>
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Risus commodo viverra maecenas accumsan lacus vel facilisis.</p>
        
                            <ul>
                                <li>
                                    <i class="bx bx-check"></i>
                                    Extemly low response  time at all time
                                </li>
                                <li>
                                    <i class="bx bx-check"></i>
                                    We are always ready for your growth
                                </li>
                                <li>
                                    <i class="bx bx-check"></i>
                                    We understand security and compliance
                                </li>
                            </ul>
                        </div>

                        <h3>Cloud Security</h3>

                        <img src="~/assets/images/services-details2.jpg" alt="Image">

                        <p>Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet comes from a line in section 1.10.32.</p>

                        <h3 class="services-related-post">Related Post</h3>
                        <div class="row">
                            <div class="col-lg-6 col-sm-6">
                                <div class="single-solutions solutions-time-bg-1 mb-0 mb-ud">
                                    <div class="solutions-content">
                                        <h3>Secure Managed IT</h3>
                                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolorer</p>
                                        <NuxtLink to="/services-details" class="read-more">
                                            Read More
                                        </NuxtLink>
                                    </div>
                                </div>
                            </div>
        
                            <div class="col-lg-6 col-sm-6">
                                <div class="single-solutions solutions-time-bg-2 mb-0">
                                    <div class="solutions-content">
                                        <h3>Compliance</h3>
                                        <p>Lorem ipsum dolor sit amet sed, consectetur adipiscing elit do</p>
                                        <NuxtLink to="/services-details" class="read-more">
                                            Read More
                                        </NuxtLink>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-md-12">
                    <aside class="widget-area" id="secondary">
                        <div class="widget widget_search">
                            <h3 class="widget-title">Search Now</h3>
                            <div class="post-wrap">
                                <form class="search-form">
                                    <label>
                                        <span class="screen-reader-text">Search for:</span>
                                        <input type="search" class="search-field" placeholder="Search...">
                                    </label>
                                    <button type="submit"><i class='bx bx-search'></i></button>
                                </form>
                            </div>
                        </div>
                        
                        <section class="widget widget_categories">
                            <h3 class="widget-title">Categories</h3>
                            <div class="post-wrap">
                                <ul>
                                    <li>
                                        <a href="#">Blockchain <span>(10)</span></a>
                                    </li>
                                    <li>
                                        <a href="#">Cyber security <span>(20)</span></a>
                                    </li>
                                    <li>
                                        <a href="#">Cybercrime <span>(10)</span></a>
                                    </li>
                                    <li>
                                        <a href="#">Global news <span>(12)</span></a>
                                    </li>
                                    <li>
                                        <a href="#">Ransomware <span>(16)</span></a>
                                    </li>
                                    <li>
                                        <a href="#">Whitepapers <span>(17)</span></a>
                                    </li>
                                </ul>
                            </div>
                        </section>

                        <section class="widget widget_tag_cloud">
                            <h3 class="widget-title">Tags</h3>
                            <div class="post-wrap">
                                <div class="tagcloud">
                                    <a href="#">Blockchain (3)</a>
                                    <a href="#">Cyber security (3)</a>
                                    <a href="#">Cybercrime (2)</a>
                                    <a href="#">Global news (2)</a>
                                    <a href="#">Ransomware (1)</a>
                                    <a href="#">Whitepapers (2) </a>
                                </div>
                            </div>
                        </section>       
                    </aside>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'ServicesDetails'
}
</script>