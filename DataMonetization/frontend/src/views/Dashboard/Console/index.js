// Chakra imports
import { Flex } from "@chakra-ui/react";
import React from "react";
import Console from "./components/Console";

import axios from "axios";

import {api} from "baseUrl";
import requireAuth from "requireAuth";
import useFetch from "fetch";

export default function _Console() {
  return (
    <Flex direction='column' pt={{ base: "120px", md: "75px" }}>
      <Console/>
    </Flex>
  );
}