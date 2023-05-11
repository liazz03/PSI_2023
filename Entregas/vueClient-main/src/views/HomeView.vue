<template>
  <main class="home">
    <h1 class="title">Join a Llahoot Game</h1>
    <participant-form @add-participant="addParticipant" />
  </main>
</template>

<script >
  import ParticipantForm from '@/components/ParticipantForm.vue'
  
  export default {
      name: 'app',
      components: {
        ParticipantForm
      },
      data() {
        return {
          participants: [],
        }
      },
      methods: {
        async addParticipant(Participant) {
          try {
              // Send resquest to the API for a new participant
              const server_url = import.meta.env.VITE_DJANGOURL + "participant/";
              const response = await fetch(server_url, {
                method: 'POST',
                body: JSON.stringify(Participant),
                headers: { 'Content-type': 'application/json; charset=UTF-8' },
              });
              // Check that the response is OK
              if (response.ok) {
                // The participant has been succesfully created
                const participantCreated = await response.json();
                this.participants = [...this.participants, participantCreated];
                // Store the game publicId in the vuex store
                const gamePublicId = Participant.game;
                this.$store.commit('setGameID', gamePublicId);
                //store participant uuidP
                this.$store.commit('setParticipantID', participantCreated.uuidP);
                // Go to game view
                this.$router.push({ name: 'game' })
              } 
              else {
                // Participant creation failed: print the returned error message
                alert((await response.text()).toString());
              }

            } catch (error) {
              console.error(error);
            }
        },
      }
    
  }

</script>

<style scoped>
  .home {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
      background-color: #F5F5F5;
    }
  
  .title {
    font-size: 3rem;
    font-weight: bold;
    margin-bottom: 2rem;
    color: #c68f65;
    text-align: center;
    text-shadow: 2px 2px 5px #C5CAE9;
  }
</style>