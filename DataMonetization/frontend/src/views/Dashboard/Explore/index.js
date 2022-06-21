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
  const [url, setUrl] = React.useState(`${api}/client-api/mine`);
  const {data: apis, fetch: fetchAPIs, loading, error, cycle} = useFetch({
    url,
    headers: { "Accept": "application/json" },
    defaultValue: [],
    repeatAfter: 5
  });
  const [selectedAPI, setSelectedAPI] = React.useState();

  requireAuth();

  return (
    <Flex direction='column' pt={{ base: "120px", md: "75px" }}>
      {(!selectedAPI) && <APIs
        title={"Explore"}
        captions={["Name", "Title", "Created"]}
        data={apis.map(api => ({
          id: api.id,
          name: api.name,
          title: api.title,
          created: timeAgo.format(new Date(api.created_at))
        }))}
        select={setSelectedAPI}
      />}
      {selectedAPI && <API id={selectedAPI} select={setSelectedAPI} fetch={fetchAPIs}/>}
    </Flex>
  );
}