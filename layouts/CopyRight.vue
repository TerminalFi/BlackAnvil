<template>
    <div>
        <div class="copy-right-area">
            <div class="container">
                <div class="row align-items-center">
                    <div class="col-lg-6 col-md-6">
                        <p>Copyright @2020 Quvia. Designed <a href="https://envytheme.com/" target="_blank">EnvyTheme</a></p>
                    </div>

                    <div class="col-lg-6 col-md-6">
                        <ul class="footer-menu">
                            <li>
                                <NuxtLink to="/privacy-policy" target="_blank">
                                    Privacy Policy 
                                </NuxtLink>
                            </li>
                            <li>
                                <NuxtLink to="/terms-conditions" target="_blank">
                                    Terms & Conditions
                                </NuxtLink>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <back-to-top bottom="50px" right="50px">
            <div class="go-top">
                <i class='bx bx-chevrons-up'></i>
                <i class='bx bx-chevrons-up'></i>
            </div>
        </back-to-top>
    </div>
</template>

<script>

export default {
    name: 'CopyRight'
}
</script>