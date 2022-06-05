<template>
  <a-layout id="components-layout-demo-custom-trigger" :style="{ minHeight: '100vh', maxHeight: '100vh' }">
    <a-layout-sider class="layout-sider"
      v-model="collapsed"
      :trigger="null"
      collapsible
      breakpoint="lg"
      @breakpoint="onBreakpoint"
    >
      <div class="logo" :style="{ border: '', height: '6%' }">
          <h1 v-if="!collapsed" :style="{ color: 'white', margin: 'auto 0', fontWeight: 'bold', fontSize: 'medium' }">Passengers Prediction</h1>
      </div>

      <!-- <a-menu class="layout-sider-menu" theme="dark" mode="inline" :default-selected-keys="default_tab"> -->
      <a-menu class="layout-sider-menu" theme="dark" mode="inline">
        <!-- <a-menu-item key="1" @click="toDashboard">
            <a-icon type="dashboard" />
            <span>Dashboard</span>
        </a-menu-item> -->

        <a-sub-menu key="5" v-if="getActiveUser['role'] === 'DISPATCHER'">
          <span slot="title"
            ><a-icon type="cluster"></a-icon><span>Stations</span></span
          >
          <!-- <a-menu-item key="5a" @click="toStations">
            Stations
          </a-menu-item> -->

          <a-menu-item key="5a" @click="toStationsStatus">
            Stations Status
          </a-menu-item>
        </a-sub-menu>

        <a-sub-menu key="2" v-if="getActiveUser['role'] === 'CONDUCTOR'">
          <span slot="title"
            ><a-icon type="rocket"></a-icon><span>Trips</span></span
          >
          <a-menu-item key="3a" @click="toMyTrip">
            My Trip
          </a-menu-item>

          <!-- <a-menu-item key="3b" @click="toCurrentTrip">
            Current
          </a-menu-item>

          <a-menu-item key="3c" @click="toOffloadedTrips">
            Offloaded
          </a-menu-item>

          <a-menu-item key="3d" @click="toAllTrips">
            All
          </a-menu-item> -->
        </a-sub-menu>

        <a-menu-item key="4" @click="toFleets" v-if="getActiveUser['role'] === 'DISPATCHER'">
            <a-icon type="car" />
            <span>Fleets</span>
        </a-menu-item>

        <a-menu-item key="6" @click="toConductors" v-if="getActiveUser['role'] === 'DISPATCHER'">
            <a-icon type="solution" />
            <span>Conductors</span>
        </a-menu-item>

        <a-menu-item key="7" @click="toUsers" v-if="getActiveUser['role'] === 'DISPATCHER'">
            <a-icon type="team" />
            <span>Users</span>
        </a-menu-item>

        <!-- <a-menu-item key="6" @click="toStations">
            <a-icon type="cluster" />
            <span>Stations</span>
        </a-menu-item> -->

        <a-menu-item key="8" @click="toRouteAllocations" v-if="getActiveUser['role'] === 'CONDUCTOR'">
            <a-icon type="pull-request" />
            <span>Route Allocations</span>
        </a-menu-item>
      </a-menu>
    </a-layout-sider>
    
    <a-layout>
      <a-layout-header :style="{ background: '#fff', padding: '0', display: 'flex' }">
        <a-icon
          class="trigger"
          :type="collapsed ? 'menu-unfold' : 'menu-fold'"
          @click="() => (collapsed = !collapsed)"
        />

        <h1 class="user-profile-description" :style="{ margin: 'auto 12px auto auto' }">
            <a-icon :style="{fontSize: '20px'}" slot="prefix" type="user" style="color: rgba(0,0,0,.25)" />
            <a-dropdown :trigger="['click']">
              <span class="ant-drop-down-link" :style="{ cursor: 'pointer' }">
                {{ getActiveUser["first_name"] }} {{ getActiveUser["last_name"] }}
                <!-- {{ getActiveUser["email"] }} -->
                <!-- Valentine Sean -->
                <a-icon type="caret-down" style="color: rgba(0,0,0,.25)" />
              </span>

              <a-menu slot="overlay">
                <a-menu-item>
                  <span @click.prevent="logout">
                    logout
                  </span>
                </a-menu-item>
              </a-menu>
            </a-dropdown>
        </h1>
      </a-layout-header>

      <a-layout-content
        :style="{ margin: '12px 12px', padding: '12px', background: '#fff', overflowY: 'scroll' }"
      >
        <div class="loading-spinner" v-if="loading">
          <a-spin />
        </div>

        <slot v-if="!loading" />
      </a-layout-content>
    </a-layout>
  </a-layout>
</template>
<script>
  import { mapGetters } from "vuex"

  export default {
    name: "DashboardLayout",

    data() {
      return {
        loading: false,
        collapsed: false,
        drawer_visibility: false,
        desktop_size: true,
        tablet_size: false,
        default_tab: "",
        // default_sub_tab: null,
      };
    },

    methods: {
        // ...mapActions(["fetchDepartments", "fetchRoles", "fetchUsers", "fetchFeeds", "activate"]),
        // ...mapActions(["logoutUser"]),

        toDashboard(){
            this.$router.replace({ name: "Dashboard" })
            // console.log("Dashboard")
        },

        // toPredictions(){
        //     this.$router.replace({ name: "Predictions" })
        // },

        toMyTrip(){
            this.$router.replace({ name: "My Trip" })
            // console.log("Predictions")
        },

        toCurrentTrip(){
            this.$router.replace({ name: "Current Trip" })
            // console.log("Predictions")
        },

        toOffloadedTrips(){
            this.$router.replace({ name: "Offloaded Trips" })
            // console.log("Predictions")
        },

        toAllTrips(){
            this.$router.replace({ name: "All Trips" })
            // console.log("Predictions")
        },

        toFleets(){
            this.$router.replace({ name: "Fleets" })
            // console.log("Fleet")
        },

        toStations(){
            this.$router.replace({ name: "Stations" })
            // console.log("Fleet")
        },

        toStationsStatus(){
            this.$router.replace({ name: "Stations Status" })
            // console.log("Fleet")
        },

        toConductors(){
            this.$router.replace({ name: "Conductors" })
            // console.log("Fleet")
        },

        toUsers(){
            this.$router.replace({ name: "Users" })
            // console.log("Fleet")
        },

        toRouteAllocations(){
            this.$router.replace({ name: "Route Allocations" })
        },

        // On Breakpoint
        onBreakpoint(){
          this.tablet_size = true
        },

        // // Show Drawer
        // showDrawer(){
        //   this.drawer_visibility = true
        // },

        // closeDrawer(){
        //   this.drawer_visibility = false
        // },

        // // LOGOUT
        async logout(){
          this.loading = true
          // this.logoutUser(false)
          window.sessionStorage.removeItem('vuex');
          window.sessionStorage.clear()
          this.$router.replace({ name: 'Login' });
          this.$message.info("You have successfully logged out")
          this.loading = false
            // console.log("Logout function")
        }
    },

    created(){
        if(this.$route.name === "Dashboard"){
          this.default_tab = "1"
        }
        
        // else if(this.$route.name === "Predictions"){
        //   this.default_tab = "2"
        // }

        else if(this.$route.name === "Appropriate Route"){
          this.default_tab = "2"
        }
        
        else if(this.$route.name === "My Trip"){
          this.default_tab = "3a"
        }

        else if(this.$route.name === "Current Trip"){
          this.default_tab = "3b"
        }

        else if(this.$route.name === "Offloaded Trips"){
          this.default_tab = "3c"
        }

        else if(this.$route.name === "All Trips"){
          this.default_tab = "3d"
        }

        // else if(this.$route.name === "Trips"){
        //   this.default_tab = "3"
        // }

        // else if(this.$route.name === "Current Trip" || this.$route.name === "Offloaded Trips"  || this.$route.name === "All Trips"){
        //   this.default_tab = "3"
        // }

        else if(this.$route.name === "Fleets"){
          this.default_tab = "4"
        }

        else if(this.$route.name === "Stations Status"){
          this.default_tab = "5"
        }

        else if(this.$route.name === "Stations"){
          this.default_tab = "6"
        }

        else if(this.$route.name === "Routes"){
          this.default_tab = "7"
        }


    },

    mounted(){
        // Mounted hook
    },

    computed: mapGetters(["getActiveUser"])
  };
</script>
<style>
  #components-layout-demo-custom-trigger .trigger {
    font-size: 18px;
    line-height: 64px;
    padding: 0 12px;
    cursor: pointer;
    transition: color 0.3s;
  }

  #components-layout-demo-custom-trigger .trigger:hover {
    color: #1890ff;
  }

  #components-layout-demo-custom-trigger .logo {
    height: 32px;
    /* background: rgba(255, 255, 255, 0.2); */
    margin: 16px;
    display: flex;
  }

  .layout-sider-menu{
  }

  /* MEDIA QUERIES */

  /* Extra Extra Large */
  @media screen and (max-width: 1600px){}

  /* Extra Large */
  @media screen and (max-width: 1200px){}

  /* Large */
  @media screen and (max-width: 992px){}

  /* Medium */
  @media screen and (max-width: 768px){
    .trigger{
      display: none !important;
    }

    .user-profile-description{
      /* border: solid 1px red; */
      /* margin: auto 12px auto auto; */
      margin-left: 12px !important;
    }

    .more-btn{
      display: inline !important;
    }
  }

  /* Small */
  @media screen and (max-width: 576px){}

  /* Extra Small */
  @media screen and (max-width: 480px){}
</style>
