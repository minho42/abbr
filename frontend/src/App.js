import { useState } from "react";
import data from "./data.json";
import Navbar from "./components/Navbar";
import Search from "./components/Search";
import AbbrList from "./components/AbbrList";

function App() {
  const [query, setQuery] = useState("");
  const onSearchChange = (q) => {
    setQuery(q);
  };
  return (
    <div className="">
      <Navbar />
      <Search onSearchChange={onSearchChange} />
      <AbbrList data={data} query={query} />
    </div>
  );
}

export default App;
