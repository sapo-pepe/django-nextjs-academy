"use client";
import React from "react";

const Container = ({ children }: { children: React.ReactNode }) => {
  return (
    <nav className="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
      <div className="relative flex h-16 items-center justify-between">
        <div className="absolute inset-y-0 left-0 flex items-center sm:hidden">
          <div className="flex flex-1 items-center justify-center sm:items-stretch sm:justify-start">
            {children}
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Container;
