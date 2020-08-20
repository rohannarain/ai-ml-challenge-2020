<template>
  <div class="text-center mt-12 mb-12">
    <v-menu
      class="mt-6 mb-6"
      v-model="menu"
      :close-on-content-click="false"
      offset-x
    >
      <!-- :nudge-width="200" -->
      <template v-slot:activator="{ on: menu, attrs }">
        <v-tooltip bottom>
          <template v-slot:activator="{ on: tooltip }">
            <v-btn
              text
              class="text-none"
              color="indigo"
              dark
              v-bind="attrs"
              v-on="{ ...tooltip, ...menu }"
            >
              {{ clause }}
            </v-btn>
          </template>
          <span>Click to view Scores and send feedback</span>
        </v-tooltip>
      </template>

      <v-card>
        <v-list>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title>
                <p>F1 Score</p>
              </v-list-item-title>
              <v-list-item-subtitle>
                {{ prediction }}
              </v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>

          <v-list-item>
            <v-list-item-content>
              <v-list-item-title>
                <p>Brier Score</p>
              </v-list-item-title>
              <v-list-item-subtitle>
                <v-progress-circular
                  :value="probability"
                  :rotate="-90"
                  :size="100"
                  :width="25"
                  :color="briercolor"
                  >{{ probability }}%</v-progress-circular
                >
              </v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list>
        <v-divider></v-divider>
        <v-list class="second-list">
          <v-list-item>
            <v-list-item-avatar>
              <img src="https://cdn.vuetifyjs.com/images/john.jpg" alt="John" />
            </v-list-item-avatar>

            <v-list-item-content>
              <v-list-item-title>Gus Leider</v-list-item-title>
              <v-list-item-subtitle
                >Director of Acquisition</v-list-item-subtitle
              >
            </v-list-item-content>

            <v-list-item-action>
              <v-radio-group class="mr-6" v-model="approved">
                <v-radio :label="`Approve`" :value="true"></v-radio>
                <v-radio :label="`Disapprove`" :value="false"></v-radio>
              </v-radio-group>
            </v-list-item-action>
          </v-list-item>
        </v-list>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn text @click="menu = false">Cancel</v-btn>
          <v-btn
            color="primary"
            text
            @click="
              menu = false;
              addFeedback();
            "
            >Send Feedback</v-btn
          >
        </v-card-actions>
      </v-card>
    </v-menu>
  </div>
</template>

<script>
import { db } from "../firebase";

export default {
  name: "Popover",
  props: ["clause", "prediction", "probability"],
  data: () => ({
    fav: true,
    menu: false,
    message: false,
    hints: true,
    f1color: "blue-grey",
    briercolor: "blue-grey",
    feedback: [],
    approved: null,
    clauseName: "agreement-clause-25",
  }),
  firestore() {
    return {
      feedback: db.collection("feedback"),
    };
  },
  mounted() {
    this.f1color = this.calculateCircleColor(this.prediction);
    this.briercolor = this.calculateCircleColor(this.probability);
  },
  methods: {
    addFeedback: function() {
      console.log(this.approved);
      this.$firestore.feedback.add({
        name: this.clauseName,
        approved: this.approved,
        f1: this.prediction,
        brier: this.probability,
        timestamp: new Date(),
      });
      this.clauseName = "";
    },
    calculateCircleColor: function(value) {
      if (value >= 0 && value <= 12.5) {
        return "red";
      } else if (value > 12.5 && value <= 25) {
        return "deep-orange";
      } else if (value > 25 && value <= 37.5) {
        return "orange";
      } else if (value > 37.5 && value <= 50) {
        return "amber";
      } else if (value > 50 && value <= 62.5) {
        return "yellow";
      } else if (value > 62.5 && value <= 75) {
        return "lime";
      } else if (value > 75 && value <= 87.5) {
        return "light-green";
      } else if (value > 87.5 && value <= 100) {
        return "green";
      }
    },
  },
};
</script>

<style>
.v-progress-circular__info {
  color: black !important;
}

.v-list.v-sheet.theme--light {
  display: flex !important;
}

.second-list > .v-list-item > .v-list-item__content {
  max-width: 50% !important;
}

.v-label.theme--light {
  padding-left: 0.5rem !important;
  margin-bottom: 0 !important;
}
</style>
