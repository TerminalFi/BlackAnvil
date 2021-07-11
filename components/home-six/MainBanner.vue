<template>
    <div class="banner-area-six">
        <div class="container-fluid">
            <div class="row align-items-center">
                <div class="col-lg-6">
                    <div class="banner-text">
                        <h1>Cyber Security Solutions Built on Customer Trust</h1>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida. Risus commodo viverra maecenas accumsan lacus vel facilisis.</p>

                        <div class="banner-btn wow fadeInUp" data-wow-delay="1s">
                            <NuxtLink class="default-btn six" to="/pricing">
                                <i class="bx bx-file"></i>
                                Get a Quote
                            </NuxtLink>
                            <NuxtLink class="default-btn active" to="/about-us">
                                <i class="bx bx-user"></i>
                                Discover More
                            </NuxtLink>
                        </div>
                    </div>
                </div>
                
                <div class="col-lg-6">
                    <div class="banner-img">
                        <img src="~/assets/images/banner-six.png" alt="Image">
                    </div>
                </div>
            </div>
        </div>

        <div class="banner-shape-1">
            <img src="~/assets/images/shape/shape-9.png" alt="Image">
        </div>
        <div class="banner-shape-2">
            <img src="~/assets/images/shape/shape-10.png" alt="Image">
        </div>
    </div>
</template>

<script>

export default {
    name: 'Banner'
}
</script>