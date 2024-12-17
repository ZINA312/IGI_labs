import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../styles/PropertyForm.css'; 

const PropertyForm = ({ fetchProperties, property }) => {
    const [title, setTitle] = useState(property ? property.title : '');
    const [description, setDescription] = useState(property ? property.description : '');
    const [price, setPrice] = useState(property ? property.price : '');
    const [imageUrl, setImage] = useState(property ? property.Urlimage : '');
    const [category, setCategory] = useState(property ? property.category : '');
    const [categories, setCategories] = useState([]); 
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchCategories = async () => {
            try {
                const response = await axios.get('http://localhost:5000/api/categories'); 
                setCategories(response.data);
            } catch (error) {
                console.error('Error fetching categories:', error);
                setError('Failed to load categories.');
            }
        };

        fetchCategories();
    }, []);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');

        if (!title || !description || !price || !imageUrl || !category) {
            setError('All fields are required.');
            return;
        }

        if (price <= 0) {
            setError('Price must be greater than zero.');
            return;
        }

        const urlPattern = /^https?:\/\/.+\.(jpg|jpeg|png|gif)$/;
        if (!urlPattern.test(imageUrl)) {
            setError('Image URL must be a valid image link (jpg, jpeg, png, gif).');
            return;
        }

        const propertyData = { 
            title, 
            description, 
            imageUrl,  
            price: Number(price),  
            category 
        };

        console.log('Submitting property data:', propertyData);

        try {
            await axios.post('http://localhost:5000/api/properties', propertyData, {
                headers: { "x-auth-token": localStorage.getItem("token") },
            });
            setTitle('');
            setDescription('');
            setPrice('');
            setImage('');
            setCategory('');
            fetchProperties();
        } catch (error) {
            console.error('Property submission error', error);
            if (error.response) {
                console.error('Server response:', error.response.data);
            }
            setError('Failed to save property. Please try again.');
        }
    };

    return (
        <form className="property-form" onSubmit={handleSubmit}>
            <h2>{property ? 'Update' : 'Add'} Property</h2>
            {error && <p className="error-message">{error}</p>}
            <input
                type="text"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                placeholder="Title"
                required
                className="form-input"
            />
            <textarea
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                placeholder="Description"
                required
                className="form-textarea"
            />
            <input
                type="number"
                value={price}
                onChange={(e) => setPrice(e.target.value)}
                placeholder="Price"
                required
                className="form-input"
            />
            <input
                type="text"
                value={imageUrl}
                onChange={(e) => setImage(e.target.value)}
                placeholder="Image URL"
                required
                className="form-input"
            />
            <select 
                value={category}
                onChange={(e) => setCategory(e.target.value)}
                required
                className="form-select"
            >
                <option value="">Select Category</option>
                {categories.map(cat => (
                    <option key={cat._id} value={cat._id}>{cat.name}</option>
                ))}
            </select>
            <button type="submit" className="submit-button">Add Property</button>
        </form>
    );
};

export default PropertyForm;