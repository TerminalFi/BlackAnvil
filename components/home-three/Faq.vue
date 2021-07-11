<template>
    <div class="faq-area ptb-100">
        <div class="container">
            <div class="section-title">
                <h2>Frequently Asked  Questions</h2>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. A facilis vel consequatur tempora atque blanditiis exercitationem incidunt, alias corporis quam assumenda dicta, temporibus.</p>
            </div>

            <div class="row align-items-center">
                <div class="col-lg-6">
                    <div class="faq-accordion">
                        <div class="accordion" role="tablist">
                            <b-card no-body class="accordion-item">
                                <b-card-header header-tag="header" class="p-1" role="tab">
                                    <b-button class="default-btn" block v-b-toggle.accordion-1 variant="info">What's The Difference Between IDS And IBS?<span></span></b-button>
                                </b-card-header>
                                <b-collapse id="accordion-1" visible accordion="my-accordion" role="tabpanel">
                                    <b-card-body>
                                        <b-card-text>{{ text }}</b-card-text>
                                    </b-card-body>
                                </b-collapse>
                            </b-card>

                            <b-card no-body class="accordion-item">
                                <b-card-header header-tag="header" class="p-1" role="tab">
                                    <b-button class="default-btn" block v-b-toggle.accordion-2 variant="info">What Is Firewall And Why It Is Used?<span></span></b-button>
                                </b-card-header>
                                <b-collapse id="accordion-2" accordion="my-accordion" role="tabpanel">
                                    <b-card-body>
                                        <b-card-text>{{ text }}</b-card-text>
                                    </b-card-body>
                                </b-collapse>
                            </b-card>

                            <b-card no-body class="accordion-item">
                                <b-card-header header-tag="header" class="p-1" role="tab">
                                    <b-button class="default-btn" block v-b-toggle.accordion-3 variant="info">What Steps Will You Take To Secure server<span></span></b-button>
                                </b-card-header>
                                <b-collapse id="accordion-3" accordion="my-accordion" role="tabpanel">
                                    <b-card-body>
                                        <b-card-text>{{ text }}</b-card-text>
                                    </b-card-body>
                                </b-collapse>
                            </b-card>

                            <b-card no-body class="accordion-item">
                                <b-card-header header-tag="header" class="p-1" role="tab">
                                    <b-button class="default-btn" block v-b-toggle.accordion-4 variant="info">How long does the application process take? <span></span></b-button>
                                </b-card-header>
                                <b-collapse id="accordion-4" accordion="my-accordion" role="tabpanel">
                                    <b-card-body>
                                        <b-card-text>{{ text }}</b-card-text>
                                    </b-card-body>
                                </b-collapse>
                            </b-card>
                        </div>
                    </div>
                </div>
                
                <div class="col-lg-6">
                    <div class="faq-img">
                        <img src="~/assets/images/faq-img.jpg" alt="Image">
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'Faq',
    data() {
      return {
        text: `Lorem, ipsum dolor sit amet How do you Startup? consectetur adipisicing elit. Accusamus ipsa error, excepturi, obcaecati aliquid veniam blanditiis quas voluptates maxime unde, iste minima dolores dolor perferendis facilis. How do you Startup blanditiis voluptates Lorem, ipsum dolor sit amet How do you Startup amet How do.`
      }
    }
}
</script>