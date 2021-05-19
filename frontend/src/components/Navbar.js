import React from "react";

const Navbar = () => {
  return (
    <div>
      <nav className="bg-white border-b border-gray-300 shadow-sm">
        <div className="flex items-center justify-center pl-3 py-2 h-12">
          <div className="flex items-center">
            <div className="px-1 py-1 font-semibold">Medical Abbreviations</div>
          </div>
        </div>
      </nav>
    </div>
  );
};

export default Navbar;
