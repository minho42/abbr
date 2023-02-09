import { IData } from "./AbbrList";

const AbbrItem: React.FC<{ data: IData }> = ({ data }) => {
  const { name, description } = data;
  return (
    <tr className="border-b border-gray-200">
      <td className="text-center py-2">{name}</td>
      <td className="pl-2">{description}</td>
    </tr>
  );
};

export default AbbrItem;
