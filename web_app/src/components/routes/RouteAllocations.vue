<template>
  <div>
    <CreateTrip @handleHide="hideCreateTrip" :createTripVisible="createTripVisible" :route_allocation="route_allocation" />
    <!-- <CreateRoute @handleHide="hideCreateRoute" :createRouteVisible="createRouteVisible" /> -->
    <!-- <AllocateFleet :fleet="fleet" @handleHide="hideAllocateFleet" :allocateFleetVisible="allocateFleetVisible" /> -->
    <!-- <UpdateEmployee :employee="employee" @handleHide="hideUpdateEmployee" :updateEmployeeVisible="updateEmployeeVisible" /> -->

    <div class="loading-spinner" v-if="loading">
        <!-- <a-spin /> -->
        <a-skeleton active />
    </div>

    <div v-if="!loading">
      <h1 :style="{ margin: '12px 12px 0' }">Route Allocations</h1>

      <div :style="{ margin: '12px 12px 0' }">
          <!-- <a-button @click.prevent="openCreateRoute" type="primary" icon="plus" :style="{ margin: '0 auto 10px auto' }">
            Create Route
          </a-button> -->
          <a-table
            :data-source="route_allocations"
            :columns="columns"
            bordered
          >
            <span slot="route_origin" slot-scope="optimal_route" :style="{ fontSize: '12px' }">
                <!-- {{ route_allocation[0]["station_name"] || "NULL" }} -->
                <span v-for="station in getStations.filter(s => s['_id']['$oid'] === optimal_route[0])" :key="station['_id']['$oid']">
                  {{ station['station_name'] || "NULL" }}
                </span>
            </span>

            <span slot="route_destination" slot-scope="optimal_route" :style="{ fontSize: '12px' }">
                <!-- {{ route_allocation[route_allocation.length-1]["station_name"] || "NULL" }} -->
                <span v-for="station in getStations.filter(s => s['_id']['$oid'] === optimal_route[optimal_route.length-1])" :key="station['_id']['$oid']">
                  {{ station['station_name'] || "NULL" }}
                </span>
            </span>

            <span slot="allocation_status" slot-scope="allocation_status" :style="{ fontSize: '12px' }">
                <!-- {{ route_allocation[route_allocation.length-1]["station_name"] || "NULL" }} -->
                {{ allocation_status || "NULL" }}
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

                    <a-menu-item>
                      <span @click.prevent="toVisualRoute(record)">
                        <a-icon type="eye" style="color: rgba(0,0,0,.25)" />
                        visualize
                      </span>
                    </a-menu-item>

                    <a-menu-item>
                      <span @click.prevent="openCreateTrip(record)">
                        <a-icon type="eye" style="color: rgba(0,0,0,.25)" />
                        create trip
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
  // import CreateRoute from "../../data_entry/trip_routes/CreateRoute"
  import CreateTrip from "../../data_entry/trips/CreateTrip"
//   import UpdateEmployee from "../../data_entry/update/UpdateEmployee"

  export default {
    name: "RouteAllocations",

    components: {
      CreateTrip,
      // CreateRoute,
    //   UpdateEmployee,
    },

    data() {
      return {
        loading: false,
        createBtnDisabled: true,
        createTripVisible: false,
        // createTripVisible: false,
        // updateEmployeeVisible: false,
        actionButton: "action",
        actionLoading: false,
        route_allocations: [],
        route_allocation: {},
        searchText: "",
        searchInput: null,
        searchedColumn: "",
        
        // Table Columns
        columns: [
          {
            title: "Route Origin",
            dataIndex: "optimal_route",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "route_origin",
            },

            // Last name is failing to search!!!
            onFilter: (value, record) =>
              (record.route[0].station_name !== undefined && record.route[0].station_name !== null) &&
              (record.route[0].station_name)
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
            title: "Route Destination",
            dataIndex: "optimal_route",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "route_destination",
            },

            onFilter: (value, record) =>
              (record.route.slice(-1).pop().station_name !== undefined && record.route.slice(-1).pop().station_name !== null) &&
              (record.route.slice(-1).pop().station_name)
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
            title: "Allocation Status",
            dataIndex: "allocation_status",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "allocation_status",
            },

            onFilter: (value, record) =>
              (record.route.slice(-1).pop().station_name !== undefined && record.route.slice(-1).pop().station_name !== null) &&
              (record.route.slice(-1).pop().station_name)
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
            title: "Allocation Date",
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
      ...mapActions(["fetchRouteAllocations", "refreshVisualRoute", "fetchStations"]),

      openCreateTrip(route_allocation){
        this.route_allocation = route_allocation
        this.createTripVisible = true
      },

      hideCreateTrip(){
        this.createTripVisible = false
      },

      toVisualRoute(route_allocation){
        this.refreshVisualRoute(route_allocation).then(() => {
            this.$router.push({ name: "Visual Route" })
        })
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
      let user_id = this.getActiveUser["_id"]["$oid"]
      await this.fetchRouteAllocations(user_id)
      this.route_allocations = this.getRouteAllocations
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
    },

    // mounted(){
    //   if(this.getActiveUser["role"]["role_name"] === "Manager"){
    //     this.createBtnDisabled = false
    //   }

    //   else{
    //     this.createBtnDisabled = true
    //   }
    // },

    computed: mapGetters(["getRouteAllocations", "getStations", "getActiveUser"])
  }
</script>

<style scoped>
  .highlight {
    background-color: rgb(255, 192, 105);
    padding: 0px;
  }
</style>
