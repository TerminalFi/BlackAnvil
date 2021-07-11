<template>
    <div>
        <CoolLightBox 
            :items="items" 
            :fullScreen="true"
            :index="index"
            @close="index = null">
        </CoolLightBox>
        <div class="video-area-six pb-100">
            <div class="container">
                <div class="video-img-six">
                    <img src="~/assets/images/video-img.png" alt="Image">
                    <div class="video-button">
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

                    <h3>Watch Video</h3>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import 'vue-cool-lightbox/dist/vue-cool-lightbox.min.css'

export default {
    name: 'Video',
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