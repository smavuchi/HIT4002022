// Chakra imports
import {
  Flex,
  Grid,
  Image,
  SimpleGrid,
  useColorModeValue,
} from "@chakra-ui/react";

import axios from "axios";
import {displayNumber, displayMoney} from "numbers";

// assets
import peopleImage from "assets/img/people-image.png";
import logoChakra from "assets/svg/logo-white.svg";
import BarChart from "components/Charts/BarChart";
import LineChart from "components/Charts/LineChart";
// Custom icons
import {
  CartIcon,
  DocumentIcon,
  GlobeIcon,
  WalletIcon,
} from "components/Icons/Icons.js";
import React from "react";
import { dashboardTableData, timelineData } from "variables/general";
import ActiveUsers from "./components/ActiveUsers";
import MiniStatistics from "./components/MiniStatistics";
import OrdersOverview from "./components/OrdersOverview";
import Projects from "./components/Projects";
import SalesOverview from "./components/SalesOverview";
import requireAuth from "requireAuth";

import {api} from "baseUrl";

function getPercentage(x, y) {
  return (Number(x) / Number(y));
}

export default function Dashboard() {
  const [loading, setLoading] = React.useState({
    "business-today": null,
    "statistics": null
  });

  const [businessToday, setBusinessToday] = React.useState({});
  const [statistics, setStatistics] = React.useState({});

  requireAuth();
  const iconBoxInside = useColorModeValue("white", "white");

  const setAsLoaded = (category) => {
    setLoading(d => ({...d, [category]: true}));
  }

  const setAsLoading = (category) => {
    setLoading(d => ({...d, [category]: false}));
  }

  React.useEffect(() => {
    setAsLoading("business-today");
    axios({
      url: `${api}/users/myself/business-today`,
      headers: {
        "Accept": "application/json"
      },
    }).then(({data}) => {
      setAsLoaded("business-today");
      if (data.status == 422) {
        localStorage.removeItem("api-key");
        window.location = `${frontend}/admin/dashboard`;
        return;
      }
      setBusinessToday(data.data);
    }).catch(e => {
      setAsLoaded("business-today");
    })
  }, [])

  React.useEffect(() => {
    setAsLoading("statistics");
    axios({
      url: `${api}/users/myself/statistics`,
      headers: {
        "Accept": "application/json"
      },
    }).then(({data}) => {
      setAsLoaded("statistics");
      if (data.status == 422) {
        localStorage.removeItem("api-key");
        window.location = `${frontend}/admin/dashboard`;
        return;
      }
      setStatistics(data.data);
    }).catch(e => {
      setAsLoaded("statistics");
    })
  }, [])

  React.useEffect(() => {
    console.log(businessToday)
  }, [businessToday])

  return (
    <Flex flexDirection='column' pt={{ base: "120px", md: "75px" }}>
      <SimpleGrid columns={{ sm: 1, md: 2, xl: 4 }} spacing='24px'>
        <MiniStatistics
          title={"Total income"}
          amount={displayMoney(statistics.total_income)}
          icon={<WalletIcon h={"24px"} w={"24px"} color={iconBoxInside} />}
          comment={`${statistics.total_income_this_month_pct}% this month`}
          loading={loading["statistics"] === false}
        />
        <MiniStatistics
          title={"Payments made"}
          amount={displayMoney(statistics.total_payment)}
          icon={<GlobeIcon h={"24px"} w={"24px"} color={iconBoxInside} />}
          comment={`${displayNumber(statistics.total_subscriptions)} subscriptions`}
          loading={loading["statistics"] === false}
        />
        <MiniStatistics
          title={"APIs"}
          amount={displayNumber(statistics.total_apis)}
          icon={<DocumentIcon h={"24px"} w={"24px"} color={iconBoxInside} />}
          comment={`${displayNumber(statistics.total_apis_this_month_pct)}% this month`}
          loading={loading["statistics"] === false}
        />
        <MiniStatistics
          title={"Subscriptions (rec.)"}
          amount={displayNumber(statistics.total_subscriptions)}
          icon={<CartIcon h={"24px"} w={"24px"} color={iconBoxInside} />}
          comment={`${displayNumber(statistics.total_subscriptions_this_month_pct)}% this month`}
          loading={loading["statistics"] === false}
        />
      </SimpleGrid>
      <br/>
      <Grid
        templateColumns={{ sm: "1fr", md: "1fr 5fr", lg: ".9fr 3fr" }}
        templateRows={{ sm: "repeat(2, 1fr)", lg: "1fr" }}
        gap='24px'
        mb={{ lg: "26px" }}
      >
        <ActiveUsers
          title={"Statistics Today"}
          data={businessToday}
          loading={loading["business-today"] === false}
        />
        <SalesOverview
          title={"Business Today"}
          percentage={5}
          watch={businessToday}
          data={businessToday}
        />
      </Grid>
      <Grid
        templateColumns={{ sm: "1fr", md: "1fr 1fr", lg: "2fr 1fr" }}
        templateRows={{ sm: "1fr auto", md: "1fr", lg: "1fr" }}
        gap='24px'>
        <Projects
          title={"Subscription History"}
          captions={["Subscriber", "API", "Package"]}
          data={statistics.recent_subscriptions || []}
        />
        <OrdersOverview
          title={"Recent Subscribers"}
          data={statistics.recent_subscribers || []}
        />
      </Grid>
    </Flex>
  );
}
