// This is a component by which we emit the username and password field for SignUp
<template>
  <v-card style="height: 100%">
    <h1 class="text-center font-weight-light">Sign Up</h1>
    <v-card-text>
      <v-form ref="form" v-model="valid" lazy-validation>
        <!-- Name field  -->
        <v-text-field
          v-model="name"
          label="Username"
          :counter="20"
          :rules="nameRules"
          required
          prepend-icon="mdi-account"
        ></v-text-field>
        <!-- Mobile Number field  -->
        <v-text-field
          v-model="mobile"
          :counter="10"
          :rules="phoneRules"
          required
          label="Mobile Number"
          name="mobile"
          prepend-icon="mdi-phone"
          type="number"
        ></v-text-field>
        <!-- Email field  -->
        <v-text-field
          required
          :rules="emailRules"
          v-model="email"
          label="User Email"
          prepend-icon="mdi-email"
          type="text"
        ></v-text-field>
        <!-- Password field  -->
        <v-text-field
          required
          :rules="[v => !!v || 'Password is required']"
          v-model="password"
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
        @click="signUp()"
      >Sign Up</v-btn>
    </v-card-actions>
  </v-card>
</template>
<script>
import { mapGetters, mapActions } from "vuex";
export default {
  data() {
    return {
      valid: true,
      name: "",
      email: "",
      password: "",
      mobile: "",
      hidePassword: true,
      nameRules: [
        (v) => !!v || "Name is required",
        (v) => (v && v.length <= 20) || "Name must be less than 20 characters",
      ],
      phoneRules: [
        (v) => !!v || "Phone Number is required",
        (v) => (v && v.length <= 10) || "Number must be less than 10 digits",
      ],
      emailRules: [
        (v) => !!v || "E-mail is required",
        (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
      ],
    };
  },
  methods: {
    signUp() {
      let user_detail = {
        name: this.name,
        email: this.email,
        password: this.password,
        mobile: this.mobile,
        type: "S",
      };
      // Emitting data to main Login Page
      this.$emit("submit1", user_detail);
    },
  },
  computed: {
    ...mapGetters([""]),
  },
};
</script>