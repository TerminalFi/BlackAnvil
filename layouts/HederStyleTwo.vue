<template>
    <div class="top-header-area">
        <div class="container-fluid">
            <div class="row align-items-center">
                <div class="col-lg-6 col-sm-8 col-md-7">
                    <ul class="header-content-left">
                        <li>
                            <a href="tel:+44-458-895-456">
                                <i class="bx bx-phone-call"></i>
                                +44 458 895 456
                            </a>
                        </li>
                        <li>
                            <a href="mailto:hello@quvia.com">
                                <i class="bx bx-envelope"></i>
                                hello@quvia.com
                            </a>
                        </li>
                    </ul>
                </div>

                <div class="col-lg-6 col-sm-4 col-md-5">
                    <div class="header-content-right">
                        <ul class="language-area">
                            <li class="language-item-top">
                                <a href="#" class="language-bar">
                                    <span>Language</span>		
                                    <i class="bx bx-chevron-down"></i>
                                </a>

                                <ul class="language-item-bottom">
                                    <li class="language-item">
                                        <a href="#" class="language-link">
                                            <img src="~/assets/images/language/english.png" alt="Image">
                                            English
                                        </a>
                                    </li>
                                    <li class="language-item">
                                        <a href="#" class="language-link">
                                            <img src="~/assets/images/language/arab.png" alt="Image">
                                            العربيّة
                                        </a>
                                    </li>
                                    <li class="language-item">
                                        <a href="#" class="language-link">
                                            <img src="~/assets/images/language/germany.png" alt="Image">
                                            Deutsch
                                        </a>
                                    </li>
                                    <li class="language-item">
                                        <a href="#" class="language-link">
                                            <img src="~/assets/images/language/portugal.png" alt="Image">
                                            󠁥󠁮󠁧󠁿Português
                                        </a>
                                    </li>
                                    <li class="language-item">
                                        <a href="#" class="language-link">
                                            <img src="~/assets/images/language/china.png" alt="Image">
                                            简体中文
                                        </a>
                                    </li>
                                </ul>
                            </li>
                        </ul>

                        <ul class="log-in-sign-up">
                            <li>
                                <i class="bx bx-log-in"></i>
                                <NuxtLink to="/log-in">Log In</NuxtLink>
                            </li>
                            <li>
                                <i class="bx bx-user"></i>
                                <NuxtLink to="/sign-in">Sign Up</NuxtLink>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'HederStyleTwo'
}
</script>