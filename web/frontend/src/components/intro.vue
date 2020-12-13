<template>
  <div>
    <div class="text-h4 mb-4">AGE GENDER ETHNICITY PREDICTION</div>
    <p>
      Our project aims to predict age, gender and ethnicity of a human face
      image using the UTK* dataset provided by Kaggle*. This dataset consists of
      23,705 images, along with their labels.
    </p>
    <v-img
      src="https://susanqq.github.io/UTKFace/icon/samples.png"
      height="250"
      width="500"
      class="mx-auto"
    ></v-img>
    <v-sheet height="50" color="transparent"></v-sheet>
    <a
      href="https://www.kaggle.com/nipunarora8/age-gender-and-ethnicity-face-data-csv"
      >*1.
      https://www.kaggle.com/nipunarora8/age-gender-and-ethnicity-face-data-csv</a
    >
    <br />
    <a href="https://susanqq.github.io/UTKFace/"
      >*2. https://susanqq.github.io/UTKFace/</a
    >

    <v-sheet height="50" color="transparent"></v-sheet>
    <div class="text-h4 mb-4">MOTIVATION</div>
    <p>
      Human faces contain features like eyes, nose, wrinkles, pimples, acne,
      blackheads and also differences in the structure of these. Such features
      vary person-to-person and determine identity, age, gender, emotions, and
      the ethnicity of people. <br />
      <br />
      Features like age and gender classification can be especially helpful in
      several real-world applications including -
      <b
        >security and video surveillance, electronic customer relationship
        management, biometrics, electronic vending machines, human-computer
        interaction, entertainment, cosmetology, and forensic art.</b
      >
      However, several issues in age and gender classification are still open
      problems.
    </p>

    <v-sheet height="25" color="transparent"></v-sheet>
    <div class="text-h4 mb-4">OUR CONTRIBUTION</div>

    <ol>
      <li>
        Preprocessed data to get rid of all kinds of anomalies like empty or
        repeated data.
      </li>
      <li>
        Different models for three different outputs - made a Multi Layer
        Perceptron model followed by Support Vector Machine and Convolutional
        Neural Network models to predict age, gender and ethnicity separately.
      </li>
      <li>
        <b>Novelty</b> : Developed a Multi Output CNN model which predicts all
        three of them simultaneously.
      </li>
      <li>
        We have highlighted the key correlations found between age, gender and
        ethnicity in a web application, which predicts the age, ethnicity and
        gender of the images in real time using the developed models.
      </li>
    </ol>
  </div>
</template>