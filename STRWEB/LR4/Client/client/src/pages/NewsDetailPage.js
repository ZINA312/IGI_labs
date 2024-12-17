import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import NewsDetail from '../components/NewsDetail';

const NewsDetailPage = () => {
    const { id } = useParams();
    const [newsItem, setNewsItem] = useState(null);

    useEffect(() => {
        const fetchNewsItem = async () => {
            const response = await axios.get(`http://localhost:5000/api/articles/${id}`);
            setNewsItem(response.data);
        };
        fetchNewsItem();
    }, [id]);

    if (!newsItem) return <div>Loading...</div>;

    return (
        <div>
            <NewsDetail newsItem={newsItem} />
        </div>
    );
};

export default NewsDetailPage;