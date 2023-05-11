<template>
    <div id="users-table">
        <div v-if="!users.length" class="alert alert-info" role="alert">
            No hay usuarios
        </div>
        <table class="table">
            <thead>
                <tr>
                    <th>id</th>
                    <th>userName</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="user in users" :key="user.id">
                    <td>
                        {{ user.id}}
                    </td>
                    <td>
                        {{ user.userName}}
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
    export default {
        name: 'users-table',
        props: {
            users: Array,
        },
        data() {
            return {
                editando: null,
            }
        },
    }
    
</script>

<style scoped></style>
