<template>
  <div>

    <a-modal
      title="Create Fleet Form"
      :visible="createFleetVisible"
      @cancel="$emit('handleHide')"
      :footer="null"
    >
      <div  :style="{ margin: '12px 12px 0' }">
        <a-form>
            <a-row>
                <a-col :span="12">
                    <a-form-item class="a-form-item" label="Fleet Number" :style="{ marginLeft: '6px' }">
                        <a-input
                            type="text"
                            v-model="fleet_number"
                            placeholder="Fleet Number"
                        />
                    </a-form-item>
                </a-col>

                <a-col :span="12">
                    <a-form-item class="a-form-item" label="Fleet Capacity" :style="{ marginLeft: '6px' }">
                        <a-input
                            type="number"
                            v-model="fleet_capacity"
                            placeholder="Fleet Capacity"
                        />
                    </a-form-item>
                </a-col>
            </a-row>

            <a-row>
                <a-col :span="24">
                    <a-form-item class="a-form-item" label="Current Station" :style="{ marginRight: '6px' }">
                        <a-select v-model="current_station" placeholder="Current Station">
                            <a-select-option v-for="station in getStations.filter(s => s['station_name'] === 'Depot')" :key="station['_id']" :value="station['_id']['$oid']">{{ station["station_name"] }}</a-select-option>
                        </a-select>
                    </a-form-item>
                </a-col>
            </a-row>

            <!-- <a-row>
                <a-col :span="12">
                    <a-form-item class="a-form-item" label="Allocation Status" :style="{ marginRight: '6px' }">
                        <a-select v-model="allocation_status" placeholder="Allocation Status">
                            <a-select-option v-for="station in getStations" :key="station['_id']" :value="station['_id']['$oid']">{{ station["station_name"] }}</a-select-option>
                            <a-select-option value="FREE">FREE</a-select-option>
                            <a-select-option value="ALLOCATED">ALLOCATED</a-select-option>
                        </a-select>
                    </a-form-item>
                </a-col>

                <a-col :span="12">
                    <a-form-item class="a-form-item" label="Fleet Status" :style="{ marginRight: '6px' }">
                        <a-select v-model="fleet_status" placeholder="Fleet Status">
                            <a-select-option value="AVAILABLE">FREE</a-select-option>
                            <a-select-option value="OCCUPIED">OCCUPIED</a-select-option>
                        </a-select>
                    </a-form-item>
                </a-col>
            </a-row> -->

            <a-row>
                <a-col :span="12">
                    <a-form-item>
                        <a-button type="danger" @click.prevent="$emit('handleHide')">cancel</a-button>
                    </a-form-item>
                </a-col>

                <a-col :span="12">
                    <a-form-item :style="{ float: 'right' }">
                        <a-button type="primary" @click.prevent="toCreateFleet" :loading="createBtnLoading">create</a-button>
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
        name: "CreateFleet",

        data() {
            return {
                createBtnLoading: false,
                disabled: true,

                // Route Details
                fleet_number: "",
                fleet_capacity: null,
                current_station: "",
                allocation_status: "",
                fleet_status: "",
                // company: this.getActiveUser["company"],
            };
        },

        props: {
            createFleetVisible: Boolean,
        },

        emits: ["handleHide"],

        methods: {
            ...mapActions(["createFleet"]),

            //   Request Route
            async toCreateFleet(){
                // this.$router.push({ name: "Appropriate Route" })
                this.createBtnLoading = true

                let fleet = {
                    fleet_number: this.fleet_number,
                    fleet_capacity: this.fleet_capacity,
                    current_station: this.current_station,
                    // allocation_status: this.allocation_status,
                    // fleet_status: this.fleet_status,
                }

                await this.createFleet(fleet).then((response) => {
                    if(response.status === "info"){
                        this.$message.info(response.message);
                    }
                    
                    else if(response.status === "success"){
                        this.$message.success(response.message);
                        this.$router.push({ name: "Fleets" })
                    }
                    
                    else if(response.status === "warn"){
                        this.$message.warn(response.message);
                    }
                    
                    else if(response.status === "error"){
                        this.$message.error(response.message);
                    }
                })

                this.createBtnLoading = false
                this.$emit('handleHide')
            },
            
            handleCancel() {
                console.log('Clicked cancel button');
                this.visible = false;
            },
        },

        computed: mapGetters(["getStations"]),
    };
</script>