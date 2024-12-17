import React from 'react';
import { useNavigate } from 'react-router-dom';
import PropertyUpdateForm from './PropertyUpdateForm';
import axios from 'axios';
import '../styles/PropertyDetail.css'; 

const PropertyDetail = ({ property, fetchProperties }) => {
    const navigate = useNavigate();

    const handleDelete = async () => {
        if (window.confirm("Are you sure you want to delete this property?")) {
            try {
                await axios.delete(`http://localhost:5000/api/properties/${property._id}`, {
                    headers: { "x-auth-token": localStorage.getItem("token") },
                });
                navigate("/properties");
            } catch (error) {
                console.error('Error deleting property:', error);
                alert('Failed to delete property. Please try again.');
            }
        }
    };

    if (!property) return <div>Loading...</div>;

    const price = typeof property.price === 'object' && property.price !== null
        ? property.price.$numberDecimal
        : property.price;

    return (
        <div className="property-detail">
            <h3 className="property-title">{property.title}</h3>
            <p className="property-description">{property.description}</p>
            <p className="property-price">Price: ${price}</p>
            {property.imageUrl && <img className="property-image" src={property.imageUrl} alt={property.title} />}
            <PropertyUpdateForm property={property} fetchProperties={fetchProperties} />
            <button onClick={handleDelete} className="delete-button">
                Delete Property
            </button>
        </div>
    );
};

export default PropertyDetail;