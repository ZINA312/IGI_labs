import React, { useContext } from 'react';
import { useNavigate } from "react-router-dom";
import { AuthContext } from '../context/AuthContext'; 
import NewsEditForm from './NewsEditForm';
import axios from 'axios';
import '../styles/NewsDetail.css'; 

const NewsDetail = ({ newsItem, fetchNews }) => {
    const { user } = useContext(AuthContext); 
    const navigate = useNavigate();
    
    if (!newsItem) return <div>Loading...</div>;

    const handleDelete = async () => {
        if (window.confirm("Are you sure you want to delete this article?")) {
            try {
                await axios.delete(`http://localhost:5000/api/articles/${newsItem._id}`, {
                    headers: { "x-auth-token": localStorage.getItem("token") },
                });
                navigate("/news");
            } catch (error) {
                console.error('Error deleting article:', error);
                alert('Failed to delete article. Please try again.');
            }
        }
    };

    return (
        <div className="news-detail">
            <h2 className="news-title">{newsItem.title}</h2>
            <p className="news-content">{newsItem.content}</p>
            {newsItem.image && <img className="news-image" src={newsItem.image} alt={newsItem.title} />}
            {user ? (
                <div className="edit-delete">
                    <NewsEditForm newsItem={newsItem} />
                    <button onClick={handleDelete} className="delete-button">
                        Delete Article
                    </button>
                </div>
            ) : null} 
        </div>
    );
};

export default NewsDetail;