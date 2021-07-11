<template>
    <footer class="footer-area pt-100 pb-70">
        <div class="container">
            <div class="row">
                <div class="col-lg-3 col-md-6">
                    <div class="single-footer-widget">
                        <NuxtLink to="/" class="logo">
                            <img src="~/assets/images/logo-black.png" alt="Image">
                        </NuxtLink>

                        <p>Lorem ipsum dolor sit amet, consec tetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et. Lorem ipsum dolor sit amet</p>

                        <ul class="social-icon">
                            <li>
                                <a href="#">
                                    <i class="bx bxl-facebook"></i>
                                </a>
                            </li>
                            <li>
                                <a href="#">
                                    <i class="bx bxl-instagram"></i>
                                </a>
                            </li>
                            <li>
                                <a href="#">
                                    <i class="bx bxl-linkedin-square"></i>
                                </a>
                            </li>
                            <li>
                                <a href="#">
                                    <i class="bx bxl-twitter"></i>
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>

                <div class="col-lg-3 col-md-6">
                    <div class="single-footer-widget">
                        <h3>Help</h3>

                        <ul class="import-link">
                            <li>
                                <NuxtLink to="/privacy-policy">Privacy Policy</NuxtLink>
                            </li>
                            <li>
                                <a href="#">Return Policy</a>
                            </li>
                            <li>
                                <NuxtLink to="terms-conditions">Termas & Conditions</NuxtLink>
                            </li>
                            <li>
                                <NuxtLink to="/terms-conditions">About Us</NuxtLink>
                            </li>
                            <li>
                                <a href="#">Careers</a>
                            </li>
                        </ul>
                    </div>
                </div>

                <div class="col-lg-3 col-md-6">
                    <div class="single-footer-widget">
                        <h3>Services Link</h3>

                        <ul class="import-link">
                            <li>
                                <a href="#">Threat Hunter</a>
                            </li>
                            <li>
                                <a href="#">Incident Responder</a>
                            </li>
                            <li>
                                <a href="#">Secure Managed IT</a>
                            </li>
                            <li>
                                <a href="#">Compliance</a>
                            </li>
                            <li>
                                <a href="#">Cyber Security</a>
                            </li>
                        </ul>
                    </div>
                </div>

                <div class="col-lg-3 col-md-6">
                    <div class="single-footer-widget">
                        <h3>Contacts</h3>

                        <ul class="address">
                            <li class="location">
                                <span>Address:</span>
                                2750 Quadra Street Victoria, Canada.
                            </li>
                            <li>
                                <span>Email:</span>
                                <a href="mailto:hello@quvia.com">hello@quvia.com</a>
                            </li>
                            <li>
                                <span>Phone:</span>
                                <a href="tel:+44-587-154756">+44 587 154756</a>
                            </li>
                            <li>
                                <span>Fax:</span>
                                <a href="tel:+44-785-4578964">+44 785 4578964</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </footer>
</template>

<script>

export default {
    name: 'FooterStyleTwo'
}
</script>