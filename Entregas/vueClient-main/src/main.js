import { createApp } from 'vue'
import { createStore } from 'vuex'
import App from './App.vue'
import router from './router'

import './assets/main.css'

// Vuex store to keep game information across the views
const store = createStore({
    state: {
        gameID: '',
        participantID: ''
    },
    mutations : {
        // game publicId setter
        setGameID(state, gameID){
            state.gameID = gameID
        },
        // participant uuidp setter
        setParticipantID(state, participantID){
            state.participantID = participantID
        }
    },
    getters : {
        // game publicId getter
        getGameID(state) {
            return state.gameID
        }
    },
})

const app = createApp(App)

app.use(router)
app.use(store) 
app.mount('#app')
