import { useState } from "react";


function Dropdown() {
  const [selectedOption, setSelectedOption] = useState('');

  const handleDropdownChange = (event: any) => {
    setSelectedOption(event.target.value);
  };

  return (
    <div>
      <select value={selectedOption} onChange={handleDropdownChange}>
        <option value="Derivative">Derivative</option>
        <option value="Integral">Integral</option>
      </select>
    </div>
  );
}

export default Dropdown;