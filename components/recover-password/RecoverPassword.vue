<template>
    <div class="user-area-all-style recover-password-area ptb-100">
        <div class="container">
            <div class="contact-form-action">
                <div class="form-heading text-center">
                    <h3 class="form-title">Reset Password!</h3>
                    <p class="reset-desc">
                        Enter the email of your account to reset the password. Then you will receive a link to email to reset the password. If you have any issue about reset password 
                        <NuxtLink to="/contact">contact us.</NuxtLink>
                    </p>
                </div>

                <form>
                    <div class="row">
                        <div class="col-12">
                            <div class="form-group">
                                <input class="form-control" type="email" name="name" placeholder="Enter Email Address">
                            </div>
                        </div>
                        
                        <div class="col-lg-6 col-md-6 col-sm-6">
                            <NuxtLink class="now-log-in font-q" to="log-in">Log In in your account</NuxtLink>
                        </div>
                        <div class="col-lg-6 col-md-6 col-sm-6">
                            <p class="now-register">
                                Not a member?
                                <NuxtLink class="font-q" to="sign-in">Register</NuxtLink>
                            </p>
                        </div>
                        <div class="col-12">
                            <button class="default-btn btn-two" type="submit">
                                Reset Password
                            </button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'RecoverPassword'
}
</script>