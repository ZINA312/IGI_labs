import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/PropertyList.css'; 

const PropertyList = ({ properties }) => {
    return (
        <ul className="property-list">
            {properties.map(property => {
                const price = typeof property.price === 'object' && property.price !== null
                    ? property.price.$numberDecimal
                    : property.price;

                return (
                    <li key={property._id} className="property-item">
                        <Link to={`/properties/${property._id}`} className="property-link">
                            <h3 className="property-title">{property.title}</h3>
                            <p className="property-description">{property.description}</p>
                            <p className="property-price">Price: ${price}</p>
                            {property.imageUrl && <img className="property-image" src={property.imageUrl} alt={property.title} />}
                        </Link>
                    </li>
                );
            })}
        </ul>
    );
};

export default PropertyList;