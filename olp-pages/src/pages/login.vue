<template>
  <div class="login">
    <div class="login-form">
      <div class="label">
        <p>登录学习，发现更大的世界</p>
      </div>
      <div class="label">
        <Input type="text" name="username" v-model="username" placeholder="用户名" size="large" clearable></Input>
      </div>
      <div class="label">
        <Input type="password" name="password" v-model="password" placeholder="密码" size="large" clearable></Input>
      </div>
      <div class="label">
        <Button type="primary" name="login-button" long @click="login()">登录</Button>
      </div>
    </div>
  </div>
</template>

<script>
  /*
  PAGE LOGIN
  1. Check local cookie, have user-info?
  2. if have, straight redirect to main
  3. if not, login
  */
  export default {
    name: 'Login',
    data () {
      return {
        username: '',
        password: ''
      }
    },
    methods: {
      login () {
        // alert(this.username+this.password);
        var username = this.username;
        var password = this.password;

        if (username === '') {
          // check username is not empty
          alert("请输入学/工号！");
          return;
        }
        if (password === '') {
          // check password is not empty
          alert("请输入密码！");
          return;
        }
        var usernameRe = /^[0-9]+.?[0-9]*/;
        if(!usernameRe.test(username) || username.length != 10) {
          // check username is 10-bit number
          alert("请输入正确的学/工号！");
          return;
        }
        // Request Login API and Callback
        // Callback with Cookie operation, a test cookie is set as following
        // Construct POST Data
        var d = {
          username: username,
          password: password
        }
        console.log(d);
        // POST, and CALLBACK
      }
    }
  }
</script>

<style scoped>
.label {
  width: 300px;
  position: relative;
  left: 50%;
  margin-left: -150px;
  margin-top: 10px;
  margin-bottom: 10px;
}
.label>p {
  color: #2d8cf0;
  font-size: 1.25rem;
  font-weight: bold;
  padding-bottom: 10px;
}
.login-form {
  background-color: #ffffff;
  width: 400px;
  border-radius: 8px;
  border: 1px solid #dddee1;
  position: relative;
  left: 50%;
  top: 10%;
  margin-left: -200px;
  padding-top: 20px;
  padding-bottom: 20px;
}
.login {
  height: 100%;
  background-color: #b8e5f8;
  background-repeat: no-repeat;
  background-size: cover;
  background-image: url(../assets/bkg.png);
}
input:focus {
  outline: 0;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
</style>
