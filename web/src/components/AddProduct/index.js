import { useState } from "react";

function AddProduct({ setIsShowAddProduct }) {
  const [name, setName] = useState("")
  const [price, setPrice] = useState()
  const [pictureUrl, setPictureUrl] = useState()

  const handleAdd = async () => {
    const result = await fetch("http://localhost:8000/api/items/create-item", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        name: name,
        price: Number(price),
        picture_url: pictureUrl,
      }),
    });
    handleCancel();
  };

  const handleCancel = () => {
    setIsShowAddProduct(false);
  };

  return (
    <div className="FlexCol" style={{ gap: 8 }}>
      <div className="FlexRow">
        <label>Name: </label>
        <input value={name} onChange={(e) => setName(e.target.value)} />
      </div>
      <div className="FlexRow">
        <label>Price: </label>
        <input
          value={price}
          onChange={(e) => setPrice(e.target.value)}
        />
      </div>
      <div className="FlexRow">
        <label>Picture Url: </label>
        <input
          value={pictureUrl}
          onChange={(e) => setPictureUrl(e.target.value)}
        />
      </div>
      <div className="FlexRow">
        <button onClick={handleAdd}>Add</button>
        <button onClick={handleCancel}>Cancel</button>
      </div>
    </div>
  );
}

export default AddProduct;
