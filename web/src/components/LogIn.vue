// Login Main page
<template>
  <v-app>
    <v-card :dark="Boolean(isDark)">
      <v-toolbar :color="isDark ? '' :'grey lighten-4'">
        <v-toolbar-title>Swatch Rasoi</v-toolbar-title>
        <!-- Loading progress bar -->
        <v-progress-linear
          :active="loading"
          :indeterminate="loading"
          absolute
          bottom
          color="yellow"
        ></v-progress-linear>
        <v-spacer></v-spacer>
        
        <v-btn small color="primary" @click="login = !login" outlined>{{login ? "Login" : "signup"}}</v-btn>
      </v-toolbar>
    </v-card>

    <v-container class="fill-height a" fluid>
      <v-row align="center" justify="center">
        <v-col cols="12" sm="8" md="4">
          <!-- Signu Up component  -->
          <sign-up v-if="login" @submit1="signUp"></sign-up>
          <!-- Logged In component  -->
          <sign-in v-else @submit="loggedIn"></sign-in>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>
<style>
</style>
<script>
import { mapGetters, mapActions } from "vuex";
import signIn from "./SignIn";
import signUp from "./SignUp";
export default {
  data() {
    return {
      login: false,
      loading: false,
    };
  },
  components: {
    signIn,
    signUp,
  },
  computed: {
    ...mapGetters([""]),
  },
  methods: {
    ...mapActions(["checkUserLoggedIn", "userSignUp",]),
    loggedIn(user) {
      this.loading = true;
      this.checkUserLoggedIn(user)
        .then((res) => {
          this.$toasted.show("Successfully Login! ", {
            type: "success",
            duration: 3000,
            position: "top-center",
            theme: "bubble",
            icon: "mdi-account-check",
            iconPack: "mdi",
          });
          this.$router.push({ name: "switch" });
          this.loading = false;
        })
        .catch((err) => {
          this.$toasted.show("Invalid Username or Password", {
            type: "error",
            duration: 3000,
            position: "top-center",
            theme: "bubble",
            icon: "mdi-account-alert",
            iconPack: "mdi",
          });
          this.loading = false;
        });
    },
    signUp(user) {
      this.userSignUp(user)
        .then((res) => {
          this.$toasted.show("User created Successfully", {
            type: "success",
            duration: 3000,
            position: "top-center",
            theme: "bubble",
            icon: "mdi-account",
            iconPack: "mdi",
          });
          this.login = false
        })
        .catch((err) => {
          this.$toasted.show("User already Exists!", {
            type: "error",
            duration: 3000,
            position: "top-center",
            theme: "bubble",
            icon: "mdi-account-alert",
            iconPack: "mdi",
          });
        });
    },
  },
};
</script>