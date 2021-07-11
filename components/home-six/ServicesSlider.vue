<template>
    <div class="services-area ptb-100">
        <div class="container">
            <div class="section-title-six">
                <span>Our Services</span>
                <h2>We Offer Best Cyber Security Solutions</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
            </div>

            <div class="services-slider-content">
                <div class="services-slider owl-theme owl-carousel">
                    <carousel
                        :autplay = "true"
                        :loop = "true"
                        :paginationEnabled = "false"
                        :navigationEnabled="true"
                        navigationNextLabel="<i class='bx bx-right-arrow-alt'></i>"
                        navigationPrevLabel="<i class='bx bx-left-arrow-alt'></i>"
                        :autoplaySpeed = "true"
                        :autoplayTimeout = "500"
                        :perPageCustom = "[[0, 1]]"
                    >
                        <slide>
                            <div class="row align-items-center">
                                <div class="col-lg-6">
                                    <div class="services-single-item">
                                        <h3>Security Advisory</h3>

                                        <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Illo ducimus vero, vero corporis voluptates beatae pariatur laudantium, fugiat illum ab deserunt nostrum aliquid quisquam esse? Voluptatibus quia velit numquam esse porro ipsum dolor, sit amet consectetur adipisicing elit. Illo ducimus vero, corporis Voluptatibus quia.</p>
            
                                        <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Perspiciatis, soluta, aspernatur dolorum sequi quisquam ullam in pariatur nihil dolorem cumque excepturi totam. Qui excepturi quasi cumque placeat fuga. Ea, eius nihil dolorem cumque</p>
                                        
                                        <NuxtLink  class="default-btn six" to="/about-us">
                                            <i class="bx bx-file"></i>
                                            Learn More
                                        </NuxtLink>
                                    </div>
                                </div>

                                <div class="col-lg-6">
                                    <div class="services-img">
                                        <img src="~/assets/images/services-slider/services-1.png" alt="Image">
                                    </div>
                                </div>
                            </div>
                        </slide>

                        <slide>
                            <div class="row align-items-center">
                                <div class="col-lg-6">
                                    <div class="services-single-item">
                                        <h3>Technical Assurance</h3>

                                        <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Illo ducimus vero, vero corporis voluptates beatae pariatur laudantium, fugiat illum ab deserunt nostrum aliquid quisquam esse? Voluptatibus quia velit numquam esse porro ipsum dolor, sit amet consectetur adipisicing elit. Illo ducimus vero, corporis Voluptatibus quia.</p>
            
                                        <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Perspiciatis, soluta, aspernatur dolorum sequi quisquam ullam in pariatur nihil dolorem cumque excepturi totam. Qui excepturi quasi cumque placeat fuga. Ea, eius nihil dolorem cumque</p>
                                        
                                        <NuxtLink  class="default-btn six" to="/about-us">
                                            <i class="bx bx-file"></i>
                                            Learn More
                                        </NuxtLink>
                                    </div>
                                </div>

                                <div class="col-lg-6">
                                    <div class="services-img">
                                        <img src="~/assets/images/services-slider/services-2.png" alt="Image">
                                    </div>
                                </div>
                            </div>
                        </slide>

                        <slide>
                            <div class="row align-items-center">
                                <div class="col-lg-6">
                                    <div class="services-single-item">
                                        <h3>Assessment Services</h3>

                                        <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Illo ducimus vero, vero corporis voluptates beatae pariatur laudantium, fugiat illum ab deserunt nostrum aliquid quisquam esse? Voluptatibus quia velit numquam esse porro ipsum dolor, sit amet consectetur adipisicing elit. Illo ducimus vero, corporis Voluptatibus quia.</p>
            
                                        <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Perspiciatis, soluta, aspernatur dolorum sequi quisquam ullam in pariatur nihil dolorem cumque excepturi totam. Qui excepturi quasi cumque placeat fuga. Ea, eius nihil dolorem cumque</p>
                                        
                                        <NuxtLink  class="default-btn six" to="/about-us">
                                            <i class="bx bx-file"></i>
                                            Learn More
                                        </NuxtLink>
                                    </div>
                                </div>

                                <div class="col-lg-6">
                                    <div class="services-img">
                                        <img src="~/assets/images/services-slider/services-3.png" alt="Image">
                                    </div>
                                </div>
                            </div>
                        </slide>

                        <slide>
                            <div class="row align-items-center">
                                <div class="col-lg-6">
                                    <div class="services-single-item">
                                        <h3>Threat Hunter</h3>

                                        <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Illo ducimus vero, vero corporis voluptates beatae pariatur laudantium, fugiat illum ab deserunt nostrum aliquid quisquam esse? Voluptatibus quia velit numquam esse porro ipsum dolor, sit amet consectetur adipisicing elit. Illo ducimus vero, corporis Voluptatibus quia.</p>
            
                                        <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Perspiciatis, soluta, aspernatur dolorum sequi quisquam ullam in pariatur nihil dolorem cumque excepturi totam. Qui excepturi quasi cumque placeat fuga. Ea, eius nihil dolorem cumque</p>
                                        
                                        <NuxtLink  class="default-btn six" to="/about-us">
                                            <i class="bx bx-file"></i>
                                            Learn More
                                        </NuxtLink>
                                    </div>
                                </div>

                                <div class="col-lg-6">
                                    <div class="services-img">
                                        <img src="~/assets/images/services-slider/services-4.png" alt="Image">
                                    </div>
                                </div>
                            </div>
                        </slide>

                        <slide>
                            <div class="row align-items-center">
                                <div class="col-lg-6">
                                    <div class="services-single-item">
                                        <h3>Splunk Services</h3>

                                        <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Illo ducimus vero, vero corporis voluptates beatae pariatur laudantium, fugiat illum ab deserunt nostrum aliquid quisquam esse? Voluptatibus quia velit numquam esse porro ipsum dolor, sit amet consectetur adipisicing elit. Illo ducimus vero, corporis Voluptatibus quia.</p>
            
                                        <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Perspiciatis, soluta, aspernatur dolorum sequi quisquam ullam in pariatur nihil dolorem cumque excepturi totam. Qui excepturi quasi cumque placeat fuga. Ea, eius nihil dolorem cumque</p>
                                        
                                        <NuxtLink  class="default-btn six" to="/about-us">
                                            <i class="bx bx-file"></i>
                                            Learn More
                                        </NuxtLink>
                                    </div>
                                </div>

                                <div class="col-lg-6">
                                    <div class="services-img">
                                        <img src="~/assets/images/services-slider/services-5.png" alt="Image">
                                    </div>
                                </div>
                            </div>
                        </slide>
                    </carousel>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'ServicesSlider'
}
</script>