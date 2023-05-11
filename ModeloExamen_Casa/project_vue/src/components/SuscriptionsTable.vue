<template>
    <div id="suscriptions-table">
        <div v-if="!suscriptions.length" class="alert alert-info" role="alert">
            No hay suscripciones
        </div>
        <table class="table">
            <thead>
                <tr>
                    <th>id</th>
                    <th>channel</th>
                    <th>user</th>
                    <th>suscriptionDate</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="suscription in suscriptions" :key="suscription.id">
                    <td>
                        {{ suscription.id}}
                    </td>
                    <td>
                        {{ suscription.channel}}
                    </td>
                    <td>
                        {{ suscription.user}}
                    </td>
                    <td>
                        {{ suscription.suscriptionDate}}
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
    export default {
        name: 'suscriptions-table',
        props: {
            suscriptions: Array,
        },
        data() {
            return {
                editando: null,
            }
        },
    }
    
</script>

<style scoped></style>
