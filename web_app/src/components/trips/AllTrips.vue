<template>
  <div>
    <RequestRoute @handleHide="hideRequestRoute" :requestRouteVisible="requestRouteVisible" />
    <!-- <CreateTrip @handleHide="hideCreateTrip" :createTripVisible="createTripVisible" /> -->
    <!-- <AllocateFleet :fleet="fleet" @handleHide="hideAllocateFleet" :allocateFleetVisible="allocateFleetVisible" /> -->
    <!-- <UpdateEmployee :employee="employee" @handleHide="hideUpdateEmployee" :updateEmployeeVisible="updateEmployeeVisible" /> -->

    <div class="loading-spinner" v-if="loading">
        <!-- <a-spin /> -->
        <a-skeleton active />
    </div>

    <div v-if="!loading">
      <h1 :style="{ margin: '12px 12px 0' }">Trips</h1>

      <div :style="{ margin: '12px 12px 0' }">
          <a-button @click.prevent="openRequestRoute" type="primary" icon="plus" :style="{ margin: '0 auto 10px auto' }">
              Request Route
          </a-button>
          <a-table
            :data-source="trips"
            :columns="columns"
            bordered
          >
            <span slot="conductor" slot-scope="conductor" :style="{ fontSize: '12px' }">
                {{ conductor['first_name'] || "NULL" }} {{ conductor['last_name'] || "NULL" }}
            </span>

            <span slot="fleet_number" slot-scope="fleet_number" :style="{ fontSize: '12px' }">
                {{ fleet_number || "NULL" }}
            </span>

            <span slot="fleet_capacity" slot-scope="fleet_capacity" :style="{ fontSize: '12px' }">
                {{ fleet_capacity || "NULL" }}
            </span>

            <span slot="departure_time" slot-scope="departure_time" :style="{ fontSize: '12px' }">
                {{ departure_time || "NULL" }}
            </span>

            <span slot="arrival_time" slot-scope="arrival_time" :style="{ fontSize: '12px' }">
                {{ arrival_time || "NOT_SET" }}
            </span>

            <span slot="trip_origin" slot-scope="trip_origin" :style="{ fontSize: '12px' }">
                {{ trip_origin || "NULL" }}
            </span>

            <span slot="trip_destination" slot-scope="trip_destination" :style="{ fontSize: '12px' }">
                {{ trip_destination || "NULL" }}
            </span>

            <span slot="head_count" slot-scope="head_count" :style="{ fontSize: '12px' }">
                {{ head_count || "NULL" }}
            </span>

            <span slot="surplus_count" slot-scope="surplus_count" :style="{ fontSize: '12px' }">
                {{ surplus_count || "NULL" }}
            </span>

            <span slot="trip_status" slot-scope="trip_status" :style="{ fontSize: '12px' }">
                {{ trip_status || "NULL" }}
            </span>

            <span slot="creation_date" slot-scope="creation_date" :style="{ fontSize: '12px' }">
                {{ creation_date || "NULL" }}
            </span>

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
                      <span @click.prevent="toUpdateTrip(record)">
                        <a-icon type="eye" style="color: rgba(0,0,0,.25)" />
                        update
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
  import RequestRoute from "../../data_entry/trip_routes/RequestRoute"
  // import CreateTrip from "../../data_entry/trips/CreateTrip"
//   import UpdateEmployee from "../../data_entry/update/UpdateEmployee"

//   const trips = [
//     {
//       key: "1",
//       conductor: {
//         first_name: "John",
//         last_name: "Doe"
//       },
//       fleet:{
//           fleet_number: 1275,
//           fleet_capacity: 18
//       },
//       departure_time: "2022-03-09 08:36:45",
//       arrival_time: "NOT_SET",
//       trip_origin: "Westgate",
//       trip_destination: "City",
//       head_count: 13,
//       surplus_count: 5,
//       creation_date: "2022-03-09 08:36:45",
//     },

//     {
//       key: "2",
//       conductor: {
//         first_name: "Foo",
//         last_name: "Bar"
//       },
//       fleet:{
//           fleet_number: 1275,
//           fleet_capacity: 18
//       },
//       departure_time: "2022-03-09 08:36:45",
//       arrival_time: "NOT_SET",
//       trip_origin: "Westgate",
//       trip_destination: "City",
//       head_count: 13,
//       surplus_count: 5,
//       creation_date: "2022-03-09 08:36:45",
//     },
//   ];

  export default {
    name: "Trips",

    components: {
      RequestRoute,
    //   UpdateEmployee,
    },

    data() {
      return {
        loading: false,
        createBtnDisabled: true,
        requestRouteVisible: false,
        // createTripVisible: false,
        // updateEmployeeVisible: false,
        actionButton: "action",
        actionLoading: false,
        trips: [],
        searchText: "",
        searchInput: null,
        searchedColumn: "",
        
        // Table Columns
        columns: [
          {
            title: "Conductor",
            dataIndex: "conductor",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "conductor",
            },

            // Last name is failing to search!!!
            onFilter: (value, record) =>
              (record.conductor !== undefined && record.conductor !== null) &&
              (record.conductor.first_name || record.conductor.last_name)
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
            title: "Fleet Number",
            dataIndex: "fleet.fleet_number",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "fleet_number",
            },

            onFilter: (value, record) =>
              (record.fleet !== undefined && record.fleet !== null) &&
              record.fleet.fleet_number
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
            title: "Fleet Capacity",
            dataIndex: "fleet.fleet_capacity",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "fleet_capacity",
            },

            onFilter: (value, record) =>
              (record.fleet !== undefined && record.fleet !== null) &&
              record.fleet.fleet_capacity
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
            title: "Departure Time",
            dataIndex: "departure_time",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "departure_time",
            },

            onFilter: (value, record) =>
              (record.departure_time !== undefined && record.departure_time !== null) &&
              record.departure_time
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
            title: "Arrival Time",
            dataIndex: "arrival_time",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "arrival_time",
            },

            onFilter: (value, record) =>
              (record.arrival_time !== undefined && record.arrival_time !== null) &&
              record.arrival_time
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
            title: "Trip Origin",
            dataIndex: "trip_origin.station_name",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "trip_origin",
            },

            onFilter: (value, record) =>
              (record.trip_origin !== undefined && record.trip_origin !== null) &&
              record.trip_origin.station_name
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
            title: "Trip Destination",
            dataIndex: "trip_destination.station_name",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "trip_destination",
            },

            onFilter: (value, record) =>
              (record.trip_destination !== undefined && record.trip_destination !== null) &&
              record.trip_destination.station_name
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
            title: "Head Count",
            dataIndex: "head_count",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "head_count",
            },

            onFilter: (value, record) =>
              (record.head_count !== undefined && record.head_count !== null) &&
              record.head_count
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
            title: "Surplus Count",
            dataIndex: "surplus_count",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "surplus_count",
            },

            onFilter: (value, record) =>
              (record.surplus_count !== undefined && record.surplus_count !== null) &&
              record.surplus_count
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
            title: "Trip Status",
            dataIndex: "trip_status",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "trip_status",
            },

            onFilter: (value, record) =>
              (record.trip_status !== undefined && record.trip_status !== null) &&
              record.trip_status
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
            title: "Creation Date",
            dataIndex: "creation_date",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "creation_date",
            },

            onFilter: (value, record) =>
              (record.creation_date !== undefined && record.creation_date !== null) &&
              record.creation_date
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
      ...mapActions(["fetchTrips"]),

      openRequestRoute(){
        this.requestRouteVisible = true
        // console.log("Create employee")
      },

      hideRequestRoute(){
        this.requestRouteVisible = false
      },

      // openCreateTrip(){
      //   this.createTripVisible = true
      //   // console.log("Create employee")
      // },

      // hideCreateTrip(){
      //   this.createTripVisible = false
      // },

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

    async created(){
      this.loading = true
      await this.fetchTrips()
      this.trips = this.getTrips
      this.loading = false
    },

    // mounted(){
    //   if(this.getActiveUser["role"]["role_name"] === "Manager"){
    //     this.createBtnDisabled = false
    //   }

    //   else{
    //     this.createBtnDisabled = true
    //   }
    // },

    computed: mapGetters(["getTrips"])
  }
</script>

<style scoped>
  .highlight {
    background-color: rgb(255, 192, 105);
    padding: 0px;
  }
</style>
