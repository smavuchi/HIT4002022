<template>
  <div>

    <a-modal
      title="Create Trip Form"
      :visible="createTripVisible"
      @cancel="$emit('handleHide')"
      :footer="null"
    >
      <div  :style="{ margin: '12px 12px 0' }">
        <a-form>
            <!-- <a-row>
                <a-col :span="12">
                    <a-form-item class="a-form-item" label="Conductor" :style="{ marginRight: '6px' }">
                        <a-select v-model="user_id" placeholder="Conductor">
                            <a-select-option v-for="conductor in getConductors" :key="conductor['_id']['$oid']" :value="conductor['user_id']['$oid']">{{ conductor["personal_details"]["first_name"] }} {{ conductor["personal_details"]["last_name"] }}</a-select-option>
                        </a-select>
                    </a-form-item>
                </a-col>

                <a-col :span="12">
                    <a-form-item class="a-form-item" label="Fleet No." :style="{ marginRight: '6px' }">
                        <a-select v-model="fleet_id" placeholder="Fleet No.">
                            <a-select-option v-for="fleet in getFleets" :key="fleet['_id']['$oid']" :value="fleet['_id']['$oid']">{{ fleet["fleet_number"] }}</a-select-option>
                        </a-select>
                    </a-form-item>
                </a-col>
            </a-row> -->

            <!-- <a-row>
                <a-col :span="12">
                    <a-form-item class="a-form-item" label="Trip Origin" :style="{ marginRight: '6px' }">
                        <a-select v-model="trip_origin" placeholder="Trip Origin">
                            <a-select-option v-for="station in getStations" :key="station['_id']['$oid']" :value="station['_id']['$oid']">{{ station["station_name"] }}</a-select-option>
                        </a-select>
                    </a-form-item>
                </a-col>

                <a-col :span="12">
                    <a-form-item class="a-form-item" label="Trip Destination" :style="{ marginRight: '6px' }">
                        <a-select v-model="trip_destination" placeholder="Trip Destination">
                            <a-select-option v-for="station in getStations" :key="station['_id']['$oid']" :value="station['_id']['$oid']">{{ station["station_name"] }}</a-select-option>
                        </a-select>
                    </a-form-item>
                </a-col>
            </a-row> -->

            <a-row>
                <a-col :span="12">
                    <a-form-item class="a-form-item" label="Head Count" :style="{ marginRight: '6px' }">
                        <a-input
                            type="number"
                            v-model="head_count"
                            placeholder="Head Count"
                        />
                    </a-form-item>
                </a-col>

                <a-col :span="12">
                    <a-form-item class="a-form-item" label="Surplus Count" :style="{ marginLeft: '6px' }">
                        <a-input
                            type="number"
                            v-model="surplus_count"
                            placeholder="Surplus Count"
                        />
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
                        <a-button type="primary" @click.prevent="saveTrip" :loading="createBtnLoading">save</a-button>
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
        name: "CreateTrip",

        data() {
            return {
                createBtnLoading: false,
                disabled: true,

                // Trip Details
                // user_id: "6228f5ad67826e53bdd5e719",
                // fleet_id: "6228e9162508950ec7b6a121",
                trip_origin: "",
                trip_destination: "",
                head_count: 0,
                surplus_count: 0
            };
        },

        props: {
            createTripVisible: Boolean,
            route_allocation: Object,
        },

        emits: ["handleHide"],

        methods: {
            ...mapActions(["createTrip"]),

            // showModal() {
            //     this.visible = true;
            // },

            //   Create Trip
            async saveTrip(){
                this.createBtnLoading = true

                let trip = {
                    conductor_id: this.getActiveUser["_id"]["$oid"],
                    fleet_id: this.getActiveUser["allocated_fleet"],
                    // trip_origin: this.trip_origin,
                    // trip_destination: this.trip_destination,
                    head_count: this.head_count,
                    surplus_count: this.surplus_count,
                    route_allocation_id: this.route_allocation["_id"]["$oid"],
                    live_route: this.route_allocation["optimal_route"],
                }

                // console.log(trip)

                await this.createTrip(trip).then((response) => {
                    if(response.status === "info"){
                        this.$message.info(response.message);
                    }
                    
                    else if(response.status === "success"){
                        this.$message.success(response.message);
                    }
                    
                    else if(response.status === "warn"){
                        this.$message.warn(response.message);
                    }
                    
                    else if(response.status === "error"){
                        this.$message.error(response.message);
                    }
                })

                this.$router.push({ name: "My Trip" })

                this.createBtnLoading = false
                
                this.$emit('handleHide')
            },
            
            handleCancel() {
                console.log('Clicked cancel button');
                this.visible = false;
            },
        },

        computed: mapGetters(["getStations", "getFleets", "getConductors", "getActiveUser"]),
    };
</script>