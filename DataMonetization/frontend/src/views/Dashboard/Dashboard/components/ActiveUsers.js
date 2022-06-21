// Chakra imports
import { Flex, SimpleGrid, Text, useColorModeValue } from "@chakra-ui/react";

// Custom components
import Card from "components/Card/Card.js";
import CardBody from "components/Card/CardBody.js"

// Custom icons
import {
  CartIcon,
  RocketIcon,
  StatsIcon,
  WalletIcon,
} from "components/Icons/Icons.js";

import React from "react";
import ChartStatistics from "./ChartStatistics";
import StatisticsCard from "./StatsCard";

import {displayNumber, displayMoney} from "numbers";

const ActiveUsers = ({ title, percentage, chart, data, loading }) => {
  const iconBoxInside = useColorModeValue("white", "white");
  const textColor = useColorModeValue("gray.700", "white");
  return (
    <Card p='16px'>
      <CardBody>
        <Flex direction='column' w='100%'>
          <Flex direction='column' mt='8px' alignSelf='flex-start'>
            <Text fontSize='lg' color={textColor} fontWeight='bold'>
              {title}
            </Text>
          </Flex>
          <StatisticsCard
            title={"Revenue"}
            amount={displayMoney(data.total_income)}
            percentage={8}
            icon={<WalletIcon h={"24px"} w={"24px"} color={iconBoxInside} />}
            comment={`${data.total_income_clients} clients`}
            bg={useColorModeValue("blue.300", "gray.600")}
            loading={loading}
          />
          <StatisticsCard
            title={"APIs used"}
            amount={displayNumber(data.apis_used)}
            percentage={8}
            icon={<StatsIcon h={"24px"} w={"24px"} color={iconBoxInside} />}
            comment={`${data.apis_used_clients} clients`}
            bg={useColorModeValue("pink.400", "gray.600")}
            loading={loading}
          />
          <StatisticsCard
            title={"Subscriptions"}
            amount={displayNumber(data.subscriptions)}
            percentage={8}
            icon={<WalletIcon h={"24px"} w={"24px"} color={iconBoxInside} />}
            bg={useColorModeValue("orange.400", "gray.600")}
            loading={loading}
          />
        </Flex>
      </CardBody>
    </Card>
  );
};

export default ActiveUsers;
