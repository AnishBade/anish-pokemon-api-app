import React, { useState, useEffect } from 'react';
import axios from 'axios';
import PokemonList from './components/PokemonList';
import SearchBar from './components/SearchBar';
import './App.css';

const App = () => {
  const [pokemons, setPokemons] = useState([]);
  const [filteredPokemons, setFilteredPokemons] = useState([]);
  const [searchParams, setSearchParams] = useState({ name: '', type: '' });

  useEffect(() => {
    const fetchPokemons = async () => {
      const response = await axios.get('http://localhost:8000/api/v1/pokemons/');
      if (response.data.success) {
        setPokemons(response.data.data);
        setFilteredPokemons(response.data.data);
      }
    };
    fetchPokemons();
  }, []);

  useEffect(() => {
    let filtered = pokemons;
    if (searchParams.name) {
      filtered = filtered.filter(pokemon => pokemon.name.includes(searchParams.name.toLowerCase()));
    }
    if (searchParams.type) {
      filtered = filtered.filter(pokemon => pokemon.type.includes(searchParams.type.toLowerCase()));
    }
    setFilteredPokemons(filtered);
  }, [searchParams, pokemons]);

  return (
    <div className="App">
      <h1>Pokémon List</h1>
      <SearchBar setSearchParams={setSearchParams} />
      <PokemonList pokemons={filteredPokemons} />
    </div>
  );
};

export default App;
