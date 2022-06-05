<template>
  <div>
    <CreateTrip @handleHide="hideCreateTrip" :createTripVisible="createTripVisible" :live_route="visual_route" :route_allocation="route_allocation" />
    <!-- <OffloadTrip @handleHide="hideOffloadTrip" :offloadTripVisible="offloadTripVisible" /> -->
    <!-- <UpdateEmployee :employee="employee" @handleHide="hideUpdateEmployee" :updateEmployeeVisible="updateEmployeeVisible" /> -->

    <!-- <div class="loading-spinner" v-if="loading">
      <a-spin />
    </div> -->

    <div v-if="!loading">
      <a-row>
        <a-col :span="12">
          <h1 :style="{ margin: '12px 12px 0' }">Visual Route</h1>
        </a-col>

        <a-col :span="12">
              <a-button @click.prevent="toRouteAllocations" type="danger" :style="{ margin: '0 12px auto auto', float: 'right' }">
                  Back
              </a-button>

              <a-button @click.prevent="openCreateTrip" type="primary" :style="{ margin: '0 12px auto auto', float: 'right' }">
                  Create Trip
              </a-button>
        </a-col>
      </a-row>

      <div :style="{ margin: '36px 12px 0' }">
        <a-row>
          <a-col :span="24" :style="{ padding: '0 0 0 6px' }">
            <a-timeline mode="alternate">
              <a-timeline-item color="blue" v-for="station_id in route_allocation['optimal_route']" :key="station_id">
                <span v-for="station in getStations.filter(s => s['_id']['$oid'] === station_id)" :key="station['_id']['$oid']">{{ station["station_name"] }}</span>
              </a-timeline-item>
            </a-timeline>
          </a-col>
        </a-row>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapGetters } from "vuex"
  import CreateTrip from "../../data_entry/trips/CreateTrip"

  export default {
    name: "VisualRoute",

    components: {
      CreateTrip
    //   offloadTrip,
    //   UpdateEmployee,
    },

    data() {
      return {
        loading: false,
        createTripVisible: false,
        offloadBtnDisabled: true,
        offloadTripVisible: false,
        offload_trip_btn_loading: false,
        refresh_trip_btn_loading: false,
        updateEmployeeVisible: false,
        actionButton: "action",
        YES: "green",
        NO: "blue",
        route_allocation: {},
        actionLoading: false,
        employee: null,
        searchText: "",
        searchInput: null,
        searchedColumn: "",
      };
    },

    methods: {
      toRouteAllocations(){
        this.$router.push({ name: "Route Allocations" })
      },

      openCreateTrip(){
        this.createTripVisible = true
      },

      hideCreateTrip(){
        this.createTripVisible = false
      },
    },

    // async offloadTrip(){
    // },

    async created(){
      this.loading = true
    //   await this.fetchMyTrip(user_id)
      this.route_allocation = this.getVisualRoute
      this.loading = false
    },

    // mounted(){
    //   if(this.getActiveUser["role"]["role_name"] === "Manager"){
    //     this.offloadBtnDisabled = false
    //   }

    //   else{
    //     this.offloadBtnDisabled = true
    //   }
    // },

    computed: mapGetters(["getVisualRoute", "getStations"])
  }
</script>

<style scoped>
  .highlight {
    background-color: rgb(255, 192, 105);
    padding: 0px;
  }
</style>
