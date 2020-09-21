<template>
  <section id="hero">
    <v-row no-gutters>
      <v-img
        :height="'calc(50vh - ' + $vuetify.application.top + 'px)'"
        src="https://www.mallgalleries.org.uk/sites/default/files/Brown-Peter-Early-Morning-The-Market-Hoi-An-Vietnam.jpg"
      >
        <v-container fill-height>
          <v-row align="center" class="black--text mx-auto" justify="center">
            <v-sheet :min-width="'calc(30vw)'">
              <div class="py-6"></div>
              <v-col class="black--text text-center" cols="12" tag="h1">
                <span
                  :class="[$vuetify.breakpoint.smAndDown ? 'display-1': 'display-2']"
                  class="font-weight-black"
                >중고마켓</span>
              </v-col>

              <div class="py-6"></div>
            </v-sheet>
          </v-row>
        </v-container>
      </v-img>
    </v-row>
  </section>
</template>

<script>
export default {};
</script>

<style>
</style>
