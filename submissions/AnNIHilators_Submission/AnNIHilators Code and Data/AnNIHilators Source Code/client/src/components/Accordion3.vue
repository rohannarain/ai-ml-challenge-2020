<template>
  <div class="accordion" id="accordionExample">
    <div class="card">
      <div class="card-header" id="headingOne">
        <h2 class="mb-0">
          <button
            class="btn btn-link"
            type="button"
            data-toggle="collapse"
            data-target="#collapseSeven"
            aria-expanded="true"
            aria-controls="collapseSeven"
          >
            Lease Part of Services
          </button>
        </h2>
      </div>

      <div
        id="collapseSeven"
        class="collapse show"
        aria-labelledby="headingOne"
        data-parent="#accordionExample"
      >
        <div class="card-body">
          Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus
          terry richardson ad squid. 3 wolf moon officia aute, non cupidatat
          skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod.
          Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid
          single-origin coffee nulla assumenda shoreditch et. Nihil anim
          keffiyeh helvetica, craft beer labore wes anderson cred nesciunt
          sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings
          occaecat craft beer farm-to-table, raw denim aesthetic synth nesciunt
          you probably haven't heard of them accusamus labore sustainable VHS.
        </div>
      </div>
    </div>
    <div class="card">
      <div class="card-header" id="headingTwo">
        <h2 class="mb-0">
          <button
            class="btn btn-link collapsed"
            type="button"
            data-toggle="collapse"
            data-target="#collapseEight"
            aria-expanded="false"
            aria-controls="collapseEight"
          >
            Use Content from Services
          </button>
        </h2>
      </div>
      <div
        id="collapseEight"
        class="collapse"
        aria-labelledby="headingTwo"
        data-parent="#accordionExample"
      >
        <div class="card-body">
          Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus
          terry richardson ad squid. 3 wolf moon officia aute, non cupidatat
          skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod.
          Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid
          single-origin coffee nulla assumenda shoreditch et. Nihil anim
          keffiyeh helvetica, craft beer labore wes anderson cred nesciunt
          sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings
          occaecat craft beer farm-to-table, raw denim aesthetic synth nesciunt
          you probably haven't heard of them accusamus labore sustainable VHS.
        </div>
      </div>
    </div>
    <div class="card">
      <div class="card-header" id="headingThree">
        <h2 class="mb-0">
          <button
            class="btn btn-link collapsed"
            type="button"
            data-toggle="collapse"
            data-target="#collapseNine"
            aria-expanded="false"
            aria-controls="collapseNine"
          >
            Use of Branding
          </button>
        </h2>
      </div>
      <div
        id="collapseNine"
        class="collapse"
        aria-labelledby="headingThree"
        data-parent="#accordionExample"
      >
        <div class="card-body">
          Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus
          terry richardson ad squid. 3 wolf moon officia aute, non cupidatat
          skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod.
          Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid
          single-origin coffee nulla assumenda shoreditch et. Nihil anim
          keffiyeh helvetica, craft beer labore wes anderson cred nesciunt
          sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings
          occaecat craft beer farm-to-table, raw denim aesthetic synth nesciunt
          you probably haven't heard of them accusamus labore sustainable VHS.
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Accordion3",
};
</script>

<style lang="scss" scoped>
.card-header {
  background-color: rgb(255 5 5 / 13%);
}
</style>
