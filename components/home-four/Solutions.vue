<template>
    <div class="project-area pb-100">
        <div class="container-fluid">
            <div class="section-title">
                <h2>Quvia Recent Project Case</h2>
                <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Doloribus quam neque quibusdam corrupti aspernatur corporis alias nisi dolorum expedita veritatis voluptates minima.</p>
            </div>

            <div class="solutions-wrap owl-carousel owl-theme">
                <carousel
                    :autplay = "true"
                    :loop = "true"
                    :paginationEnabled = "false"
                    :autoplaySpeed = "true"
                    :autoplayTimeout = "500"
                    :perPageCustom = "[[0, 1], [576, 1], [768, 2], [992, 3], [1200, 3]]"
                >
                    <slide>
                        <div class="single-solutions solutions-time-bg-7">
                            <div class="solutions-content">
                                <h3>Hacking Parotection Software</h3>
                                <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Officia, obcaecati praesentium. Labore sint recusandae perspiciatis laudantium, deleniti non</p>
                                <a href="#" class="read-more">
                                    Read More
                                </a>
                            </div>
                        </div>
                    </slide>
                
                    <slide>
                        <div class="single-solutions solutions-time-bg-8">
                            <div class="solutions-content">
                                <h3>Security Awarness Training</h3>
                                <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Officia, obcaecati praesentium. Labore sint recusandae perspiciatis laudantium, deleniti non</p>
                                <a href="#" class="read-more">
                                    Read More
                                </a>
                            </div>
                        </div>
                    </slide>
                
                    <slide>
                        <div class="single-solutions solutions-time-bg-9">
                            <div class="solutions-content">
                                <h3>Cyber Security Manged IT</h3>
                                <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Officia, obcaecati praesentium. Labore sint recusandae perspiciatis laudantium, deleniti non</p>
                                <a href="#" class="read-more">
                                    Read More
                                </a>
                            </div>
                        </div>
                    </slide>

                    <slide>
                        <div class="single-solutions solutions-time-bg-7">
                            <div class="solutions-content">
                                <h3>Hacking Parotection Software</h3>
                                <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Officia, obcaecati praesentium. Labore sint recusandae perspiciatis laudantium, deleniti non</p>
                                <a href="#" class="read-more">
                                    Read More
                                </a>
                            </div>
                        </div>
                    </slide>
                
                    <slide>
                        <div class="single-solutions solutions-time-bg-8">
                            <div class="solutions-content">
                                <h3>Security Awarness Training</h3>
                                <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Officia, obcaecati praesentium. Labore sint recusandae perspiciatis laudantium, deleniti non</p>
                                <a href="#" class="read-more">
                                    Read More
                                </a>
                            </div>
                        </div>
                    </slide>
                
                    <slide>
                        <div class="single-solutions solutions-time-bg-9">
                            <div class="solutions-content">
                                <h3>Cyber Security Manged IT</h3>
                                <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Officia, obcaecati praesentium. Labore sint recusandae perspiciatis laudantium, deleniti non</p>
                                <a href="#" class="read-more">
                                    Read More
                                </a>
                            </div>
                        </div>
                    </slide>
                </carousel>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'Solutions'
}
</script>