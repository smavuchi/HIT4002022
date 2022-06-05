<template>
  <div>

    <a-modal
      title="Request Route Form"
      :visible="requestRouteVisible"
      @cancel="$emit('handleHide')"
      :footer="null"
    >
      <div  :style="{ margin: '12px 12px 0' }">
        <a-form>
            <a-row>
                <a-col :span="12">
                    <a-form-item class="a-form-item" label="Current Station" :style="{ marginRight: '6px' }">
                        <a-select v-model="current_station" placeholder="Current Station">
                            <a-select-option v-for="station in getStations" :key="station['_id']" :value="station['_id']['$oid']">{{ station["station_name"] }}</a-select-option>
                            <!-- <a-select-option value="Marlborough">Marlborough</a-select-option>
                            <a-select-option value="Avondale">Avondale</a-select-option>
                            <a-select-option value="Mabelreign">Mabelreign</a-select-option>
                            <a-select-option value="Westgate">Westgate</a-select-option> -->
                        </a-select>
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
                <a-col :span="12">
                    <a-form-item>
                        <a-button type="danger" @click.prevent="$emit('handleHide')">cancel</a-button>
                    </a-form-item>
                </a-col>

                <a-col :span="12">
                    <a-form-item :style="{ float: 'right' }">
                        <a-button type="primary" @click.prevent="requestRoute" :loading="createBtnLoading">request</a-button>
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
        name: "RequestRoute",

        data() {
            return {
                createBtnLoading: false,
                disabled: true,

                // Route Details
                current_station: "6202617d08c535c258e414e3",
                fleet_capacity: null
                // company: this.getActiveUser["company"],
            };
        },

        props: {
            requestRouteVisible: Boolean,
        },

        emits: ["handleHide"],

        methods: {
            ...mapActions(["generateRoutesPredictions"]),

            //   Request Route
            async requestRoute(){
                // this.$router.push({ name: "Appropriate Route" })
                this.createBtnLoading = true

                let route = {
                    current_station: this.current_station,
                    fleet_capacity: this.fleet_capacity,
                }

                await this.generateRoutesPredictions(route).then((response) => {
                    if(response.status === "info"){
                        this.$message.info(response.message);
                    }
                    
                    else if(response.status === "success"){
                        this.$message.success(response.message);
                        this.$router.push({ name: "Appropriate Route" })
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