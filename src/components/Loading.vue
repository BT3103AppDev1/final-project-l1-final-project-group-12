
<template>
    <div class="vl-parent">
        <loading v-model:active="isLoading"
                 :is-full-page="fullPage"
                 :loader = "loader"
                 :width = "width"
                 :color = "color"
                 :background-color = "backgroundColor"
                 :lock-scroll = "lockScroll"
                 />
    </div>
</template>

<script>
    import Loading from 'vue-loading-overlay';
    import 'vue-loading-overlay/dist/css/index.css';

    export default {
        data() {
            return {
                isLoading: false,
                fullPage: true,
                loader: "dots",
                width: 95,
                color: "blue",
                backgroundColor: "white",
                lockScroll: true,

            }
        },

        components: {
            Loading
        },

        methods: {

            onLoading() {
                this.isLoading = true;

            },

            offLoading() {
                this.isLoading = false;
            },
        }

        
    }
</script>