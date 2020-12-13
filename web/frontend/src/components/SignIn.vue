// This is a component by which we emit the username and password field for SignIN
<template>
  <v-card style="height: 100%" >
    <h1 class="text-center font-weight-light">Sign In</h1>
    <v-card-text>
      <v-form ref="form" v-model="valid" lazy-validation>
        <!-- Email text field  -->
        <v-text-field
          :rules="emailRules"
          v-model="user.email"
          label="UserEmail"
          prepend-icon="mdi-account"
          required
        ></v-text-field>
        <!-- Password field  -->
        <v-text-field
          required
          :rules="[v => !!v || 'Password is required']"
          v-model="user.password"
          prepend-icon="mdi-lock"
          :type="hidePassword ? 'password' : 'text'"
          :append-icon="hidePassword ? 'mdi-eye-off' : 'mdi-eye'"
          label="Password"
          @click:append="hidePassword = !hidePassword"
        />
      </v-form>
    </v-card-text>
    <v-card-actions>
      <v-btn
        :style="!valid ? 'pointer-events: none' : '' "
        block
        rounded
        color="primary"
        dark
        @click="loggedIn()"
      >Log In</v-btn>
    </v-card-actions>
  </v-card>
</template>
<script>
import { mapGetters, mapActions } from "vuex";
export default {
  data() {
    return {
      valid: true,
      user: {
        email: "",
        password: "",
      },
      hidePassword: true,
      emailRules: [
        (v) => !!v || "UserEmail is required",
        (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
      ],
    };
  },
  methods: {
    loggedIn() {
      this.$refs.form.validate();
      // Emitting data to main Login Page
      this.$emit("submit", this.user);
    },
  },
  computed: {
    ...mapGetters([""]),
  },
};
</script>