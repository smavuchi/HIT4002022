import React from "react";
import ReactApexChart from "react-apexcharts";

const lineChartOptions = {
  chart: {
    toolbar: {
      show: false,
    },
  },
  tooltip: {
    theme: "dark",
  },
  dataLabels: {
    enabled: false,
  },
  stroke: {
    curve: "smooth",
  },
  xaxis: {
    type: "string",
    categories: [
      "0100",
      "0200",
      "0300",
      "0400",
      "0500",
      "0600",
      "0700",
      "0800",
      "0900",
      "1000",
      "1100",
      "1200",
      "1300",
      "1400",
      "1500",
      "1600",
      "1700",
      "1800",
      "1900",
      "2000",
      "2100",
      "2200",
      "2300",
      "0000",
    ],
    labels: {
      style: {
        colors: "#000",
        fontSize: "12px",
      },
    },
  },
  yaxis: {
    labels: {
      style: {
        colors: "#c8cfca",
        fontSize: "12px",
      },
    },
  },
  legend: {
    show: false,
  },
  grid: {
    strokeDashArray: 10,
  },
  fill: {
    type: "gradient",
    gradient: {
      shade: "light",
      type: "vertical",
      shadeIntensity: 0.5,
      gradientToColors: undefined, // optional, if not defined - uses the shades of same color in series
      inverseColors: true,
      opacityFrom: 0.8,
      opacityTo: 0,
      stops: [],
    },
    colors: ["#4FD1C5", "#2D3748"],
  },
  colors: ["#4FD1C5", "#2D3748"],
};


function LineChart({data}) {
  const [chartData, setChartData] = React.useState([]);
  const [chartOptions, setChartOptions] = React.useState(lineChartOptions);

  React.useEffect(() => {
    setChartData([
      {
        name: "Requests",
        data: data.requests_hourly,
      },
      {
        name: "APIs used",
        data: data.apis_used_hourly,
      },
      {
        name: "Subscriptions",
        data: data.subscriptions_hourly,
      },
    ])
  }, [data]);

  return (
    <ReactApexChart
      options={chartOptions}
      series={chartData}
      type="area"
      width="100%"
      height="100%"
    />
  )
}

export default LineChart;
