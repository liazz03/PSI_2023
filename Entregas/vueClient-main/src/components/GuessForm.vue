<template>
  <div id="guess-form">
    <h2 class="form-heading">Choose one answer</h2>
    <div class="box-container">
      <div class="box" @click="enviarFormulario(0)">1</div>
      <div class="box" @click="enviarFormulario(1)">2</div>
      <div class="box" @click="enviarFormulario(2)">3</div>
      <div class="box" @click="enviarFormulario(3)">4</div>
    </div>
  </div>
</template>

 <script>

    export default {
        name: 'guess-form',
        data() {
            return {
                procesando: false,
                correcto: false,
                error: false,
                Guess: {
                    game: '',
                    uuidp: '',
                    answer: '',
                },
            }
        },
         methods: {
            enviarFormulario(AnswNumber) {
               this.procesando = true;
               this.resetEstado();

               this.Guess.answer = AnswNumber
               this.Guess.game = this.$store.state.gameID
               this.Guess.uuidp = this.$store.state.participantID

               this.$emit('add-guess', this.Guess);
               this.$refs.nombre.focus();
               this.error = false;
               this.correcto = true;
               this.procesando = false;
               
               // Restablecemos el valor de la variables
               this.Guess= {
                    game: '',
                    uuidp: '',
                    answer: '',
               }
            },
            resetEstado() {
               this.correcto = false;
               this.error = false;
            },
         },
    }
 </script>
 
 <style scoped>
.box-container {
  display: flex;
  justify-content: space-between;
  width: 80%;
  margin: auto;
}

.box {
  width: 100px;
  height: 100px;
  background-color: #d4a373;
  margin: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  font-size: 64px;
  font-weight: bold;
  color: black;
  text-shadow: 2px 2px #715235;
}

.form-heading {
  text-align: center;
  font-size: 2rem;
  font-weight: bold;
  color: black;
  margin-bottom: 1rem;
}
</style>