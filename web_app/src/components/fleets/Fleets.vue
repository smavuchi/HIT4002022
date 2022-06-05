<template>
  <div>
    <CreateFleet @handleHide="hideCreateFleet" :createFleetVisible="createFleetVisible" />
    <AllocateFleet :fleet="fleet" @handleHide="hideAllocateFleet" :allocateFleetVisible="allocateFleetVisible" />
    <!-- <UpdateEmployee :employee="employee" @handleHide="hideUpdateEmployee" :updateEmployeeVisible="updateEmployeeVisible" /> -->

    <div class="loading-spinner" v-if="loading">
        <!-- <a-spin /> -->
        <a-skeleton active />
    </div>

    <div v-if="!loading">
      <h1 :style="{ margin: '12px 12px 0' }">Fleets</h1>

      <div :style="{ margin: '12px 12px 0' }">
          <a-button @click.prevent="openCreateFleet" type="primary" icon="plus" :style="{ margin: '0 auto 10px auto' }">
              Create Fleet
          </a-button>
          <a-table
            :data-source="fleets"
            :columns="columns"
            bordered
          >
            <span slot="fleet_number" slot-scope="fleet_number" :style="{ fontSize: '12px' }">
                {{ fleet_number || "NULL" }}
            </span>

            <span slot="fleet_capacity" slot-scope="fleet_capacity" :style="{ fontSize: '12px' }">
                {{ fleet_capacity || "NULL" }}
            </span>

            <span slot="allocation_status" slot-scope="allocation_status" :style="{ fontSize: '12px' }">
                {{ allocation_status || "NULL" }}
            </span>

            <span slot="fleet_status" slot-scope="fleet_status" :style="{ fontSize: '12px' }">
                {{ fleet_status || "NULL" }}
            </span>

            <!-- <span slot="active_trip_origin" slot-scope="active_trip_origin" :style="{ fontSize: '12px' }">
                {{ active_trip_origin || "NULL" }}
            </span>

            <span slot="active_trip_target" slot-scope="active_trip_target" :style="{ fontSize: '12px' }">
                {{ active_trip_target || "NULL" }}
            </span> -->

            <span slot="current_station" slot-scope="current_station" :style="{ fontSize: '12px' }">
                {{ current_station || "NULL" }}
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
                      <span @click.prevent="openAllocateFleet(record)">
                        <a-icon type="edit" style="color: rgba(0,0,0,.25)" />
                        allocate
                      </span>
                    </a-menu-item>

                    <a-menu-item>
                      <span @click.prevent="toUpdateFleet(record)">
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
  import CreateFleet from "../../data_entry/fleets/CreateFleet"
  import AllocateFleet from "../../data_entry/fleets/AllocateFleet"
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
      CreateFleet,
      AllocateFleet,
    //   UpdateEmployee,
    },

    data() {
      return {
        loading: false,
        createBtnDisabled: true,
        createFleetVisible: false,
        allocateFleetVisible: false,
        // updateEmployeeVisible: false,
        actionButton: "action",
        actionLoading: false,
        fleets: [],
        fleet: {},
        searchText: "",
        searchInput: null,
        searchedColumn: "",
        
        // Table Columns
        columns: [
          {
            title: "Fleet Number",
            dataIndex: "fleet_number",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "fleet_number",
            },

            onFilter: (value, record) =>
              (record.fleet_number !== undefined && record.fleet_number !== null) &&
              record.fleet_number
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
            dataIndex: "fleet_capacity",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "fleet_capacity",
            },

            onFilter: (value, record) =>
              (record.fleet_capacity !== undefined && record.fleet_capacity !== null) &&
              record.fleet_capacity
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
              (record.allocation_status !== undefined && record.allocation_status !== null) &&
              record.allocation_status
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
            title: "Fleet Status",
            dataIndex: "fleet_status",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "fleet_status",
            },

            onFilter: (value, record) =>
              (record.fleet_status !== undefined && record.fleet_status !== null) &&
              record.fleet_status
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

          // {
          //   title: "Active Trip Origin",
          //   dataIndex: "active_trip_origin",
          //   scopedSlots: {
          //     filterDropdown: "filterDropdown",
          //     filterIcon: "filterIcon",
          //     customRender: "active_trip_origin",
          //   },

          //   onFilter: (value, record) =>
          //     (record.active_trip_origin !== undefined && record.active_trip_origin !== null) &&
          //     record.active_trip_origin
          //       .toString()
          //       .toLowerCase()
          //       .includes(value.toLowerCase()),
          //   onFilterDropdownVisibleChange: (visible) => {
          //     if (visible) {
          //       setTimeout(() => {
          //         this.searchInput.focus();
          //       }, 0);
          //     }
          //   },
          // },

          // {
          //   title: "Active Trip Target",
          //   dataIndex: "active_trip_target",
          //   scopedSlots: {
          //     filterDropdown: "filterDropdown",
          //     filterIcon: "filterIcon",
          //     customRender: "active_trip_target",
          //   },

          //   onFilter: (value, record) =>
          //     (record.active_trip_target !== undefined && record.active_trip_target !== null) &&
          //     record.active_trip_target
          //       .toString()
          //       .toLowerCase()
          //       .includes(value.toLowerCase()),
          //   onFilterDropdownVisibleChange: (visible) => {
          //     if (visible) {
          //       setTimeout(() => {
          //         this.searchInput.focus();
          //       }, 0);
          //     }
          //   },
          // },

          {
            title: "Current Station",
            dataIndex: "current_station.station_name",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "current_station",
            },

            onFilter: (value, record) =>
              (record.current_station !== undefined && record.current_station !== null && record.current_station !== []) &&
              record.current_station.station_name
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
      ...mapActions(["fetchFleets"]),

      openCreateFleet(){
        this.createFleetVisible = true
        // console.log("Create employee")
      },

      hideCreateFleet(){
        this.createFleetVisible = false
      },

      openAllocateFleet(fleet){
        this.fleet = {...fleet}
        this.allocateFleetVisible = true
        // console.log("Create employee")
      },

      hideAllocateFleet(){
        this.allocateFleetVisible = false
      },

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
      await this.fetchFleets()
      this.fleets = this.getFleets
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

    computed: mapGetters(["getFleets"])
  }
</script>

<style scoped>
  .highlight {
    background-color: rgb(255, 192, 105);
    padding: 0px;
  }
</style>
