<template>
  <div>
    <v-app-bar
      absolute
      color="#1E88E5"
      dark
      shrink-on-scroll
      prominent
      fade-img-on-scroll
      scroll-target="#scrolling-techniques-3"
      src="https://storage.googleapis.com/kaggle-datasets-images/855240/1458546/f898a26716503730ec201e7bce576ed4/dataset-cover.jpg?t=2020-09-02-13-47-39"
    >
      <template v-slot:img="{ props }">
        <v-img
          v-bind="props"
          gradient="to top right, rgba(19,84,122,.5), rgba(128,208,199,.8)"
        ></v-img>
      </template>

      <v-toolbar-title>Age-Gender-Ethnicity Predictor</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>

      <template v-slot:extension>
        <v-tabs v-model="tab" align-with-title>
          <v-tabs-slider color="yellow"></v-tabs-slider>

          <v-tab>Introduction </v-tab>
          <v-tab>SVM </v-tab>
          <v-tab>MLP </v-tab>
          <v-tab>CNN </v-tab>
          <v-tab>Multi Output CNN </v-tab>
          <v-tab>Prediction</v-tab>
        </v-tabs>
      </template>
    </v-app-bar>
    <v-sheet
      style="
        background-color: #d9afd9;
        background-image: linear-gradient(0deg, #d9afd9 0%, #97d9e1 100%);
      "
      id="scrolling-techniques-3"
      class="overflow-y-auto"
      max-height="725"
    >
      <v-container style="height: 800px">
        <v-tabs-items
          style="
            background-color: #d9afd9;
            background-image: linear-gradient(0deg, #d9afd9 0%, #97d9e1 100%);
            margin-top: 230px;
          "
          class="pa-8"
          v-model="tab"
        >
          <v-tab-item>
           <intro/>
          </v-tab-item>
          <v-tab-item>
            <svm />
          </v-tab-item>
          <v-tab-item>
            <mlp />
          </v-tab-item>
          <v-tab-item>
            <cnn />
          </v-tab-item>
          <v-tab-item>
            <moc />
          </v-tab-item>
          <v-tab-item>
            <home />
          </v-tab-item>
        </v-tabs-items>
      </v-container>
    </v-sheet>
  </div>
</template>
<script>
export default {
  data() {
    return {
      tab: null,
    };
  },
  components: {
    Home: () => import("@/components/Home"),
    Cnn: () => import("@/components/cnn"),
    Mlp: () => import("@/components/mlp"),
    Moc: () => import("@/components/moc"),
    Svm: () => import("@/components/svm"),
    Intro: () => import("@/components/intro"),
  },
};
</script>