<template>
  <div>
    <RequestRoute @handleHide="hideRequestRoute" :requestRouteVisible="requestRouteVisible" />
    <!-- <UpdateEmployee :employee="employee" @handleHide="hideUpdateEmployee" :updateEmployeeVisible="updateEmployeeVisible" /> -->

    <!-- <div class="loading-spinner" v-if="loading">
      <a-spin />
    </div> -->

    <div v-if="!loading">
      <h1 :style="{ margin: '12px 12px 0' }">Predictions</h1>

      <div :style="{ margin: '12px 12px 0' }">
          <a-button @click.prevent="openRequestRoute" type="primary" icon="plus" :style="{ margin: '0 auto 10px auto' }">
              Request Route
          </a-button>
          <a-table
            :data-source="predictions"
            :columns="columns"
            bordered
          >
            <span slot="station_name" slot-scope="station_name" :style="{ fontSize: '12px' }">
                {{ station_name || "NULL" }}
            </span>

            <span slot="predicted_passengers" slot-scope="predicted_passengers" :style="{ fontSize: '12px' }">
                {{ predicted_passengers || "NULL" }}
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
//   import { mapActions, mapGetters } from "vuex"
  import RequestRoute from "../../data_entry/trip_routes/RequestRoute"
//   import UpdateEmployee from "../../data_entry/update/UpdateEmployee"

  const predictions = [
    {
      key: "1",

      station_name: "Avondale",

      predicted_passengers: 75
    },

    {
      key: "2",

      station_name: "Marlborough",

      predicted_passengers: 65
    },

    {
      key: "3",

      station_name: "Westgate",

      predicted_passengers: 55
    },

    {
      key: "4",

      station_name: "Mabelreign",

      predicted_passengers: 45
    },
  ];

  export default {
    name: "Predictions",

    components: {
      RequestRoute,
    //   UpdateEmployee,
    },

    data() {
      return {
        loading: false,
        createBtnDisabled: true,
        requestRouteVisible: false,
        updateEmployeeVisible: false,
        actionButton: "action",
        actionLoading: false,
        predictions,
        employee: null,
        searchText: "",
        searchInput: null,
        searchedColumn: "",
        
        // Table Columns
        columns: [
          {
            title: "Station Name",
            dataIndex: "station_name",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "station_name",
            },

            onFilter: (value, record) =>
              (record.station_name !== undefined && record.station_name !== null) &&
              record.station_name
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
            title: "Predicted Passengers",
            dataIndex: "predicted_passengers",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "predicted_passengers",
            },

            onFilter: (value, record) =>
              (record.predicted_passengers !== undefined && record.predicted_passengers !== null) &&
              record.predicted_passengers
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
        //     title: "Action",
        //     dataIndex: "",
        //     key: "x",
        //     scopedSlots: {
        //       customRender: "action"
        //     },
        //   },
        ],
      };
    },

    methods: {
    //   ...mapActions(["fetchAllEmployees", "refreshEmployeeDescription"]),

      openRequestRoute(){
        this.requestRouteVisible = true
        // console.log("Create employee")
      },

      hideRequestRoute(){
        this.requestRouteVisible = false
      },

    //   openUpdateEmployee(employee){
    //     this.employee = {...employee}
    //     this.updateEmployeeVisible = true
    //     // console.log("Create employee")
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

    async created(){
    //   this.loading = true
    //   await this.fetchAllEmployees(this.getActiveUser["company"])
    //   this.allEmployees = this.getAllEmployees
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

    // computed: mapGetters(["getAllEmployees", "getAllCompanies", "getAllDepartments", "getActiveUser"])
  }
</script>

<style scoped>
  .highlight {
    background-color: rgb(255, 192, 105);
    padding: 0px;
  }
</style>
