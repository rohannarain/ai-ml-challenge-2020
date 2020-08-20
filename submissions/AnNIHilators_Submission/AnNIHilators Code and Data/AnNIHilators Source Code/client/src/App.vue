<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <div class="d-flex align-center">
        <h1>GSA EULA</h1>
      </div>
    </v-app-bar>
    <v-main>
      <FileInput @apiDone="assignData($event)" />
      <!-- <v-spacer></v-spacer> -->
      <Clauses />
      <div ref="EULA" id="EULA">
        <h1>
          Generic EULA template End-User License Agreement ("Agreement") Last
        </h1>
        <Popover
          clause="What constitutes a material change will be determined at our sole discretion."
          prediction="prediction"
          probability="56"
        />
      </div>
    </v-main>
    <canvas ref="map" id="map"></canvas>
  </v-app>
</template>
<style>
header {
  height: 6%;
}
#EULA {
  padding: 5rem 12rem;
}
.v-main {
  width: 90% !important;
}
h1 {
  margin: 0rem;
}
#map {
  position: fixed;
  top: 4rem;
  right: 0;
  /* width: 160px; */
  height: 100%;
  z-index: 100;
  width: 10% !important;
}
.green {
  background-color: green;
}
.purple {
  background-color: purple;
}
</style>
<script>
import FileInput from "./components/FileInput";
import Clauses from "./components/Clauses";
// import MiniMap from "minimap-js";
import pagemap from "pagemap";
import Mark from "mark.js";
import Popover from "./components/Popover";

export default {
  name: "App",

  components: {
    FileInput,
    Clauses,
    Popover,
  },

  mounted() {
    // 'element' is desired dom element

    // var minimap = new MiniMap(this.$refs.EULA, {});
    // minimap.show();

    pagemap(this.$refs.map);

    // var instance = new Mark(this.$refs.EULA);
    // instance.mark("term", {
    //   className: "green",
    // });

    // var instance2 = new Mark(this.$refs.EULA);
    // instance2.mark("EULA", {
    //   className: "purple",
    // });

    var instance3 = new Mark(this.$refs.EULA);
    instance3.mark("license", {
      className: "red",
    });

    // var instance4 = new Mark(this.$refs.EULA);
    // instance4.mark("Application", {
    //   className: "yellow",
    // });

    // var instance5 = new Mark(this.$refs.EULA);
    // instance5.mark("install", {
    //   className: "blue",
    // });

    // var instance6 = new Mark(this.$refs.EULA);
    // instance6.mark("agree", {
    //   className: "orange",
    // });
  },

  data: () => ({
    predictions: null,
    probabilities: null,
    clauses_full: null,
  }),
  methods: {
    assignData(response) {
      console.log("api done, assign data");
      this.predictions = response.predictions;
      this.probabilities = response.probabilities;
      this.clauses_full = response.clauses_full;
      console.log(this.predictions);
      console.log(this.probabilities);
      console.log(this.clauses_full);
    },
  },
};
</script>
