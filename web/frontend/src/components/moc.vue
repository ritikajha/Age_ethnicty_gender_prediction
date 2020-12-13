<template>
  <div>
    <v-row>
      <v-col cols="12" sm="6">
        <div class="text-h4 mb-4">Multi Output CNN</div>
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
          <v-img :src="require('@/assets/nov_arch.png')"></v-img>
        </v-card>
      </v-dialog>
    </div>
    <p>
      The model is pretty straightforward CNN until the bottleneck returned by
      the Global Max Pooling layer.
      <br /><br />
      Up to the bottleneck layer we have repeated the convolutional blocks with
      ‘Leaky Relu’ layers, batch normalization and average or max pooling.
      <br /><br />
      The bottleneck layer’s output is branched out into three separate branches
      to predict three different outputs. For predicting age, the bottleneck
      layer’s output is given as input to the dense layer with linear
      activation. Thus, a ‘linear regressor’ is created to predict age.
      <br /><br />
      Similarly, for race and gender the same bottleneck output is given as
      input to another dense layer with ‘Sigmoid’ activation function. The
      optimizer used is root mean square propagation(rmsprop).
    </p>

    <div class="text-h5 mb-4" style="color: #1e88e5">Training History</div>

    <v-row>
      <v-col cols="6" sm="4">
        <v-img :src="require('@/assets/moc/1.png')" height="180px" contain>
        </v-img>
        <div class="text-caption text-center">
          Plot of losses while training
        </div>
      </v-col>
      <v-col cols="6" sm="4">
        <v-img :src="require('@/assets/moc/2.png')" height="180px" contain>
        </v-img>
        <div class="text-caption text-center">
          Training history for gender and ethnicity
        </div>
      </v-col>
      <v-col cols="6" sm="4">
        <v-img :src="require('@/assets/moc/3.png')" height="180px" contain>
        </v-img>
        <div class="text-caption text-center">Training history for age</div>
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
              <td class="text-right">5.09</td>
            </tr>
            <tr>
              <td>Gender:</td>
              <td class="text-right">84.3%</td>
            </tr>
            <tr>
              <td>Ethnicity:</td>
              <td class="text-right">60.5%</td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
    </v-card>

    <v-row class="my-8">
      <v-col cols="6" sm="4">
        <v-img :src="require('@/assets/moc/c1.png')" height="180px" contain>
        </v-img>
        <div class="text-caption text-center">
          Confusion matrix for ethnicity
        </div>
      </v-col>
      <v-col cols="6" sm="4">
        <v-img :src="require('@/assets/moc/c2.png')" height="180px" contain>
        </v-img>
        <div class="text-caption text-center">Confusion matrix for gender</div>
      </v-col>
      <v-col cols="6" sm="4">
        <v-img :src="require('@/assets/moc/c3.png')" height="180px" contain>
        </v-img>
        <div class="text-caption text-center">Confusion matrix for age</div>
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