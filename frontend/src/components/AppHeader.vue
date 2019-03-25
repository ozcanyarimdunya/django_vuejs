<template>
  <div>
    <a-menu
            theme="light"
            mode="horizontal"
            :defaultSelectedKeys="['1']"
            :style="{ lineHeight: '64px' }">
      <a-menu-item key="1">
        <router-link :to="{name:'home'}">
          <a-icon type="home"/>
          Home
        </router-link>
      </a-menu-item>
      <a-menu-item key="2">
        <router-link :to="{name:'about'}">
          <a-icon type="exclamation-circle"/>
          About
        </router-link>
      </a-menu-item>
      <a-sub-menu key="3" style="float: right">
        <span slot="title" class="submenu-title-wrapper">
            <a-icon type="user"/>
            <span> Admin </span>
            <a-icon type="caret-down"/>
        </span>
        <a-menu-item key="3:1">
          <a href="/admin/" target="_blank">
            <a-icon type="setting"/>
            <span>Admin Panel</span>
          </a>
        </a-menu-item>
        <a-menu-item key="3:2">
          <router-link :to="{name:'logout'}">
            <a-icon type="logout"/>
            <span>Logout</span>
          </router-link>
        </a-menu-item>
      </a-sub-menu>
    </a-menu>
  </div>
</template>

<script>
  export default {
    name: "AppHeader",
    methods: {}
  }
</script>

<style scoped>

</style>