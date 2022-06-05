<template>
  <div>
    <!-- <CreateFleet @handleHide="hideCreateFleet" :createFleetVisible="createFleetVisible" />
    <AllocateFleet :fleet="fleet" @handleHide="hideAllocateFleet" :allocateFleetVisible="allocateFleetVisible" /> -->

    <!-- <UpdateEmployee :employee="employee" @handleHide="hideUpdateEmployee" :updateEmployeeVisible="updateEmployeeVisible" /> -->

    <TimeTravel @handleHide="hideTimeTravel" :timeTravelVisible="timeTravelVisible" />

    <div class="loading-spinner" v-if="loading">
        <!-- <a-spin /> -->
        <a-skeleton active />
    </div>

    <div v-if="!loading">
      <a-row>
        <a-col :span="12">
          <h1 :style="{ margin: '12px 12px 0' }">Stations Status</h1>
        </a-col>

        <a-col :span="12">
          <h1 :style="{ margin: '12px 12px 0', float: 'right' }">Prediction Time: <span :style="{ fontStyle: 'italic' }">{{ prediction_day }}, {{ prediction_time }}</span></h1>
        </a-col>
      </a-row>

      <div :style="{ margin: '12px 12px 0' }">
          <a-button @click.prevent="openTimeTravel" type="primary" icon="" :style="{ margin: '0 auto 10px auto' }">
            Time Travel
          </a-button>
          <a-table
            :data-source="stations_status"
            :columns="columns"
            bordered
          >
            <span slot="pickup_station" slot-scope="pickup_station" :style="{ fontSize: '12px' }">
                {{ pickup_station || "NULL" }}
            </span>

            <span slot="dropoff_station" slot-scope="dropoff_station" :style="{ fontSize: '12px' }">
                {{ dropoff_station || "NULL" }}
            </span>

            <span slot="prediction_count" slot-scope="prediction_count" :style="{ fontSize: '12px' }">
                {{ prediction_count || 0 }}
            </span>

            <span slot="last_pickup_time" slot-scope="last_pickup_time" :style="{ fontSize: '12px' }">
                {{ last_pickup_time || "NULL" }}
            </span>

            <!-- <span slot="last_pickup_fleet_number" slot-scope="last_pickup_fleet_number" :style="{ fontSize: '12px' }">
                {{ last_pickup_fleet_number || "NULL" }}
            </span>

            <span slot="last_pickup_fleet_capacity" slot-scope="last_pickup_fleet_capacity" :style="{ fontSize: '12px' }">
                {{ last_pickup_fleet_capacity || "NULL" }}
            </span> -->

            <span slot="action" slot-scope="record">
                <a-dropdown :trigger="['click']">
                  <span class="ant-drop-down-link" :style="{ cursor: 'pointer' }">
                      <a-button :loading="actionLoading[`action${record['_id']}`]" title="More..." :style="{ marginRight: '4px' }">
                        <a-icon v-if="!actionLoading[`action${record['_id']}`]" type="more" style="color: rgba(0,0,0,.25)" />
                      </a-button>
                  </span>

                  <a-menu slot="overlay">
                    <!-- <a-menu-item>
                      <span @click.prevent="openAllocateFleet(record)">
                        <a-icon type="edit" style="color: rgba(0,0,0,.25)" />
                        allocate
                      </span>
                    </a-menu-item> -->

                    <a-menu-item>
                      <span @click.prevent="toViewMore(record)">
                        <a-icon type="eye" style="color: rgba(0,0,0,.25)" />
                        view more
                      </span>
                    </a-menu-item>
                </a-menu>
              </a-dropdown>
            </span>

            <div
                slot="filterDropdown"
                slot-scope="{
                setSelectedKeys,
                selectedKeys,
                confirm,
                clearFilters,
                column,
                }"
                style="padding: 8px"
            >
                <a-input
                v-ant-ref="(c) => (searchInput = c)"
                :placeholder="`Search ${column.title}`"
                :value="selectedKeys[0]"
                style="width: 188px; margin-bottom: 8px; display: block;"
                @change="
                    (e) => setSelectedKeys(e.target.value ? [e.target.value] : [])
                "
                @pressEnter="
                    () => handleSearch(selectedKeys, confirm, column.dataIndex)
                "
                />
                <a-button
                type="primary"
                icon="search"
                size="small"
                style="width: 90px; margin-right: 8px"
                @click="() => handleSearch(selectedKeys, confirm, column.dataIndex)"
                >
                Search
                </a-button>
                <a-button
                size="small"
                style="width: 90px"
                @click="() => handleReset(clearFilters)"
                >
                    Reset
                </a-button>
            </div>

            <a-icon
                slot="filterIcon"
                slot-scope="filtered"
                type="search"
                :style="{ color: filtered ? '#108ee9' : undefined }"
            />
            <template slot="customRender" slot-scope="text, record, index, column">
                <span v-if="searchText && searchedColumn === column.dataIndex">
                <template
                    v-for="(fragment, i) in text
                    .toString()
                    .split(new RegExp(`(?<=${searchText})|(?=${searchText})`, 'i'))"
                >
                    <mark
                    v-if="fragment.toLowerCase() === searchText.toLowerCase()"
                    :key="i"
                    class="highlight"
                    >{{ fragment }}</mark
                    >
                    <template v-else>{{ fragment }}</template>
                </template>
                </span>
                <template v-else>
                {{ text }}
                </template>
            </template>
          </a-table>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from "vuex"
  import * as moment from "moment"
  import TimeTravel from "../../data_entry/stations/TimeTravel"
//   import AllocateFleet from "../../data_entry/fleets/AllocateFleet"
//   import UpdateEmployee from "../../data_entry/update/UpdateEmployee"

  // const fleets = [
  //   {
  //     key: "1",
  //     fleet_number: "1989",
  //     fleet_capacity: 75,
  //     allocation_status: "FREE",
  //     fleet_status: "AVAILABLE",
  //     active_trip_origin: "London",
  //     active_trip_target: "Paris",
  //   },

  //   {
  //     key: "2",
  //     fleet_number: "1989",
  //     fleet_capacity: 75,
  //     allocation_status: "FREE",
  //     fleet_status: "AVAILABLE",
  //     active_trip_origin: "Pretoria",
  //     active_trip_target: "Cape Town",
  //   },

  //   {
  //     key: "3",
  //     fleet_number: "1989",
  //     fleet_capacity: 75,
  //     allocation_status: "FREE",
  //     fleet_status: "AVAILABLE",
  //     active_trip_origin: "King Kong",
  //     active_trip_target: "Moscow",
  //   },
  // ];

  export default {
    name: "Fleets",

    components: {
      TimeTravel,
    //   AllocateFleet,
    //   UpdateEmployee,
    },

    data() {
      return {
        loading: false,
        createBtnDisabled: true,
        timeTravelVisible: false,
        allocateFleetVisible: false,
        // updateEmployeeVisible: false,
        actionButton: "action",
        actionLoading: false,
        stations_status: [],
        prediction_day: moment().format("dddd"),
        prediction_time: moment().format("HH:mm"),
        public_holiday: 0,
        fleet: {},
        searchText: "",
        searchInput: null,
        searchedColumn: "",
        
        // Table Columns
        columns: [
          {
            title: "Pickup Station",
            dataIndex: "pickup_station",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "pickup_station",
            },

            onFilter: (value, record) =>
              (record.pickup_station !== undefined && record.pickup_station !== null) &&
              record.pickup_station
                .toString()
                .toLowerCase()
                .includes(value.toLowerCase()),
            onFilterDropdownVisibleChange: (visible) => {
              if (visible) {
                setTimeout(() => {
                  this.searchInput.focus();
                }, 0);
              }
            },
          },

          {
            title: "Dropoff Station",
            dataIndex: "dropoff_station",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "dropoff_station",
            },

            onFilter: (value, record) =>
              (record.dropoff_station !== undefined && record.dropoff_station !== null) &&
              record.dropoff_station
                .toString()
                .toLowerCase()
                .includes(value.toLowerCase()),
            onFilterDropdownVisibleChange: (visible) => {
              if (visible) {
                setTimeout(() => {
                  this.searchInput.focus();
                }, 0);
              }
            },
          },

          {
            title: "Prediction Count",
            dataIndex: "prediction_count",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "prediction_count",
            },

            onFilter: (value, record) =>
              (record.prediction_count !== undefined && record.prediction_count !== null) &&
              record.prediction_count
                .toString()
                .toLowerCase()
                .includes(value.toLowerCase()),
            onFilterDropdownVisibleChange: (visible) => {
              if (visible) {
                setTimeout(() => {
                  this.searchInput.focus();
                }, 0);
              }
            },
          },

          {
            title: "Last Pickup Time",
            dataIndex: "last_pickup_time",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "last_pickup_time",
            },

            onFilter: (value, record) =>
              (record.last_pickup_time !== undefined && record.last_pickup_time !== null) &&
              record.last_pickup_time
                .toString()
                .toLowerCase()
                .includes(value.toLowerCase()),
            onFilterDropdownVisibleChange: (visible) => {
              if (visible) {
                setTimeout(() => {
                  this.searchInput.focus();
                }, 0);
              }
            },
          },

        //   {
        //     title: "Last Pickup Fleet Number",
        //     dataIndex: "last_pickup_fleet.fleet_number",
        //     scopedSlots: {
        //       filterDropdown: "filterDropdown",
        //       filterIcon: "filterIcon",
        //       customRender: "last_pickup_fleet_number",
        //     },

        //     onFilter: (value, record) =>
        //       (record.last_pickup_fleet !== undefined && record.last_pickup_fleet !== null) &&
        //       record.last_pickup_fleet.fleet_number
        //         .toString()
        //         .toLowerCase()
        //         .includes(value.toLowerCase()),
        //     onFilterDropdownVisibleChange: (visible) => {
        //       if (visible) {
        //         setTimeout(() => {
        //           this.searchInput.focus();
        //         }, 0);
        //       }
        //     },
        //   },

        //   {
        //     title: "Last Pickup Fleet Capacity",
        //     dataIndex: "last_pickup_fleet.fleet_capacity",
        //     scopedSlots: {
        //       filterDropdown: "filterDropdown",
        //       filterIcon: "filterIcon",
        //       customRender: "last_pickup_fleet_capacity",
        //     },

        //     onFilter: (value, record) =>
        //       (record.last_pickup_fleet !== undefined && record.last_pickup_fleet !== null) &&
        //       record.last_pickup_fleet.fleet_capacity
        //         .toString()
        //         .toLowerCase()
        //         .includes(value.toLowerCase()),
        //     onFilterDropdownVisibleChange: (visible) => {
        //       if (visible) {
        //         setTimeout(() => {
        //           this.searchInput.focus();
        //         }, 0);
        //       }
        //     },
        //   },

          {
            title: "Action",
            dataIndex: "",
            key: "x",
            scopedSlots: {
              customRender: "action"
            },
          },
        ],
      };
    },

    methods: {
      ...mapActions(["fetchStationsStatus", "refreshStationStatusDetails", "fetchFleets", "fetchStations", "fetchConductors"]),

      async toViewMore(station_status){
          await this.refreshStationStatusDetails(station_status).then(() => {
                // console.log(station_status)
                this.$router.push({ name: "Station Status Details" })
          })
      },

      openTimeTravel(){
        this.timeTravelVisible = true
        // console.log("Create employee")
      },

      async hideTimeTravel(prediction_body){
        this.loading = true

        await this.fetchStationsStatus(prediction_body).then((response) => {
          if(response.status === "info"){
              this.$message.info(response.message);
          }
          
          else if(response.status === "success"){
              // this.$message.success(response.message);
              this.prediction_day = prediction_body["prediction_day"]
              this.prediction_time = prediction_body["prediction_time"]
              this.public_holiday = prediction_body["public_holiday"]
              this.stations_status = this.getStationsStatus
          }
          
          else if(response.status === "warn"){
              this.$message.warn(response.message);
          }
          
          else if(response.status === "error"){
              this.$message.error(response.message);
          }

          this.loading = false
        })

        this.timeTravelVisible = false
      },

      openAllocateFleet(fleet){
        this.fleet = {...fleet}
        this.allocateFleetVisible = true
        // console.log("Create employee")
      },

      hideAllocateFleet(){
        this.allocateFleetVisible = false
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
      this.loading = true
      let prediction_body = {
        prediction_day: this.prediction_day,
        prediction_time: this.prediction_time,
        public_holiday: this.public_holiday
      }      
      
      await this.fetchStationsStatus(prediction_body)
      this.stations_status = this.getStationsStatus
      this.loading = false

      await this.fetchStations().then((response) => {
        if(response.status === "info"){
            this.$message.info(response.message);
        }
        
        else if(response.status === "success"){
            // this.$message.success(response.message);
        }
        
        else if(response.status === "warn"){
            this.$message.warn(response.message);
        }
        
        if(response.status === "error"){
            this.$message.error(response.message);
        }
      })

      await this.fetchFleets().then((response) => {
        if(response.status === "info"){
            this.$message.info(response.message);
        }
        
        else if(response.status === "success"){
            // this.$message.success(response.message);
        }
        
        else if(response.status === "warn"){
            this.$message.warn(response.message);
        }
        
        if(response.status === "error"){
            this.$message.error(response.message);
        }
      })

      await this.fetchConductors().then((response) => {
        if(response.status === "info"){
            this.$message.info(response.message);
        }
        
        else if(response.status === "success"){
            // this.$message.success(response.message);
        }
        
        else if(response.status === "warn"){
            this.$message.warn(response.message);
        }
        
        if(response.status === "error"){
            this.$message.error(response.message);
        }
      })
    },

    // mounted(){
    //   if(this.getActiveUser["role"]["role_name"] === "Manager"){
    //     this.createBtnDisabled = false
    //   }

    //   else{
    //     this.createBtnDisabled = true
    //   }
    // },

    computed: mapGetters(["getStationsStatus"])
  }
</script>

<style scoped>
  .highlight {
    background-color: rgb(255, 192, 105);
    padding: 0px;
  }
</style>
