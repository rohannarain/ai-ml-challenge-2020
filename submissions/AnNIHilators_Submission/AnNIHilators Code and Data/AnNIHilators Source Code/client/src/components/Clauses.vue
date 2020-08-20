<template>
  <v-container class="clause-expands">
    <!-- <h1>WHAT</h1> -->
    <!-- <v-spacer></v-spacer> -->
    <v-row class="text-center">
      <v-col class="mb-5" cols="4">
        <h2 class="headline font-weight-bold mb-3">
          Permission
        </h2>

        <Accordion />
      </v-col>

      <v-col class="mb-5" cols="4">
        <h2 class="headline font-weight-bold mb-3">
          Duty
        </h2>

        <Accordion2 />
      </v-col>

      <v-col class="mb-5" cols="4">
        <h2 class="headline font-weight-bold mb-3">
          Prohibition
        </h2>

        <Accordion3 />
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>
.clause-expands {
  padding: 5rem;
}
</style>
<script>
import Accordion from "./Accordion";
import Accordion2 from "./Accordion2";
import Accordion3 from "./Accordion3";
export default {
  components: {
    Accordion,
    Accordion2,
    Accordion3,
  },
  name: "Clauses",
  data: () => ({}),
};
</script>
