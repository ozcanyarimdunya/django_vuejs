<template>
  <a-row>
    <a-col :span="8" :offset="8" class="m-wrapper">
      <a-card>
        <div class="header">Login to Website</div>
        <a-form @submit.prevent="submit" @keyup.enter="login(inputs)">
          <a-form-item has-feedback :validate-status="status.username">
            <a-input v-model="inputs.username"
                     @keyup.enter="onLoginClick(inputs)"
                     type="text"
                     placeholder="Username">
              <a-icon slot="prefix" type="user" style="color:rgba(0,0,0,.25)"/>
            </a-input>
          </a-form-item>
          <a-form-item has-feedback :validate-status="status.password">
            <a-input v-model="inputs.password"
                     @keyup.enter="onLoginClick(inputs)"
                     type="password"
                     placeholder="Password">
              <a-icon slot="prefix" type="lock" style="color:rgba(0,0,0,.25)"/>
            </a-input>
          </a-form-item>
          <a-form-item>
            <a-button type="primary"
                      class="btn-login"
                      :loading="authenticating"
                      @click="onLoginClick(inputs)">
              Login
            </a-button>
          </a-form-item>
        </a-form>
      </a-card>
    </a-col>
  </a-row>
</template>

<script>
  import {mapState, mapActions} from 'vuex';

  export default {
    data() {
      return {
        inputs: {
          username: '',
          password: '',
        },
        status: {
          username: '',
          password: '',
        },
      };
    },
    computed: {
      ...mapState('auth', ['authenticating', 'error', 'token']),
    },
    methods: {
      ...mapActions('auth', ['login']),

      onLoginClick({username, password}) {

        this.status.username = '';
        this.status.password = '';
        if (!username) {
          this.status.username = 'error';
          return
        } else if (!password) {
          this.status.password = 'error';
          return
        }


        this.login({username, password})
          .then(() => {
            if (!this.error) {
              this.$router.push('/')
            } else {
              this.$message.error('Invalid credentials', 2.5);
            }
          });
      },
    }
  };
</script>

<style scoped>
  .m-wrapper {
    margin-top: 40px;
  }

  .header {
    text-align: center;
    margin-bottom: 32px;
    font-size: 20px;
    border-bottom: 1px solid #e6e6e6;
  }

  .btn-login {
    width: 100%;
    background-color: #013769
  }
</style>