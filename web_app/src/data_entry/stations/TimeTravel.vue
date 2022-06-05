<template>
  <div>

    <a-modal
      title="Time Travel Form"
      :visible="timeTravelVisible"
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
                    <a-form-item class="a-form-item" label="Prediction Day" :style="{ marginRight: '6px' }">
                        <a-select
                            v-model="prediction_day"
                            placeholder="Prediction Day"
                        >
                            <a-select-option value="Sunday">Sunday</a-select-option>
                            <a-select-option value="Monday">Monday</a-select-option>
                            <a-select-option value="Tuesday">Tuesday</a-select-option>
                            <a-select-option value="Wednesday">Wednesday</a-select-option>
                            <a-select-option value="Thursday">Thursday</a-select-option>
                            <a-select-option value="Friday">Friday</a-select-option>
                            <a-select-option value="Saturday">Saturday</a-select-option>
                        </a-select>
                    </a-form-item>
                </a-col>

                <a-col :span="12">
                    <a-form-item class="a-form-item" label="Prediction Time" :style="{ marginLeft: '6px' }">
                        <a-time-picker
                            v-model="prediction_time"
                            :default-value="moment()" format="HH:mm"
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
                        <a-button type="primary" @click.prevent="preTravel" :loading="createBtnLoading">travel</a-button>
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
    import * as moment from "moment"
    
    export default {
        name: "CreateTrip",

        data() {
            return {
                createBtnLoading: false,
                disabled: true,

                // Trip Details
                // user_id: "6228f5ad67826e53bdd5e719",
                // fleet_id: "6228e9162508950ec7b6a121",
                prediction_day: moment().format("dddd"),
                prediction_time: "",
            };
        },

        props: {
            timeTravelVisible: Boolean,
        },

        emits: ["handleHide"],

        methods: {
            ...mapActions(["timeTravel"]),

            // showModal() {
            //     this.visible = true;
            // },

            //   Pretravel
            async preTravel(){
                this.createBtnLoading = true

                let prediction_body = {
                    prediction_day: this.prediction_day,
                    prediction_time: moment(this.prediction_time).format("HH:mm"),
                }

                // await this.timeTravel(prediction_body).then((response) => {
                //     if(response.status === "info"){
                //         this.$message.info(response.message);
                //     }
                    
                //     else if(response.status === "success"){
                //         this.$message.success(response.message);
                //     }
                    
                //     else if(response.status === "warn"){
                //         this.$message.warn(response.message);
                //     }
                    
                //     else if(response.status === "error"){
                //         this.$message.error(response.message);
                //     }
                // })

                // this.$router.push({ name: "My Trip" })

                this.createBtnLoading = false

                this.$emit('handleHide', prediction_body)
            },
            
            handleCancel() {
                console.log('Clicked cancel button');
                this.visible = false;
            },
        },

        computed: mapGetters(["getStations", "getFleets", "getConductors", "getActiveUser"]),
    };
</script>