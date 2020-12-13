<template>
  <div>
    <div class="text-h4 mb-4">Result and Conclusion</div>
    <p>
      We have finally compared all our results below. We can infer that CNN
      models have worked out the best for us, although the results of Multi
      Output CNN were quite comparative, but due to the inefficiency of
      ethnicity prediction we can't declare it as the best model.
    </p>
    <v-sheet color="transparent" height="25"></v-sheet>
    <v-card width="500" class="mx-auto">
      <v-simple-table dark>
        <template v-slot:default>
          <thead>
            <tr>
              <th class="">
                Model→ <br />
                Category↓
              </th>
              <th class="">MLP</th>
              <th class="">SVM</th>
              <th class="">CNN</th>
              <th class="">Multi Output CNN</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Age (Mse):</td>
              <td class="">-</td>
              <td class="">15.3</td>
              <td class="">6.85</td>
              <td class="text-center">5.09</td>
            </tr>
            <tr>
              <td>Gender (Accuracy):</td>
              <td class="">83.1%</td>
              <td class="">82%</td>
              <td class="">89.42%</td>
              <td class="text-center">84.3%</td>
            </tr>
            <tr>
              <td>Ethnicity (Accuracy):</td>
              <td class="">42.3%</td>
              <td class="">52%</td>
              <td class="">81.5%</td>
              <td class="text-center">60.5%</td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
    </v-card>
    <v-sheet color="transparent" height="50"></v-sheet>
    <p>
      We have now tried to pluck out some key inferences from the results
      obtained by the CNN models.
    </p>
    <ol>
      <li>
        In Gender prediction, out of 4588 samples of testing data, 412 samples
        were misclassified. Out of these misclassified faces, 200 belong to the
        age group of 10 years and below, 72 are from age group 10 to 25 years,
        64 are from age group of 25 to 40 years and 76 from age group of 40
        years and more. Also among the 412 misclassified, 181 belong to
        ethnicity class ‘White’ and only 29 belong to class ‘Others’.
      </li>
      <li>
        In gender classification, out of 4588 samples of testing data, 588 were
        misclassified. Out of these misclassifications, 311 belong to class
        ‘Female’ and 277 to ‘Male’. Also among these 588 misclassified samples,
        240 belong to the age group of 25 to 40 years, and only 94 belong to the
        age group of 10 years and below. We can therefore say that the chances
        of predicting a wrong gender is highest among the children that are aged
        10 years and below and people that belong to the ethnicity class
        ‘White’.
      </li>
    </ol>
    <v-sheet color="transparent" height="50"></v-sheet>
    <v-img
      class="mx-auto"
      :src="require('@/assets/1.png')"
      height="250"
      width="500"
    ></v-img>
    <div class="text-caption text-center">
      Images for which ethnicity prediction was wrong
    </div>

    <v-sheet color="transparent" height="25"></v-sheet>
    <v-row>
      <v-col cols="12" sm="6">
        <v-img
          class="mx-auto"
          :src="require('@/assets/2.png')"
          height="250"
          width="500"
        ></v-img>
        <div class="text-caption text-center">
          Predicted female but actually male
        </div>
      </v-col>
      <v-col cols="12" sm="6">
        <v-img
          class="mx-auto"
          :src="require('@/assets/3.png')"
          height="250"
          width="500"
        ></v-img>
        <div class="text-caption text-center">
          Predicted male but actually female
        </div></v-col
      >
    </v-row>
    <p>
      <b>
        <ul>
          <li>
            The chances of predicting a wrong gender is highest among the
            children that are aged 10 years and below and people that belong to
            the ethnicity class ‘White’.
          </li>
          <li>
            While classifying the ethnicity, the chances of wrong prediction are
            almost equivalent for class ‘Male’ and ‘Female’.
          </li>
          <li>
            The people between the age group of 25 to 40 years have the highest
            probability of being misclassified for ethnicity.
          </li>
        </ul>
      </b>
    </p>
  </div>
</template>