<template>
    <div class="partner-area bg-color-f9f9f9 ptb-100">
        <div class="container">
            <div class="partner-slider-six owl-carousel owl-theme">
                <carousel
                    :autplay = "true"
                    :loop = "true"
                    :paginationEnabled = "false"
                    :autoplaySpeed = "true"
                    :autoplayTimeout = "500"
                    :perPageCustom = "[[0, 1], [576, 2], [768, 2], [992, 3], [1200, 4]]"
                >
                    <slide>
                        <div class="partner-item">
                            <a href="#">
                                <img src="~/assets/images/partner/partner-11.png" alt="Image">
                            </a>
                        </div>
                    </slide>

                    <slide>
                        <div class="partner-item">
                            <a href="#">
                                <img src="~/assets/images/partner/partner-12.png" alt="Image">
                            </a>
                        </div>
                    </slide>

                    <slide>
                        <div class="partner-item">
                            <a href="#">
                                <img src="~/assets/images/partner/partner-13.png" alt="Image">
                            </a>
                        </div>
                    </slide>
                        
                    <slide>
                        <div class="partner-item">
                            <a href="#">
                                <img src="~/assets/images/partner/partner-14.png" alt="Image">
                            </a>
                        </div>
                    </slide>

                    <slide>
                        <div class="partner-item">
                            <a href="#">
                                <img src="~/assets/images/partner/partner-11.png" alt="Image">
                            </a>
                        </div>
                    </slide>

                    <slide>
                        <div class="partner-item">
                            <a href="#">
                                <img src="~/assets/images/partner/partner-12.png" alt="Image">
                            </a>
                        </div>
                    </slide>

                    <slide>
                        <div class="partner-item">
                            <a href="#">
                                <img src="~/assets/images/partner/partner-13.png" alt="Image">
                            </a>
                        </div>
                    </slide>
                        
                    <slide>
                        <div class="partner-item">
                            <a href="#">
                                <img src="~/assets/images/partner/partner-14.png" alt="Image">
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
    name: 'Partner'
}
</script>