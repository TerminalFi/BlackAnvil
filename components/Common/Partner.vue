<template>
    <div class="partner-area ptb-100">
        <div class="container">
            <div class="partner-wrap owl-carousel owl-theme">
                <carousel
                    :autplay = "true"
                    :loop = "true"
                    :paginationEnabled = "false"
                    :autoplaySpeed = "true"
                    :autoplayTimeout = "500"
                    :perPageCustom = "[[0, 2], [576, 3], [768, 4], [1024, 4], [1200, 5]]"
                >
                    <slide>
                        <div class="partner-item">
                            <img src="~/assets/images/partner/partner-1.png" alt="Image">
                            <a class="partner-overly" href="#" target="_blank">
                                <img src="~/assets/images/partner/partner-6.png" alt="Image">
                            </a>
                        </div>
                    </slide>

                    <slide>
                        <div class="partner-item">
                            <img src="~/assets/images/partner/partner-2.png" alt="Image">
                            <a class="partner-overly" href="#" target="_blank">
                                <img src="~/assets/images/partner/partner-7.png" alt="Image">
                            </a>
                        </div>
                    </slide>

                    <slide>
                        <div class="partner-item">
                            <img src="~/assets/images/partner/partner-3.png" alt="Image">
                            <a class="partner-overly" href="#" target="_blank">
                                <img src="~/assets/images/partner/partner-8.png" alt="Image">
                            </a>
                        </div>
                    </slide>
                        
                    <slide>
                        <div class="partner-item">
                            <img src="~/assets/images/partner/partner-4.png" alt="Image">
                            <a class="partner-overly" href="#" target="_blank">
                                <img src="~/assets/images/partner/partner-9.png" alt="Image">
                            </a>
                        </div>
                    </slide>

                    <slide>
                        <div class="partner-item">
                            <img src="~/assets/images/partner/partner-5.png" alt="Image">
                            <a class="partner-overly" href="#" target="_blank">
                                <img src="~/assets/images/partner/partner-10.png" alt="Image">
                            </a>
                        </div>
                    </slide>
                    <slide>
                        <div class="partner-item">
                            <img src="~/assets/images/partner/partner-1.png" alt="Image">
                            <a class="partner-overly" href="#" target="_blank">
                                <img src="~/assets/images/partner/partner-6.png" alt="Image">
                            </a>
                        </div>
                    </slide>

                    <slide>
                        <div class="partner-item">
                            <img src="~/assets/images/partner/partner-2.png" alt="Image">
                            <a class="partner-overly" href="#" target="_blank">
                                <img src="~/assets/images/partner/partner-7.png" alt="Image">
                            </a>
                        </div>
                    </slide>

                    <slide>
                        <div class="partner-item">
                            <img src="~/assets/images/partner/partner-3.png" alt="Image">
                            <a class="partner-overly" href="#" target="_blank">
                                <img src="~/assets/images/partner/partner-8.png" alt="Image">
                            </a>
                        </div>
                    </slide>
                        
                    <slide>
                        <div class="partner-item">
                            <img src="~/assets/images/partner/partner-4.png" alt="Image">
                            <a class="partner-overly" href="#" target="_blank">
                                <img src="~/assets/images/partner/partner-9.png" alt="Image">
                            </a>
                        </div>
                    </slide>

                    <slide>
                        <div class="partner-item">
                            <img src="~/assets/images/partner/partner-5.png" alt="Image">
                            <a class="partner-overly" href="#" target="_blank"> 
                                <img src="~/assets/images/partner/partner-10.png" alt="Image">
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