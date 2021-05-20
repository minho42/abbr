const Search = (props) => {
  const handleSubmit = (e) => {
    e.preventDefault();
  };
  const handleChange = (e) => {
    props.onSearchChange(e.target.value.toLowerCase().trim());
  };

  return (
    <div className="flex flex-col justify-center px-2 py-2">
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Search abbreviations"
          className="px-6 py-2 rounded-lg w-full border border-gray-300 focus:border-gray-800 bg-gray-100 focus:outline-none"
          autoFocus
          onChange={handleChange}
        />
      </form>
    </div>
  );
};

export default Search;
