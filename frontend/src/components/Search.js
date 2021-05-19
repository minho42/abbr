const Search = (props) => {
  const handleSubmit = (e) => {
    e.preventDefault();
  };
  const handleChange = (e) => {
    props.onSearchChange(e.target.value.toLowerCase().trim());
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Search abbreviations"
          className="pl-6 mx-4 pr-24 py-2 rounded-lg w-full border border-gray-300 focus:border-gray-800 bg-gray-100 focus:outline-none"
          autoFocus
          onChange={handleChange}
        />
      </form>
    </div>
  );
};

export default Search;
