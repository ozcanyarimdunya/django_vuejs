<template>
  <div class="about">
    <div class="title">
      <a-badge :count="version" :title="'Recorder '+version"
               :numberStyle="{backgroundColor: '#1890ff'} ">
        <h1>Application &nbsp;&nbsp;</h1>
      </a-badge>
    </div>
    <div class="body">
      <p>This tool has been developed for <strong> a team</strong>.</p>
      <p v-if="false">
        Detail about the team
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad adipisci corporis deserunt dolore earum
        eius et ex facere labore laboriosam laudantium, officiis omnis perspiciatis qui quibusdam saepe
        voluptate! Eius hic in iusto similique. Ab atque dicta eius error, laborum magnam necessitatibus
        nesciunt nihil nobis pariatur placeat quasi qui repellendus sint unde. Ab aspernatur deleniti, iste
        iusto nam possimus sequi velit voluptatem? Dolorum excepturi laboriosam magni quam quo repellendus vel?
        Ad animi aperiam commodi, consequatur debitis dolor dolores doloribus et ipsa itaque magnam, modi nihil
        nulla odit placeat possimus praesentium quae quaerat quam, quidem sapiente similique temporibus
        veritatis! Accusantium dolorem enim, fuga repellendus reprehenderit temporibus! Animi culpa doloribus
        est fuga fugiat laboriosam minima molestiae, nemo nulla, quae similique veritatis. Ab alias beatae
        consequuntur, corporis culpa cupiditate deserunt dolore ea eaque illo laboriosam modi molestiae nobis
        odit perferendis quia quibusdam reiciendis, rem reprehenderit saepe sed temporibus veritatis vero
        voluptas, voluptatum. A ab cum itaque perspiciatis ullam! Adipisci consequuntur earum pariatur provident
        ratione recusandae? Consectetur delectus exercitationem id iste magnam, maiores maxime, nostrum optio
        possimus quam quos recusandae rem repellendus rerum voluptate? Atque dolor doloribus ducimus eveniet
        excepturi harum neque nisi obcaecati perferendis quae repellendus sequi, temporibus ut vitae
        voluptatibus? Blanditiis, impedit, soluta!
      </p>
    </div>
  </div>
</template>
<script>
  export default {
    data() {
      return {
        version: 'v1.0'
      }
    }
  }
</script>
<style scoped>
  .about {
    text-align: center;
  }

  .title {
    text-align: center;
    padding: 10px 0;
  }

  .body {
    padding: 24px;
  }
</style>