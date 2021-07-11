<template>
    <div class="performance-area ptb-100">
        <div class="container">
            <div class="section-title white-title">
                <h2>High-Performance Solutions</h2>
                <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Doloribus quam neque quibusdam corrupti aspernatur corporis alias nisi dolorum expedita veritatis voluptates minima.</p>
            </div>

            <div class="single-security-wrap owl-carousel owl-theme">
                <carousel
                    :autplay = "true"
                    :loop = "true"
                    :paginationEnabled = "true"
                    :autoplaySpeed = "true"
                    :autoplayTimeout = "500"
                    :perPageCustom = "[[0, 1], [576, 2], [768, 2], [992, 3], [1200, 4]]"
                >
                    <slide>
                        <div class="single-security">
                            <i class="flaticon-website"></i>
                            <h3>Confidential Information</h3>
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor</p>

                            <a href="#" class="read-more">
                                Read More
                            </a>
                        </div>
                    </slide>
                    
                    <slide>
                        <div class="single-security">
                            <i class="flaticon-profile"></i>
                            <h3>Mobile Security</h3>
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor</p>

                            <a href="#" class="read-more">
                                Read More
                            </a>
                        </div>
                    </slide>
                    
                    <slide>
                        <div class="single-security">
                            <i class="flaticon-content"></i>
                            <h3>Website Protection</h3>
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor</p>

                            <a href="#" class="read-more">
                                Read More
                            </a>
                        </div>
                    </slide>
                    
                    <slide>
                        <div class="single-security">
                            <i class="flaticon-cyber"></i>
                            <h3>Hacking Protection</h3>
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor</p>

                            <a href="#" class="read-more">
                                Read More
                            </a>
                        </div>
                    </slide>

                    <slide>
                        <div class="single-security">
                            <i class="flaticon-profile"></i>
                            <h3>Mobile Security</h3>
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor</p>

                            <a href="#" class="read-more">
                                Read More
                            </a>
                        </div>
                    </slide>

                    <slide>
                        <div class="single-security">
                            <i class="flaticon-website"></i>
                            <h3>Confidential Information</h3>
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor</p>

                            <a href="#" class="read-more">
                                Read More
                            </a>
                        </div>
                    </slide>
                    
                    <slide>
                        <div class="single-security">
                            <i class="flaticon-profile"></i>
                            <h3>Mobile Security</h3>
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor</p>

                            <a href="#" class="read-more">
                                Read More
                            </a>
                        </div>
                    </slide>
                    
                    <slide>
                        <div class="single-security">
                            <i class="flaticon-content"></i>
                            <h3>Website Protection</h3>
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor</p>

                            <a href="#" class="read-more">
                                Read More
                            </a>
                        </div>
                    </slide>
                </carousel>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'Performance',
}
</script>