import { XMarkIcon } from "@heroicons/react/24/outline";

const Search = (props) => {
  const searchInput = document.querySelector<HTMLInputElement>("input");
  const handleSubmit = (e) => {
    e.preventDefault();
  };
  const handleChange = (e) => {
    props.onSearchChange(e.target.value.toLowerCase().trim());
  };

  const clearInput = () => {
    searchInput.value = "";
    searchInput.focus();
    props.onSearchChange("");
  };

  return (
    <div className="flex flex-col justify-center px-4 py-2 relative">
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Search abbreviations"
          className="pl-6 pr-16 py-2 rounded-lg w-full border border-gray-300  bg-gray-100 "
          autoFocus
          onChange={handleChange}
        />
        {searchInput && searchInput.value.trim().length > 0 ? (
          <div className="absolute inset-y-0 right-10 flex items-center">
            <button
              type="button"
              onClick={clearInput}
              className="h-full px-3 text-gray-500 hover:text-gray-800 focus:outline-none"
            >
              <XMarkIcon className="w-6 h-6" />
            </button>
          </div>
        ) : (
          ""
        )}
      </form>
    </div>
  );
};

export default Search;
