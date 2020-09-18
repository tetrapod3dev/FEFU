<template>
  <v-card max-width="900" class="mx-auto px-3">
    <v-container class="pa-1">
      <v-item-group v-model="selected" multiple>
        <v-row>
          <v-col v-for="n in 12" :key="n" cols="12" md="3">
            <v-item v-slot:default="{ active, toggle }">
              <v-card
                :color="active ? 'primary' : ''"
                class="d-flex align-center"
                dark
                height="200"
                @click="toggle"
              >
                <v-scroll-y-transition>
                  <div v-if="active" class="display-3 flex-grow-1 text-center">Done</div>
                </v-scroll-y-transition>
              </v-card>
            </v-item>
          </v-col>
        </v-row>
      </v-item-group>
    </v-container>
  </v-card>
</template>

<script>
export default {};
</script>

<style>
</style>
