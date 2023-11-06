
<template>
    <div class="vl-parent">
        <loading v-model:active="isLoading"
                 :is-full-page="fullPage"
                 loader = "dots"
                 color = "blue"
                 background-color = "white"
                 before = "test"
                 lock-scroll = true
                 />
    </div>
</template>

<script>
    import Loading from 'vue-loading-overlay';
    import 'vue-loading-overlay/dist/css/index.css';

    export default {
        data() {
            return {
                fullPage: true,
                isLoading: false,
            }
        },

        components: {
            Loading
        },

        methods: {

            onLoading(fullPage) {
                this.isLoading = true;
                this.fullPage = fullPage;
            },

            offLoading() {
                this.isLoading = false;
            },
        }

        
    }
</script>