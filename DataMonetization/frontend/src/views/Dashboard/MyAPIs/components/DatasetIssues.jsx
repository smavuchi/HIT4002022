import React from "react";
import {
  Text
} from '@chakra-ui/react'

import {frontend, api} from "baseUrl";
import useFetcher from "fetch";

export default function DatasetIssues({data}) {
  return (
  	<>
  		<Text>1. <Text style={{display: "inline" }} fontWeight="normal">columns_missing_all_values</Text>: <Text style={{color: "blue", display: "inline"}} fontWeight="bold">{data && data.columns_missing_all_values}</Text></Text>
  		<Text>2. <Text style={{display: "inline" }} fontWeight="normal">columns_with_capitalization_issues</Text>: <Text style={{color: "blue", display: "inline"}} fontWeight="bold">{data && data.columns_with_capitalization_issues}</Text></Text>
  		<Text>3. <Text style={{display: "inline" }} fontWeight="normal">columns_with_potential_outliers</Text>: <Text style={{color: "blue", display: "inline"}} fontWeight="bold">{data && data.columns_with_potential_outliers}</Text></Text>
  		<Text>4. <Text style={{display: "inline" }} fontWeight="normal">columns_with_same_values</Text>: <Text style={{color: "blue", display: "inline"}} fontWeight="bold">{data && data.columns_with_same_values}</Text></Text>
  		<Text>5. <Text style={{display: "inline" }} fontWeight="normal">duplicated_rows</Text>: <Text style={{color: "blue", display: "inline"}} fontWeight="bold">{data && data.duplicated_rows}</Text></Text>
  		<Text>6. <Text style={{display: "inline" }} fontWeight="normal">rows_missing_most_values</Text>: <Text style={{color: "blue", display: "inline"}} fontWeight="bold">{data && data.rows_missing_most_values}</Text></Text>
  		<Text>7. <Text style={{display: "inline" }} fontWeight="normal">rows_with_whitespace_issues</Text>: <Text style={{color: "blue", display: "inline"}} fontWeight="bold">{data && data.rows_with_whitespace_issues}</Text></Text>
  	</>
  );
}