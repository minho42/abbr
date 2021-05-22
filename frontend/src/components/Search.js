const Search = (props) => {
  const searchInput = document.querySelector("input");
  const handleSubmit = (e) => {
    e.preventDefault();
  };
  const handleChange = (e) => {
    props.onSearchChange(e.target.value.toLowerCase().trim());
  };

  const clearInput = () => {
    console.log("clear");
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
          className="pl-6 pr-16 py-2 rounded-lg w-full border border-gray-300 focus:border-gray-800 bg-gray-100 focus:outline-none"
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
              <svg
                className="w-6 h-6"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M6 18L18 6M6 6l12 12"
                ></path>
              </svg>
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
