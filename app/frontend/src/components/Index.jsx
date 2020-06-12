import React from "react";

const Index = ({ formulas, selectedItem, setSelectedItem }) => {
  const handleSelect = e => {
    setSelectedItem(e.target.getAttribute("value"));
  };

  return (
    <div className="index-wrapper">
      <div className="index-title">Index</div>
      <div>
        {Object.keys(formulas).map(item => {
          const class_item =
            item == selectedItem ? "index-selected" : "index-item";
          return (
            <div
              className={class_item}
              key={item}
              value={item}
              onClick={handleSelect}
            >
              {item}
            </div>
          );
        })}
      </div>
    </div>
  );
};
export default Index;
