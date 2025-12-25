// Uses the route /api/shoes/id
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { fetchShoeById } from "../../Components/Services/api.";

const ShoeDetails = () => {
    const { id } = useParams();
    const [shoe, setShoe] = useState(null);
   
    useEffect(() => {
        fetchShoeById(id)
            .then(setShoe)
            .catch(console.error);
        },[id]);

        if (!shoe) return <div>Loading...</div>;
        
    return (
        <div>
            <h1>{shoe.name}</h1>
            <img src={shoe.imageUrl} alt={shoe.name} />
            <p>Brand: {shoe.brand}</p>
            <p>Price: ${shoe.price}</p>
            <p>status: {shoe.status}</p>
            <p>Vendor: {shoe.vendor}</p>
        </div>
    );
}
export default ShoeDetails;


