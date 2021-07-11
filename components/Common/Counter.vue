<template>
    <div class="counter-area pt-50 pb-70">
        <div class="container">
            <div class="section-title">
                <h2>Our Numbers and Counting</h2>
                <p>We are growing faster than expected</p>
            </div>
            <div class="row">
                <div class="col-lg-3 col-sm-6">
                    <div class="single-counter">
                        <i class="flaticon-anti-virus-software"></i>
                        <h2>{{ impact.penetration_tests.count }}+</h2>
                        <p>{{ impact.penetration_tests.title }}</p>
                    </div>
                </div>

                <div class="col-lg-3 col-sm-6">
                    <div class="single-counter">
                        <i class="flaticon-cyber"></i>
                        <h2>{{ impact.security_assessments.count }}+</h2>
                        <p>{{ impact.security_assessments.title }}</p>
                    </div>
                </div>

                <div class="col-lg-3 col-sm-6">
                    <div class="single-counter">
                        <i class="flaticon-content"></i>
                        <h2>{{ impact.secure_code_reviews.count }}+</h2>
                        <p>{{ impact.secure_code_reviews.title }}</p>
                    </div>
                </div>

                <div class="col-lg-3 col-sm-6">
                    <div class="single-counter">
                        <i class="flaticon-medal"></i>
                        <h2>{{ impact.incident_response_forensics.count }}+</h2>
                        <p>{{ impact.incident_response_forensics.title }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'Counter',
    data() {
      return {
        impact: {
            penetration_tests: {
                title: 'Penetration Tests',
                count: 136
            },
            security_assessments: {
                title: 'Security Assessments',
                count: 58
            },
            secure_code_reviews: {
                title: 'Secure Code Reviews',
                count: 31
            },
            incident_response_forensics: {
                title: 'Incident Response & Forensics',
                count: 22
            }
        }
      }
    }
}
</script>
