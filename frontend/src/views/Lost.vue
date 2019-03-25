<template>
  <div class="l-wrapper">
    <a-row type="flex" justify="space-around" align="middle">
      <a-col :span="8">
        <div class="forbidden">
          <a-icon
                  type="warning"
                  theme="twoTone"
                  twoToneColor="#CC0011"
                  class="not-found"/>
          <h2>Page Not Found!</h2>
          <div class="go-back">
            <a-icon type="arrow-left"/>
            <router-link to="/"> Take me home.</router-link>
          </div>
        </div>
      </a-col>
    </a-row>
  </div>

</template>

<script>
  export default {
    name: 'lost',
  };
</script>
<style scoped>
  .l-wrapper {
    text-align: center;
  }

  .forbidden {
    /*356x460*/
    position: absolute;
    left: 50%;
    width: 100%;
    top: 180px;
    -webkit-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
  }

  .forbidden h2 {
    color: #CC0011;
  }

  .not-found svg {
    width: 5em;
    height: 5em
  }

  .go-back {
    opacity: .7;
    color: #2c3e50;
    text-align: center;
    width: 40%;
    margin: auto;
  }

  .go-back:hover {
    cursor: pointer;
    opacity: 1;
  }
</style>