<template>
    <div>
        <AllocateRoute @handleHide="hideAllocateRoute" :allocateRouteVisible="allocateRouteVisible" :fleet="fleet" />

        <div>
            <!-- <h1 :style="{ margin: '12px 12px 0' }">Station Status Details</h1> -->

            <a-row :style="{ margin: '12px 12px 0' }">
                <a-col :span="8">
                    <a-descriptions title="Station Status Details" :column="1">
                        <a-descriptions-item label="Route Source">{{ station_status_details['pickup_station'] }}</a-descriptions-item>
                        <a-descriptions-item label="Prediction Count">{{ station_status_details['prediction_count'] }}</a-descriptions-item>
                        <a-descriptions-item label="Route Destination">{{ station_status_details['dropoff_station'] }}</a-descriptions-item>
                        <a-descriptions-item label="Last Pickup Time">{{ station_status_details['last_pickup_time'] }}</a-descriptions-item>
                    </a-descriptions>
                </a-col>

                <a-col :span="8" :style="{ marginRight: '6px' }">
                    <h1 :style="{ fontSize: '16px', fontWeight: 'bold' }">Free Fleet</h1>

                    <a-list size="small" bordered :data-source="getFreeFleets">
                        <a-list-item  slot="renderItem" slot-scope="item">
                            <a-list-item-meta
                                :description="item['fleet_capacity'] + ' Seater, Currently in ' + item['current_station']['station_name']"
                            >
                                <a slot="title">Fleet {{ item['fleet_number'] }}</a>
                            </a-list-item-meta>
                            <!-- <span>Fleet {{ item }}, 50 Seats, Currently in Belvedere</span> -->
                            <a-button @click.prevent="openAllocateRoute(item)">allocate</a-button>
                        </a-list-item>
                    </a-list>
                </a-col>
                
                <a-col :span="7" :style="{ marginLeft: '6px' }">
                    <h1 :style="{ fontSize: '16px', fontWeight: 'bold' }">Occupied Fleet</h1>

                    <a-list size="small" bordered :data-source="getOccupiedFleets">
                        <a-list-item  slot="renderItem" slot-scope="item">
                            <a-list-item-meta
                                :description="item['fleet_capacity'] + ' Seater, Currently in ' + item['current_station']['station_name']"
                            >
                                <a slot="title">Fleet {{ item['fleet_number'] }}</a>
                            </a-list-item-meta>
                            <a-button @click.prevent="openAllocateRoute(item)">allocate</a-button>
                        </a-list-item>
                    </a-list>
                </a-col>
            </a-row>
        </div>
    </div>
</template>

<script>
    import { mapGetters } from "vuex"
    import AllocateRoute from "../../data_entry/trip_routes/AllocateRoute"

    export default{
        name: "StationStationDetails",

        components: {
            AllocateRoute,
        },

        data(){
            return{
                station_status_details: {},
                free_fleets: [],
                occupied_fleets: [],
                // conductor_id: "",
                fleet: {},
                allocateRouteVisible: false,
            }
        },

        created(){
            this.station_status_details = this.getStationStatusDetails
            this.free_fleets = this.getFreeFleets
            this.occupied_fleets = this.getOccupiedFleets
        },

        computed: mapGetters(["getStationStatusDetails", "getFreeFleets", "getOccupiedFleets"]),

        methods: {
            openAllocateRoute(fleet){
                // this.conductor_id = fleet["allocated_conductor"]
                this.fleet = fleet
                this.allocateRouteVisible = true
                // console.log("Create employee")
            },

            hideAllocateRoute(){
                this.allocateRouteVisible = false
            },
        },
    }
</script>

<style scoped></style>