<template>
   <div id="participant-form">
     <form @submit.prevent="enviarFormulario">
       <div class="form-group">
         <label for="game">Game ID  </label>
         <input
           ref="nombre"
           v-model="Participant.game"
           type="number"
           class="form-control"
           :class="{ 'is-invalid': procesando && GameInvalid }"
           @focus="resetEstado"
           @keypress="resetEstado"
           id="game"
           required
         />
         <div class="invalid-feedback">
           Please enter a valid Game ID.
         </div>
       </div>

       <div class="form-group">
         <label for="alias">Alias  </label>
         <input
           v-model="Participant.alias"
           type="text"
           class="form-control"
           :class="{ 'is-invalid': procesando && AliasInvalid }"
           @focus="resetEstado"
           id="alias"
           required
         />
         <div class="invalid-feedback">
           Please enter a valid alias.
         </div>
       </div>

       <br>

       <button type="submit" class="btn btn-primary" :disabled="procesando">
         {{ procesando ? 'Processing...' : 'Submit' }}
       </button>
 
       <div v-if="error && procesando" class="alert alert-danger mt-3" role="alert">
         Please fill out all fields.
       </div>
       <div v-if="correcto" class="alert alert-success mt-3" role="alert">
         Participant form request sent!
       </div>
     </form>
   </div>
 </template>

 <script>

    export default {
        name: 'participant-form',
        data() {
            return {
                procesando: false,
                correcto: false,
                error: false,
                Participant: {
                    game: '',
                    alias: '',
                },
            }
        },
         methods: {
            enviarFormulario() {
               this.procesando = true;
               this.resetEstado();
               // Check for errors in the form
               if (this.GameInvalid || this.AliasInvalid ) {
                  this.error = true;
                  return;
               }
               this.$emit('add-participant', this.Participant);
               this.$refs.nombre.focus();
               this.error = false;
               this.correcto = true;
               this.procesando = false;
               
               // Reset the values
               this.Participant= {
                    game: '',
                    alias: '',
               }
            },
            resetEstado() {
               this.correcto = false;
               this.error = false;
            },
         },
        computed: {
            GameInvalid() {
                return this.Participant.game <= 0;
            },
            AliasInvalid() {
                return this.Participant.alias.length < 1;
            },
        },
    }
 </script>
 
 <style scoped>
 form {
  margin-bottom: 2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.form-group label {
  font-weight: bold;

   border-radius: 0;
   height: 50px;
   font-size: 1.5rem;
 
}

.form-group {
  margin-bottom: 1rem;
}

.form-control {
   border-radius: 0;
   font-size: 1.5rem;
   width: 200px;
}

.invalid-feedback {
  display: block;
  font-size: 0.8rem;
}

.btn-primary {
  font-size: 1.2rem;
  font-weight: bold;
  padding: 10px 30px;
  margin-top: 10px;
}
 </style>