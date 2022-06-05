<template>
  <div>

    <a-modal
      title="Create User Form"
      :visible="createUserVisible"
      @cancel="$emit('handleHide')"
      :footer="null"
    >
      <div  :style="{ margin: '12px 12px 0' }">
        <a-form>
            <a-row>
                <a-col :span="12">
                    <a-form-item class="a-form-item" label="First Name" :style="{ marginLeft: '6px' }">
                        <a-input
                            type="text"
                            v-model="first_name"
                            placeholder="First Name"
                        />
                    </a-form-item>
                </a-col>

                <a-col :span="12">
                    <a-form-item class="a-form-item" label="Last Name" :style="{ marginLeft: '6px' }">
                        <a-input
                            type="text"
                            v-model="last_name"
                            placeholder="Last Name"
                        />
                    </a-form-item>
                </a-col>
            </a-row>

            <a-row>
                <a-col :span="12">
                    <a-form-item class="a-form-item" label="Email" :style="{ marginLeft: '6px' }">
                        <a-input
                            type="email"
                            v-model="email"
                            placeholder="Email"
                        />
                    </a-form-item>
                </a-col>

                <a-col :span="12">
                    <a-form-item class="a-form-item" label="Password" :style="{ marginLeft: '6px' }">
                        <a-input
                            type="password"
                            v-model="password"
                            placeholder="Password"
                        />
                    </a-form-item>
                </a-col>
            </a-row>

            <a-row>
                <a-col :span="24">
                    <a-form-item class="a-form-item" label="Role" :style="{ marginRight: '6px' }">
                        <a-select v-model="role" placeholder="Role">
                            <a-select-option value="DISPATCHER">DISPATCHER</a-select-option>
                            <a-select-option value="CONDUCTOR">CONDUCTOR</a-select-option>
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
                        <a-button type="primary" @click.prevent="toCreateUser" :loading="createBtnLoading">create</a-button>
                    </a-form-item>
                </a-col>
            </a-row>
        </a-form>
      </div>
    </a-modal>
  </div>
</template>
<script>
    import { mapActions } from "vuex"
    
    export default {
        name: "CreateUser",

        data() {
            return {
                createBtnLoading: false,
                disabled: true,

                // User Details
                first_name: "",
                last_name: "",
                email: "",
                password: "",
                role: "",
            };
        },

        props: {
            createUserVisible: Boolean,
        },

        emits: ["handleHide"],

        methods: {
            ...mapActions(["createUser"]),

            //   Request Route
            async toCreateUser(){
                // this.$router.push({ name: "Appropriate Route" })
                this.createBtnLoading = true

                let user = {
                    first_name: this.first_name,
                    last_name: this.last_name,
                    email: this.email,
                    password: this.password,
                    role: this.role,
                }

                await this.createUser(user).then((response) => {
                    if(response.status === "info"){
                        this.$message.info(response.message);
                    }
                    
                    else if(response.status === "success"){
                        this.$message.success(response.message);
                        // this.$router.push({ name: "Users" })
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

        // computed: mapGetters(["getStations"]),
    };
</script>