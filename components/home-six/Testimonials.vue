<template>
    <section class="testimonials-area bg-color-f9f9f9 pt-100 pb-70">
        <div class="container">
            <div class="section-title-six">
                <span>Testimonials</span>
                <h2>What Customers Say About Us</h2>
            </div>

            <div class="testimonials">
                <div class="testimonials-slider owl-carousel owl-theme">
                    <carousel
                        :autplay = "true"
                        :loop = "true"
                        :paginationEnabled = "false"
                        :navigationEnabled = "true"
                        navigationNextLabel="<i class='bx bx-right-arrow-alt'></i>"
                        navigationPrevLabel="<i class='bx bx-left-arrow-alt'></i>"
                        :autoplaySpeed = "true"
                        :autoplayTimeout = "500"
                        :perPageCustom = "[[0, 1]]"
                    >
                        <slide>
                            <div class="testimonials-item">
                                <p>“Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Risus commodo viverramaecenas accumsan lacus vel facilisis.”</p> 

                                <div class="testimonials-view">
                                    <img src="~/assets/images/testimonials/testimonials-1.jpg" alt="Image">
                                    <h3>Jason Doe</h3>
                                    <span>Web Developer</span>
                                </div>
                            </div>
                        </slide>

                        <slide>
                            <div class="testimonials-item">
                                <p>“Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Risus commodo viverramaecenas accumsan lacus vel facilisis.”</p> 

                                <div class="testimonials-view">
                                    <img src="~/assets/images/testimonials/testimonials-2.jpg" alt="Image">
                                    <h3>Alex Dew</h3>
                                    <span>Web Designer</span>
                                </div>
                            </div>
                        </slide>

                        <slide>
                            <div class="testimonials-item">
                                <p>“Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Risus commodo viverramaecenas accumsan lacus vel facilisis.”</p> 

                                <div class="testimonials-view">
                                    <img src="~/assets/images/testimonials/testimonials-4.jpg" alt="Image">
                                    <h3>Peter Pers</h3>
                                    <span>Web Developer</span>
                                </div>
                            </div>
                        </slide>

                        <slide>
                            <div class="testimonials-item">
                                <p>“Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Risus commodo viverramaecenas accumsan lacus vel facilisis.”</p> 

                                <div class="testimonials-view">
                                    <img src="~/assets/images/testimonials/testimonials-3.jpg" alt="Image">
                                    <h3>Alex Dew</h3>
                                    <span>Web Designer</span>
                                </div>
                            </div>
                        </slide>
                    </carousel>
                </div>
                <i class='quote bx bxs-quote-alt-right'></i>
            </div>
        </div>
    </section>
</template>

<script>

export default {
    name: 'Testimonials'
}
</script>