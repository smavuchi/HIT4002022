import {
  Text, 
  SimpleGrid,
  useColorModeValue
} from "@chakra-ui/react";

import APIStatisticsCard from "./APIStatisticsCard";
import {
  CartIcon,
  DocumentIcon,
  GlobeIcon,
  WalletIcon,
  StatsIcon,
} from "components/Icons/Icons.js";
import {Avatar} from "@chakra-ui/react";
import {displayNumber, displayMoney} from "numbers";

export default function APIStatisticsCardSection({heading, revenue, subscribers, requests}) {
  const iconBoxInside = useColorModeValue("white", "white");
  return (
    <div>
      <Text fontSize="sm" fontWeight="bold">{heading}</Text>
      <SimpleGrid columns={{ sm: 1, md: 2, xl: 3 }} spacing='24px'>
        <APIStatisticsCard
          title="total revenue"
          value={displayMoney(revenue)}
          loading={false}
          icon={<WalletIcon color={iconBoxInside} />}
        />
        <APIStatisticsCard
          title="total subscribers"
          value={displayNumber(subscribers)}
          loading={false}
          icon={<Avatar color={iconBoxInside} size="xs"/>}
        />
        <APIStatisticsCard
          title="total requests"
          value={displayNumber(requests)}
          loading={false}
          icon={<StatsIcon color={iconBoxInside} />}
        />
      </SimpleGrid>
      <br/>
    </div>
  )
}