<template>
  <v-main
    style="
      background-color: #85ffbd;
      background-image: linear-gradient(45deg, #85ffbd 0%, #fffb7d 100%);
    "
  >
    <!-- <home /> -->
  </v-main>
</template>

<script>
export default {
  name: "CoreView",

  components: {
    Home: () => import("@/components/Home"),
  },
};
</script>
