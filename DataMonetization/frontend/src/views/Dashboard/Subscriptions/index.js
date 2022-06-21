// Chakra imports
import { Flex } from "@chakra-ui/react";
import React from "react";
import APIs from "./components/Authors";
import API from "./components/API";
import { tablesTableData } from "variables/general";

import axios from "axios";

import {api} from "baseUrl";
import requireAuth from "requireAuth";
import timeAgo from "timeAgo";
import useFetch from "fetch";

export default function Explore() {
  const [url, setUrl] = React.useState(`${api}/users/myself/subscriptions`);
  const {data: apis, fetch: fetchAPIs, loading, error, cycle} = useFetch({
    url,
    headers: { "Accept": "application/json" },
    defaultValue: [],
    repeatAfter: 5
  });

  requireAuth();

  return (
    <Flex direction='column' pt={{ base: "120px", md: "75px" }}>
      {(!loading) && apis && <APIs
        title={"Subscriptions"}
        captions={["Name", "Title", "Requests Left", "Expires"]}
        data={apis.map(api => ({
          id: api.api.id,
          name: api.api.name,
          title: api.api.title,
          requests: api.subscription.requests,
          expires: timeAgo.format(new Date(api.subscription.expires_at))
        }))}
        select={(x) => console.log(x)}
      />}
    </Flex>
  );
}