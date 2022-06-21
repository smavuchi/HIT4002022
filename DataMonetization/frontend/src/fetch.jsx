import React from "react";
import axios from "axios";

export const FetchContext = React.createContext();

export default function useFetch({url, repeatAfter, headers, children, defaultValue}) {
  const [loading, setLoading] = React.useState(true);
  const [error, setError] = React.useState(false);
  const [data, setData] = React.useState(defaultValue);
  const [response, setResponse] = React.useState();
  const [cycle, setCycle] = React.useState(0);

  const fetch = React.useCallback(() => {
    setCycle(cycle => cycle + 1);
    setLoading(true);
    axios({
      url: url,
      headers: {
        "Accept": "application/json",
        ...headers
      },
    }).then(({data}) => {
      setLoading(false);
      setResponse(data);
      setData(data.data);
    }).catch(e => {
      setLoading(false);
      setError("network error. Please reload the page");
    })
  }, []);

  React.useEffect(() => {
    fetch();
    if (repeatAfter) {
      const interval = setInterval(fetch, repeatAfter * 1000);
      return () => clearInterval(interval);
    }
  }, [url]);

  return ({
    url,
    repeatAfter,
    fetch,
    loading,
    error,
    response,
    data,
    cycle
  });
}