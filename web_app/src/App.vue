<template>
  <div id="app">
    <component :is="this.$route.meta.layout || 'div'">
      <router-view />
    </component>

    <!-- <SystemLayout /> -->
  </div>
</template>

<script>
  // import SystemLayout from "./components/layout/SystemLayout"
  import { mapActions, mapGetters } from "vuex"

  export default {
    
    name: 'App',
    
    components: {
      // SystemLayout
    },

    methods: {
      ...mapActions(["refreshStation", "refreshFleet", "refreshNewRouteAllocation"])
    },

    created(){
      let refresh_fleet_channel = this.$pusher.subscribe("passengers-prediction-channel")
      let route_allocation_channel = this.$pusher.subscribe("route-allocation-channel")

      // channel.bind("refresh-station", refreshed_station => {
      //   this.refreshStation(refreshed_station["refreshed_station"])
      // })

      refresh_fleet_channel.bind("refresh-fleet", refreshed_fleet => {
        this.refreshFleet(refreshed_fleet["refreshed_fleet"])
      })

      route_allocation_channel.bind("route-allocation", new_route_allocation => {
        if(new_route_allocation["new_route_allocation"]["conductor_id"]["$oid"] === this.getActiveUser["_id"]["$oid"]){
          this.refreshNewRouteAllocation(new_route_allocation["new_route_allocation"])

          this.$message.success(`You were allocated new route`);
        }
      })
    },

    computed: mapGetters(["getActiveUser"]),
  }
</script>

<style>
  .loading-spinner{
    text-align: center;
    /* background: rgba(0, 0, 0, 0.05); */
    border-radius: 4px;
    margin-bottom: 20px;
    padding: 30px 50px;
    margin: 20px 0;
  }
</style>
