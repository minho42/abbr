const AbbrItem = (props) => {
  return (
    <tr className="border-b border-gray-200">
      <td className="text-center py-2">{props.data.name}</td>
      <td className="pl-2">{props.data.description}</td>
    </tr>
  );
};

export default AbbrItem;
