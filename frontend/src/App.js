import data from "./data.json";
import Navbar from "./components/Navbar";
import Search from "./components/Search";
import AbbrList from "./components/AbbrList";

function App() {
  return (
    <div className="">
      <Navbar />
      <Search />
      <AbbrList data={data} />
    </div>
  );
}

export default App;
