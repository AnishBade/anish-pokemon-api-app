import React, { useState } from 'react';

const SearchBar = ({ setSearchParams }) => {
  const [name, setName] = useState('');
  const [type, setType] = useState('');

  const handleSearch = () => {
    setSearchParams({ name, type });
  };

  return (
    <div className="search-bar">
      <input
        type="text"
        placeholder="Search by name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <input
        type="text"
        placeholder="Search by type"
        value={type}
        onChange={(e) => setType(e.target.value)}
      />
      <button onClick={handleSearch}>Search</button>
    </div>
  );
};

export default SearchBar;
