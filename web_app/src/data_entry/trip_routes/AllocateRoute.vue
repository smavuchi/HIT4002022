<template>
  <div>

    <a-modal
      :title="'Allocate route  to Fleet ' + fleet['fleet_number']"
      :visible="allocateRouteVisible"
      @cancel="$emit('handleHide')"
      :footer="null"
    >
      <div  :style="{ margin: '12px 12px 0' }">
        <a-form>
            <a-row>
                <!-- <a-col :span="12">
                    <a-form-item class="a-form-item" label="Conductor" :style="{ marginRight: '6px' }">
                        <a-select v-model="user_id" placeholder="Conductor">
                            <a-select-option v-for="conductor in getConductors" :key="conductor['_id']['$oid']" :value="conductor['_id']['$oid']">
                                {{ conductor["first_name"] }} {{ conductor["last_name"] }}
                            </a-select-option>
                        </a-select>
                    </a-form-item>
                </a-col> -->

                <a-col :span="24">
                    <a-form-item class="a-form-item" label="Route" :style="{ marginRight: '6px' }">
                        <a-select
                            v-model="optimal_route"
                            placeholder="Route"
                            mode="multiple"
                            style="width: 100%"
                            defaultValue="6270b375999175a7df8b3743"
                        >
                            <a-select-option v-for="station in getStations" :key="station['_id']['$oid']" :value="station['_id']['$oid']">
                                {{ station["station_name"] }}
                            </a-select-option>
                        </a-select>
                    </a-form-item>
                </a-col>
            </a-row>

            <a-row>
                <a-col :span="12">
                    <a-form-item>
                        <a-button type="danger" @click.prevent="$emit('handleHide')">cancel</a-button>
                    </a-form-item>
                </a-col>

                <a-col :span="12">
                    <a-form-item :style="{ float: 'right' }">
                        <a-button type="primary" @click.prevent="toAllocateRoute" :loading="allocateBtnLoading">allocate</a-button>
                    </a-form-item>
                </a-col>
            </a-row>
        </a-form>
      </div>
    </a-modal>
  </div>
</template>
<script>
    import { mapActions, mapGetters } from "vuex"
    
    export default {
        name: "AllocateRoute",

        data() {
            return {
                allocateBtnLoading: false,
                disabled: true,

                // Route Details
                optimal_route: [],
                // company: this.getActiveUser["company"],
            };
        },

        props: {
            allocateRouteVisible: Boolean,
            fleet: Object,
            // conductor_id: String,
        },

        emits: ["handleHide"],

        methods: {
            ...mapActions(["allocateRoute"]),

            //   Allocate Route
            async toAllocateRoute(){
                // this.$router.push({ name: "Appropriate Route" })
                this.allocateBtnLoading = true

                let route = {
                    conductor_id: this.fleet["allocated_conductor"],
                    fleet_id: this.fleet["_id"]["$oid"],
                    optimal_route: this.optimal_route,
                }

                // console.log(route)

                await this.allocateRoute(route).then((response) => {
                    if(response.status === "info"){
                        this.$message.info(response.message);
                    }
                    
                    else if(response.status === "success"){
                        this.$message.success(response.message);
                        this.$router.push({ name: "Stations Status" })
                    }
                    
                    else if(response.status === "warn"){
                        this.$message.warn(response.message);
                    }
                    
                    else if(response.status === "error"){
                        this.$message.error(response.message);
                    }
                })

                this.allocateBtnLoading = false
                this.$emit('handleHide')
            },
            
            handleCancel() {
                console.log('Clicked cancel button');
                this.visible = false;
            },
        },

        computed: mapGetters(["getStations", "getConductors"]),
    };
</script>