import AbbrItem from "./AbbrItem";

const AbbrList = (props) => {
  const { query } = props;

  let result = [];
  if (query.length >= 1) {
    result.push(
      ...props.data.filter((item) => {
        return item.name.toLowerCase() === query;
      })
    );
    result.push(
      ...props.data.filter((item) => {
        return item.name.toLowerCase().startsWith(query);
      })
    );
    result.push(
      ...props.data.filter((item) => {
        return item.name.toLowerCase().includes(query);
      })
    );
    result.push(
      ...props.data.filter((item) => {
        return item.description.toLowerCase().includes(query);
      })
    );
  }

  return (
    <div className="flex flex-col justify-center mx-2 sm:mx-6">
      <table className="table-auto mb-6">
        <thead>
          <tr className="border-b-2 border-gray-300">
            <th className="font-bold">Abbr</th>
            <th className="font-bold text-left pl-2">Description</th>
          </tr>
        </thead>
        <tbody>
          {/* {props.data.map((row) => { */}
          {[...new Set(result)].map((row) => {
            return <AbbrItem key={row.id} data={row} />;
          })}
        </tbody>
      </table>
    </div>
  );
};

export default AbbrList;
