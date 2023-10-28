<template>
  <div style="text-align: center">
    <h1 id="mainHead">CRYPTO PAPER PORTFOLIO</h1>
    <div id="firebaseui-auth-container"></div>
    <div id="pagecontent">
      CPP is an app to track your crypto portfolio. <br />
      Enter Coin Details and get real time Profit and Loss update of your Portfolio
    </div>
    <h5>copyright@cpp-2021-group12</h5>
  </div>
</template>

<script>
import firebase from '@/uifire.js'
import 'firebase/compat/auth'
import * as firebaseui from 'firebaseui'
import 'firebaseui/dist/firebaseui.css'

export default {
  name: 'LogIn',
  mounted() {
    var ui = firebaseui.auth.AuthUI.getInstance()
    if (!ui) {
      ui = new firebaseui.auth.AuthUI(firebase.auth())
    }

    var uiConfig = {
      signInSuccessUrl: '/portfolio',
      signInOptions: [
        firebase.auth.GoogleAuthProvider.PROVIDER_ID,
        firebase.auth.EmailAuthProvider.PROVIDER_ID
      ]
    }

    ui.start('#firebaseui-auth-container', uiConfig)
  }
}
</script>

<style scoped >
#firebaseui-auth-container {
  margin-top: 50px;
  margin-bottom: 50px;
}

#pagecontent {
  height: 100px;
  font-size: larger;
  font-weight: bolder;
  text-align: center;
}

#mainHead {
  text-align: center;
  /* font-size: 50px; */
  /* height: 100px; */
  text-shadow: 2px 2px grey;
}

#bg {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 60%;
}

h5 {
  text-align: center;
  background-color: rgb(194, 202, 188);
}
</style>