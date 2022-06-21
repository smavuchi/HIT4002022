import React from "react";
import APIStatisticsCardSection from "./APIStatisticsCardSection";

import useFetcher from "fetch";
import {api as apiUrl, frontend as frontendUrl} from "baseUrl";
import axios from "axios"

export default function APIStatistics({apiId}) {
  const [url, setUrl] = React.useState(apiUrl + "/client-api/" + apiId + "/statistics");
  const {data, loading, error, response} = useFetcher({url, defaultValue: {}, repeatAfter: 5});

  return (    
    <>
      <APIStatisticsCardSection
        heading="Overall"
        revenue={data.total_revenue}
        subscribers={data.total_subscribers}
        requests={data.total_requests}
        loading={loading}
      />
      <APIStatisticsCardSection
        heading="This Month"
        revenue={data.total_revenue_this_month}
        subscribers={data.total_subscribers_this_month}
        requests={data.total_requests_this_month}
        loading={loading}
      />
      <APIStatisticsCardSection
        heading="Today"
        revenue={data.total_revenue_today}
        subscribers={data.total_subscribers_today}
        requests={data.total_requests_today}
        loading={loading}
      />
    </>
  );
}