import React, { Component } from 'react';
import axios from 'axios';
import '../styles/NewsEditForm.css'; 

class NewsEditForm extends Component {
    constructor(props) {
        super(props);
        this.state = {
            title: props.newsItem.title || '',
            content: props.newsItem.content || '',
            image: props.newsItem.image || '',
            error: '',
        };
    }

    handleChange = (e) => {
        this.setState({ [e.target.name]: e.target.value, error: '' });
    };

    handleSubmit = async (e) => {
        e.preventDefault();
        const { title, content, image } = this.state;
        const { newsItem } = this.props;

        if (!title || !content) {
            this.setState({ error: 'Title and content are required.' });
            return;
        }

        if (image && !/^https?:\/\/.+\.(jpg|jpeg|png|gif)$/.test(image)) {
            this.setState({ error: 'Image URL must be a valid image link.' });
            return;
        }

        const newsData = { title, content, image };

        try {
            await axios.put(`http://localhost:5000/api/articles/${newsItem._id}`, newsData, {
                headers: { "x-auth-token": localStorage.getItem("token") },
            });
            this.setState({ title: '', content: '', image: '', error: '' });
        } catch (error) {
            this.setState({ error: 'Failed to update news. Please try again.' });
            console.error('News update error', error);
        }
    };

    render() {
        const { title, content, image, error } = this.state;

        return (
            <form className="news-edit-form" onSubmit={this.handleSubmit}>
                {error && <p className="error-message">{error}</p>}
                <input
                    type="text"
                    name="title"
                    value={title}
                    onChange={this.handleChange}
                    placeholder="Title"
                    required
                    className="form-input"
                />
                <textarea
                    name="content"
                    value={content}
                    onChange={this.handleChange}
                    placeholder="Content"
                    required
                    className="form-textarea"
                />
                <input
                    type="text"
                    name="image"
                    value={image}
                    onChange={this.handleChange}
                    placeholder="Image URL"
                    className="form-input"
                />
                <button type="submit" className="submit-button">Update News</button>
            </form>
        );
    }
}

export default NewsEditForm;