<template>
  <div>
    <CreateTrip @handleHide="hideCreateTrip" :createTripVisible="createTripVisible" :live_route="live_route" />
    <!-- <UpdateEmployee :employee="employee" @handleHide="hideUpdateEmployee" :updateEmployeeVisible="updateEmployeeVisible" /> -->

    <!-- <div class="loading-spinner" v-if="loading">
      <a-spin />
    </div> -->

    <div v-if="!loading">
      <h1 :style="{ margin: '12px 12px 0' }">Appropriate Route</h1>

      <a-row>
        <a-col :span="12" :style="{ padding: '0 6px 0 0' }">
          <div :style="{ margin: '12px 12px 0' }">
            <a-button @click.prevent="openCreateTrip(appropriate_route)" type="primary" icon="plus" :style="{ margin: '0 auto 10px auto' }">
                Create Trip
            </a-button>

            <!-- <span>{{appropriate_route}}</span> -->
            
            <a-timeline mode="alternate">
              <a-timeline-item color="blue" v-for="station in appropriate_route" :key="station['station']">
                <span v-for="s in getStations.filter((s) => s['_id']['$oid'] === station['station'])" :key="s['_id']['$oid']">{{ s["station_name"] }} ({{ station["prediction_count"] }})</span>
              </a-timeline-item>
            </a-timeline>
          </div>
        </a-col>

        <a-col :span="12" :style="{ padding: '0 0 0 6px' }">
          <h3 :style="{ margin: '12px 0' }">Possible Routes</h3>
            <a-carousel :after-change="refreshRouteStatus">
              <a-timeline mode="alternate" v-for="route in possible_routes" :key="route['route_id']">
                <a-timeline-item color="blue" v-for="r in route['predictions']" :key="r['station']">
                  <span class="station-name" v-for="s in getStations.filter((s) => s['_id']['$oid'] === r['station'])" :key="s['_id']">{{ s["station_name"] }} ({{ r["prediction_count"] }})</span>
                </a-timeline-item>

                <br>

                <a-button @click.prevent="openCreateTrip(route['predictions'])" type="primary" icon="plus" :style="{ margin: '0 auto 10px auto' }">
                  Create Trip
                </a-button>
              </a-timeline>
            </a-carousel>
        </a-col>
      </a-row>

      <a-row>
        <a-col :span="24">
          <h1 :style="{ margin: '12px 12px 0' }">Route Status</h1>

          <a-table
            :data-source="route_status"
            :columns="columns"
            bordered
            :style="{ margin: '12px 12px 0' }"
            :pagination="false"
          >
            <span slot="station_name" slot-scope="station_id" :style="{ fontSize: '12px' }">
              <!-- {{ station_name || "NULL" }} -->
              <span class="station-name" v-for="s in getStations.filter((s) => s['_id']['$oid'] === station_id)" :key="s['_id']">{{ s["station_name"] || "NULL" }}</span>
            </span>

            <span slot="prediction_count" slot-scope="prediction_count" :style="{ fontSize: '12px' }">
                {{ prediction_count || "NULL" }}
            </span>

            <span slot="last_pickup_time" slot-scope="station_id" :style="{ fontSize: '12px' }">
                <!-- {{ last_pickup_time || "NULL" }} -->
                <span class="station-name" v-for="s in getStations.filter((s) => s['_id']['$oid'] === station_id)" :key="s['_id']" :style="{ color: moment().diff(moment(s['last_pickup_time']), 'seconds') < 15 ? 'red' : 'black'}">{{ s["last_pickup_time"] || "NULL" }}</span>
            </span>

            <span slot="last_pickup_fleet_number" slot-scope="station_id" :style="{ fontSize: '12px' }">
                <!-- {{ last_pickup_fleet_number || "NULL" }} -->
                <span class="station-name" v-for="s in getStations.filter((s) => s['_id']['$oid'] === station_id)" :key="s['_id']">{{ s["last_pickup_fleet"] || "NULL" }}</span>
            </span>

            <span slot="last_pickup_fleet_capacity" slot-scope="station_id" :style="{ fontSize: '12px' }">
                <!-- {{ last_pickup_fleet_capacity || "NOT_SET" }} -->
                <span class="station-name" v-for="s in getStations.filter((s) => s['_id']['$oid'] === station_id)" :key="s['_id']">{{ s["last_pickup_fleet"] || "NULL" }}</span>
            </span>
          </a-table>
        </a-col>
      </a-row>
    </div>
  </div>
</template>

<script>
//   import { mapActions, mapGetters } from "vuex"
  import { mapGetters } from "vuex"
  import CreateTrip from "../../data_entry/trips/CreateTrip"
//   import UpdateEmployee from "../../data_entry/update/UpdateEmployee"

  let route_status = [
    {
      key: "1",
      station: "6202617d08c535c258e414e3",
      prediction_count: 75,
    },

    {
      key: "2",
      station: "6202617d08c535c258e414e3",
      prediction_count: 75,
    },

    {
      key: "3",
      station: "6202617d08c535c258e414e3",
      prediction_count: 75,
    },
  ];

  export default {
    name: "AppropriateRoute",

    components: {
      CreateTrip,
    //   UpdateEmployee,
    },

    data() {
      return {
        loading: false,
        createBtnDisabled: true,
        createTripVisible: false,
        updateEmployeeVisible: false,
        actionButton: "action",
        actionLoading: false,
        routes: this.getPossibleRoutes,
        appropriate_route: [],
        recent: "NO",
        // possible_routes,
        possible_routes: [],
        route_status,
        live_route: [],
        employee: null,
        searchText: "",
        searchInput: null,
        searchedColumn: "",
        
        // Table Columns
        columns: [
          {
            title: "Station Name",
            dataIndex: "station",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "station_name",
            }
          },

          {
            title: "Predicted Passengers",
            dataIndex: "prediction_count",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "prediction_count",
            }
          },

          {
            title: "Last Pickup Time",
            dataIndex: "station",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "last_pickup_time",
            }
          },

          {
            title: "Last Pickup Fleet Number",
            dataIndex: "station",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "last_pickup_fleet_number",
            }
          },

          {
            title: "Last Pickup Fleet Capacity",
            dataIndex: "station",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "last_pickup_fleet_capacity",
            }
          },
        ],
      };
    },

    methods: {
    //   ...mapActions(["fetchAllEmployees", "refreshEmployeeDescription"]),

      openCreateTrip(route){
        this.live_route = [...route]

        this.createTripVisible = true
        // console.log("Create employee")
      },

      hideCreateTrip(){
        this.createTripVisible = false
      },

      refreshRouteStatus(route_index){
        this.route_status = this.possible_routes[route_index]["predictions"]
      },

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

    async created(){
    //   this.loading = true
    //   await this.fetchAllEmployees(this.getActiveUser["company"])
      this.appropriate_route = this.getPossibleRoutes["appropriate_route"]["predictions"]
      this.possible_routes = this.getPossibleRoutes["possible_routes"]
      this.route_status = this.appropriate_route
    //   this.loading = false
    },

    // mounted(){
    //   if(this.getActiveUser["role"]["role_name"] === "Manager"){
    //     this.createBtnDisabled = false
    //   }

    //   else{
    //     this.createBtnDisabled = true
    //   }
    // },

    computed: mapGetters(["getPossibleRoutes", "getStations"])
  }
</script>

<style scoped>
  .highlight {
    background-color: rgb(255, 192, 105);
    padding: 0px;
  }

  .ant-carousel >>> .slick-slide {
    text-align: center;
    /* height: 160px; */
    height: 65vh;
    /* line-height: 160px; */
    background: #364d79;
    line-height: 65vh;
    overflow: hidden;
  }

  .ant-carousel >>> .slick-slide .station-name {
    color: #fff;
  }
</style>