import { Tabs, TabList, TabPanels, Tab, TabPanel } from '@chakra-ui/react'
import APIStatistics from "./APIStatistics";
import APIResources from "./APIResources";
import APIPackages from "./APIPackages";

export default function TabView({api, setItemToAdd}) {
  if (!api) {return <></>}
  return (
    <Tabs variant="enclosed" size="sm" width="100%">
      <TabList>
        <Tab onClick={() => setItemToAdd()}>Statistics</Tab>
        <Tab onClick={() => setItemToAdd("resource")}>Resources</Tab>
        <Tab onClick={() => setItemToAdd("package")}>Packages</Tab>
      </TabList>

      <TabPanels>
        <TabPanel>
          <APIStatistics apiId={api.id}/>
        </TabPanel>
        <TabPanel>
          <APIResources apiId={api.id}/>
        </TabPanel>
        <TabPanel>
          <APIPackages apiId={api.id}/>
        </TabPanel>
      </TabPanels>
    </Tabs>
  )
}