<template>
  <div>
    <v-row>
      <v-col cols="12" sm="6">
        <div class="text-h4 mb-4">Convolution Neural Network</div>
      </v-col>
      <v-col cols="12" sm="6"
        ><v-btn color="red lighten-2" dark @click="dialog = true">
          Architecture diagram
        </v-btn></v-col
      >
    </v-row>

    <div class="text-center">
      <v-dialog v-model="dialog" width="500">
        <v-card>
          <v-card-title class="headline grey lighten-2">
            Architecture diagram
          </v-card-title>
          <v-img :src="require('@/assets/cnn_arc.png')"></v-img>
        </v-card>
      </v-dialog>
    </div>
    <p>
      Convolutional Neural Networks refer to a sub-category of neural networks
      that are used to process images.
      <br />
      <br />
      Three different models for age, ethnicity and gender are made. Since age
      is a continuous data, the last activation function used for age is
      ‘Linear’ which gave continuous output for age from one neuron. To classify
      the gender and ethnicity, the activation function used was ‘Sigmoid’. We
      one-hot encoded the output label that was obtained by five different
      neurons. The optimizer used was ‘Adam’ optimiser . <br />
      <br />
      The loss functions were, for age: mean square error(mse), ethnicity:
      categorical cross entropy, and for gender: binary cross entropy.
    </p>

    <div class="text-h5 mb-4" style="color: #1e88e5">Training History</div>

    <v-row>
      <v-col cols="6" sm="4">
        <v-img :src="require('@/assets/cnn/1.png')" height="180px" contain>
        </v-img>
        <div class="text-caption text-center">Age Model Training history</div>
      </v-col>
      <v-col cols="6" sm="4">
        <v-img :src="require('@/assets/cnn/2.png')" height="180px" contain>
        </v-img>
        <div class="text-caption text-center">
          Gender Model Training history
        </div>
      </v-col>
      <v-col cols="6" sm="4">
        <v-img :src="require('@/assets/cnn/3.png')" height="180px" contain>
        </v-img>
        <div class="text-caption text-center">
          Ethnicity Model Training history
        </div>
      </v-col>
    </v-row>
    <div class="text-h5 mb-4" style="color: #1e88e5">Accuracy</div>
    <v-card width="500" class="mx-auto">
      <v-simple-table dark>
        <template v-slot:default>
          <thead>
            <tr>
              <th class="">Model</th>
              <th class="text-right">Accuracy/ Mse</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Age (Mse):</td>
              <td class="text-right">6.85</td>
            </tr>
            <tr>
              <td>Gender:</td>
              <td class="text-right">89.42%</td>
            </tr>
            <tr>
              <td>Ethnicity:</td>
              <td class="text-right">81.5%</td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
    </v-card>

    <v-row class="my-8">
      <v-col cols="6" sm="4">
        <v-img :src="require('@/assets/cnn/age.png')" height="180px" contain>
        </v-img>
        <div class="text-caption text-center">Age Model Training history</div>
      </v-col>
      <v-col cols="6" sm="4">
        <v-img
          :src="require('@/assets/cnn/ethnicity.png')"
          height="180px"
          contain
        >
        </v-img>
        <div class="text-caption text-center">
          Confusion matrix for ethnicity
        </div>
      </v-col>
      <v-col cols="6" sm="4">
        <v-img :src="require('@/assets/cnn/gender.png')" height="180px" contain>
        </v-img>
        <div class="text-caption text-center">Confusion matrix for gender</div>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dialog: false,
    };
  },
};
</script>