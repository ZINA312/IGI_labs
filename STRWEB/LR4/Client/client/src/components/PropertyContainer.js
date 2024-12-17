import React, { useContext } from 'react';
import PropertyList from './PropertyList';
import PropertyForm from './PropertyForm';
import { AuthContext } from '../context/AuthContext';
import '../styles/PropertyContainer.css'; 

const PropertyContainer = ({ properties }) => {
    const { user } = useContext(AuthContext); 

    return (
        <div className="property-container">
            <h1 className="property-title">Properties</h1>
            {user && <PropertyForm />}
            <PropertyList properties={properties} /> 
        </div>
    );
};

export default PropertyContainer;