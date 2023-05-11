<template>
  <main>
    <guess-form @add-guess="addGuess" />
  </main>
</template>

<script>
import GuessForm from '@/components/GuessForm.vue'

export default {
      name: 'app',
      components: {
        GuessForm
      },
      data() {
        return {
          guesses: [],
        }
      },
      methods: {
        async addGuess(Guess) {
          try {
              // Send resquest to the API for a new guess
              const server_url = import.meta.env.VITE_DJANGOURL + "guess/";
              const response = await fetch(server_url, {
                method: 'POST',
                body: JSON.stringify(Guess),
                headers: { 'Content-type': 'application/json; charset=UTF-8' },
              });
              // Check that the response is OK
              if (response.ok) {
                // The guess has been succesfully created
                const GuessCreated = await response.json();
                this.guesses = [...this.guesses, GuessCreated];
                alert('Guess registered!')
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
