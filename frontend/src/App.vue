<template>
  <a-layout id="components-layout-demo-top" class="layout">
    <a-layout-header v-if="isAuthenticated">
      <app-header></app-header>
    </a-layout-header>
    <a-layout-content style="padding: 0 50px">
      <!--<app-bread-crumb></app-bread-crumb>-->
      <div class="breadcrumb-wrapper"></div>
      <div class="router-view-wrapper">
        <router-view></router-view>
      </div>
    </a-layout-content>
    <a-layout-footer style="text-align: center">
      <app-footer></app-footer>
    </a-layout-footer>
  </a-layout>

</template>

<script>
  import {mapGetters} from 'vuex';
  import AppHeader from "./components/AppHeader";
  import AppFooter from "./components/AppFooter";

  export default {
    name: 'app',
    components: {
      AppFooter,
      AppHeader,
    },
    computed: mapGetters('auth', [
      'isAuthenticated',
    ]),
  };
</script>

<style>
  html {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    /*color: #2c3e50;*/
  }

  body, html {
    margin: 0;
    height: 100%;
  }

  .ant-layout-header {
    background: #f0f2f5;
    /*background: #fff;*/
  }

  .router-view-wrapper {
    background: #fff;
    padding: 16px;
    min-height: 480px;
  }

  .breadcrumb-wrapper {
    margin: 12px 0
  }
</style>
