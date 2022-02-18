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
    <div className="flex flex-col items-center justify w-full">
      <div className="w-full max-w-2xl">
        <Navbar />
        <Search onSearchChange={onSearchChange} />
        <AbbrList data={data} query={query} />
      </div>
    </div>
  );
}

export default App;
