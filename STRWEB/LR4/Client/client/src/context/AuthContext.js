import React, { createContext, useState, useEffect } from "react";
import api from "./Api";

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {

  const [user, setUser] = useState(null);
  
  useEffect(() => {
    const fetchUser = async () => {
      const token = localStorage.getItem("token");
      
      if (token) {
        try {
          const response = await api.get("http://localhost:5000/api/users/me", {
            headers: { "x-auth-token": token },
          });
          setUser(response.data);
        } catch (error) {
          console.error(error);
        }
      }
    };

    const checkGoogleLogin = () => {
      const urlParams = new URLSearchParams(window.location.search);
      const token = urlParams.get("token");
      console.log(token);
      if (token) {
        localStorage.setItem("token", token);
        fetchUser();
        window.history.replaceState({}, document.title, "/");
      }
    };
    fetchUser();
    checkGoogleLogin();
  }, []);

  const login = async (username, password) => {
    const response = await api.post("http://localhost:5000/api/users/login", {
        username,
        password,
    });
    localStorage.setItem("token", response.data.token);
    console.log(response.data.user);
    setUser(response.data.user);
  };

  const logout = () => {
    localStorage.removeItem("token");
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};