<template>
  <div>
    <CreateUser @handleHide="hideCreateUser" :createUserVisible="createUserVisible" />
    <!-- <UpdateEmployee :employee="employee" @handleHide="hideUpdateEmployee" :updateEmployeeVisible="updateEmployeeVisible" /> -->

    <div class="loading-spinner" v-if="loading">
        <!-- <a-spin /> -->
        <a-skeleton active />
    </div>

    <div v-if="!loading">
      <h1 :style="{ margin: '12px 12px 0' }">Users</h1>

      <div :style="{ margin: '12px 12px 0' }">
          <a-button @click.prevent="openCreateUser" type="primary" icon="plus" :style="{ margin: '0 auto 10px auto' }">
              Create User
          </a-button>

          <a-table
            :data-source="users"
            :columns="columns"
            bordered
          >
            <span slot="first_name" slot-scope="first_name" :style="{ fontSize: '12px' }">
                {{ first_name || "NULL" }}
            </span>

            <span slot="last_name" slot-scope="last_name" :style="{ fontSize: '12px' }">
                {{ last_name || "NULL" }}
            </span>

            <span slot="email" slot-scope="email" :style="{ fontSize: '12px' }">
                {{ email || "NULL" }}
            </span>

            <span slot="role" slot-scope="role" :style="{ fontSize: '12px' }">
                {{ role || "NULL" }}
            </span>

            <!-- <span slot="action" slot-scope="record">
                <a-dropdown :trigger="['click']">
                  <span class="ant-drop-down-link" :style="{ cursor: 'pointer' }">
                      <a-button :loading="actionLoading[`action${record['_id']}`]" title="More..." :style="{ marginRight: '4px' }">
                        <a-icon v-if="!actionLoading[`action${record['_id']}`]" type="more" style="color: rgba(0,0,0,.25)" />
                      </a-button>
                  </span>

                  <a-menu slot="overlay">
                    <a-menu-item>
                      <span @click.prevent="toAllocateConductor(record)">
                        <a-icon type="edit" style="color: rgba(0,0,0,.25)" />
                        allocate
                      </span>
                    </a-menu-item>

                    <a-menu-item>
                      <span @click.prevent="toUpdateConductor(record)">
                        <a-icon type="eye" style="color: rgba(0,0,0,.25)" />
                        update
                      </span>
                    </a-menu-item>
                </a-menu>
              </a-dropdown>
            </span> -->

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
  import CreateUser from "../../data_entry/users/CreateUser"
//   import UpdateEmployee from "../../data_entry/update/UpdateEmployee"

//   const conductors = [
//     {
//       key: "1",
//       first_name: "Kurt",
//       last_name: "Weller",
//       email: "kurt@google.co.us",
//       allocation_status: "FREE",
//     },

//     {
//       key: "2",
//       first_name: "Edgar",
//       last_name: "Reade",
//       email: "edgar@google.co.us",
//       allocation_status: "FREE",
//     },

//     {
//       key: "3",
//       first_name: "William",
//       last_name: "Patterson",
//       email: "bill@google.co.us",
//       allocation_status: "FREE",
//     },
//   ];

  export default {
    name: "Users",

    components: {
      CreateUser,
    //   UpdateEmployee,
    },

    data() {
      return {
        loading: false,
        createBtnDisabled: true,
        createUserVisible: false,
        // updateEmployeeVisible: false,
        actionButton: "action",
        actionLoading: false,
        users: [],
        searchText: "",
        searchInput: null,
        searchedColumn: "",
        
        // Table Columns
        columns: [
          {
            title: "First Name",
            dataIndex: "first_name",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "first_name",
            },

            onFilter: (value, record) =>
              (record !== undefined && record !== null) &&
              record.first_name
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
            title: "Last Name",
            dataIndex: "last_name",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "last_name",
            },

            onFilter: (value, record) =>
              (record !== undefined && record !== null) &&
              record.last_name
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
            title: "Email",
            dataIndex: "email",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "email",
            },

            onFilter: (value, record) =>
              (record !== undefined && record !== null) &&
              record.email
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
            title: "Role",
            dataIndex: "role",
            scopedSlots: {
              filterDropdown: "filterDropdown",
              filterIcon: "filterIcon",
              customRender: "role",
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

          // {
          //   title: "Action",
          //   dataIndex: "",
          //   key: "x",
          //   scopedSlots: {
          //     customRender: "action"
          //   },
          // },
        ],
      };
    },

    methods: {
      ...mapActions(["fetchUsers"]),

      openCreateUser(){
        this.createUserVisible = true
      },

      hideCreateUser(){
        this.createUserVisible = false
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
      this.loading = true
      await this.fetchUsers()
      this.users = this.getUsers
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

    computed: mapGetters(["getUsers"])
  }
</script>

<style scoped>
  .highlight {
    background-color: rgb(255, 192, 105);
    padding: 0px;
  }
</style>
