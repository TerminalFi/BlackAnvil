<template>
    <div class="user-area-all-style sign-up-area ptb-100">
        <div class="container">
            <div class="section-title">
                <h2>Create an account!</h2>
                <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Laudantium quas cumque iste veniam id dolorem deserunt ratione error voluptas rem ullam possimus placeat, ut, odio</p>
            </div>

            <div class="contact-form-action">
                <form>
                    <div class="row">
                        <div class="col-lg-4 col-md-4 col-sm-12">
                            <button class="default-btn" type="submit">
                                Google
                            </button>
                        </div>

                        <div class="col-lg-4 col-md-4 col-sm-12">
                            <button class="default-btn" type="submit">
                                Facebook
                            </button>
                        </div>

                        <div class="col-lg-4 col-md-4 col-sm-12">
                            <button class="default-btn" type="submit">
                                Twitter
                            </button>
                        </div>

                        <div class="col-md-12 col-sm-12">
                            <div class="form-group">
                                <input class="form-control" type="text" name="name" placeholder="First Name">
                            </div>
                        </div>

                        <div class="col-md-12 col-sm-12 ">
                            <div class="form-group">
                                <input class="form-control" type="text" name="name" placeholder="Last Name">
                            </div>
                        </div>

                        <div class="col-md-12 col-sm-12">
                            <div class="form-group">
                                <input class="form-control" type="text" name="name" placeholder="Enter your Username">
                            </div>
                        </div>

                        <div class="col-md-12 col-sm-12">
                            <div class="form-group">
                                <input class="form-control" type="email" name="email" placeholder="Email Address">
                            </div>
                        </div>

                        <div class="col-md-12 col-sm-12">
                            <div class="form-group">
                                <input class="form-control" type="text" name="password" placeholder="Password">
                            </div>
                        </div>

                        <div class="col-md-12 col-sm-12 ">
                            <div class="form-group">
                                <input class="form-control" type="text" name="password" placeholder="Confirm Password">
                            </div>
                        </div>

                        <div class="col-md-12 col-sm-12 col-xs-12 form-condition">
                            <div class="agree-label">
                                <input type="checkbox" id="chb1">
                                <label for="chb1">
                                    I agree with 
                                    <NuxtLink to="/privacy-policy">Privacy Policy</NuxtLink>
                                </label>
                            </div>

                            <div class="agree-label">
                                <input type="checkbox" id="chb2">
                                <label for="chb2">
                                    I agree with 
                                    <NuxtLink to="/terms-conditions">Terms & Conditions</NuxtLink>
                                </label>
                            </div>
                        </div>

                        <div class="col-12">
                            <button class="default-btn btn-two" type="submit">
                                Register Account
                            </button>
                        </div>
                        
                        <div class="col-12">
                            <p class="account-desc">
                                Already have an account?
                                <NuxtLink to="log-in"> Log In</NuxtLink>
                            </p>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'SignUp'
}
</script>