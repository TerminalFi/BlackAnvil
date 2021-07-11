<template>
    <div>
        <CoolLightBox 
            :items="items" 
            :fullScreen="true"
            :index="index"
            @close="index = null">
        </CoolLightBox>
        
        <div class="hero-slider-area">
            <div class="hero-slider-wrap owl-carousel owl-theme">
                <carousel
                    :autplay = "true"
                    :loop = "true"
                    :paginationEnabled = "false"
                    :autoplaySpeed = "true"
                    :autoplayTimeout = "500"
                    :perPageCustom = "[[0, 1]]"
                >
                    <slide>
                        <div class="slider-item slider-item-bg-1">
                            <div class="d-table">
                                <div class="d-table-cell">
                                    <div class="container">
                                        <div class="row align-items-center">
                                            <div class="col-lg-9">
                                                <div class="slider-text one">
                                                    <h1>Cyber Security & IT Management</h1>
                                                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nihil architecto laborum eaque! Deserunt maxime, minus quas molestiae reiciendis esse natus nisi iure.</p>
                
                                                    <div class="slider-btn">
                                                        <NuxtLink class="default-btn" to="/contact">
                                                            Contact Us
                                                        </NuxtLink>
                                                        <NuxtLink class="default-btn active" to="/about-us">
                                                            Learn More
                                                        </NuxtLink>
                                                    </div>
                                                </div>
                                            </div>
                                            
                                            <div class="col-lg-3">
                                                <div class="video-btn-animat one">
                                                    <div
                                                        class="video-btn popup-youtube"
                                                        v-for="(image, imageIndex) in items"
                                                        :key="imageIndex"
                                                        @click="index = imageIndex"
                                                        style="cursor: pointer"
                                                    >
                                                        <i class="bx bx-play"></i>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </slide>

                    <slide>
                        <div class="slider-item slider-item-bg-2">
                            <div class="d-table">
                                <div class="d-table-cell">
                                    <div class="container">
                                        <div class="row align-items-center">
                                            <div class="col-lg-9">
                                                <div class="slider-text two">
                                                    <h1>Cyber Security Is Not Optional</h1>
                                                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nihil architecto laborum eaque! Deserunt maxime, minus quas molestiae reiciendis esse natus nisi iure.</p>
                                                    
                                                    <div class="slider-btn">
                                                        <NuxtLink class="default-btn" to="/contact">
                                                            Contact Us
                                                        </NuxtLink>
                                                        <NuxtLink class="default-btn active" to="/about-us">
                                                            Learn More
                                                        </NuxtLink>
                                                    </div>
                                                </div>
                                            </div>

                                            <div class="col-lg-3">
                                                <div class="video-btn-animat two">
                                                    <div
                                                        class="video-btn popup-youtube"
                                                        v-for="(image, imageIndex) in items"
                                                        :key="imageIndex"
                                                        @click="index = imageIndex"
                                                        style="cursor: pointer"
                                                    >
                                                        <i class="bx bx-play"></i>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </slide>
                </carousel>
            </div>
        </div>
    </div>
</template>

<script>
import 'vue-cool-lightbox/dist/vue-cool-lightbox.min.css'

export default {
    name: 'Banner',
    data: function () {
        return {
            items: [
                {
                    src: 'https://www.youtube.com/watch?v=sdpxddDzXfE',
                }
            ],
            index: null
        };
    },
}
</script>