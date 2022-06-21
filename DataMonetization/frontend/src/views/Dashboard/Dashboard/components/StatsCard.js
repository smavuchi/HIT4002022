// Chakra imports
import {
  Flex,
  Stat,
  StatHelpText,
  StatLabel,
  StatNumber,
  useColorModeValue,
} from "@chakra-ui/react";
// Custom components
import Card from "components/Card/Card.js";
import CardBody from "components/Card/CardBody.js";
import IconBox from "components/Icons/IconBox";
import React from "react";

const StatisticsCard = ({ title, amount, icon, comment, bg, loading }) => {
  const iconblue = bg;
  const textColor = useColorModeValue("white", "white");

  return (
    <Card minH='70px' bg={bg} mb="5px">
      <CardBody>
        <Flex flexDirection='row' align='center' justify='center' w='100%'>
          <Stat me='auto'>
            <StatLabel
              fontSize='sm'
              color='#fff'
              fontWeight='bold'
              pb='.1rem'>
              {title}
            </StatLabel>
              <StatNumber fontSize='lg' color={textColor}>
                {(!loading) && amount}
              </StatNumber>
              <StatHelpText
                alignSelf='flex-end'
                justifySelf='flex-end'
                m='0px'
                color={"#fff"}
                fontStyle="italic"
                fontWeight='bold'
                ps='3px'
                fontSize='xs'>
                {loading && "...loading"}
                {(!loading) && comment}
              </StatHelpText>
          </Stat>
          <IconBox as='box' h={"45px"} w={"45px"} bg={iconblue}>
            {icon}
          </IconBox>
        </Flex>
      </CardBody>
    </Card>
  );
};

export default StatisticsCard;
