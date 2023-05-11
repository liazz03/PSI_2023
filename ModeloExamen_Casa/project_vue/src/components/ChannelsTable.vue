<template>
    <div id="channels-table">
        <div v-if="!channels.length" class="alert alert-info" role="alert">
            No hay canales
        </div>
        <table class="table">
            <thead>
                <tr>
                    <th>id</th>
                    <th>channelName</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="channel in channels" :key="channel.id">
                    <td>
                        {{ channel.id}}
                    </td>
                    <td>
                        {{ channel.channelName}}
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
    export default {
        name: 'channels-table',
        props: {
            channels: Array,
        },
        data() {
            return {
                editando: null,
            }
        },
    }
    
</script>

<style scoped></style>
