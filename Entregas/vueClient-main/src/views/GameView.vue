<template>
  <main>
    <game-status :Game="Game"/>
  </main>
</template>

<script >
  import GameStatus from '@/components/GameStatus.vue'


  export default {
    name: 'app',
    components: {
      GameStatus
    },
    data() {
      return {
        Game: {},
        interval: null,
      }
    },
    methods: {
      async listgame(){
        try {
          // Retrieve the game publicId from the store
          const gameID = this.$store.state.gameID;
          // Fetch game info response from the api
          const server_url = import.meta.env.VITE_DJANGOURL + "games/" + gameID + "/";
          const response = await fetch(server_url);
          // Check that the response is OK
          if (response.ok) {
            this.Game = await response.json();
            console.log(this.Game.state);
            if (this.Game.state > 1) {
              // If the game is ready, go to the guess view
              this.$router.push({ name: 'guess' })
            }
          }
        } catch (error) {
          console.error(error);
        }
      },
    },
    mounted() {
      // Retrieve initial information
      this.listgame()
      // Set up 2sec information reload cycle
      this.interval = setInterval(this.listgame, 2000);
    },
    beforeUnmount() {
      // Halt the reload cycle
      clearInterval(this.interval);
    },
  }

</script>

<style scoped>
  main {
    margin-top: 3rem;
    display: flex;
    justify-content: center;
  }

  @media (min-width: 1024px) {
    main {
      margin-top: 6rem;
    }
  }
</style>
