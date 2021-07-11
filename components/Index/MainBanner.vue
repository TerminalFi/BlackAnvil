<template>
    <div>
        <CoolLightBox
            :items="items"
            :fullScreen="true"
            :index="index"
            @close="index = null"
        >
        </CoolLightBox>
        <div class="banner-area banner-item-bg-1 jarallax">
            <div class="container">
                <div class="row align-items-center">
                    <div class="col-lg-9">
                        <div class="banner-text">
                            <span
                                >Continuously researching to stay at the
                                bleeding edge of security</span
                            >
                            <h1>Modern Information Security Assessments</h1>
                            <p>
                                Identify and surface security vulnerabilities
                                affecting your organization through a systematic
                                testing process focused on your networks,
                                applications, physical facilities and human
                                assets.
                            </p>

                            <!-- <div class="banner-btn">
                                <NuxtLink to="/pricing" class="default-btn">
                                    Booking Now
                                </NuxtLink>

                                <NuxtLink
                                    to="/about-us"
                                    class="default-btn active"
                                >
                                    About Us
                                </NuxtLink>
                            </div> -->
                        </div>
                    </div>

                    <div class="col-lg-3">
                        <div class="video-btn-animat">
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

            <div class="container pt-100">
                <div class="row">
                    <div class="col-lg-4 col-sm-6">
                        <div class="single-features">
                            <h3><i class="bx bx-check-shield"></i> Security</h3>
                            <p>
                                Assessing the security of your services and
                                infrastructure that make up your organization
                            </p>
                            <span class="bx bx-check-shield"></span>
                        </div>
                    </div>

                    <div class="col-lg-4 col-sm-6">
                        <div class="single-features">
                            <h3><i class="bx bx-lock"></i> Data</h3>
                            <p>
                                Validate that security controls are in place to
                                protect you and your organizations privacy and
                                data.
                            </p>
                            <span class="bx bx-lock"></span>
                        </div>
                    </div>

                    <div class="col-lg-4 col-sm-6 offset-sm-3 offset-lg-0">
                        <div class="single-features mb-0">
                            <h3>
                                <i class="bx bx-certification"></i> Industry
                                Standards
                            </h3>
                            <p>
                                Baseline the environment against industry
                                security standards from NIST, DISA, NSA and
                                various others.
                            </p>
                            <span class="bx bx-certification"></span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="lines">
                <div class="line"></div>
                <div class="line"></div>
                <div class="line"></div>
            </div>
        </div>
    </div>
</template>

<script>
import CoolLightBox from 'vue-cool-lightbox'
import 'vue-cool-lightbox/dist/vue-cool-lightbox.min.css'
export default {
    name: 'MainBanner',
    components: { CoolLightBox },
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
