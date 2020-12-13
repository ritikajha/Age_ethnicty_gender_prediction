<template>
  <div>
    <div class="text-h4 mb-4">Support Vector Machine</div>
    <p>
      A Support Vector Machine (SVM) in supervised learning, is a discriminative
      classifier formally defined by a separating hyperplane. Given the labeled
      training data, the algorithm outputs an optimal hyperplane which
      categorizes new examples. In two dimensional space this hyperplane is a
      line dividing a plane in two parts where class lies on either side.
      <br />
      <br />
      Our method - <br /><br />
      Since SVMs are prone to overfitting data and aren’t useful for large
      datasets, we spliced the dataset to find unique 2000 images and separated
      it into testing and training sets.
    </p>

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
              <td class="text-right">15.3</td>
            </tr>
            <tr>
              <td>Gender:</td>
              <td class="text-right">82%</td>
            </tr>
            <tr>
              <td>Ethnicity:</td>
              <td class="text-right">52%</td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
    </v-card>

     <v-row class="my-8">
      <v-col cols="6" sm="4">
        <v-img :src="require('@/assets/svm/1.png')" height="180px" contain>
        </v-img>
        <div class="text-caption text-center">
          Confusion matrix for ethnicity
        </div>
      </v-col>
      <v-col cols="6" sm="4">
        <v-img :src="require('@/assets/svm/2.png')" height="180px" contain>
        </v-img>
        <div class="text-caption text-center">Confusion matrix for gender</div> 
      </v-col>
      <v-col cols="6" sm="4">
        <v-img :src="require('@/assets/svm/3.jpeg')" height="180px" contain>
        </v-img>
        <div class="text-caption text-center">Confusion matrix for age</div>
      </v-col>
    </v-row>
  </div>
</template>