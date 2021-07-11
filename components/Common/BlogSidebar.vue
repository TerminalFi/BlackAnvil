<template>
    <div class="widget-area" id="secondary">
        <div class="widget widget_search">
            <h3 class="widget-title">Search Now</h3>
            <div class="post-wrap">
                <form class="search-form">
                    <label>
                        <span class="screen-reader-text">Search for:</span>
                        <input type="search" class="search-field" placeholder="Search...">
                    </label>
                    <button type="submit"><i class='bx bx-search'></i></button>
                </form>
            </div>
        </div>

        <div class="widget widget-peru-posts-thumb">
            <h3 class="widget-title">Popular Posts</h3>
            <div class="post-wrap">
                <div class="item">
                    <NuxtLink to="/blog-details" class="thumb">
                        <span class="fullimage cover bg1" role="img"></span>
                    </NuxtLink>
                    <div class="info">
                        <time datetime="2020-06-30">April 20, 2020</time>
                        <h4 class="title usmall">
                            <NuxtLink to="/blog-details">
                                Drughydrus Add Google Drive To Roughrobin Torjan
                            </NuxtLink>
                        </h4>
                    </div>

                    <div class="clear"></div>
                </div>

                <div class="item">
                    <NuxtLink to="/blog-details" class="thumb">
                        <span class="fullimage cover bg2" role="img"></span>
                    </NuxtLink>
                    <div class="info">
                        <time datetime="2020-06-30">Jun 21, 2020</time>
                        <h4 class="title usmall">
                            <NuxtLink to="/blog-details">
                                DHS Issues Emergency Directive To Prevent Hacking Attack
                            </NuxtLink>
                        </h4>
                    </div>

                    <div class="clear"></div>
                </div>

                <div class="item">
                    <NuxtLink to="/blog-details" class="thumb">
                        <span class="fullimage cover bg3" role="img"></span>
                    </NuxtLink>
                    <div class="info">
                        <time datetime="2020-06-30">Jun  22, 2020</time>
                        <h4 class="title usmall">
                            <NuxtLink to="/blog-details">
                                Security In A Fragment World Of Workload
                            </NuxtLink> 
                        </h4>
                    </div>

                    <div class="clear"></div>
                </div>
            </div>
        </div>
 
        <div class="widget widget_categories">
            <h3 class="widget-title">Categories</h3>
            <div class="post-wrap">
                <ul>
                    <li>
                        <a href="#">Blockchain <span>(10)</span></a>
                    </li>
                    <li>
                        <a href="#">Cyber security <span>(20)</span></a>
                    </li>
                    <li>
                        <a href="#">Cybercrime <span>(10)</span></a>
                    </li>
                    <li>
                        <a href="#">Global news <span>(12)</span></a>
                    </li>
                    <li>
                        <a href="#">Ransomware <span>(16)</span></a>
                    </li>
                </ul>
            </div>
        </div>
 
        <div class="widget widget_tag_cloud">
            <h3 class="widget-title">Tags</h3>
            <div class="post-wrap">
                <div class="tagcloud">
                    <a href="#">Blockchain (3)</a>
                    <a href="#">Cyber security (3)</a>
                    <a href="#">Cybercrime (2)</a>
                    <a href="#">Global news (2)</a>
                    <a href="#">Ransomware (1)</a>
                    <a href="#">Whitepapers (2) </a>
                </div>
            </div>
        </div>       
    </div>
</template>

<script>

export default {
    name: 'BlogSidebar'
}
</script>