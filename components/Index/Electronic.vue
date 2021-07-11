<template>
    <div class="electronic-area bg-color ptb-100">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-6">
                    <div class="electronic-content">
                        <h2>Engagements From Start To Finish And Beyond</h2>
                        <div class="electronic-tab-wrap">
                            <div class="electronic-tab">
                                <b-card no-body>
                                    <b-tabs card>
                                        <b-tab title="Pre-game">
                                            <b-card-text
                                                ><p>
                                                    Involves the work and
                                                    logistics that are required
                                                    to be completed before our
                                                    engineers actively engage in
                                                    the assessment.
                                                </p>

                                                <p>
                                                    Frequently involves
                                                    initiating the project
                                                    workspace, preparing the
                                                    attack plan, project
                                                    scoping, kickoff planning
                                                    and finalizing the attack
                                                    plan.
                                                </p>
                                            </b-card-text>
                                            <NuxtLink
                                                class="default-btn"
                                                to="/about-us"
                                            >
                                                Learn About
                                            </NuxtLink>
                                        </b-tab>

                                        <b-tab title="Game-time">
                                            <b-card-text
                                                ><p>
                                                    At this point, our engineers
                                                    consider this the execution
                                                    phase.
                                                </p>

                                                <p>
                                                    Our engineers will take our
                                                    manual, automated and hybrid
                                                    approaches to full execute
                                                    on the defined scope.
                                                    Leveraging years of
                                                    expertise and application to
                                                    identify risks and
                                                    vulnerabilities.
                                                </p>
                                            </b-card-text>
                                            <NuxtLink
                                                class="default-btn"
                                                to="/about-us"
                                            >
                                                Learn About
                                            </NuxtLink>
                                        </b-tab>

                                        <b-tab title="Post-game">
                                            <b-card-text
                                                ><p>
                                                    This consists of the
                                                    engagement close out. Our
                                                    engineers will deliver a
                                                    high quality report and
                                                    debrief stakeholders.
                                                    Reviewing the most severe
                                                    security risks identified
                                                    and reflect on lessons
                                                    learned.
                                                </p>
                                            </b-card-text>
                                            <NuxtLink
                                                class="default-btn"
                                                to="/about-us"
                                            >
                                                Learn About
                                            </NuxtLink>
                                        </b-tab>
                                    </b-tabs>
                                </b-card>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="col-lg-6">
                    <div class="electronic-img">
                        <img
                            src="~/assets/images/electronic-img.png"
                            alt="Image"
                        />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'Electronic',
    data() {
      return {
        text: `Lorem, ipsum dolor sit amet How do you Startup? consectetur adipisicing elit. Accusamus ipsa error, excepturi, obcaecati aliquid veniam blanditiis quas voluptates maxime unde, iste minima dolores dolor perferendis facilis. How do you Startup blanditiis voluptates Lorem, ipsum dolor sit amet How do you Startup amet How do.`
      }
    }
}
</script>
