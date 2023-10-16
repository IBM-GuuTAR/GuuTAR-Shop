import { BACKEND_ENDPOINT } from "../../config/config";

function ProductCard({ id, name, price, picture_url }) {
  const handleDelete = async () => {
    const result = await fetch(
      `${BACKEND_ENDPOINT}/api/items/delete-item/${id}`,
      {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
        },
      }
    );
  };

  return (
    <div className="FlexCol" style={{ gap: 8 }}>
      <img src={picture_url} width={100} height={150} />
      <div className="FlexRow">
        <label>Name: </label>
        <label>{name}</label>
      </div>
      <div className="FlexRow">
        <label>Price: </label>
        <label>{price} ฿</label>
      </div>
      <div className="FlexRow">
        <button onClick={handleDelete}>Delete</button>
      </div>
    </div>
  );
}

export default ProductCard;
