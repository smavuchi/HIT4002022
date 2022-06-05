<template>
  <div>
    <!-- <OffloadTrip @handleHide="hideOffloadTrip" :offloadTripVisible="offloadTripVisible" /> -->
    <!-- <UpdateEmployee :employee="employee" @handleHide="hideUpdateEmployee" :updateEmployeeVisible="updateEmployeeVisible" /> -->

    <!-- <div class="loading-spinner" v-if="loading">
      <a-spin />
    </div> -->

    <div v-if="!loading">
      <!-- <h1 :style="{ margin: '12px 12px 0' }">Current Trip</h1> -->

      <div :style="{ margin: '12px 12px 0' }">
          <!-- <a-button @click.prevent="offloadTrip" type="danger" icon="issues-close" :style="{ margin: '0 auto 10px auto' }">
              Offload Trip
          </a-button> -->

          <a-descriptions title="My Trip">
            <a-descriptions-item label="Fleet Number">
                {{ my_trip["fleet"]["fleet_number"] }}
            </a-descriptions-item>

            <a-descriptions-item label="Trip Origin">
                {{ my_trip["trip_origin"]["station_name"] }}
            </a-descriptions-item>
            
            <a-descriptions-item label="Trip Destination">
                {{ my_trip["trip_destination"]["station_name"] }}
            </a-descriptions-item>

            <a-descriptions-item label="Head Count">
                {{ my_trip["head_count"] }}
            </a-descriptions-item>
            
            <a-descriptions-item label="Surplus Count">
                {{ my_trip["surplus_count"] }}
            </a-descriptions-item>

            <a-descriptions-item label="Departure Time">
                {{ my_trip["departure_time"] }}
            </a-descriptions-item>

            <a-descriptions-item label="Trip Status">
              <span
                :style="{ color: my_trip['trip_status'] === 'OFFLOADED' ? 'red' : 'black'}"
              >
                {{ my_trip["trip_status"] }}
              </span>
            </a-descriptions-item>
        </a-descriptions>
        
        <a-row>
          <a-col :span="12">
            <!-- <a-button @click.prevent="toOffloadTrip" type="danger" icon="issues-close" :loading="offload_trip_btn_loading" :style="{ margin: '0 auto 10px auto' }">
              Offload Trip
            </a-button> -->
          </a-col>

          <a-col :span="12">
            <!-- <a-button type="primary" icon="issues-close" :style="{ margin: '0 auto 10px auto', float: 'right' }">
              Refresh Trip
            </a-button> -->
          </a-col>
        </a-row>

        <a-row>
          <a-col :span="12" :style="{ padding: '0 0 0 6px' }">
            <h3 :style="{ margin: '12px 0' }">Live Route</h3>
            <a-button @click.prevent="toRefreshTrip" type="primary" icon="reload" :loading="refresh_trip_btn_loading" :style="{ margin: '0 auto 10px auto' }">
              Refresh Trip
            </a-button>

            <a-timeline mode="alternate">
              <a-timeline-item :color="(station['visited'] === 'YES' ? 'green' : 'blue')" v-for="station in my_trip['live_route']" :key="station['station']">
                <span v-for="s in getStations.filter((s) => s['_id']['$oid'] === station['station'])" :key="s['_id']['$oid']">{{ s["station_name"] }}</span>
              </a-timeline-item>
            </a-timeline>
          </a-col>
        </a-row>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from "vuex"
//   import offloadTrip from "../../data_entry/trips/offloadTrip"
//   import UpdateEmployee from "../../data_entry/update/UpdateEmployee"

    // const current_trip = {
    //     fleet_number: "2998",

    //     departure_time: "2022-02-08 14:31:34",
        
    //     trip_origin: "Avondale",

    //     trip_destination: "City",

    //     head_count: 18,

    //     surplus_count: 5,

    //     trip_status: "LOADED"
    // }

    // const live_route = [
    //   "6202617d08c535c258e414e3",
    //   "620261a408c535c258e414e4",
    //   "620263048a3ca5e59d88c1f6",
    //   "620f4da8cae60129e07de085"
    // ]

  export default {
    name: "MyTrip",

    components: {
    //   offloadTrip,
    //   UpdateEmployee,
    },

    data() {
      return {
        loading: false,
        offloadBtnDisabled: true,
        offloadTripVisible: false,
        offload_trip_btn_loading: false,
        refresh_trip_btn_loading: false,
        updateEmployeeVisible: false,
        actionButton: "action",
        YES: "green",
        NO: "blue",
        my_trip: {},
        actionLoading: false,
        employee: null,
        searchText: "",
        searchInput: null,
        searchedColumn: "",
      };
    },

    methods: {
      ...mapActions(["fetchMyTrip", "offloadTrip", "refreshTrip"]),

      async toOffloadTrip(){
        this.offload_trip_btn_loading = true

        await this.offloadTrip(this.my_trip).then((response) => {
          if(response.status === "info"){
              this.$message.info(response.message);
            }
            
            else if(response.status === "success"){
              this.my_trip = this.getMyTrip
              this.$message.success(response.message);
              this.$router.replace({ name: "All Trips" })
            }
            
            else if(response.status === "warn"){
              this.$message.warn(response.message);
            }
            
            if(response.status === "error"){
              this.$message.error(response.message);
            }
        })

        this.offload_trip_btn_loading = false
      },

      async toRefreshTrip(){
        this.refresh_trip_btn_loading = true

        await this.refreshTrip(this.my_trip).then((response) => {
          if(response.status === "info"){
              this.$message.info(response.message);
            }
            
            else if(response.status === "success"){
              this.my_trip = this.getMyTrip
              this.$message.success(response.message);
            }
            
            else if(response.status === "warn"){
              this.$message.warn(response.message);
            }
            
            if(response.status === "error"){
              this.$message.error(response.message);
            }
        })

        this.refresh_trip_btn_loading = false
      },

    //   openUpdateEmployee(employee){
    //     this.employee = {...employee}
    //     this.updateEmployeeVisible = true
    //     // console.log("offload employee")
    //   },

    //   hideUpdateEmployee(){
    //     this.updateEmployeeVisible = false
    //   },

    //   confirmEmployeeDeletion(employee){
    //     console.log(employee)
    //   },

    //   async openEmployeeDescription(employee){
    //     // console.log(employee)
    //     this.actionLoading = true
    //     await this.refreshEmployeeDescription(employee).then((response) => {
    //       if(response["status"] === "success"){
    //         this.$router.push({ name: "Employee Description" })
    //       }

    //       else if(response["status"] === "error"){
    //         this.$message.error(response["message"])
    //       }
    //     })
    //     this.actionLoading = false
    //   },

      handleSearch(selectedKeys, confirm, dataIndex) {
        confirm();
        this.searchText = selectedKeys[0];
        this.searchedColumn = dataIndex;
      },

      handleReset(clearFilters) {
        clearFilters();
        this.searchText = "";
      },
    },

    // async offloadTrip(){
    // },

    async created(){
      this.loading = true
      let conductor_id = this.getActiveUser["_id"]["$oid"]
      await this.fetchMyTrip(conductor_id)
      this.my_trip = this.getMyTrip
      console.log(this.my_trip)
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

    computed: mapGetters(["getMyTrip", "getStations", "getActiveUser"])
  }
</script>

<style scoped>
  .highlight {
    background-color: rgb(255, 192, 105);
    padding: 0px;
  }
</style>
