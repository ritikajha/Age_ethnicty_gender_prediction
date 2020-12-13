<template>
  <div>
    <v-row>
      <v-col cols="12" sm="6"> <div class="text-h4 mb-4">Multi Layer Perceptron</div>   </v-col>
      <v-col cols="12" sm="6"><v-btn
          color="red lighten-2"
          dark
          @click="dialog = true"
         
        >
          Architecture diagram
        </v-btn></v-col>
    </v-row>
   
    <div class="text-center">
    <v-dialog
      v-model="dialog"
      width="500"
    >
      

      <v-card>
        <v-card-title class="headline grey lighten-2">
          Architecture diagram
        </v-card-title>
<v-img :src="require('@/assets/mlp_gender.jpg')"></v-img>
    
      </v-card>
    </v-dialog>
  </div>
    <p>
      MLP used for supervised learning, is a feedforward neural network that has
      some hidden layers apart from the input and output layers. The
      architecture diagram shown in figure is of gender MLP model. This model is
      same for both ethnicity and gender except the output layers.

      <br>
      <br>

      The output layers for :
 <ul>
   <li>Gender MLP model - It has two neurons corresponding to each class (0:Male, 1:Female), that outputs 1 if the class is present otherwise 0. Thus, it is a binary MLP classifier. </li>
   <li>Ethnicity MLP model - It has five neurons corresponding to each class that outputs 1 if the class is present otherwise 0. Thus, it is a multi class classifier. </li>
 </ul>



    </p>

    <div class="text-h5 mb-4" style="color: #1e88e5">Training History</div>

    <v-row>
      <v-col cols="6" sm="4">
        <v-img :src="require('@/assets/mlp/1.png')" height="180px" contain>
        </v-img>
        <div class="text-caption text-center">Age Model Training history</div>
      </v-col>
      <v-col cols="6" sm="4">
        <v-img :src="require('@/assets/mlp/2.png')" height="180px" contain>
        </v-img>
        <div class="text-caption text-center">
          Gender Model Training history
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
              <th class="text-right">Accuracy</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Age:</td>
              <td class="text-right">--</td>
            </tr>
            <tr>
              <td>Gender:</td>
              <td class="text-right">83.1%</td>
            </tr>
            <tr>
              <td>Ethnicity:</td>
              <td class="text-right">42.3%</td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
    </v-card>
     <v-row class="my-8">
      <v-col cols="6" sm="4">
        <v-img :src="require('@/assets/mlp/c1.jpeg')" height="180px" contain>
        </v-img>
        <div class="text-caption text-center">Confusion matrix for gender</div>
      </v-col>
      <v-col cols="6" sm="4">
        <v-img
          :src="require('@/assets/mlp/c2.jpeg')"
          height="180px"
          contain
        >
        </v-img>
        <div class="text-caption text-center">Confusion matrix for ethnicity</div>
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