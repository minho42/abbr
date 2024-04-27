type Data = {
  id: number
  name: string
  description: string
}

const AbbrItem: React.FC<{ data: Data }> = ({ data }) => {
  const { name, description } = data
  return (
    <tr className="border-b border-gray-200">
      <td className="text-center py-2">{name}</td>
      <td className="pl-2">{description}</td>
    </tr>
  )
}

const AbbrList: React.FC<{ query: string; data: Data[] }> = ({ query, data }) => {
  const searchResult = () => {
    let result: Data[] = []

    if (query.length < 1) {
      return []
    }

    result.push(
      ...data.filter((item) => {
        return item.name.toLowerCase() === query
      })
    )
    result.push(
      ...data.filter((item) => {
        return item.name.toLowerCase().startsWith(query)
      })
    )
    result.push(
      ...data.filter((item) => {
        return item.name.toLowerCase().includes(query)
      })
    )

    if (query.length > 2) {
      result.push(
        ...data.filter((item) => {
          return item.description.toLowerCase().includes(query)
        })
      )
    }
    return [...new Set(result)]
  }

  return (
    <div className="flex flex-col justify-center mx-2 sm:mx-6">
      <table className="table-auto mb-6">
        <thead>
          <tr className="border-b-2 border-gray-300">
            <th className="font-bold w-1/4">Abbr</th>
            <th className="font-bold w-3/4 text-left pl-2">Description</th>
          </tr>
        </thead>
        <tbody>
          {searchResult().map((row) => {
            return <AbbrItem key={row.id} data={row} />
          })}
        </tbody>
      </table>
    </div>
  )
}

export default AbbrList
