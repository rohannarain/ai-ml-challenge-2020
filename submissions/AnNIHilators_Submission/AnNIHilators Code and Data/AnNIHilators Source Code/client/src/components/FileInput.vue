<template>
  <v-form v-model="valid" id="file-wrapper">
    <p class="text-center">
      Drag your files into the grey field below, or click to add files.
      <br />Then you may click the blue 'Upload' button to begin analyzing your
      files (.docx, .pdf)
    </p>
    <v-file-input
      class=""
      v-model="files"
      placeholder="Upload your files Here"
      label="End User License Agreement(s)"
      accept=".docx,.pdf"
      :rules="rules"
      filled
      @change="onFileInput"
      outlined
      prepend-icon="mdi-paperclip"
    >
      <!-- multiple -->
      <template v-slot:selection="{ text }">
        <v-chip small label color="primary">
          {{ text }}
        </v-chip>
      </template>
    </v-file-input>

    <div class="text-center">
      <v-btn
        :loading="uploadLoading"
        :disabled="uploadDisabled"
        color="primary"
        class="ma-2 white--text"
        @click="onSubmit"
        x-large
        type="submit"
      >
        Upload
        <v-icon right dark>mdi-cloud-upload</v-icon>
      </v-btn>
    </div>
    <v-snackbar v-model="snackbarSuccess" :bottom="true" :color="'success'">
      Your poster was uploaded!
      <v-btn dark text @click="snackbar = false">
        Close
      </v-btn>
    </v-snackbar>

    <v-snackbar v-model="snackbarFailure" :bottom="true" :color="'success'">
      Your poster was uploaded!
      <v-btn dark text @click="snackbar = false">
        Close
      </v-btn>
    </v-snackbar>
  </v-form>
</template>

<script>
export default {
  data: () => ({
    snackbarSuccess: false,
    snackbarFailure: false,
    files: null,
    loader: null,
    loading3: false,
    uploadLoading: false,
    uploadDisabled: true,
    rules: [],
    valid: false,
    response: null,
  }),
  watch: {
    files() {
      this.rules = [];
    },
    loader() {
      const l = this.loader;
      this[l] = !this[l];

      setTimeout(() => (this[l] = false), 3000);

      this.loader = null;
    },
  },
  methods: {
    onSubmit() {
      this.rules = [
        (v) => !!v || "This field is required",
        // (v) => !v || v.size < 2000000 || "File size should be less than 2 MB!",
        (v) =>
          v.type !==
            ("application/pdf" ||
              "application/msword" ||
              "text/plain" ||
              "application/vnd.openxmlformats-officedocument.wordprocessingml.document") ||
          "Invalid file type, must be .pdf or .docx",
      ];
      this.loader = "loading3";
      console.log(this.files);

      const fd = new FormData();
      fd.append("file", this.files);

      var request = new XMLHttpRequest();
      request.open(
        "POST",
        "https://zai955cvia.execute-api.us-west-2.amazonaws.com/gsa-eula-ml"
      );
      request.send(fd);
      request.onreadystatechange = async () => {
        if (request.readyState == XMLHttpRequest.DONE) {
          // console.log(request.responseURL);
          ((data) => {
            // do something with the response in the variable data
            // console.log(data);
            this.response = JSON.parse(data);

            this.$emit("apiDone", JSON.parse(data));
          })(request.response);
        }
      };
      // if (request.status == 200) {
      //   let resp = request.responseXML;
      //   // console.log(resp);
      //   process(resp); //here!
      // }
      // function process(resp) {
      //   alert(resp); //do something more useful eventually
      // }
    },
    onFileInput() {
      if (this.files.length !== 0) {
        this.uploadDisabled = false;
      } else {
        this.uploadDisabled = true;
      }
    },
  },
};
</script>

<style scoped>
#file-wrapper {
  padding: 5rem !important;
}
h1 {
  padding-bottom: 2rem;
}
span {
  font-size: 1.2rem;
}

/* loader styles */
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
