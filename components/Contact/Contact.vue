<template>
    <div class="faq-contact-area ptb-100">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <div class="contact-wrap">
                        <div class="contact-form">
                            <div class="section-title">
                                <span class="top-title">Contact Us</span>
                                <h2>Drop us a message for any query</h2>
                                <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Eaque quibusdam deleniti porro praesentium. Aliquam minus quisquam velit in at nam.</p>
                            </div>

                            <form id="contactForm">
                                <div class="row">
                                    <div class="col-lg-6 col-sm-6">
                                        <div class="form-group">
                                            <input type="text" name="name" id="name" class="form-control" required placeholder="Your Name">
                                        </div>
                                    </div>
        
                                    <div class="col-lg-6 col-sm-6">
                                        <div class="form-group">
                                            <input type="email" name="email" id="email" class="form-control" required placeholder="Your Email">
                                        </div>
                                    </div>
        
                                    <div class="col-lg-6 col-sm-6">
                                        <div class="form-group">
                                            <input type="text" name="phone_number" id="phone_number" required class="form-control" placeholder="Your Phone">
                                        </div>
                                    </div>
        
                                    <div class="col-lg-6 col-sm-6">
                                        <div class="form-group">
                                            <input type="text" name="msg_subject" id="msg_subject" class="form-control" required placeholder="Your Subject">
                                        </div>
                                    </div>
        
                                    <div class="col-lg-12 col-md-12">
                                        <div class="form-group">
                                            <textarea name="message" class="form-control" id="message" cols="30" rows="8" required></textarea>
                                        </div>
                                    </div>
        
                                    <div class="col-lg-12 col-md-12">
                                        <button type="submit" class="default-btn page-btn">
                                            Send Message
                                        </button>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'Contact'
}
</script>