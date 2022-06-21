// Chakra imports
import { Flex, Grid, useColorModeValue } from "@chakra-ui/react";
import avatar4 from "assets/img/avatars/avatar7.png";
// import ProfileBgImage from "assets/img/ProfileBackground.png";
import ProfileBgImage from "assets/img/profile-banner.jpg";
import React from "react";
import { FaCube, FaPenFancy } from "react-icons/fa";
import { IoDocumentsSharp } from "react-icons/io5";
import Conversations from "./components/Conversations";
import Header from "./components/Header";
import PlatformSettings from "./components/PlatformSettings";
import ProfileInformation from "./components/ProfileInformation";
import Projects from "./components/Projects";

import axios from "axios";
import {api} from "baseUrl";

import requireAuth from "requireAuth";
import useFetch from "fetch";

function Profile() {
  // Chakra color mode
  const textColor = useColorModeValue("gray.700", "white");
  const bgProfile = useColorModeValue(
    "hsla(0,0%,100%,.8)",
    "linear-gradient(112.83deg, rgba(255, 255, 255, 0.21) 0%, rgba(255, 255, 255, 0) 110.84%)"
  );

  const [url, setUrl] = React.useState(`${api}/users/myself`);
  const {data: user, fetch, loading, error, cycle} = useFetch({
    url,
    headers: { "Accept": "application/json" },
    defaultValue: {}
  });

  requireAuth();

  return (
    <Flex direction='column'>
      <Header
        backgroundHeader={ProfileBgImage}
        backgroundProfile={bgProfile}
        name={user.first_name + " " + user.last_name}
        email={user.email}
      />
      <Grid templateColumns={{ sm: "1fr", xl: "repeat(2, 1fr)" }} gap='22px'>
        <ProfileInformation
          title={"Profile Information"}
          description={"The following is your information"}
          name={user.first_name + " " + user.last_name}
          mobile={user.phone}
          email={user.email}
        />
        <PlatformSettings
          title={"Alter details"}
        />
      </Grid>
    </Flex>
  );
}

export default Profile;
