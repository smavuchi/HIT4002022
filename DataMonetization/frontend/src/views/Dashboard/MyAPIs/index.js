import axios from "axios";

// Chakra imports
import { Flex } from "@chakra-ui/react";
import React from "react";
import MyAPIs from "./components/MyAPIs";
import API from "./components/API";
import { tablesTableData } from "variables/general";
import {api} from "baseUrl";
import requireAuth from "requireAuth";
import timeAgo from "timeAgo";
import useFetch from "fetch";

function Tables() {
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
      {(!selectedAPI) && <MyAPIs
        fetchAPIs={() => {}}
        title={"My APIs"}
        captions={["Name", "Title", "Status", "Created"]}
        select={setSelectedAPI}
        data={apis.map(api => ({
          id: api.id,
          name: api.name,
          title: api.title,
          status: api.published ? "Published" : "Not published",
          created: timeAgo.format(new Date(api.created_at))
        }))}
        />
      }
      {selectedAPI && <API id={selectedAPI} select={setSelectedAPI}/>}
    </Flex>
  );
}

export default Tables;
