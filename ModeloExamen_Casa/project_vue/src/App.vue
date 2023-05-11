

<template>
<div id="app" class="container">
    <div class="row">
        <div class="col-md-12">
          <h1>Channels</h1>
        </div>
      </div>
      <div class="row">
        <div class="col-md-12">
          <channels-table :channels="channels"/>
        </div>
    </div>

    <div class="row">
        <div class="col-md-12">
          <h1>Users</h1>
        </div>
      </div>
      <div class="row">
        <div class="col-md-12">
          <users-table :users="users"/>
        </div>
    </div>

    <div class="row">
        <div class="col-md-12">
          <h1>Suscriptions</h1>
        </div>
      </div>
      <div class="row">
        <div class="col-md-12">
          <suscriptions-table :suscriptions="suscriptions"/>
        </div>
    </div>
</div>
</template>


<script>
  import ChannelsTable from '@/components/ChannelsTable.vue'
  import SuscriptionsTable from '@/components/SuscriptionsTable.vue'
  import UsersTable from '@/components/UsersTable.vue'

  export default {
    name: 'app',
    components: {
      ChannelsTable,
      SuscriptionsTable,
      UsersTable,
    },
    data() {
      return {
        channels: [],
        users: [],
        suscriptions: [],
      }
    },
    methods: {
      async listObjects(){
        try {

          const channels_url = import.meta.env.VITE_DJANGOURL + 'channel';
          const response_channels = await fetch(channels_url);
          this.channels = await response_channels.json();
          
          const users_url = import.meta.env.VITE_DJANGOURL + 'user';
          const response_users = await fetch(users_url);
          this.users = await response_users.json();
          
          const suscriptions_url = import.meta.env.VITE_DJANGOURL + 'suscription';
          const response_suscriptions = await fetch(suscriptions_url);
          this.suscriptions = await response_suscriptions.json();

        } catch (error) {
          console.error(error);
        }
      },
     
    },
    mounted() {
      this.listObjects();
    },
  }



</script>
