<template>
  <v-container class="pa-4 text-center">
    <v-chip x-small class="ma-2" color="primary" label>
      <v-icon x-small left>mdi-gender-male-female</v-icon>
      Gender:
    </v-chip>
    <v-chip x-small class="ma-2" color="primary" label>
      <v-icon x-small left>mdi-earth</v-icon>
      Ethnicity:
    </v-chip>
    <v-chip x-small class="ma-2" color="primary" label>
      <v-icon x-small left>mdi-calendar-clock</v-icon>
      Age:
    </v-chip>
    <div class="text-h3 my-8">Prediction</div>
    {{ this.items }}
    <v-row class="fill-height" align="center" justify="center">
      <template v-for="(item, i) in items">
        <v-col :key="i" cols="12" md="2">
          <v-hover v-slot="{ hover }">
            <v-card
              class="op"
              :elevation="hover ? 12 : 2"
              :class="{ 'on-hover': hover }"
            >
              <v-img
                :src="`${link}/${item.filename}`"
                height="130px"
                :class="{ zoom: hover }"
                @click="selectImage(item.filename)"
              >
              </v-img>
              <!--  -->
            </v-card>
          </v-hover>
        </v-col>
      </template>
    </v-row>
    {{ this.image }}
    <div class="text-caption">Upload 48*48 image</div>
    <div style="width: 50%" class="mx-auto">
      <v-file-input
        v-model="image"
        label="Use your own photo"
        filled
        prepend-icon="mdi-camera"
      ></v-file-input>
    </div>
    <v-btn
      class="ma-2"
      :loading="loading4"
      :disabled="loading4"
      color="info"
      @click="predict()"
    >
      PREDICT
      <template v-slot:loader>
        <span class="custom-loader">
          <v-icon light>mdi-cached</v-icon>
        </span>
      </template>
    </v-btn>
    <!-- dialog box -->
    <div class="text-center">
      <v-dialog v-model="dialog" width="500">
        <v-card>
          <v-card-title class="headline grey lighten-2"> Result </v-card-title>
          <v-container>
            <v-row>
              <v-col cols="12" xs="6">
                <v-img
                  class="mx-auto"
                  :src="require('@/assets/boy.svg')"
                  width="100"
                >
                </v-img
              ></v-col>
              <v-col cols="12" xs="6">
                <v-list shaped>
                  <!-- <v-subheader>REPORTS</v-subheader> -->
                  <v-list-item-group color="primary">
                    <v-list-item>
                      <v-list-item-icon>
                        <v-icon>mdi-gender-male-female</v-icon>
                      </v-list-item-icon>
                      <v-list-item-content>
                        <v-list-item-title>Gender: </v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                    <v-list-item>
                      <v-list-item-icon>
                        <v-icon>mdi-earth</v-icon>
                      </v-list-item-icon>
                      <v-list-item-content>
                        <v-list-item-title>Ethnicity: </v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                    <v-list-item>
                      <v-list-item-icon>
                        <v-icon>mdi-calendar-clock</v-icon>
                      </v-list-item-icon>
                      <v-list-item-content>
                        <v-list-item-title>Age: </v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                  </v-list-item-group>
                </v-list>
              </v-col>
            </v-row>
          </v-container>

          <v-divider></v-divider>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn icon color="blue" @click="dialog = false">
              <v-icon>mdi-thumb-up</v-icon>
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </div>
  </v-container>
</template>
<script>
const axios = require("axios");
export default {
  data: () => ({
    items: null,
    transparent: "rgba(255, 255, 255, 0)",
    loading4: false,
    loader: null,
    dialog: false,
    image: null,
    link: "http://d29f3c5fe142.ngrok.io",
  }),
  watch: {
    loader() {
      const l = this.loader;
      this[l] = !this[l];

      setTimeout(() => (this[l] = false), 3000);

      this.loader = null;
    },
  },
  methods: {
    predict(filename) {
      this.dialog = true;
      // this.loader = "loading4";
    },
    selectImage(filename) {
      axios.post("", this.image).then((res) => console.log(res));
    },
  },
  async created() {
    await axios
      .get(`${this.link}/files`)
      .then((res) => (this.items = res.data));
  },
};
</script>
<style>
.op {
  transition: opacity 0.4s ease-in-out;
}

.op:not(.on-hover) {
  opacity: 0.6;
}
.zoom {
  transform: scale(1.5);
}
.custom-loader {
  animation: loader 1s infinite;
  display: flex;
}
@-moz-keyframes loader {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(360deg);
  }
}
@-webkit-keyframes loader {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(360deg);
  }
}
@-o-keyframes loader {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(360deg);
  }
}
@keyframes loader {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(360deg);
  }
}
</style>