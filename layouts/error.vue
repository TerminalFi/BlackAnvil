<template>
    <div class="error-area">
        <div class="d-table">
            <div class="d-table-cell">
                <div class="error-content-wrap">
                    <img src="~/assets/images/404.jpg" alt="Image">
                    <h3>Oops! Page Not Found</h3>
                    <p>The page you were looking for could not be found.</p>
                    <NuxtLink to="/" class="default-btn page-btn">
                        Return To Home Page
                    </NuxtLink>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'Error'
}
</script>